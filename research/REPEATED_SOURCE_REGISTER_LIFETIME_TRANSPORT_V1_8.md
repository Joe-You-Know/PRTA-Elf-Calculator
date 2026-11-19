# PRTA Elf repeated-source, register lifetime and contact alternatives v1.8

**Date:** 2026-11-19. **Executable artifact:** conversation attachment `prta_elf_repeated_source_lifetime_transport_v1_8.zip` (complete original Python compiler, inherited v1.7/1.6 modules, 73 tests, complete benchmarks and README_V18.md). Source in ZIP, not independently uploaded to GitHub.

## Actual changes
1. **Repeated-source joining:** A single witnessed source occurrence may fill both operand roles of an arithmetic instruction, e.g. 2+2=4. The authored physical joining grammar retains two separately real, non-colliding shared-edge input paths to the output face without inventing a second occurrence. Example radius-3 placement faces (2,4) gives two paths from source face 2; different faces (1,8) with a hop-3 cap cannot route the same join. One legal Elf instruction `['+',0,0,0]` is independently checked.
2. **Source-proof versus 48-register lifetime:** Source-owned physical event receipts retain identity and contact even after the last arithmetic use. A *separate offline allocator* computes each constructed occurrence's final upcoming arithmetic read and may overwrite its Elf register on that read. It refuses reuse when an earlier numeric occurrence is still required. Controlled three-step chain 2+2=4, 4+4=8, 8+4=12 compiles to 2 registers; synthetic 55-event doubling from starting 1 compiles in 1 register. These allocator controls alone do not assert 55 physical contact proofs.
3. **Alternative authored placement, discrete turn and source-preserving multi-face transport:** v1.8 can seed multiple finite triangular face assignments; on a failed join it may attempt a rigid whole-patch third-turn, or a new finite actual-edge contact route, before rerunning the join. A five-edge route test retains its original source and receiving obligation and independently replays; turns/transports/withholding never emit Elf arithmetic.
4. **Independent verification:** every numerical program is replayed with the 48-register contest interpreter; physical event history is re-executed from the actual initial source and original arithmetic bound rather than accepted as a supplied state tuple. **73/73** inherited/new tests pass (11 new).

## Complete scored ablations
Input exact independently verified externally credited public 1000-puzzle portfolio **141086** instructions. Two full bounded settings:

| Scored full benchmark | Search setting | Join offers | Face trials | Retained boundaries | Final instructions |
| --- | --- | ---: | ---: | ---: | ---: |
| A single placement | depth 1, beam 1, pair 4, offer 2, faces 2, hop 3 | 1988 | 3319 | 829 | **141086** |
| B two placements and turn/transport enabled | same, two placements | 3976 | 13463 | 871 | **141086** |

Both 1000/1000 valid. Exact unchanged output SHA-256 `21d1d5245de5d41810e06ce6435df99059b2ba8a35f2bfcde3256e827675a5d7`. **0 scored savings**, no Kaggle submission warranted. The broader 2-step full search timed out and is not counted. A completed 100-puzzle, depth-2, turn/transport probe did not improve 14330 instructions.

## Evidence boundaries
This is a *particular finite authored contact grammar*, not proof of universal PRTA triangle algebra. Physical event occurrence/register IDs are virtual source witnesses; the actual 48-register assignment is a separate projection, not a physical release of historical contacts. Contact/relay occupancy remains reserved while the physical event exists; legal discharge and relay reuse are not derived yet. The search still uses equal-numerical-value suppression as a heuristic and has very shallow scored depth. None of these runs show intrinsic geometric score gain or a verified physical memory-area reduction.

**Next:** source-preserving contact discharge with provable historical retention; physically valid relay lifetime reuse and source-occurrence-aware future equivalence; multi-depth joint target planning across placement and register allocation, with matched numerical-only ablation. Do not equate unknown/withheld with scalar zero or a computed target.
