# Physically gated PRTA producer selection v0.3

**Date:** 2026-11-19. **Status:** literal three-edge contact admissibility implemented and tested; no new Kaggle score.

The runnable source, tests, and full census audit were delivered in `prta_physical_contacts_v0_3.zip` (conversation attachment). Executable files include `contact_selection.py`, `contact_benchmark.py` and the prior geometric and arithmetic baseline modules. This research record is committed; executable files remain in the attachment.

## Specific authored grammar

Each source-owned arithmetic producer `out=op(a,b)` must pass both an exact arithmetic check and a **physical full-edge contact check**: the triangular face assigned to the output actually shares one distinct full edge with each distinct operand face in a **single injective placement** in the finite, packed triangular-face patch. Source IDs and actual common vertex pairs are retained as witnesses. A rejected producer gets a source-specific typed withholding reason. An unexamined option is not thereby proved absent or zero.

The grammar is intentionally *stricter* than the general numerical algebra of PRTA: requiring two immediate operand/output full-edge contacts is **not** claimed as universal. The triangular-face dual adjacency has no odd cycles, so some genuine arithmetic producer networks cannot be represented using this specific direct-contact law. The point is to establish a real geometric admissibility decision rather than merely prioritizing candidates by a decorative triangle index.

## Positive and negative controls

- Real two-contact producer 5=2+3: two witnessed **distinct actual edges** to the output face.
- Connected two-event compound 5=2+3 then 35=5×7: finite physical embedding and exact arithmetic verified.
- 5=2+3 then 8=5+3: impossible three-cycle of direct face-edge contact; rejected with typed `odd-contact-cycle` witness, although the arithmetic operations themselves are legal.
- Two alternative producers for 5: 2+3 and 7−2. With a fixed authored placement, the first is admissible and the second physically inadmissible; selection keeps the former, not simply ranking both.
- Moving an assigned source value to a nonincident face can invalidate a producer while its numerical equation remains true. Wrong arithmetic is independently rejected.
- **16/16 standard-library unit tests passed** (six new, ten inherited).

## Scored-data geometry census (bounded, no program replacement)

All 1,000 puzzles in the **externally credited** exact public 141,086-instruction portfolio were numerically validated. The matched candidate domain is the first two source-history producers with three distinct values per puzzle (993 eligible pairs). In a radius-3 finite physically packed patch, requiring both producers' direct full-edge receipts together:

| Outcome | Count |
|---|---:|
| Puzzles audited | 1,000 |
| Two-producer numerically valid motifs | 993 |
| Both producer contacts physically admissible | 767 |
| Physically excluded under this authored grammar | 226 |
| Excluded by witnessed odd-contact cycle | 207 |
| Excluded by exhausted finite radius-3 placements | 19 |
| Insufficient eligible two-producer motifs | 7 |
| Changed Kaggle programs / instructions saved | **0 / 0** |

Example scored_0005: 587=411+176 and 241257=587×411 are both numerically lawful. Demanding immediate full-edge contacts for both creates a forbidden triangle in the *face-adjacency graph*. This **does not** invalidate either arithmetic construction or refute PRTA's alternative authored grammars; it reveals where an edge-only compilation is incomplete and an intermediate connector/contact-transport grammar is needed.

Baseline is retained unchanged, SHA-256 `21d1d5245de5d41810e06ce6435df99059b2ba8a35f2bfcde3256e827675a5d7`. No new Kaggle submission warranted.

## Next missing component

Create real *multi-face contact transports* that allow the same numerical value/source relationship to be carried via approved connector compounds rather than pretending every operand must directly touch the output face. Construct and verify source-owned contacts at each intermediate face, establish the effect of withheld contacts, and jointly select the producer family, physical placement and actual 48-register arithmetic program. Compare against identical arithmetic candidates without the physical filter and separately measure geometric constraints and score improvements.
