# A/B/C + source-certified absence + PRTA numerical contact comparison (v0.7)

**Local result: no further scored improvement.** The exact externally credited public portfolio remains **141,086 instructions**, validated on 1,000/1,000 scored puzzles. Exact CSV SHA-256: `21d1d5245de5d41810e06ce6435df99059b2ba8a35f2bfcde3256e827675a5d7`.

## Compiled candidate laws

- **A:** Replace one witnessed producer using currently resident operands, then prune truly unnecessary ancestors.
- **B:** Rebuild bounded helper groups through exact forward arithmetic BFS; absent candidates are not numeric zero.
- **C:** Reconstruct two final targets jointly from one/two counted shared helpers. Each contact packet retains actual input values, operators, positive outputs, and exact quotient–remainder witnesses for division.
- **Withheld suffix:** Discard a source-identified suffix only when the replacement's actual arithmetic re-witnesses every remaining target. No absence is credited as a free computation.

**Important source boundary:** PRTA v122 marks arbitrary ECC-to-physical-PRTA face attachment **UNWITNESSED**. PRTA factor-family v1.2 demonstrates that arbitrary lawful reindexings need not preserve contact metrics. These are source-certified **numerical contact packets**, *not* asserted geometric face rotations.

## Reproducible bounded experiments

| Test | Scored domain | Final instructions | Saved |
| --- | --- | ---: | ---: |
| Public baseline | 1,000 validated | 141,086 | — |
| A live-producer substitution (30 candidates per puzzle) | 1,000 | 141,086 | 0 |
| A/C two-join probe (20 puzzles, up to 250 alternatives) | 20 probed, full CSV retained | 141,086 | 0 |
| B exact group BFS (max value 40; ≤5 targets; 40,000 states) | 16 eligible | 141,086 | 0 |
| Withheld final-single-target suffix (12 cuts; 300 proposals/cut) | 1,000 | 141,086 | 0 |
| One-helper pair (18 cuts, 500 proposals) | 1,000 | 141,086 | 0 |
| Two-helper pair (8 cuts, 30 witnessed suffix intermediates) | 1,000 | 141,086 | 0 |

Every resulting scored CSV was reread, validated, and had the exact same SHA-256 as the public baseline.

## Demonstrated controls

- **A** start 5, targets 35 and 125: 5 → **4** instructions by replacing 100+25 with 5×25.
- **B** start 2, targets 22 and 96: 6 → **5** by joint helper rebuilding.
- **C** starts 2, 3, targets 21, 35: 7 → **4** by constructing 5=2+3, 7=5+2, 21=7×3, 35=7×5. Three source events are withheld, but four real steps remain charged. The numerical packet's physical PRTA face attachment is **UNWITNESSED**.
- Undefined source cannot act as numeric zero; inexact division is rejected.
- 23 local project unit tests passed.

**Interpretation:** The bounded A/B/C and typed-absence experiments successfully reproduce expected shorter programs in controls, but do **not** outperform the much stronger public Kaggle program bank. They do not prove optimality and do not establish PRTA-specific score gains. The earlier 105,228 target is outstanding. Do not submit unchanged CSV.

## Next experiment

Replace fixed-prefix rewrites with multi-producer value/occurrence **hypergraph** planning. Compare a conventional bounded hypergraph optimizer against an identical one with certified forbidden/forced producers at matched time and search budgets. Compile each chosen plan into literal 48-register instructions, retain witnesses and historical target coverage, independently verify each emitted program, and attribute the *incremental* savings strictly to the actual change.

Runnable scripts/tests and a detailed local audit are in the companion archive `prta-elf-abc-absence-v0_7.zip` from this conversation. The archive contains no competition CSV.
