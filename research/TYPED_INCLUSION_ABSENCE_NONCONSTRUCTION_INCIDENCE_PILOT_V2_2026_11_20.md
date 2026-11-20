# PRTA–Elf v2: typed inclusion/absence incidence pilot — 2026-11-20

**Question from user:** Every number, operator, relation and join needs an independent occurrence identity and set membership. The user's *unequivalence* is not ordinary inequality, indices are not necessarily a sequence, and each distinguishable participant can be represented as included or absent relative to a specific join. The source should preserve whole causes and effects rather than only arithmetic counts.

## Executed real Elf source

Reopened original complete operator-occurrence atlas v1 from user-provided conversation ZIP and extracted verified strong-submission scored puzzle `scored_0126` (input `3`, targets `1,2,5,8`), with its actual four original instructions:

1. `["/",0,0,1]` yields 1 from 3/3 (exact QR);
2. `["+",1,1,2]` yields 2 from 1+1;
3. `["+",0,2,3]` yields 5 from 3+2;
4. `["+",3,0,4]` yields 8 from 5+3.

**Do not conflate source role with numerical identity:** both operand roles in division0 use original `in:0`, but are separately typed left and right participation occurrences; all operators have their own IDs `op:0..3`, outputs `out:0..3`, separate result relation entities.

## Implemented typed participation

SQLite `entities`, `joins`, `obligations` (unordered typed roles), `participation` (context, join, role, entity, included/absent/unresolved, reason), `evaluations` (admission), and `unavailable` (explicit controlled nonconstruction). **Result and result-relation are effects**, not original prerequisites. Each operator/operand is a prerequisite, and each admitted instruction produces its original result. Missing operand/operator propagates into dependent join nonadmission. A separate **derived simultaneous-source-query** joins the exact original source `in:0` with recorded consumers `op:2` and `op:3`; it is an unordered higher-order source-incidence condition and does not claim concurrent machine execution or native geometric contact. A hypothetical never-attempted operator candidate stays **unresolved**, not automatically absent.

15 entities; 6 joins (4 arithmetic, 1 shared source, 1 unresolved candidate); 4 contexts; 24 evaluated joins; 100 typed incidence records. Actual original replay admits all 4 arithmetic joins and shared-source query. **Controlled counterfactual replays, not historical native events:** withholding operator `op:1` admits 1 and withholds 3 downstream; withholding result effect `out:0` admits 0 and withholds all 4; withholding original input `in:0` admits 0 and withholds 4. Each case withholds shared-source query. Candidate operator remains unresolved in all four.

Independent verifier replays original CSV arithmetic and original exact operand occurrence identities; tests all context admissions, five typed source/effect roles, shared-source query, unresolved candidate. **12/12 directed regression tests PASS**, including altered operator-admission rejection and altered effect-status rejection. Original v1 134002-instruction atlas remains separately preserved; no claim of whole-atlas rollout, new Elf instruction savings, previously witnessed historical failure, or derived PRTA geometry.

## Artifacts

Reproducible self-contained ZIP `prta_elf_inclusion_absence_atlas_v2.zip`, SHA256 `9df7b2314d365892d7700a1d46403f16a4ff566cb25e1db89ee07d997c7b34d7`. Includes independently extracted 4-operator source SQLite, exact original official puzzle and strong submission CSVs, pilot incidence SQLite, code, independent verifier, tests, JSON results, README, LaTeX source and successfully compiled 2-page PDF. From package run `py incidence_experiment.py`, `py independent_check.py`, `py -m unittest -v test_incidence.py`.

## Next research

Generalize typed incidence and witnessed nonconstruction data schema to the full 1,000 puzzle and 134,002 operator atlas without treating all unattempted combinations as absent. Define the user's unequivalence operation only from explicitly specified join/prepend/append/concatenation construction laws, distinguishing set-index incidence from arithmetic numerical inequality. Derive higher-order intersections on observed event incidence rather than inventing geometric contact.
