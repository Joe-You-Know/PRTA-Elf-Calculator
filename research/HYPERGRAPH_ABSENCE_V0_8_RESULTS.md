# Multi-producer hypergraph + source-certified absence v0.8

November 19, 2026. Negative scored result, not a global optimality proof. Baseline is the externally credited public portfolio, 141,086 instructions.

Both modes receive identical candidate graph, source cuts, node limits, depths and expansion budgets. Conventional mode combines alternative arithmetic producers. Absence mode additionally excludes branches where the number of constructed steps plus a lower bound of one necessary step per uncovered target cannot beat the current plan. Withheld operations do not produce numerical zero or free outputs. Exact divisions require an integer quotient and remainder zero.

| Measure | Default | Wider |
|---|---:|---:|
| Independently validated puzzles | 1000/1000 | 1000/1000 |
| Previous instructions | 141086 | 141086 |
| Output instructions | 141086 | 141086 |
| Saved | 0 | 0 |
| Cuts / candidate node cap | 3 / 70 | 6 / 100 |
| Producer depth / expansion budget | 3 / 160 | 4 / 320 |
| Conventional explored states | 13000 | 58499 |
| Absence explored states | 12814 | 58117 |
| Certified lower-bound exclusions | 484 | 1002 |
| Tests passed | 27 | 27 |

Both CSVs exactly match public baseline SHA-256 21d1d5245de5d41810e06ce6435df99059b2ba8a35f2bfcde3256e827675a5d7. On constructed (2,3)->(21,35) control, both planners shorten seven steps to six. Prior A/B/C control reached four, so this is not a stronger control result.

Boundaries: graph only contains source-live and historically witnessed suffix candidate values, excluding genuinely new shared helpers. This experiment tests admissible cost-based exclusion, not full forced-producer propagation. Physical PRTA face attachment is UNWITNESSED. Search-work reduction is not a measured wall-time or Kaggle-score gain. The identical output should not be resubmitted.

Code, unit tests, two audit JSONs and detailed report are available in the accompanying prta-elf-hypergraph-absence-v0_8.zip artifact; executable code has not been added to this GitHub branch. Next experiment should generate genuinely new helper values by reverse exact QR rules and compare a complete, explicitly scoped forced/forbidden producer solver against a matched conventional hypergraph planner.