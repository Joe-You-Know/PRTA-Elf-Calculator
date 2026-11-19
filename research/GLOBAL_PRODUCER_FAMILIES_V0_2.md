# Global producer-family selection and packed triangle incidence v0.2

**Date:** 2026-11-19. **Status:** bounded experimental implementation, all scored programs validated, no score gain.

The executable Python implementation and tests are attached to the conversation as `prta_global_producer_families_v0_2.zip`. It includes `global_producers.py`, `triangular_faces.py`, two test modules, README, and audit JSON. It is **not** yet committed as executable source in GitHub.

## Implementation

- Derive candidate helper families from **all puzzle targets**, including exact target–source quotients with retained remainders, target differences, and target-pair common factors.
- Keep original historical construction producers as legal candidate witnesses; also generate alternate one-step producers including helper values absent from the original program.
- Jointly choose compatible producer families, build a whole-puzzle dependency closure, and emit a topologically ordered calculator program with 48-register liveness checks.
- Record unselected producers as **planning nonconstructions**, not proof of impossible values or successful computation. Typed absence is never a negative integer or free register value. Exact division requires remainder zero.
- Compare two bounded selection priorities over the **same arithmetic candidate universe**: conventional and discrete triangular-family ordering.
- Separately construct actual 3-edge equilateral-triangle incidence in finite packed hexagonal patches of 6r² primitive faces. The rigid third-turn preserves every shared-edge relationship; each triangle is the indexed primitive. Authored numeric value-to-face assignments are distinct from the physical edge graph. The physical embedding is not yet used as a proved numerical producer selection law.

## Whole-set measured result

| Measurement | Conventional | Triangular-prioritized |
|---|---:|---:|
| Scored puzzles independently valid | 1000/1000 | 1000/1000 |
| Public source score | 141086 | 141086 |
| New instruction total | 141086 | 141086 |
| Scored savings | 0 | 0 |
| Producer proposals | 1,336,419 | 1,332,352 |
| Unselected candidate records | 489,055 | 489,055 |
| Failed planner/allocator attempts safely retaining source | 379 | 466 |
| Single-run time (seconds) | 24.681 | 23.556 |

Output SHA-256 in both modes: `21d1d5245de5d41810e06ce6435df99059b2ba8a35f2bfcde3256e827675a5d7`; matches the exact publicly credited 141086-score portfolio. **No new Kaggle submission warranted.**

**Positive constructed control:** source (2,3), targets (8,12), four-step reference creates 6,8,9,12. The new helper candidate 4=2+2 did not occur in source; each mode constructs 4 and shares it for 8=2×4 and 12=3×4, totaling 3 legal steps. This validates global helper candidate generation, not a distinct PRTA advantage.

**Tests:** 10/10 pass, including exact quotient/remainder rejection of inexact division, undefined source cannot be treated as zero, construction of a genuinely novel helper, packed face three-edge incidence and bijective authored placement, and third-turn preservation of all physical edge contacts.

## Open boundaries

The numerical PRTA priority is still an authored **ordering heuristic**, not a consequence derived from actual physical contact closure. Candidate generation and recursive selection are bounded, not a complete global minimizer. Register packing remains greedy, and producer selection is not jointly optimized with register lifetimes. The user-proposed substantive next experiment is to make *verified physical contact and source-authorized joining obligations* constrain new helper-family selection, and compare an equal-budget non-geometric planner. Do not infer the entire numerical algebra from freely chosen placement alone. Do not equate unselected producers with proven impossible constructions. The public starting instructions and contest files remain uncommitted.
