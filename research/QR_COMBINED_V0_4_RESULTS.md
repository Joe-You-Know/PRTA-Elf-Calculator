# QR construction and occurrence reuse: combined candidate

Status: locally validated, **not yet Kaggle-confirmed**. Date: 2026-11-19.

Using user-provided Santa 2026 scored CSV (1,000 puzzles), the source-preserving QR construction suite produced these locally validated totals:

| Compiler | Total instructions |
| --- | ---: |
| Original baseline | 1,490,379 |
| First accepted Kaggle submission | 1,433,802 |
| SSA optimization | 1,350,568 |
| Unsigned QR base selection | 387,941 |
| Balanced signed QR | 325,032 |
| Compact balanced | 322,813 |
| Target transport / shared-prefix QR | 322,426 |
| QR chain + occurrence reuse | **315,683** |

For the final combination, the SSA allocator improved **897/1,000** QR-chain source programs, with **zero allocation failures**. All 1,000 resulting programs were reloaded from the final CSV and independently validated for arithmetic, target coverage, value limit, and register usage. It saved 6,743 instructions against the chain-only candidate. SHA-256 of `submission_chain_ssa.csv`: `b81a8b179667f2168b58444362d1a2351964b0f2a3c96ac413a17cb734cfeef1`.

The shared QR method retains integer divisions as quotient/remainder relations. For any zero residual digit, the corresponding addition is *withheld*; this is a deliberate nonconstruction decision and **not** an emitted operation. A negative digit requires a genuine legal subtraction. In source-occurrence reuse, a repeated result may be witnessed by an already resident equal value without another arithmetic instruction.

**Scope:** The reported improvement comes from conventional QR digit construction, shared prefixes, and compiler occurrence reuse. It does not establish a separate benefit from geometric PRTA rotation, nor any generalized physical absence law. An absent event is not a numeric value.

The runnable QR modules, independent tests, and full candidate builder are available in the companion local `prta-elf-qr-ssa-v0_4.zip` package; these modules still need to be integrated into this Git branch. Only the final combination script is committed so far. Until those modules are integrated, `scripts/compile_chain_ssa.py` expects `results/submission_chain.csv` supplied locally rather than reconstructing it from scratch.

Next target: bounded multi-producer graph search including exact target-to-target quotients, inverse predecessor options, prospective withheld operations, and independent source-contact certificates. Compare PRTA-specific candidate generation against conventional graph search at matched budgets; only credit absent events when a real scored instruction disappears.
