# PRTA Elf v1.9 — witnessed one-shot contact discharge and relay reuse

**Date:** November 19, 2026. **Status:** working executable implementation, adversarial tests and two matched complete 1,000-puzzle audits; **no new scored improvement**.

**Executable source/test/audit archive:** `prta_elf_contact_discharge_relay_reuse_v1_9.zip` attached in this conversation. Includes `event_boundary_v19.py`, `elf_event_compiler_v19.py`, `test_discharge_v19.py`, inherited v1.8/v1.7 modules/tests, `README_V19.md`, and the **completed** v1.8/v1.9 comparative JSON audits. Raw third-party Kaggle programs excluded from the archive.

## Formal operational discharge condition

A source-occurrence-specific receiving obligation `(receiver, role, source)` is **dischargeable** in this authored **one-shot** triangular contact grammar if its receiver has already undergone a real positive, source-verified arithmetic join, both original role contacts were simultaneously witnessed as actual shared-edge paths at that join, and the particular role's contact remains active. Because this grammar specifies that the receiving contact's required work is completed at the join, the path may cease occupying relay faces once an immutable historical discharge certificate has been produced. If another PRTA grammar imposes additional continuing contact consumers, these must also be closed before discharge: **this prototype has not derived a universal no-pending-consumer theorem**.

The new `discharge(receiver, role)` transition independently verifies the active physical machine, captures original source/receiver IDs and recursive source terms, source/receiver physical faces, complete actual shared-edge receipt, contact construction and discharge epochs, then removes only its **active** relay/receiving-port reservation. The untouched original event ledger and new `archive` preserve historical construction. Archived contact receipts are checked against the original source catalogue, not reconstructed from current numeric values. Source release is a **separate** event that is refused while outgoing contacts remain active; archived sources still cannot be fabricated into live numeric operands. A witnessed optional withholding remains recorded after source release. Independent replay reconstructs every action from the actual seed, rejecting forged archived or event data.

## Physically specific positive result

Inputs 2 and 3 on triangular faces (2,4), finite radius 3, hop cap 4. Construct `j0: 2+2=4` on face 0 through two distinct role-specific actual paths `(2,1,0)` and `(2,10,9,8,0)`. A subsequent `j1: 2+3=5` on face 10 is blocked while face 10 remains a relay reserved by `j0`. After discharging both `j0` role contacts, `j1` becomes lawful using real paths `(2,10)` and `(4,12,11,10)`. The physical event history independently replays, and the compiled Elf program `[['+',0,0,2],['+',0,1,0]]` independently creates both targets 4 and 5. Four exact source receipts remain in the immutable archive after both joins discharge. Discharge events themselves create **no arithmetic instructions**.

## Verification

**85/85 unit tests passed**: 12 new adversarial discharge tests + 73 inherited tests. New tests include actual relay reallocation, source release only after physical contact discharge, refusal to use released numerical source, no discharge before completed join or twice, forged source/path/receipt rejection, withheld-evidence preservation, historical source ID nonreuse, independent event replay and legal register projection.

Completed **matched 1,000-puzzle screens** at depth 2, beam 2, pair cap 6, join cap 3, face cap 4, 2 source placements, radius 3, hop 4. Full original arithmetic outputs independently verified:
| Metric | v1.8 no discharge | v1.9 one-shot discharge |
| --- | ---: | ---: |
| Offered joins | 10305 | 10300 |
| Physical face trials | 35613 | 34853 |
| Bounded unresolved contact offers | 7129 | 6766 |
| Event-derived retained boundaries | 3176 | 3534 |
| Complete found plans | 0 | 1 |
| Valid scored instructions | 141086 | 141086 |
| Verified puzzles | 1000/1000 | 1000/1000 |

The **363 fewer bounded-unresolved offers** (~5.1%) arise under equal **search parameter ceilings**, not a candidate-by-candidate identical proposal list. Both portfolios are byte-for-byte identical to the publicly credited 141086-instruction starting source, SHA-256 `21d1d5245de5d41810e06ce6435df99059b2ba8a35f2bfcde3256e827675a5d7`. Single run times 30.315s and 30.529s do not establish a speed benefit. **Do not submit** the unchanged CSV.

## Research boundary

This is a constructive discharge **law for a declared one-shot receiving-contact grammar**, not automatically a theorem about every PRTA/physical relationship. The nonconstruction of an active relay reservation is not literal absence or scalar zero; its original witnessed history persists. Register allocation remains a separate 48-register arithmetic projection. Deeper global multi-target planning, proof that every future contact consumer is closed, and a source-occurrence/obligation-aware future-equivalence quotient remain unresolved. Recommended next proof: implement explicit future contact-consumer obligations and require a witnessed closure record for each before any discharging physical resource, then test long compound histories under placement/relay reuse and compare same-budget numerical and physical ablations.
