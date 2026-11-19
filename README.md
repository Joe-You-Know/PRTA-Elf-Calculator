# PRTA — Santa 2026 Elf Calculator

Research repository for **Primitive Rotating Triangular Algebra (PRTA)** applied to the Santa 2026 Elf Calculator integer-arithmetic instruction optimization challenge.

## Research status

- **Verified implementation:** strict puzzle validator with 48-register execution, positive-only results, exact division, integer value limits, and target-event coverage.
- **Verified implementation:** causal-provenance pruning of supplied valid programs, preserving each first witnessed target event and its ancestors.
- **Experimental representation only:** three-contact triangular candidate generator.
- **Not established:** PRTA outperforming the baseline or general shared-DAG optimization. No performance claim is made before reproducible trials.

## Competition rules incorporated

Each program uses `['op', source_i, source_j, destination]` with `+`, `-`, `*`, `/`. Both sources are read before overwriting the destination. All values must remain positive and at or below `value_limit`. Division is legal only if exact. Targets need to appear **once**, even if later overwritten. All executed steps contribute to the score. Register count is provided per puzzle (48 for supplied data).

## Local setup (PowerShell)

```powershell
py -m pip install -e .
py -m unittest discover -s tests -v
```

Extract `santa-2026.zip` privately into `data/` (not tracked; competition material is subject to competition rules). The archive includes `practice_puzzles.csv`, `puzzles.csv`, and `sample_submission.csv`.

## Run a reproducible baseline comparison

```powershell
py -m prta_elf.cli --puzzles data/puzzles.csv --programs data/sample_submission.csv --out results/submission_pruned.csv
```

Create `results/` first. Output programs must be independently validated against every applicable official limit before submission. Optimization is a conservative provenance pass, not yet the PRTA solver.

## Research roadmap

1. Audit sample programs and record instruction counts per puzzle and family.
2. Build an operation DAG with exact positive-integer arithmetic and quotient–remainder witnesses.
3. Derive oriented, three-contact PRTA reuse moves with specified compilation cost.
4. Compare PRTA planning to a non-PRTA shared-DAG optimizer under matched time budgets.
5. Validate all generated programs independently; report savings, failures, memory/register pressure, and runtime.
6. Keep unproven claims and negative results in `research/` with fixture hashes.

## Data policy

Original contest files are **not bundled into the Git repository**. Supply them locally from the original competition download and follow the competition's redistribution/submission rules.

## Research principles

Retain provenance of every constructed number and every lawful quotient–remainder extraction. Do not identify the absence of a construction with an existing zero-valued object. Do not count a PRTA rotation as free: if it changes a calculator value, compile it into scored arithmetic instructions.
