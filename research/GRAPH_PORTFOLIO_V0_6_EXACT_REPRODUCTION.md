# Public arithmetic graph rewrite portfolio — exact reconstruction v0.6

Date: 2026-11-19. This record supersedes the missing-public-start limitation in v0.5, without deleting its historical provenance.

## Inputs

- User-uploaded public starting `submission.csv` (1,000 scored programs): SHA-256 `1147067ff0ea9545bdd0625b5de216320b762d6f3f6413a183b8b8a63035973f`, **142,940** instructions.
- User-uploaded `sources.csv`: SHA-256 `df4debb59d79094d5e3b1683f69286e6e6a77c627148703ce2c9b334b3e5d1f9`. This is the external provenance/strategy index and not the instruction-submission file.
- User-provided public notebook `santa-2026-arithmetic-graph-rewrites.ipynb`: 754 compressed/encoded replacement programs; notebook records Kaggle-confirmed score 141,086, submission ID 58541609, and credits upstream authors.
- Official scored puzzle CSV matching notebook's pinned SHA-256 `b0c70d849eca078a0e1cf9a4f7b47fd40b7435663f6f84de6725f84724500428`.

## Results

Decoded 754 literal replacements from the notebook *without executing untrusted notebook cells*. Applied them over the exact starting `submission.csv`, retaining each original encoded program string and row order. Reconstructed **1,000/1,000** valid programs, with **141,086** instructions.

Crucially, the byte-for-byte reconstructed `submission_public_exact.csv` SHA-256 was

`21d1d5245de5d41810e06ce6435df99059b2ba8a35f2bfcde3256e827675a5d7`

which **exactly matches** the digest published in the supplied public notebook. This supports reproducibility of the externally credited 141,086 portfolio rather than authorship of its algorithm.

Compared each independently validated public program with our prior local 178,266 hybrid. All public programs were at least as short, so the fused result remained 141,086. Re-running our existing SSA reuse optimizer over all 1,000 public programs yielded **zero improvements and zero failures**. No new Kaggle CLI submission was performed in this turn.

## Next scientific comparison

Our stretch target from the earlier 315,683 local QR+SSA result remains about **105,228** instructions (one third). Beating the now-reproduced public result would require at least 35,859 saved instructions. The feasible research direction is a bounded joint construction-search experiment with shared helper groups and prerequisite-producer choices, including source-certified withheld events, not further post-hoc value reuse alone.

All proposed PRTA contact and absence rules require an explicit compilation into counted, valid calculator instructions. Keep third-party provenance and independently verified score claims distinct from our original research contributions.

## How to reproduce without executing notebook code

1. Verify input hashes.
2. Parse notebook JSON cell 4 with Python `ast.parse`; evaluate only the literal assigned to `encoded` using `ast.literal_eval`.
3. Decode `json.loads(zlib.decompress(base64.b85decode(encoded)))`.
4. Load starting CSV rows preserving `program` strings and ID order, update by replacement dictionary.
5. Write `id,program` CSV with Python `csv.writer`, validate every parsed program with `prta_elf.core.validate`.
6. Check exact final SHA-256 above.

No uploaded competition CSV or externally contributed instruction programs are committed into the repository.
