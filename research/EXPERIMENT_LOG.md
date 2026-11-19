# Experiment log

## 2026-11-18 — Initial hypothesis

PRTA might lower instruction cost by discovering oriented shared constructions across sets of arithmetic targets, rather than constructing each target independently. This remains an **untested optimization hypothesis**.

Dataset structure inspected: `practice_puzzles.csv` (200 rows), `puzzles.csv`, `sample_submission.csv`. The source archive marks competition data as subject to competition rules, so data is excluded from version control.

Baseline: supplied sample program. First exact transformation: delete non-ancestor arithmetic events while preserving first occurrences of targets. The PRTA candidate explorer is not yet an integrated program generator.
