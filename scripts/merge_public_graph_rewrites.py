"""Merge attributed Kaggle graph-rewrite notebook replacements with our incumbent.

The public notebook supplied by the project owner contains independently
validated replacement programs and credits upstream authors. Do not erase
their provenance. This script parses the literal encoded payload without
executing notebook code.

Inputs:
  --notebook santa-2026-arithmetic-graph-rewrites.ipynb
  --puzzles data/puzzles.csv
  --incumbent results/submission_chain_ssa.csv
  --out results/submission_hybrid.csv

Optionally --public-start data/submission.csv obtains the remaining rows
of the publicly credited 142940-instruction starting portfolio.
"""
import argparse
import ast
import base64
import csv
import hashlib
import json
import sys
import zlib
from pathlib import Path

try:
    from prta_elf.core import load_programs, load_puzzles, validate
    from prta_elf.ssa_reuse import optimize_ssa
except ModuleNotFoundError:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
    from prta_elf.core import load_programs, load_puzzles, validate
    from prta_elf.ssa_reuse import optimize_ssa

PUBLIC_START_SHA256 = "1147067ff0ea9545bdd0625b5de216320b762d6f3f6413a183b8b8a63035973f"
PUZZLES_SHA256 = "b0c70d849eca078a0e1cf9a4f7b47fd40b7435663f6f84de6725f84724500428"


def decode_notebook(notebook_path):
    data = json.loads(Path(notebook_path).read_text(encoding="utf8"))
    for cell in data["cells"]:
        if cell["cell_type"] != "code":
            continue
        tree = ast.parse("".join(cell["source"]))
        if not tree.body:
            continue
        assignment = tree.body[0]
        if not isinstance(assignment, ast.Assign):
            continue
        if len(assignment.targets) != 1:
            continue
        target = assignment.targets[0]
        if not isinstance(target, ast.Name) or target.id != "encoded":
            continue
        literal = ast.literal_eval(assignment.value)
        blob = zlib.decompress(base64.b85decode(literal))
        decoded = json.loads(blob)
        if not isinstance(decoded, dict):
            raise ValueError("encoded notebook payload is not a dictionary")
        return {key: json.loads(value) if isinstance(value, str) else value
                for key, value in decoded.items()}
    raise ValueError("no literal encoded replacement dictionary")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--notebook", required=True)
    ap.add_argument("--puzzles", required=True)
    ap.add_argument("--incumbent", required=True)
    ap.add_argument("--public-start")
    ap.add_argument("--out", required=True)
    ap.add_argument("--reuse", action="store_true")
    args = ap.parse_args()
    puzzles = load_puzzles(args.puzzles)
    incumbent = load_programs(args.incumbent)
    changes = decode_notebook(args.notebook)
    if set(puzzles) != set(incumbent):
        raise ValueError("incumbent puzzle ID mismatch")
    if set(changes) - set(puzzles):
        raise ValueError("unrecognized replacement puzzle IDs")
    if args.public_start:
        start_path = Path(args.public_start)
        digest = hashlib.sha256(start_path.read_bytes()).hexdigest()
        if digest != PUBLIC_START_SHA256:
            raise ValueError("public starting portfolio SHA-256 mismatch")
        if hashlib.sha256(Path(args.puzzles).read_bytes()).hexdigest() != PUZZLES_SHA256:
            raise ValueError("official puzzle SHA-256 mismatch")
        public_start = load_programs(start_path)
        if set(public_start) != set(puzzles):
            raise ValueError("public program ID mismatch")
        if sum(len(x) for x in public_start.values()) != 142940:
            raise ValueError("public starting portfolio instruction count mismatch")
    else:
        public_start = {}

    public_full = dict(public_start)
    public_full.update(changes)
    if public_start and sum(len(x) for x in public_full.values()) != 141086:
        raise ValueError("public graph rewrite portfolio count mismatch")

    out = {}
    adopted = {}
    gain = 0
    for pid, puzzle in puzzles.items():
        chosen = incumbent[pid]
        if not validate(puzzle, chosen)["valid"]:
            raise ValueError(f"invalid incumbent {pid}")
        public = public_full.get(pid)
        if public is not None:
            if not validate(puzzle, public)["valid"]:
                raise ValueError(f"invalid external portfolio program {pid}")
            if len(public) < len(chosen):
                gain += len(chosen) - len(public)
                chosen = public
                adopted[pid] = "public_graph_rewrite" if pid in changes else "public_start"
        if args.reuse:
            try:
                candidate = optimize_ssa(puzzle, chosen)
                if len(candidate) < len(chosen):
                    chosen = candidate
                    adopted[pid] = adopted.get(pid, "incumbent") + "_ssa"
            except (AssertionError, ValueError):
                pass
        out[pid] = chosen

    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf8") as stream:
        writer = csv.writer(stream)
        writer.writerow(["id", "program"])
        for pid, program in out.items():
            writer.writerow([pid, json.dumps(program, separators=(",", ":"))])
    reloaded = load_programs(path)
    assert set(reloaded) == set(puzzles)
    for pid, puzzle in puzzles.items():
        assert validate(puzzle, reloaded[pid])["valid"], pid
    total = sum(len(p) for p in reloaded.values())
    print(json.dumps({
        "instructions": total,
        "improvement_over_incumbent": sum(len(p) for p in incumbent.values()) - total,
        "public_portfolio_complete": bool(public_start),
        "public_programs_adopted": len(adopted),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }, indent=2))


if __name__ == "__main__":
    main()
