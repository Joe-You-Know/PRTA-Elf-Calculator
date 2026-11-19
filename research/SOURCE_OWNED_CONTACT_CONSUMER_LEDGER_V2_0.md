# v2.0 — Source-owned outstanding-contact-consumer ledger for PRTA Elf Calculator

**Date:** 2026-11-19. **Experimental verification:** 100/100 unit tests; complete 1,000-puzzle shallow scored audit unchanged at **141,086**. This is a typed source-contact discharge safeguard, not yet a new competition instruction saving.

**Reproducible executable source:** `prta_elf_outstanding_consumer_ledger_v2_0.zip` attached to this conversation. Includes new `event_boundary_v20.py`, `elf_event_compiler_v20.py`, `test_consumer_v20.py`, 85 inherited tests, standalone README, completed 1,000-puzzle and 100-puzzle audit JSONs. Public Kaggle puzzle data and competitor-authored CSV excluded from the ZIP.

## New obligation law

A contact's fulfilled original receiving join does **not** automatically authorize discharge when additional source-owned future consumers have been declared.

Each `ContactConsumer` is a distinct typed record with `(duty_id, receiver occurrence, receiving source role A/B, owner occurrence, kind, required future join ID, optional flag, status, witness)`. It is **indexed by occurrence identity, not numerical value**. The finite active-contact ledger admits:
- `declare_consumer`, only while the real contact is physically active, requiring a fresh identity;
- `complete_consumer`, either by an explicit witnessed contact-observation event on the active actual-edge path, or by an actual recorded future arithmetic join **using the exact owner occurrence ID**;
- `exclude_consumer`, only for an explicitly optional duty whose owner previously produced a matching `withhold(...,'optional:duty:<ID>',witness)` source event. An unobserved, pending or mandatory duty cannot be excluded;
- `discharge`, only once there are no pending declared duties for that receiving occurrence/role and the original receipt is physically valid; retains immutable source, path and closure history;
- `release`, refused while the source owns pending consumers or still retains active receiving or outgoing contacts.

Future-equivalence boundaries retain each duty's identity, ownership, status and witness. Independent event replay reconstructs every action and refuses forged witness/history data. Withholding never becomes binary zero, a negative value, a free arithmetic value, or a false claim that the underlying source is nonexistent.

## Positive and negative controls

One physical join `j0:2+2=4` has two genuinely routed original role contacts. Two separately identified consumers of role B must *both* close; completion of the first alone blocks discharge. A later `2+3=5` join requires relay face 10 and is blocked while B's original route still reserves it. One required consumer is explicitly witnessed through its live contact, and another optional consumer is excluded only through a matching source-owned witnessed withholding. After B is fully discharged, the relay is re-used by the new lawful join; the immutable original edge receipts and consumer statuses remain auditable. A `use_in_join` consumer is independently checked against a later actual arithmetic event using the **exact occurrence ID**. Repeated equal-valued occurrences with different source-joining terms remain distinct. Premature release, duplicate duty names, forged receipts, re-labeled identities, after-discharge obligation insertion and mandatory exclusion are rejected.

## Completed benchmark

- **100/100 unit tests passed**: 15 new consumer tests plus 85 inherited v1.9 tests.
- Full 1,000-puzzle v2.0 shallow search: depth 1, beam 1, pair cap 4, offer cap 2, face cap 2, radius 3, two placements, hop 3. Generated 3,976 proposed joins, 7,253 face trials, 3,105 contact-bounded unresolved, 871 boundaries; **all 1,000 independently valid**, final **141,086** unchanged, SHA-256 `21d1d5245de5d41810e06ce6435df99059b2ba8a35f2bfcde3256e827675a5d7`.
- Matched first 100 scored puzzles at depth 2, beam 2, pair cap 6, offer cap 3, face cap 4, two placements, hop 4: v1.9 and v2.0 each offer 1,053 joins, 3,542 face trials, 679 unresolved and 374 retained boundaries; **14,330** independently valid instructions, no improvements. Single execution times are not stable runtime evidence.
- An attempted **1,000-puzzle depth-2 run timed out**; no completed claim is made for that run. No Kaggle submission warranted.

## Formal scope/limits

This is a **sufficient discharge rule for a closed, explicitly declared future-consumer specification** within a finite authored physical contact grammar. It does not infer every future consumer from a universal PRTA joining law. The explicit contact-observation event is a declared verification action, not an instrument-measured device event. Optional exclusions require an authored optional contract and a matching witnessed nonconstruction, not a mathematical proof of universal impossibility. The scored compiler currently auto-declares and witnesses immediate contact-consumption duties, but does **not** generate arbitrary deferred consumer dependencies across deep PRTA compounds; this explains why the score and most scored search counts are unchanged. The next defensible improvement is to derive the complete consumer ledger from a real multi-stage source-joining specification *before* any discharge, with relay-lifetime scheduling and a multi-depth search that actually exercises competing future contacts.

Original result provenance: externally credited public 141,086-instruction starting portfolio. No user information, credentials or secrets stored here.
