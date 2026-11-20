# Elf Calculator collective chosen-denominator GCD experiment — 2026-11-20

**Result:** Independently replayed all 1000 scored puzzles in independently validated 134,002-instruction conventional submission. Group each exact nontrivial division's chosen denominator by puzzle, preserve source-operand occurrence and numerator, and compare common-factor structure to alternative same-size and exact legal candidate denominators.

- 3,220 exact nontrivial divisions, 728 puzzles with >=2, 167 with one, 105 none.
- 6,384 chosen-denominator pairs; 3,942 noncoprime, 3,145 nested (one exactly divides other), 830 equal, 29 pairwise GCD >=256.
- 261 multi-division puzzles have GCD of all chosen denominators >1, six GCD >=16.
- **120 global bit-length matched shuffle controls**, preserve observed denominator multiset and within-puzzle number of division occurrences: noncoprime mean 3,623.6 [maximum 3,742], nested mean 2,712.0 [max 2,812], pairs GCD>=256 mean 4.85 [max11], all-denominator shared-GCD puzzles mean 221.35 [max257]. None equals observations on these four metrics.
- **120 conditional live-register controls**, select another live positive integer of similar bitlength (when available): noncoprime 3,125.7, nested 1,917.5, GCD>=256 12.79, all shared-GCD puzzles 168.0.
- **120 stricter exact-live-divisor controls**, other live values are required to exactly divide same numerator, with fallback to originally chosen denominator if no alternate available: noncoprime 3,835.5, nested 2,989.2, GCD>=256 30.28, shared-GCD puzzles 242.1. This control reveals part of the signal is necessary exact-factor availability and its fallback is biased; not independent generator evidence.
- Every collective denominator GCD divides its grouped numerators' GCD, a mathematical consequence of each remainder being zero; do not count as independent result.
- Concrete verified scored_0117 denom 256,4096, GCD256.
- New 4/4 directed tests PASS; independent pair-by-pair reconstruction checks core counts.
- Formal LaTeX + two-page compiled PDF, replay source, 120 null trials, 728 per-puzzle reports and tests bundled `elf_collective_denominator_gcd_v1.zip` SHA256 `91191111a15c6b0fb795a8b4284d0dce5bb0e32f53d20b0efab5fc1940cdeed0` (conversation artifact).

**Interpretation:** a nonrandom *factor hierarchy in solver-chosen denominators* appears; exact-divisor conditioning explains a large portion of it. No ECC, finite-field modular inverse or private puzzle-generator design has been established. Next experimental engineering target is compressing repeated quotient constructions using collective denominator GCD source certificates vs conventional graph rewrites, with independent exact Elf interpreter verification.