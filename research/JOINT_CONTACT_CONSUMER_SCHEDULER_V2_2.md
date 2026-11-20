# PRTA Elf v2.2 — Joint contact / relay / consumer scheduling

Date: **2026-11-19**. Result: **implemented, 127/127 tested**, independently replayed finite source-specific physical join histories and actual calculator programs. Complete runnable artifact attached in conversation: `prta_elf_joint_contact_consumer_scheduler_v2_2.zip` (source, 127 test suite, audit JSON, README).

## Change from v2.1

v2.1 accepted an already ordered, face-assigned closed plan; a poor choice could permanently block subsequent contact routing when pending future use prevented discharge. v2.2 starts instead with a *closed, unordered, acyclic graph of exact arithmetic joins* (immutable original source occurrence IDs and ordered operand roles; arithmetic graph is still authored, **not discovered**). It derives every mandatory direct future-consumer duty from this graph **before** search begins and before any discharge decision. Each consumption of constructed J by K generates two source-owned duties, on J's original A and B input contacts; J used twice generates four distinct duties. No invented second source or optional exclusion. An invalid/ cyclic graph, invalid arithmetic or dangling source is rejected before search.

The DFS jointly chooses which ready arithmetic join to build, its physical triangle receiving face, the pair of simultaneous actual shared-edge contact paths, a valid virtual register and which original contacts can discharge once their *specific* pending duties have been witnessed. The v2.0 physical event machine independently verifies each event and historical source ownership. No duty can close merely by numerical value equivalence; exact source occurrence and role are checked. Original contact receipts remain archived when a relay is freed. Optional rigid turns and source-preserving contact transport are supported as bounded candidate actions, but no successful control needed them, so no maneuver advantage is claimed. Conservative v2.0 `future_boundary` used as state key; no merges demonstrated.

On completion, derive the complete chronological `CommittedPlan` through independent v2.1 `derive_plan`, ensure its entire duty ledger equals the execution's derived ledger, independently replay history from original source placements, and emit/verify a legal <=48-register Elf program.

## Positive test and measured audit

With initial occurrences 2 and 3 on actual faces (2,4), radius-three triangle patch and hop cap four:
- Previously fixed schedule `j0=2+2=4` face 0 followed by `j1=4+3=7` face 9 **fails** due to simultaneous physical paths unavailable while previous pending consumer obligations cannot be discharged.
- Joint v2.2 scheduler automatically finds faces **(9,11,10)** for `j0=2+2=4`, `j1=4+3=7`, `j2=7+2=9`. **47** join/face offers; **42** bounded contact rejections; **5** accepted candidate placements; **6** DFS nodes; **1** completed history; **6** lawful original-contact discharges and archived receipts; **4** fully witnessed future duties; **17** recorded events. Independently verified program `[['+',0,0,2], ['+',2,1,3], ['+',3,0,1]]`. The v2.1 verified execution and contest interpreter accept the result.
- Two independent target constructions `2+3=5`, `2*3=6` have both source-order schedules admitted and replayed across candidate face placements. **36** complete candidate histories found within the bounded 50-solution cap; no numerical-value-based source merging.
- Insufficient face cap results in *no completed plan*, not a geometric impossibility claim; node cap 1 is reported `incomplete`.

**127/127** regression tests pass: 116 inherited and 11 new. Source bundle: `joint_scheduler_v22.py`, `test_joint_scheduler_v22.py`, `audit_joint_v22.py`, full previous source, audit JSON, README.

## Current verification boundary and next step

Complete 1000-puzzle scored Kaggle run **not done**. Last independently verified, externally credited baseline **141,086**; no score gain claimed. More importantly, v2.2 searches join chronology, contact placement and relay discharge **given** a closed multi-stage arithmetic graph, not the arithmetic producer/helper graph itself. Physical joins still use an authored bounded triangular contact grammar, non-arithmetic turns/transports not measured as advantageous, no alpha future-boundary compression and no active source-release in the scheduler. Next: integrate arithmetic graph invention jointly with contact/consumer planning and register last-use while keeping a closed-plan proof boundary; measure equal-budget controls rather than presuming a scored improvement.
