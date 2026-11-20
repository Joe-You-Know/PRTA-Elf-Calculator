# v1.4 Conditional Future Equivalence: source-term alpha-isomorphism (2026-11-19)

**Result:** A scoped, constructive future-equivalence candidate found and independently tested. Executable proof-of-concept bundle in conversation: `prta_future_equivalence_v1_4.zip`.

## Definition
Every initial source occurrence retains its original source slot and numerical value, represented by `I(slot,value)`. Every constructed join occurrence has a recursively retained term `J(op,result,left_source_term,right_source_term)`. Retain **the multiset of all occurrence terms**, not just the set of numerical values and not necessarily their chronological order. Two finite histories are alpha-equivalent when their initial source slots agree and their multisets of source terms agree. Ordered source roles remain distinguishable, even for commutative arithmetic; two equal-valued occurrences are retained with multiplicity.

## Conditional finite-future derivation
When the next-step grammar allows *every ordered pair* of already constructed occurrences; exact operation semantics depend only on positive integer inputs and the declared arithmetic legality; and no other rule tests chronological epochs, physical placement, source-owned contact obligations, withheld-edge evidence, or current register location, alpha-equivalent histories possess a term-preserving occurrence bijection. That bijection maps every lawful next arithmetic join to a corresponding join with the same source-role term and output value. Inductively this yields matching finite future construction opportunities. This is **not** a theorem of unrestricted PRTA physical/algebraic equivalence. The implementation declines to merge when contact, placement, epoch, source-ID-sensitive rule, register bindings, or truncated index-biased operand enumeration is active.

## Evidence
8/8 new source-term tests pass. Exhaustive bounded two-join census starts with source occurrences (2,3), considers all ordered operand pairs and exact +, -, *, / outcomes in positive range <=50: **278 histories**, **33 numerical-value-set classes**, **223 source-alpha classes**, **55 safely merged duplicate chronological histories**, **190 distinct alpha classes that numeric-set merging would have collapsed**. All 55 alpha merges were independently checked to have identical exhaustive one-step continuation multisets. This is a small finite arithmetic event model test, **not** a scored Kaggle improvement or physical triangular contact proof.

The key representative safe merge is `2+2=4` then `2+3=5`, versus the reverse chronology, retaining the exact original operands in each join. A non-merge is `2+3=5` versus `3+2=5`: equal numbers but distinct ordered source roles. Two equal-valued but source-distinct occurrence constructions also do not disappear because multiset multiplicity is retained.

## Next
Extend future equivalence to real PRTA source-owned edge obligations, witnessed unavailable contacts, source-relative rotations, contact-transport rules, and register-lifetime boundary. Do not integrate unconditional chronological commutation if event order can change physical contact or register admissibility. Then score a v1.3 search under the strengthened safe equivalence against source-history baseline and numerical projection with independently verified contest interpreter.

Reproducible source, 8 tests, bounded census and README are packaged in the ZIP attachment.