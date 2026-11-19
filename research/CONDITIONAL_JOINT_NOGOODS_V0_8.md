# PRTA conditional no-good learning and joint bounded search v0.8

**Date:** 2026-11-19. **Result:** executable tested research prototype; no improvement to independently validated 141,086-instruction public Kaggle portfolio.

### New implementation

`prta_conditional_joint_search_v0_8.zip` attached to the conversation. The code extends v0.7 with `learned_joint.py`, `test_learned_joint.py`, and `benchmark_v08.py` plus inherited source and tests. Its `ConflictLedger` learns a deletion-minimal exact fixed-placement obligation conflict and conditionally reuses it only when: all source occurrence IDs, values, birth/final-use epochs, complete face assignments, patch radius and contact-hop bound match; and the candidate obligation set contains the certified conflicting set. This intentionally conservative full-context key blocks unsound carryover between different physical placements or altered source histories. Nonexhaustive placement search yields bounded-unresolved, not constructive zero or universal absence.

`joint_search` explores complete recursively reconstructed producer networks with up to two coordinated substitutions, two source-valid topological orders, two explicit legal register destination policies, and alternative authored physical placements. Each arithmetic program is independently validated. The inherited occurrence binder still defaults to the latest matching equal-valued source; full alternative source-occurrence selection remains open.

### Verification

19/19 focused and inherited regression tests pass, including learned-conflict reuse; invalidating the exclusion when placement or radius changes; joint two-producer repaired control; alternate placement retaining arithmetic producers; independent valid low/high register allocations; protected contact provenance; exact division and absence safety.

Full **numeric candidate screen only** over the same 1000 third-party-attributed public puzzles: 2000 families examined under matched two-family limit; 1994 not shorter, 6 compilation failures, zero shorter arithmetic programs. Retained baseline 141086. Since there was no scored shorter candidate, physical v0.8 exclusion/reconstruction was not exercised on a scored improvement. Time for single candidate screen 22.795 seconds. No Kaggle resubmission warranted.

### Literature reviewed

User-supplied 96-cell `santa-2026-inside-the-elf-s-calculator.ipynb`, particularly its reading room on addition chains, multi-target power evaluation and register allocation. Voronenko/Spiral Hcub multiple constant multiplication (https://spiral.ece.cmu.edu/mcm/); Aksoy, Günes & Flores, exact/approximate multiple constant multiplication (DOI 10.1016/j.micpro.2009.10.001); Massalin (1987) superoptimization; Schkufza et al. STOKE (arXiv:1211.0557); Hutton countdown (DOI 10.1017/S0956796801004300). The two linked Kaggle shared-helper/joint-recipe notebook pages returned no readable code through web; their contents were not verified.

### Remaining concrete tasks

(1) Prove smaller conflict-support guards independent of unaffected assignments rather than full-context cache keys; (2) jointly explore genuine alternative equal-value source occurrences; (3) improve deep multi-target candidate generation before emission, informed by MCM DAG sharing; (4) integrate stronger register lifetime allocation; (5) compare matched geometric and nongeometric search on **shorter candidate networks**. The present result does not certify global optimum or any intrinsic PRTA speedup.

Research ZIP is attached in this conversation; executable source is not separately pushed to GitHub.