# PRTA Elf v3.1: exact third-turn source-contact transfer test (2026-11-19)

**Verified limited result:** Reproducible experiment and source in current conversation ZIP `prta_elf_rotation_role_transfer_v3_1.zip` (SHA-256 `472d94a7833c9d5c46fd200c9b977792d683d4101baeb6128f775f65636f4a70`). All **25/25** unittest cases passed (12 new). 181-site five-shell original CIM v0.3/v10 positive-source triangular construction; tested unchanged full 18-op `scored_0149` instructions. **Zero instructions saved.**

Test question: Does existing L/R/D-style third-turn edge successor on native triangular shell source history determine whether and how one original occurrence may supply both ordered operand roles (J02 9×9 and J06 17×17) of a later joining event?

Native third-turn face map `rho(U,i,j)=U(-i-j,i)`, `rho(D,i,j)=D(-i-j-1,i)` preserves the occupied footprint, all full-edge contact adjacency, and all edge paths. Source-edge ports shift exactly `0→1→2→0`; `rho^3=id`. A finite route enumerator exhausts *simple, edge-only routes of at most six edges* and independently checks that each edge is a real shared boundary of two source triangles. Two intermediate-face-disjoint paths (common start and result triangles permitted) exist in all four compared configurations:

| placement | join/source→destination | path A | path B |
| --- | --- | --- | --- |
| v2.9 optimized | J02 / 5→14 | 5,14 | 5,2,6,15,24,14 |
| v2.9 optimized | J06 / 3→9 | 3,9 | 3,1,4,11,10,9 |
| v3.0 source-before-result | J02 / 4→5 | 4,1,2,5 | 4,12,13,5 |
| v3.0 source-before-result | J06 / 3→10 | 3,9,10 | 3,1,4,11,10 |

All routes are transformed into legal shared-edge routes by the third-turn and retain their original source endpoints. A deliberately invalid partial-turn negative control rotates only the destination of 255 original full-edge-contact pairs while fixing their sources; **252/255** lose direct-edge contact, emphasizing that correct equivariance requires rotating the *whole* construction.

**What is NOT demonstrated:** The edge path pair is a static finite geometric existence witness, not an actual executable physical-contact scheduler certificate. All 181 source-site triangles coexist; the check does not model resource occupation by other source events, role duty declaration/completion, relay reservations, discharge/transport/release, or simultaneous routing in the v2.4/v2.6 physical grammar. More importantly, while two ordered A/B path labels can be assigned, their reverse assignment is equally geometrically lawful in all four same-source cases. **The rotation and L/R/D cyclic port successor alone do not uniquely determine which distinct path must serve which arithmetic role.** This is an evidenced non-uniqueness under the tested geometry, *not* a universal impossibility theorem. Separate original source-owned roles, consumer obligations or additional witnessed contact/orientation history would be required to resolve the assignment.

V10 E/V stage-first geometry and CCW placement tie policy are not themselves a derived unique full user L/R/D origin numbering. Native shell distance remains distinct from graph edge hops. The 18 Elf arithmetic instructions remain unchanged, independent interpreter valid; public portfolio total remains 141086. Next: attempt resource-constrained source-owned dual path event replay and wrong-port / path occupancy ablation; seek multi-output arithmetic cone shortening only if independently verified.
