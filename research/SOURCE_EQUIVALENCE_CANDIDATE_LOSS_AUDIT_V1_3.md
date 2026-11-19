# PRTA Elf source-equivalence and operand-pair search audit v1.3

Date: 2026-11-19. **Implemented executable corrections and independently tested complete 1,000-puzzle ablations.** Downloadable artifact in current conversation: `prta_elf_source_equivalence_audit_v1_3.zip`. Original v1.2 source included for comparison. The ZIP includes corrected `construct_audit_v13.py`, full `benchmark_v13.py`, 15 tests (8 inherited + 7 new), an independent interpreter, and three complete benchmark audits.

## Source-level defects

1. `construct_first.plan` used `tuple(sorted(set(state.values())))` as a complete search-state identity. This discards source-distinct events e.g. `2+3=5` versus `3+2=5`, and distinct orders for separately constructing 4 and 5. A numerical projection is not sufficient to prove future PRTA contact equivalence, source-occurrence equality, register slot equivalence or identical future under bounded candidate enumeration. This does **not** mean equal numerical value sets can never share a correct arithmetic continuation in an unconstrained numerical model.
2. `construct_first.offer_joins` limited candidate ordered pairs via flat prefix `i*n+j<cap_pairs`. With n=6, cap_pairs=20, none has newest occurrence as **first operand**; hence `12/2=6` can be absent even if 12 and 2 are witnessed. A source-fair recent-first ordered pair scheduling now includes six pairs with newest occurrence as first operand in the same cap.
3. Other still-open restrictions: new occurrences whose numeric value already exists are suppressed before source audit (`if v in known:continue`); an ever-new dedicated register is allocated per joining occurrence with no freed-register reuse; only first completed history returned; candidate heuristic does not derive physical PRTA contact or witnessed absence laws. Neither v1.2 nor v1.3 establishes a full triangular algebra machine.

## New prototype

`history_key` retains every join occurrence ID, exact ordered source roles, operation and value. `prioritized_pairs` allocates the bounded candidate pair budget to recent sources first, including noncommutative orientations. Same target score, arithmetic evaluation, and source-valid independent replay as v1.2. Three ablation modes:
- original v1.2;
- corrected pair enumeration + **old numeric state identity**;
- corrected pair enumeration + **source-history identity**.

All matched depth=4, beam=4, cap_pairs=20, cap_out=16, 1,000 scored puzzles from the third-party credited exact 141086 instruction baseline.

| Mode | Proposed joins | Visited state keys | Numeric/history exclusions | Complete plans | Valid final instruction total | Single-run elapsed |
|---|---:|---:|---:|---:|---:|---:|
| Original v1.2 | 201678 | 135212 | 67466 | 11 | 141086 | 33.15s |
| Corrected pairing + numeric equivalence | 201688 | 118504 | 84184 | 11 | 141086 | 32.43s |
| Corrected pairing + occurrence history | 201683 | 202683 | 0 | 11 | 141086 | 38.25s |

**All three outputs independently validate all 1,000 puzzles**, unchanged SHA-256 `21d1d5245de5d41810e06ce6435df99059b2ba8a35f2bfcde3256e827675a5d7`. 15/15 unit tests pass. Zero new scored improvements. No new Kaggle submission warranted.

## Verified interpretation and next test

This reproduces two genuine bounded-search representation losses. Retaining all histories increases the state space, but with beam=4 and depth=4 it does **not** improve the scored portfolio. More states alone do not establish useful new constructions; no physical gate-level PRTA effect is claimed.

**Next:** derive a source-occurrence/edge-obligation/lifetime-aware **future-equivalence predicate** with a positive witness for safe merging (not numeric value equality); experimentally preserve alternate equal-valued constructors where their obligations differ; integrate a lifetime-aware 48-register emitter and score a multi-depth joint-target benchmark against an identical-budget nongeometric construction planner. Use exact QR, no conflation of literal absence, unobserved sources, numeric zero, and signed differences. Source ZIP is attached to this conversation; only findings are committed here.