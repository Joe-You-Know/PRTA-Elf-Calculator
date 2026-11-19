# PRTA collective marginal entire-helper DAG v1.0 — 2026-11-19

**Artifact:** `prta_collective_marginal_dag_v1_0.zip` (conversation attachment): executable `marginal_planner.py`, `test_marginal.py`, previous v0.9 modules, README, completed 1,000-puzzle audit. **Source code in ZIP, this file is the GitHub research record.**

## New measurement

The old v0.9 planner ranked helper H by number of target obligations referencing it, an unreliable proxy for savings. v1.0 computes the full dependency closure of H, with every actual source operation counted, then constructs the complete target DAG with the shared helper producers forced, counts shared constructed events **once**, and reports (a) seed-only ancestor event count, (b) extra events against unforced network, (c) removed events, (d) entire DAG event-count change. These are exact counts for **the specific source-valid dependency DAGs found** by the bounded recursive chooser, not a proof of globally minimal cost.

Every candidate passing this event bound is compiled into legal 48-register arithmetic instructions and independently replayed for source validity, target coverage, bounds and exact integer division. Failed allocation or unconstructible dependencies do not cause numerical zero or an inferred absence. Physical/source-contact acceptance hook remains available but was never used on a scored improvement.

## Controls

Starting (2,3), goals (8,12), four-step reference, helper H=4 can be built using 2+2, then targets 8=2×4 and 12=3×4. Full helper ancestor closure **1** executed event; entire shared target network **3** events, legal and verified (one better). An apparent helper that feeds both targets but has an unconstructible cyclic dependency is rejected. Full v0.9 and v1.0 unit tests **11/11 pass**.

## Completed 1,000-puzzle audit

Exact independently validated public competitor-attributed 141086-instruction source program. Same candidate pool, cap 32 new helpers/puzzle, 8 ranked seed helpers, at most 10 seed-family offers, recursive beam 4; single local run 30.805 s.

- Target control: 1000 attempted baseline closures, 3 allocator/arithmetic rejections, final **141086**.
- Full-DAG marginal planner: **3322** complete candidate networks, **10978** joint dependency-unresolved offers, **10** unresolved standalone helper closures, **11** allocator/arithmetic rejections, **zero** shorter scored programs, final **141086**.
- Both independently replay valid on all 1000 puzzles, both output SHA256 `21d1d5245de5d41810e06ce6435df99059b2ba8a35f2bfcde3256e827675a5d7`, byte-equal to the external public starting source.
- Unforced candidate network event total 141080 is **not a verified 141080-instruction program**; do not conflate graph event counts with allocated legal instructions. The public 141086 remains the only scored-level validated number.
- No Kaggle submission warranted.

## Scope and next action

The seed discovery still starts from direct multi-target usage and is limited to single-helper seeds, even though ranking evaluates complete deeper ancestry. It is **not** global proof of optimality, nor complete global multi-depth multi-helper construction. The inherited source value DAG chooses a numerical value's producer rather than exhaustively branching all equal-valued occurrence identities. Genuine PRTA physical contacts and conditional no-goods are not scored-tested here. Next: generate *reachable multi-depth helper subgraphs* as candidate hyperedges first; jointly choose several helpers; incorporate exact incremental register lifetime cost and source-occurrence conditioned physical conflict guards, with matched nongeometric ablation.
