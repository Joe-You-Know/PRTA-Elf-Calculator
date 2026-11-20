# PRTA–Elf multi-output denominator GCD restructuring v2 — 2026-11-20

## Executed hypothesis
Can one original source-constructed common factor `g=gcd(d1,...,dk)` be constructed once and reused across two or three separate exact-division denominator source branches, retiring enough original constructions to lower the whole Santa 2026 Elf program below the independently verified 134,002-instruction benchmark? Compare strictly against a conventional arithmetic-graph optimizer with the same input. No ECC laws or assumed native triangular contact assignments.

**Status:** Fully executed on 1,000/1,000 official scored programs, all resulting programs independently validated. Zero accepted scored improvement in all bounded search families, including conventional DAG control. A controlled positive three-output case with true collective g=8 reduces a valid intentionally duplicated ten-instruction program to seven, but it is ordinary arithmetic DAG sharing, not a PRTA-specific advantage.

## Complete executed benchmark

| Search | Relevant source candidate relationships | Full rewrite trials | Accepted savings |
| --- | ---: | ---: | ---: |
| Pair, g and factor quotients both live at source producer steps | 25 | 10 | 0 |
| Pair, pay +1 instruction constructing g in scratch, replace 2 producers | 317 quotient-compatible source pairs; 314 scratch feasible | 605 | 0 |
| Triple, one common g, replace 3 original producer occurrences | 626 triples sharing g>1, 37 have factor quotients live | 52 | 0 |
| Matched conventional source-aware arithmetic DAG | 55 ranked source positions/puzzle, up to 2 rounds | all 1000 puzzles | 0 |

Earlier GCD audit counted 3,942 denominator VALUE pairs with shared factor; current count is 1,947 distinct original denominator **producer event** pairs, a stricter test because equal scalar values and the same original writer don't count as two independent construction sources.

**Correctness boundary:** original source SSA last-writer identities, chronology, register overwrites and early read-before-write, positivity and numeric bounds, exact integer quotient/remainder zero, actual availability of g and all factors, and cost of inserting g all enforced; accept only if whole graph provenance pruning strictly reduces instructions and full Elf validator passes. Every GCD candidate not fully source certified is rejected before crediting savings. Searches are bounded; do not infer global impossibility of multi-output savings.

**Independent verification:** Separate Elf machine interpreter with no optimizer imports replayed complete baseline, live-pair, paid-pair, triple, and conventional output CSVs: **1000/1000 for each, all exactly 134002**. JSON content identical at instruction-history level across all five; SHA256 for all CSVs **8288acc0e43c9b945c178842bac715a7a03bb5fe7a781b7e5cebfa493e9b17c9**. Eight directed regression tests PASS, including actual source nonconstruction rejection.

**Controlled positive:** Starting registers [2,96,128,320]; targets [12,8,10]. Denominators (8,16,32) share collective GCD **8**. In a deliberately duplicated 10-instruction valid program, each denominator builds its own factor chain. Sharing actually constructed g=8 and then 16=8*2, 32=16*2 gives a seven-instruction correct program. Both independently verified. This example is NOT shortest-program proof or a uniquely PRTA improvement.

**Reproducibility:** User-facing self-contained ZIP `prta_elf_multi_output_gcd_restructuring_v2.zip`, SHA256 `a4c3f56d9f7627f0a0e23d5d060bbace810b8e200231912d0d3098e363b72815`, includes official user-provided puzzle input and baseline, four output CSVs, 5 interpreters/optimizers, exact JSON ledgers, 8 tests, PowerShell Windows runner (`py`), and formal LaTeX + compiled 2-page PDF. Run `powershell -NoProfile -ExecutionPolicy Bypass -File .\run_windows.ps1`. A PDF SHA256 is `ee4a83d8a2d7089009d1ecaaeb9ee226f644ac90da939a38b886351c0b2a63b0`.

**Next:** Source-derived factor hyperedges connecting >=4 denominator branches, including factor construction and shared subexpressions across original parent ancestry, multiple coordinated rewires/early source relocation (not necessarily final producer substitutions). Require matching unrestricted arithmetic DAG hyperedge control and blind exact independent execution. A native PRTA geometric necessity has NOT been derived for these Elf source events; numeric GCD is a candidate index, not original contact proof.
