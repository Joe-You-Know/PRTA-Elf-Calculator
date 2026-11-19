# Arithmetic-graph portfolio recombination — checkpoint v0.5

Date: 2026-11-18/19. **Local validation only; not Kaggle-submitted.**

## Target and measured checkpoint

Goal proposed: reduce the previously measured 315,683 instructions to at most
105,227–105,228 (approximately one third). This was **not achieved**.

The user-provided `santa-2026-arithmetic-graph-rewrites.ipynb` contains a
public, externally contributed arithmetic-graph-rewrite portfolio reported as
Kaggle submission 58541609, score 141,086, with explicit attribution to
konbu17, Bikram Basnet and others. This is **not our independently invented
optimizer**. The notebook carries 754 alternative programs encoded in its
literal data cell, not all 1,000. The remaining programs come from an external
public starting CSV, SHA-256:
`1147067ff0ea9545bdd0625b5de216320b762d6f3f6413a183b8b8a63035973f`.
The notebook reports its full public portfolio at 141,086; without that
starting CSV the complete result cannot be reconstructed locally.

We decoded that supplied notebook's literal replacement dictionary *without
executing its cells*, independently validated all 754 candidate programs with
the competition validator, and selected the shorter of each candidate and the
previous 315,683-instruction submission.

| Local construction | Instructions |
| --- | ---: |
| Previous QR + SSA local | 315,683 |
| Hybrid with 754 externally credited programs | 178,272 |
| Hybrid after SSA reuse pass | **178,266** |
| Public notebook complete (reported) | 141,086 |
| Stretch target | ~105,228 |

Results: 754 public replacement programs adopted; **all 1,000/1,000 final
CSV rows independently valid**, zero invalid external replacements; SSA
subsequently improved five programs by six more instructions, zero failures.

SHA-256 of final `submission_hybrid_reopt.csv`:
`b29f0e0312148b0afe588ce24cc0accfc838495d1d151fabaaa5d8f847cd99e4`.

The resulting measured improvement over previous local portfolio is 137,417
instructions (43.53%). This is not a third of the previous count and it is
not an independently demonstrated PRTA-specific improvement. No new Kaggle
submission was made.

## Attribution and interpretation

Do not erase original authorship. The attached Kaggle notebook explicitly
credits the Apache-2.0 konbu17 starting portfolio, Bikram Basnet graph rewrites,
Roman Rozen/IceFire, Vladislav Lavrentev, and other cited portfolio authors.
These externally sourced programs are selected as competitors/inputs. Our
new contribution here is the independently verified portfolio comparison,
combination with the existing QR/SSA compiler and reproducibility ledger.

## Reproduction

With the supplied notebook (and optionally the pinned public starting CSV):

```bash
python3 scripts/merge_public_graph_rewrites.py \
  --notebook data/santa-2026-arithmetic-graph-rewrites.ipynb \
  --puzzles data/puzzles.csv \
  --incumbent results/submission_chain_ssa.csv \
  --out results/submission_hybrid_reopt.csv --reuse
```

To obtain the public starting portfolio on the user's authenticated WSL Kaggle
CLI, download the user-attributed dataset
`konbu17/santa-2026-elf-calculator-programs` and select the CSV whose SHA
matches the notebook's pinned hash; do not assume its download filename.

A next valid research direction is to compare target-pair helper rebuilding,
inverse dependency routes, and bounded three-contact PRTA source obligations
against the public 141,086 portfolio, not merely against our weaker 315,683
QR compiler. Count every emitted arithmetic operation and preserve withheld
source-event status separately from numeric zero.
