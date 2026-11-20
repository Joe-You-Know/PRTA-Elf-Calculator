# Occurrence-indexed simultaneous source-contact compiler v0.5 — 2026-11-19

## Delivered executable
Conversation attachment: `prta_occurrence_indexed_compiler_v0_5.zip` containing `occurrence_compiler.py`, 10 unit tests, inherited source code (physical triangular faces, v0.4 multi-face transport, v0.2 global numerical producer selection), README, two completed benchmark audits, and test log. No competition datasets or public third-party CSV included.

## Newly implemented
- Every numerical construction source event has a unique occurrence ID, even when a later event reconstructs the same numerical value. Initial occurrences are separately identified. Each occurrence retains its birth and last input-use epoch.
- Each selected arithmetic producer has two distinct source-role-to-receiver **contact obligations** at its construction epoch. The compiler checks these simultaneously, with every relay route a walk over actual full-edge adjacency and explicit shared-edge proof receipts.
- No numerical source may reside on a relay face while its lifetime covers that contact epoch. Two incompatible simultaneous contacts cannot use the same relay. Source-distinct inputs cannot claim a single receiver entry port.
- Physical search jointly selects occurrence-to-face assignment and event-time relay paths within a finite search budget; exhausted search is **unresolved**, not an absence theorem. Relay faces are contact provenance, not numbers.
- Bounded global numerical producer-family selection is inherited from v0.2, including newly invented shared helpers from all target exact quotient-remainder relationships. Existing 48-register compiler independently validates target coverage, integer division, register sources and bounds.
- This version tests the **single selected** global numerical family for physical feasibility, rather than jointly finding alternate family assignments after physical rejection. This is an important unsolved integration boundary.

## Controls and results
A controlled arithmetic puzzle starting (2,3), targets (8,12) has a 4-instruction reference; both conventional and physical modes invent/retain a shared helper and compile a valid **3-instruction** program. The physical mode certifies **6** source-role edge-contact receipts spanning the 3 constructed events. This is a control, **not a new scored improvement or a claim that geometry caused the arithmetic saving**.

Ten new tests pass: source ownership, duplicate-value occurrence distinctness, contact completeness, lifetimes, forged-edge rejection, occupied-relay rejection, missing source and wrong arithmetic rejection, global helper control.

The matched scored audit used the exact publicly credited 141,086-instruction portfolio on 1,000 puzzles:
- Conventional whole-network selection: 141,086, 1,000 valid; 379 allocator-rejected plans, 621 not shorter.
- Identical arithmetic selection with occurrence-indexed physical certificate required for shorter candidates: 141,086, 1,000 valid; 379 allocator-rejected, 621 not shorter.
- SHA-256 both: `21d1d5245de5d41810e06ce6435df99059b2ba8a35f2bfcde3256e827675a5d7`, identical to third-party credited baseline.
- **No scored candidate was shorter, so physical gate was never exercised on a scored improved plan.** Timings of one run (22.777 s vs 22.179 s) should not be interpreted as a speed difference.

## Epistemic boundaries and next action
The authored numerical-to-face assignment is an experiment, not a physical theorem forcing arbitrary arithmetic identities. The contact path is not arithmetic evaluation. Source selection for repeated equal-valued occurrences currently resolves to the latest available occurrence rather than searching all source-identity alternatives. The physical search is bounded; 48-register allocation is greedy. This is not yet a fully joint global producer-family + geometric-placement optimization engine.

**Next test:** physical-routing failures should feed back into global source-occurrence producer selection and select an alternate complete family before compilation, with simultaneous contact/relay lifetimes and matched equal-budget nongeometric control; then test scored instruction savings and lifetime-aware allocator. No Kaggle submission warranted for unchanged public baseline.
