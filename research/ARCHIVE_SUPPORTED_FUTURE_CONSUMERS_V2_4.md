# PRTA v2.4 — Archive-supported future consumers (2026-11-19)

## Tested implementation

Executable source bundle: `prta_archive_supported_future_consumers_v2_4.zip` in conversation (SHA-256 `fd93aa89321c796c7524c07da558d76cea023241bce6a0dfcaf3f9658d4b6c78`). Includes separate `event_boundary_v24.py` (original `event_boundary_v20.py` unchanged), `archive_plan_v24.py`, `test_archive_consumers_v24.py`, `test_archive_plan_v24.py`, `audit_archive_v24.py`, result JSON and README, inherited source and tests.

**149/149 tests pass:** 132 inherited, 17 new. Independent replay recomputes all transitions from initial source occurrences.

## Alternative rule

For any original receiving-contact receipt `(J,A/B)`, a pending *future numerical use* consumer is supported by its source-owned **immutable original contact archive**, while its old physical edge path and relay reservation may discharge before that future use occurs. **Pending remains pending**. The exact source occurrence J must remain live and must be named in the later real arithmetic join event. The consumer closes only when its required later join and specified operand role are witnessed. Archived source identities, source/receiver terms, actual triangular edges, receipt epochs, event chain and resulting 48-register arithmetic output remain independently checked.

By contrast, a pending `observe_contact` consumer cannot discharge: archived history is not an observation of a required live path. An archived source with pending use duties may not be released. Explicit future consumers may be attached to a discharged contact later if the original owner remains live, but this **open-plan** option cannot retroactively prove completeness of all future obligations. `archive_plan_v24` supports a stronger **closed-plan** case: derive all mandatory source-and-role-specific consumers from an immutable multi-stage joining plan before construction; verify exact ledger after each step, while allowing physical discharge even before downstream use occurs.

## Equal-bound physical counterexample

Initial source 2 at triangular face 2, 3 at face 4; radius=3, max hops=4. Source occurrence `j0=i0+i0=4` physically built at face 0 with two noncolliding contact routes. Two source-owned `use_in_join` duties for future `j1=j0+i1=7` in **left** role are declared. Under guarded v2.0: both discharges refused and **zero** lawful receiving faces for j1 among all faces of the same finite patch and hop setting. Under archive-supported v2.4: both discharges succeed; **both obligations stay pending**; four lawful receiving faces for j1: **9, 10, 11, 20**. Actual join at face 9 closes the two future duties. Both original contact receipts persist; independent physical history replay and independent Elf interpreter confirm `[['+',0,0,2],['+',2,1,3]]` witnesses targets 4 and 7. Early release of j0 rejected before future use; forged archive, source or operand-role and event-ID mismatches rejected. The archived historical contacts create no new numeric values.

## Interpretation, verification boundaries and next

This demonstrates that compulsory active contact persistence is **not necessary under the alternative authored future-use grammar** to retain exact source and realize later joins. It does NOT prove all PRTA physical contact obligations may be archived; live-path observations remain different. No full Kaggle 1000-puzzle run in v2.4, no score benefit claimed. Externally credited public baseline remains 141086. Next: run **multi-depth, multi-target graph invention with this archive-supported discharge law**, preserving source occurrence and pending duties across physical scheduling. Compare against guarded policy with equal candidate and contact budget and independently validate every winning program; do not assume a score improvement.

Note: Cortex memory write quota previously exhausted; GitHub is current durable research ledger.