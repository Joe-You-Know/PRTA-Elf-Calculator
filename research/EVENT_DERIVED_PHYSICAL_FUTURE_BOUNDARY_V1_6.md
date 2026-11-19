# PRTA v1.6 — Event-derived source/contact future boundaries

Date: 2026-11-19. Status: **tested finite event-machine extension**, NOT full PRTA future-equivalence theorem and NOT an improved Kaggle Elf score.

## Motivation and substantive correction
v1.5 verified a strong boundary equality rule on histories that had been externally assigned a common posthistory physical/register boundary. v1.6 obtains the boundary **only by executing and independently replaying the original lawful construction events**. A boundary cannot be certified solely from an asserted matching tuple or a fabricated path.

## Executable implementation
Delivered artifact: `prta_event_derived_future_boundary_v1_6.zip` in current conversation, containing `event_boundary_v16.py`, `test_event_boundary_v16.py`, `audit_event_boundary_v16.py`, inherited `future_equivalence_v14.py`, `future_equivalence_v15.py`, combinatorial `triangular_faces.py`, detailed `README_V16.md`, complete audit JSON and test log.

Supported event types:
- `join`: actual positive integer arithmetic with source IDs and roles; new output owns a real triangular face/register; both exact source-to-output contact paths verified simultaneously (complete common-edge witnesses, separate incoming ports, no relay overlap).
- `turn`: rigid combinatorial third-turn of *all* placed occurrences and active contact paths. Re-verify shared edges. No orthogonal geometry or metric-angle primitive.
- `transport`: physically certified replacement contact path, retaining original source and receiver; test includes an executed **five-edge multi-face alternative route**.
- `withhold`: separately witnessed purposefully unconstructed **optional observation action**, never numerical zero or an absent source. Its permissibility is an **authored policy** in this experiment.
- `release`: frees occurrence and its own contact receipts only if it is not a live dependency of another result. Original contact history preserved in event ledger.
- Every event changes explicit integer epoch; live source deadline, contact path, face occupancy, 48-register-like **bounded register assignment** (8 in control), and typed absence evidence remain future-relevant.

## Conditional future-equivalence theorem for declared event grammar
Compare verified posthistory state fields: exact initial source identities, live source occurrences with recursively retained ordered source terms and numeric values, physical face and register bindings, deadline and epoch, current contact paths and complete actual edge receipts, source-indexed witnessed optional omissions, and declared patch/hop/register/grammar parameters. The full event ledger is separately retained for independent replay; it is not itself automatically necessary to distinguish future behavior if the declared transition rules never inspect historical events except through the retained boundary. For this finite deterministic transition grammar, equal derived boundaries imply matching enabled next actions and corresponding resulting boundaries; iterate through finite futures by induction. This is **sufficient, conservative, grammar-relative**, not universal PRTA equivalence.

## Completed verification
Run `py -m unittest -q test_future_equivalence_v14 test_future_equivalence_v15 test_event_boundary_v16`: **52/52** passed (23 inherited, 29 new). `py audit_event_boundary_v16.py` independently replays **six** representative concrete event histories. One positive commutation test: using the same two original source occurrences, independently construct `5=2+3` and `6=2×3` in opposite orders. Event logs differ but the verified final physical/source/register/temporal boundary is the same. Negatives: witnessed omitted observation changes boundary; rigid turn changes placement; real five-edge transport changes path; three turns restore face incidence but spend epochs; source lifetime/register differences block equivalence; source release with unresolved downstream obligation is rejected; fake contact/receiver edge, missing join witness, nonexistent operands, inexact quotient and forged historical event payload are rejected. A test shows a forged first event prestate can pass naive adjacent-snapshot checks but not independent replay.

**No full Kaggle 1,000-puzzle search rerun in v1.6**, no instruction reduction. Last independently verified external public portfolio baseline remains **141,086**.

## Evidence limitations / next work
- Current contact grammar is an experimentally authored subset. Does not yet implement every PCL/PRTA primitive rotation, row-compound obligation, or genuinely derivable effect of nonobservation.
- Current equivalence uses strict source-occurrence IDs rather than a general proved alpha-renaming under physical source contacts.
- Withheld action requires a declared optional policy witness; autonomous physical consequences are not demonstrated.
- The complete original history is replayed to justify poststate reachability; long-term contact discharge and register lifetime compaction remain open.
- Next: integrate event-derived states into forward multi-target Elf synthesis, use proven boundary congruence to deduplicate, retain real registers under lifetime and contact constraints, run a matched comparison with source-history and numeric-only ablations. No withheld action may substitute for a target-producing arithmetic instruction.

Archive contains exact implementation and reproduction instructions.