# Whole-puzzle authored QR helper-family experiment v0.1

Date: 2026-11-19. This is a bounded experimental compiler, **not** a demonstration of Kaggle savings from PRTA geometric indexing.

## Law and representation

All puzzle target values are read before helper candidate generation. Families arise from exact target–input and target–target quotients/remainders, pairwise differences and common factors; the compiler never consults original-program intermediate values when inventing helper candidates. Each proposed helper receives a typed triangular face index `k`, shell `s = isqrt(k-1)+1`, and slot `k-(s-1)^2-1`. Each shell adds `2s-1` entire triangular faces and total face count is `s^2`. Parity is a discrete orientation report, not an angle. Exact contact ledger entries preserve `target = p*q+r`, `0<=r<p`, full source ID, face index and one of three authored edge roles. An exact-zero residual becomes a *typed closure report*, not a constructed zero-valued face or a free numerical result.

This indexes *abstract whole triangular faces*. It does not yet prove all authored numerical contact roles correspond to actual neighboring physical PRTA faces in a global packed substrate. That must be established separately.

## Construction comparison

Candidate programs are generated from initial input registers alone, using zero, one, or two newly proposed helpers followed by legal one-step target constructions. Multiple target obligations can share one new helper. Each entire candidate program must cover *every* puzzle target within 48 registers, with positive intermediate values and exact division. Original public program is retained if no strictly shorter valid whole candidate is found. No candidate numerical value is treated as available until an actual arithmetic step constructs it.

**Control**: start `(2,3)`; targets `(8,12)`. Original four steps use 6 and 9; invented helper 4=2+2, then 8=2*4 and 12=3*4, for three instructions. 5/5 unit tests pass, including triangle shell counts and typed QR closure.

**Full benchmark (exact public attribution retained)**: 1,000 puzzles, 141,086 baseline instructions; 74,549 helper-face candidates across puzzles, 2,111,263 QR contact records, 223,157 alternate plans tested. **0 improved puzzles and 0 instructions saved**. Final verified 1,000/1,000, 141,086 instructions, SHA-256 `21d1d5245de5d41810e06ce6435df99059b2ba8a35f2bfcde3256e827675a5d7`, byte-identical to public baseline. Runtime of this bounded Python experiment 7.263 s in the local container. **Do not resubmit** the unchanged CSV.

## Precise unsolved boundary

'Whole-puzzle' currently describes selecting and validating an *entire program* from all target obligations; search depth is still intentionally shallow: at most two newly invented helpers and one direct scored join for each goal. Many 15–18-digit targets need substantially deeper shared compounds. No source-certified forced-producer closure or physically validated global PRTA shell contact law was proved by this experiment. The next fair test is a multi-depth, global helper-family scheduler using a genuinely packed triangular face incidence network, compared with an equally budgeted non-geometric arithmetic planner.

Executable `whole_puzzle.py`, tests and audit delivered in `prta_whole_puzzle_v0_1.zip` from this conversation. Contest puzzle files and contestant-produced CSVs are not committed to GitHub.
