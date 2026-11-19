import argparse
import csv
import json
from pathlib import Path
from .core import load_puzzles, load_programs, validate
from .optimize import prune_provenance


def main():
    p = argparse.ArgumentParser(description="Elf Calculator constructive program audit")
    p.add_argument("--puzzles", required=True)
    p.add_argument("--programs", required=True)
    p.add_argument("--out", help="Write optimized submission CSV")
    p.add_argument("--limit", type=int, help="Process at most N puzzles")
    a = p.parse_args()
    puzzles = load_puzzles(a.puzzles)
    programs = load_programs(a.programs)
    optimized = {}
    before = after = count = 0
    failures = []
    for pid, puzzle in puzzles.items():
        if a.limit is not None and count >= a.limit: break
        if pid not in programs: continue
        try:
            source = programs[pid]
            reduced = prune_provenance(puzzle, source)
            result = validate(puzzle, reduced)
            if not result["valid"]: raise ValueError(f"uncovered targets: {result['missing']}")
            optimized[pid] = reduced
            before += len(source)
            after += len(reduced)
            count += 1
        except Exception as exc:
            failures.append({"id": pid, "error": str(exc)})
    if a.out:
        with open(a.out, "w", newline="", encoding="utf-8") as stream:
            writer = csv.writer(stream)
            writer.writerow(["id", "program"])
            for pid, program in optimized.items():
                writer.writerow([pid, json.dumps(program, separators=(",", ":"))])
    print(json.dumps({"puzzles_validated": count, "total_before": before,
                      "total_after": after, "instructions_saved": before-after,
                      "failed": failures[:20], "failure_count": len(failures)}, indent=2))
    if failures: raise SystemExit(1)

if __name__ == "__main__": main()
