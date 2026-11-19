# PRTA discrete gate observation interventions v0.2 — 2026-11-19

**Scope:** Executable discrete causal event model, **not** transistor/device simulation. Source ZIP `prta_discrete_gate_event_boundary_v0_2.zip` attached in this conversation.

## Tested question
Keep source bit occurrence, existing substrate and fixed authored contact law unchanged. Vary only whether a sensing request is constructed; distinguish source presence, request, purposeful nonconstruction, output state, observer measurement. With the **stipulated** contact law, a sensing request constructs an overlay reporting 1; withholding it leaves an already existing substrate reporting 0. The underlying bit is present and may be 0 or 1 in either history. There is no assigning the unobserved bit 0 or 1, no use of a signed difference as absence, and no causal output constructed out of literal nonexistence.

## Evidence
Original 7/7 primitive gate tests rerun; new 10/10 event-boundary tests pass. For each input bit (0,1), authored overlay intervention yields requested output 1, withheld output 0, independent observer reports accordingly, one fewer modeled sensor read and one fewer modeled overlay contact event. If terminal output is forced 1 independent of sensor history, output remains 1; if overlay equals substrate 0, output stays 0. Ordinary short-circuit AND/NAND/OR eager vs causal outputs always agree despite omitted reads. Thus a policy-dependent output difference is distinct from shortcut observation savings.

## Limitations
The sensor-to-overlay coupling is itself an explicitly authored law. Therefore this is a demonstration of **conditional effect within that model**, not proof of an autonomous physical effect caused by lack of observation, energy reduction, transistor area halving, a new triangular gate fabrication, or a novel consequence beyond standard causal interventions. Counted events are ledger events, not transistor switching. The next meaningful test needs a specified real circuit/netlist with contact coupling, independent observer, controlled inputs and enable, and quantitative electrical validation. Source code, tests, README, and audited benchmark JSON in attached ZIP.
