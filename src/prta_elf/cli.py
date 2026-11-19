import argparse
import csv
import json
from pathlib import Path
from .core import load_puzzles, load_programs, validate
from .optimize import prune_provenance
from .value_reuse import safe_reuse_values


def main():
    p = argparse.ArgumentParser(description="Elf Calculator constructive program audit")
    p.add_argument("--puzzles", required=True)
    p.add_argument("--programs", required=True)
    p.add_argument("--out", help="Write optimized submission CSV")
    p.add_argument("--limit", type=int, help="Process at most N puzzles")
    p.add_argument("--optimizer", choices=("provenance", "reuse"), default="provenance",
                   help="reuse is a value-occurrence compiler with safe fallback")
    a = p.parse_args()
    puzzles = load_puzzles(a.puzzles)
    programs = load_programs(a.programs)
    optimized = {}
    before = after = count = 0
    failures = []
    methods = {"value_reuse": 0, "provenance_fallback": 0, "provenance": 0}
    for pid, puzzle in puzzles.items():
        if a.limit is not None and count >= a.limit: break
        if pid not in programs: continue
        try:
            source = programs[pid]
            if a.optimizer == "reuse":
                reduced, method = safe_reuse_values(puzzle, source)
            else:
                reduced, method = prune_provenance(puzzle, source), "provenance"
            result = validate(puzzle, reduced)
            if not result["valid"]: raise ValueError(f"uncovered targets: {result['missing']}")
            if len(reduced) > len(source): raise AssertionError("optimizer grew instruction count")
            optimized[pid] = reduced
            methods[method] += 1
            before += len(source)
            after += len(reduced)
            count += 1
        except Exception as exc:
            failures.append({"id": pid, "error": str(exc)})
    if a.out:
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        with open(a.out, "w", newline="", encoding="utf-8") as stream:
            writer = csv.writer(stream)
            writer.writerow(["id", "program"])
            for pid, program in optimized.items():
                writer.writerow([pid, json.dumps(program, separators=(",", ":"))])
    print(json.dumps({"optimizer": a.optimizer, "puzzles_validated": count, "total_before": before,
                      "total_after": after, "instructions_saved": before-after,
                      "savings_percent": round(100*(before-after)/before, 6) if before else 0,
                      "methods": methods,
                      "failed": failures[:20], "failure_count": len(failures)}, indent=2))
    if failures: raise SystemExit(1)

if __name__ == "__main__": main()
