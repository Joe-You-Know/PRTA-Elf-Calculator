# PRTA Elf v2.6 — Physical maneuver branching with instruction-count optimization audit

**Date:** 2026-11-19. Status: **implemented, 166/166 tests passing**, complete 1000-puzzle score audit and three independent scored reference-program reduction audits. **No competitive instruction savings established.** Exact reproducible Python source + test suite + JSON audit records in current conversation download `prta_elf_physical_maneuvers_score_audit_v2_6.zip`. The public authored Kaggle baseline and puzzle dataset are not claimed as new work.

## Implemented interleaved physical events

Starting with v2.5's source-occurrence-indexed arithmetic/physical search and v2.4's archive-supported pending consumers:
- **Third-turn** is performed as a real combinatorial whole-configuration rotation under the original primitive triangular incidence law, checked by independent event replay. It is not a free arithmetic transformation.
- **Transport** reroutes a still-active role-specific contact over genuine shared triangle edges while retaining the same source and receiver IDs; an independent control discharges A of `j0=2+2=4` and transports the surviving B contact from path (2,10,9,8,0) to (2,1,0), without changing the archived original source history. This proves actual rerouting in the bounded physical model, not generic mechanical realizability or a unique causal improvement in other joins.
- **Release** speculatively retires a constructed occurrence from live physical resources only after the event machine verifies no active outgoing/own contacts or pending source-owned consumer obligation. The original occurrence and exact receipts remain in the immutable catalogue/archive, and the released source cannot be used as a numerical operand again.
- **Contact policy** now branches between immediate original-receipt archive and maintaining a live original contact available for later transport. Each candidate next arithmetic join retains ordered original source identities, exact positive computation, consumer declarations before later joining, exact witnessed completion and 48-register independently verified compilation.
- **Score bound:** given public reference length L, accept a complete candidate only if its actual verified number of arithmetic instructions is <L; cap search depth at L-1. Discharge, transport, turn and release are never counted as target-producing operations. Equal-value candidate suppression persists only as a disclosed bounded-search heuristic.

## Evidence and controls

**166/166 tests pass** (158 inherited + eight new). New tests include a real source-identical transport receipt, independently replayable rigid rotation, legitimate source release with intact original archive, contest score-based search rejection, positive independently verified multi-target construction, deliberately redundant 3-to-2 program contraction, and dead-join source-occurrence slicing.

**Complete 1000-puzzle benchmark:** independent interpreter verifies all 1000 programs against exact externally authored public 141086 instruction CSV (SHA256 `21d1d5245de5d41810e06ce6435df99059b2ba8a35f2bfcde3256e827675a5d7`). Depth2, beam1, offer cap4, physical face cap4, one seed placement, maneuver cap5: 64419 numerically enumerated actions, 6651 arithmetic offers, 16049 face trials, 4102 physically accepted event states (some multiple contact-lifetime variants of the same numerical join), 9398 attempted maneuver branches, 590 successful joins *after a maneuver branch*, **zero shorter complete programs**, final **141086**. Do not confuse maneuver success with a necessary cause of that join; no paired same-face counterfactual for every accepted join.

Matched first-100 probe depth3 beam2, arithmetic cap5 face cap6: maneuver-enabled 728 accepted physical states versus 582 with maneuvers disabled. Subsequent searches differ so they are not strictly matched numeric candidate trajectories; both independently validate 14330 instructions (no savings).

**Score-directed existing-program audits, all independently validated 1000/1000:**
- Exact source occurrence dependency backward slicing: 141086→141086, zero removable instructions.
- Exact one-operation replacement of adjacent two-operation windows: 33374 candidates tested, **0** valid savings, 141086→141086.
- Exact two-operation replacement of adjacent three-operation windows: 37776 candidates tested, **0** valid savings, 141086→141086.
Separate deliberately redundant programs *do* shrink in unit tests; negative public results reflect lack of successes in these narrowly bounded rewrite grammars, not broken scoring checks or global optimality proof.

## Interpretation / next score reduction

This proves additional admissible event histories and source-preserving maneuvers under the experiment's bounded authored finite triangular grammar, plus meaningful negative evidence for local redundancy in the public program. It does **not** establish score savings. The primary blocker is **search horizon mismatch**: most public programs witness dozens of targets over dozens/hundreds of instructions, while full-puzzle v2.6 search depth is only two or three. The correct next contest-first experiment is multi-output local source-graph / cone replacement within existing long programs: identify a bounded cone with many externally consumed values/targets, synthesize a shorter shared-helper network via exact QR / MCM / joint-recipe search, compile legal 48-register replacements, and only then prove physical contacts using archive-supported PRTA events. Benchmark a candidate-matched numeric-only control and count only strictly shorter independently valid whole programs. Physical route reachability alone is insufficient. Do not report no-result as success. No changed Kaggle submission warranted.
