"""Experimental PRTA planning representation (not yet a competitive compiler)."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Contact:
    """Witnessed result of an oriented arithmetic joining event.

    A prospective triangular construction is a three-contact packet with
    shared operands/results. Geometry/orientation is metadata, not a free
    calculator operation. Every realized join must compile to a legal step.
    """
    operator: str
    left: int
    right: int
    result: int
    instruction_cost: int = 1


def triangle_candidates(values: set[int], targets: set[int], limit: int):
    """Propose shared 3-contact structures among witnessed positive values.

    This is a bounded, deterministic research probe, not a proof of
    instruction savings. Candidates are descriptive and are not submitted.
    """
    values = sorted(v for v in values if 1 <= v <= limit)
    contacts = []
    for i, a in enumerate(values):
        for b in values[i:]:
            for op, result in (("+", a+b), ("*", a*b)):
                if result in targets and result <= limit:
                    contacts.append(Contact(op, a, b, result))
            if b > a and b-a in targets:
                contacts.append(Contact("-", b, a, b-a))
            q, rem = divmod(b, a)
            if rem == 0 and q in targets:
                contacts.append(Contact("/", b, a, q))
    return contacts
