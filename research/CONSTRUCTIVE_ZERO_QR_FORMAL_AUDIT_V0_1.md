# Constructive zero, quotient–remainder and failed division attempts — formal audit v0.1

Date: November 19, 2026. **Source-grounded clarification and operational proposal; not a claim of new PCL theorem or Kaggle score improvement.**

Primary uploaded sources read: `primitive_constructive_logic_complete_proof_v1_0.pdf`, Sections 3, 10, 24–29, 38; `primitive_constructive_algebra_v0_4.pdf`, Sections 1–3 and quotient-lane discussion; `PRTA_Factor_Family_Grammar_Invariants_v1_2(1).pdf`; `PRTA_v122_exact_occupied_absent_transport(1).zip` README and original source-boundary claims. The PCL source was already explicit; previous conversation conflated distinct types.

**Established in PCL v1.0:**
- Literal absence has no object, report, index, or representable mark. A constructive zero is a **distinguishable typed report** of no declared contribution or remainder, not literal nonexistence (Definitions 3.1–3.3).
- Division by an actual positive grouping template is a source-preserving extraction ledger `D(X,B;gamma)=(X,B,Q,R,gamma)` with count projection `N=k*b+r`, `0<=r<b` (Definitions 24.1–24.2).
- With `0<=N<b`, there are no complete extracted groups; the dividend survives as the entire remainder. This is the apple-box case (Section 29).
- With an exact positive-template extraction, there is a differently typed zero-remainder **closure** report (Definition 26.1).
- With a zero-contribution divisor, a completed ratio cannot be constructed: PCL Theorem 38.1 expressly rejects a numeric quotient/infinity/zero assignment. A zero symbol's existence does not furnish a positive divisor template.
- A negative signed relative difference is not the physical absence of an occurrence, not a constructive zero report, and not the same type as a witnessed extraction failure.

**New proposed operational extension, NOT a PCL theorem:** define a typed `Attempt(X,B,gamma)` returning `Completed(D)` when `|B|>0`; otherwise a distinguishable `Failed(X,B,gamma,NoPositiveTemplate)` report **without numerical quotient or normalized remainder**. This retains an attempted `/0` operation's source and intention without misrepresenting it as successful division.

**Notation:** User's `0_q*q+N=N` is meaningful as shorthand for no complete grouping of size `q` when `0<=N<q` and `q>0`. To disambiguate the group size from quotient count, write `N=0*b+N`, with a separate source-indexed zero-*group* report. This is distinct from an exact-remainder zero and from division by a zero-contribution denominator.

**Checks:** Six Python standard-library tests passed: one apple / two-apple group, exact remainder closure, two distinct zero-source reports with same scalar projection, no positive-divisor-template failure, zero dividend with positive divisor, and required extraction-rule identity.

**PRTA/compiler boundary:** Record authored value-to-face mapping, actual oriented edges and source-owned contacts, construction vs witnessed lack vs unresolved; never equate a freely relabeled geometric neighbor with a proven numerical relation. An absent construction can prune a planner obligation but does not directly produce a Kaggle value or authorize division-by-zero.

LaTeX source, compiled four-page PDF and source/test scripts were delivered as `constructive_zero_qr_v0_1.zip` in the conversation. No revision of the user's canonical PCL paper was made, and no leaderboard improvement is claimed.
