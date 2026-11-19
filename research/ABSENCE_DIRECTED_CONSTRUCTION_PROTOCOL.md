# Absence-directed construction planning — research protocol v0.1

Date: 2026-11-18/19. **Status: proposed mechanism, not benchmarked.** This note is a hypothesis and test design, not a claim of additional Kaggle savings.

## Grounded source distinctions

1. CIM ECC v13 distinguishes existing numeric zero from nonexistence of a source occurrence/operation, preserves separate repeated factors and integer QR producers, and reports an unavailable slope at present y=0 separately from an existing slope of value zero. Source: `Joe-You-Know/CIM/causal-mathematics/ecc/experiments/collective_divisor_qr_v1/v13_intrinsic_properties/README_V13.md`. A missing source is **not** silently a numeric zero.
2. CIM ECC v6 independently retains two construction histories and derives rejection constraints on a **source-attested child boundary** before constructing a whole giant child table. Source: `Joe-You-Know/CIM/causal-mathematics/ecc/experiments/collective_divisor_qr_v1/v6_cross_history/NO_GIANT_CHILD_CONSTRAINTS.md`. This is an analogy for constraint propagation; not an arithmetic calculator cost result.
3. Uploaded native publication v14 source: a temporary receipt's existence does not equal valid publication, and the presence/absence of a verified final path determines whether a later recovery attempt reuses or recomputes. File: `native_causal_publication_boundary_v14(2).zip` / README. Its observed 72/72 holdout visibility accuracy is **process SIGKILL**, not hardware power loss.
4. Uploaded PRTA Factor-Family Grammar Invariants v1.2: source factor relations remain valid across declared placement changes; rigid physical rotations preserve actual contacts, but arbitrary relabelings need not. Held-out 15↔121 support change falsifies a spurious universal contact claim. Source: `PRTA_Factor_Family_Grammar_Invariants_v1_2(1).pdf`, November 17, 2026.

## Typed bounded state

Define a planner state as

`S=(W,A,U,F,L,B)`

- `W`: witnessed arithmetic occurrences with source IDs, operator, output, and register location/timestamp.
- `A`: absent / not-yet-constructed candidate events, **not** numeric zero.
- `U`: unknown candidate events for which no witness or exclusion is established.
- `F`: forbidden candidate events with exact reason: arithmetic violation, register impossible, bounded-value limit, source unavailable, or dominated by a witnessed reusable result.
- `L`: live source obligations and first-witnessed target coverage.
- `B`: remaining instruction/ register budget.

For an integer division, retain `a=bq+r, 0<=r<b`; a calculator division event is admissible only at `r=0` with positive result.

A candidate event `e=(op,x,y,z)` has a binary selection flag `x_e` in the **planner**. Setting `x_e=0` represents purposeful nonconstruction. It is *not* a calculator instruction and does not produce a value. The planner propagates consequences through producer and dependency relationships:

- An event may be selected only when its source occurrences are available.
- Each uncovered target requires at least one actual (existing or newly executed) witness.
- If target `t` is already witnessed, other producer events serving only `t` may be withheld.
- If all but one admissible producer of an uncovered target are excluded, the remaining producer is required (assuming the declared candidate set is complete for that proof scope).
- A missing source excludes downstream events dependent on that source unless an independent route establishes it.
- A forbidden operation is not equivalent to a future source being absent; the absence conclusion must have a valid scope and complete producer set.
- Register lifetimes and overwrites are temporal obligations; 48 is a cap on *simultaneously resident* values, not total historical constructions.

## First experiment / falsifiable benchmark

Build a two-layer candidate DAG from the 1,350,568-instruction incumbent, with target-relative source relations; compare:

1. Baseline fixed-event SSA allocator.
2. Conventional multi-producer DAG selection without absence propagation.
3. Matched DAG search with absence certificates, forced/forbidden propagation and optional PRTA contact packets whose physical and numeric source mapping is independently verified.

All candidates must compile to literal `[op,i,j,d]` instructions and pass independent numerical validation. A missing event receives no free arithmetic credit unless its absence actually removes a previously required operation from the emitted program.

Metrics: emitted instruction count, 1000/1000 valid target coverage, maximum register occupancy, candidate/propagation nodes visited, wall time, explicit false-exclusion controls, and savings attributable exclusively to step (3) over (2) at a matched search budget.

**Open boundary:** no demonstrated PRTA-induced Kaggle score reduction yet. Do not claim a geometric rotation is a free arithmetic operation. Do not infer factor or arithmetic properties from an arbitrary PRTA label placement that would not be preserved under a legal reassignment.
