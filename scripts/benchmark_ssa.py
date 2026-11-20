"""Reproduce the occurrence-aware Elf Calculator benchmark.

Example:
python3 scripts/benchmark_ssa.py --puzzles data/puzzles.csv \
    --baseline data/sample_submission.csv \
    --prior results/submission_reuse.csv \
    --out results/submission_ssa.csv
"""
import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

# Supports running from an editable install or directly from repository root.
try:
    from prta_elf.core import load_puzzles, load_programs, validate
    from prta_elf.ssa_reuse import optimize_ssa
except ModuleNotFoundError:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
    from prta_elf.core import load_puzzles, load_programs, validate
    from prta_elf.ssa_reuse import optimize_ssa


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--puzzles", required=True)
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--prior", required=True, help="Already accepted, valid submission CSV")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    puzzles = load_puzzles(args.puzzles)
    baseline = load_programs(args.baseline)
    prior = load_programs(args.prior)
    assert set(puzzles) == set(baseline) == set(prior), "puzzle ID mismatch"
    totals = Counter()
    output = {}
    failures = []
    for pid, puzzle in puzzles.items():
        original = baseline[pid]
        incumbent = prior[pid]
        assert validate(puzzle, incumbent)["valid"], pid
        totals["initial"] += len(original)
        totals["prior"] += len(incumbent)
        try:
            candidate = optimize_ssa(puzzle, original)
            assert validate(puzzle, candidate)["valid"], pid
            if len(candidate) < len(incumbent):
                choice = candidate
                totals["improved"] += 1
            else:
                choice = incumbent
                totals["retained_prior"] += 1
        except (AssertionError, ValueError) as exc:
            choice = incumbent
            totals["fallback"] += 1
            failures.append((pid, str(exc)))
        output[pid] = choice
        totals["new"] += len(choice)

    dest = Path(args.out)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("w", newline="", encoding="utf8") as stream:
        writer = csv.writer(stream)
        writer.writerow(["id", "program"])
        for pid, program in output.items():
            writer.writerow([pid, json.dumps(program, separators=(",", ":"))])

    # Post-serialization independent audit of the exact submission file.
    reloaded = load_programs(dest)
    assert set(reloaded) == set(puzzles)
    independent_total = 0
    for pid, puzzle in puzzles.items():
        result = validate(puzzle, reloaded[pid])
        assert result["valid"], (pid, result)
        independent_total += result["instruction_count"]
    assert independent_total == totals["new"]
    print(json.dumps({
        "puzzles": len(puzzles),
        "counts": dict(totals),
        "saved_vs_prior": totals["prior"] - totals["new"],
        "saved_vs_original": totals["initial"] - totals["new"],
        "verified_total": independent_total,
        "failures": failures[:10],
    }, indent=2))


if __name__ == "__main__":
    main()
