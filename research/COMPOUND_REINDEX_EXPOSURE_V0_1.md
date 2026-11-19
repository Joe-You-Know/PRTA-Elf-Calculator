# Deliberate compound reindexing / shared-helper exposure v0.1

Date: 2026-11-19. **Source-identified, bounded negative scored result**, with a successful constructed control.

## Constructed rule
When an already witnessed helper occupies register d, an overlay writes d, and a later instruction reconstructs that same helper before any intervening access to d, the planner can relocate the overlay to another safe register k (where the prior contents will not be read before its next write) and withhold the helper rebuild. Every actual overlay target is still constructed. All source register reads are checked and every candidate undergoes full numerical validation. This uses three structural contact roles, no angle calculations and no absent numerical values.

**Control:** starts (2,3), targets (10,21,35), limit 100, 7 registers. Original: 5=2+3; 7=5+2; overlay 10=5+5 overwrites 7; rebuild 7; 21=7*3; 35=7*5 (six instructions). Relocate 10 construction to a safe register, preserve 7, omit helper rebuild: **five instructions** with all three targets still witnessed. This is a source-valid allocator/dataflow optimization; PRTA geometric attachment is not independently proved.

## Full comparison
Input: exact publicly credited 1,000-puzzle portfolio at **141,086 instructions**. The targeted first-overwrite/next-write helper-restoration search found **zero** eligible local pairs; no program changed. Output still **141,086**, independently validated 1,000/1,000. SHA-256 `21d1d5245de5d41810e06ce6435df99059b2ba8a35f2bfcde3256e827675a5d7`, identical to the public baseline. Four focused unit tests passed, including a mandatory overlay witness and an allocation guard. An auxiliary trace census found only **six** repeated previously produced numerical values across the entire public portfolio, and these were long-distance cases not addressable by the local move.

## Scope and next step
This does **not** prove the absence of profitable whole-compound rewrites. It shows that this precise source-preserving overlay relocation rule is exhausted on the strong current public programs. No new Kaggle submission is warranted. Next test must invent helper values/compounds and reschedule multiple source obligations jointly, rather than only relocate a witness in the existing event order. Compare against an identically budgeted conventional graph optimizer, and retain full source and edge-joining certificates.

Working Python code, independent validator, four tests, and detailed README are provided to the user as `prta_compound_reindex_v0_1.zip`. The archive contains no contest dataset or large output CSV.