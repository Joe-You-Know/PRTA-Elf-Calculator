# PRTA v122 -> Elf Calculator: bridge and baseline experiment

Experiment checkpoint: November 18, 2026.

## Source and scope

Source archive: `PRTA_v122_exact_occupied_absent_transport(1).zip` (provided by project owner). This archive is **not committed** here.

PRTA v122 verifies conditional common-tip UP/DOWN face-count and occupied/withheld-contact laws, with source-owned row IDs and contact incidences. The experiment reports 32,586 paired 17-bit ECC half-orbit depths, and one independently source-anchored eight-by-four example: 32 UP present, seven authorized DOWN present, 14 DOWN withheld, 21 fulfilled red contacts, 42 unfulfilled interior contacts, and 33 external whole-edge ports. It explicitly marks actual ECC-to-physical-PRTA face attachment as **UNWITNESSED**. The seven DOWN contacts cannot be assigned indiscriminately to every slope triangle.

For the Elf Calculator, a permitted arithmetic instruction is a witnessed construction: operator, two source occurrences, one destination occurrence. An undefined register is an absence of construction, **not** a numeric zero. A deleted operation does not certify that its result existed; only a previous witnessed result can justify reuse. A geometric rotation is **not** a free calculator instruction. There is not yet a verified direct compiler that maps PRTA rotations into shorter legal arithmetic sequences.

## Conventional comparator: value-occurrence reuse

The new `value_reuse.py` compiler processes an existing legal instruction program, preserves its chronological value ledger, and reuses exact numbers currently resident in registers rather than recalculating them. It retains future-use counts to protect operands from destructive overwrites. When current register allocation cannot complete the compilation, the attempt is discarded and the independently validated provenance pruner is used.

Local inputs: all **1,000 scored puzzles** and the baseline sample submission from the user-provided `santa-2026.zip` archive.

| Metric | Result |
| --- | ---: |
| Initial instructions | 1,490,379 |
| Result instructions | 1,433,802 |
| Instructions saved | 56,577 |
| Total reduction | 3.796148% |
| Direct value-reuse success | 354 puzzles |
| Safe provenance fallback | 646 puzzles |
| Invalid output programs under local validator | 0 |
| Unit tests | 8 passed |

These are **measured conventional compiler results**, NOT established PRTA-specific savings and not a Kaggle leaderboard score. The independent validator checked positive intermediates, exact division, limits, register semantics and target coverage.

## Reproduce

Keep competition files locally under ignored `data/`, then run:

```bash
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
python3 -m prta_elf.cli \
  --puzzles data/puzzles.csv \
  --programs data/sample_submission.csv \
  --optimizer reuse \
  --out results/submission_reuse.csv
```

## Next test

Compare the sample, conventional value-reuse baseline, and future PRTA three-contact source-authorized planning under matched time budgets. Prove legal compilation and count every arithmetic operation. Report savings and failures separately on shared, mixed, independent, multiplicative and tiny families. Establish the actual source geometry before calling an arithmetic rearrangement a PRTA rotation.
