# PRTA Elf v2.1 — Source-Indexed Multi-stage Future Consumer Derivation
Date: 2026-11-19. Status: **working finite closed-plan derivation and event-derived discharge verification**. Complete runnable ZIP attached in conversation as `prta_elf_derived_multistage_consumers_v2_1.zip`.

## Correction to v2.0
v2.0 allowed manually declared contact consumers and discharge when no declared pending duties. v2.1 first examines an entire **committed, acyclic source-occurrence joining plan** and derives all direct future-use duties before running any joins or attempting discharge. An output source occurrence J later used by K in role rho creates a separate mandatory consumer on **each of J's original receiving contacts A and B**, identified as (J, original_role, K, future_operand_role). If K uses J in both operand roles, four distinct duties arise, without a fabricated second source. No optional exclusion is invented.

The plan itself retains unique source IDs, original ordered operand roles, exact positive-integer arithmetic and a SHA-256 content fingerprint. A v2.1 verified execution must match the plan's join prefix exactly, possess the complete derived duty set (not a voluntary subset), and independently replay every v2.0 event and historical contact. A pending duty cannot be closed without its actual specified subsequent join using exactly the indicated source occurrence. `verify_execution` rejects a direct v2.0 bypass that omits consumer duties or changes the plan digest. Unlike v2.0, this gives a closed-world justification for the completeness of the ledger **relative to the committed plan**.

## Verified physical 3-stage control
Inputs (2,3) at faces (2,4), radius 3, hop cap 4. Original multi-stage plan:
- j0: i0+i0 = 4, receiving face 9
- j1: j0+i1 = 7, receiving face 11
- j2: j1+i0 = 9, receiving face 10

After j0, the two original receiving contacts remain active with mandatory pending duties for j1. After the actual physically routed j1, those obligations are witnessed and the two j0 contacts discharge, while two new j1 obligations for j2 remain active. After actually routing j2, all four derived duties are witnessed and all six original source-contact receipts are immutable archived history. Independent replay and arithmetic verification pass. Actual calculator instructions: `[['+',0,0,2],['+',2,1,3],['+',3,0,1]]` (5-register capacity control, legal under 48-register cap). The evidence is in `audit_v21.json` and tests.

Adversarial: a future join in a different placement can become physically unroutable if earlier contacts must stay live. The implementation refuses to violate the pending obligations just to free relays; bounded failure is *unresolved*, not impossible.

## Tests and boundaries
**116/116 regression tests pass:** 100 inherited v2.0 + 16 new derivation, binding, bypass, exact arithmetic, repeated-role, two/three-stage and replay tests. This is an executable, finite *plan-execution layer* built directly upon the real v2.0 triangular incident-face and event replay code. It is **not yet integrated into full 1000-puzzle search** and does not improve the known 141,086 public baseline. It proves exhaustive duties only for the declared, closed plan; does not infer all future consumers from geometry alone nor prove a unique future. Future proof: plan-boundary closure and contact-route-aware scheduling in multi-target search, jointly with register allocation.

Reproduce with `py -m unittest -q test_future_equivalence_v14 test_future_equivalence_v15 test_event_boundary_v16 test_elf_event_v17 test_elf_event_v18 test_discharge_v19 test_consumer_v20 test_derived_multistage_v21`.