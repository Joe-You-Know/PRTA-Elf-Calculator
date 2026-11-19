"""SSA occurrence-aware register allocator for the Elf Calculator.

Each original register write creates a distinct source occurrence; numerically
identical occurrences may share a physical calculator register while their
future uses remain separately accounted. No uncharged arithmetic transitions.
This is a conventional value-reuse comparator, not a proven PRTA rotation.
"""
from collections import Counter
from .core import validate
from .optimize import prune_provenance


def optimize_ssa(puzzle, source):
    """Optimize a valid source program and independently validate its output."""
    source = prune_provenance(puzzle, source)
    nreg = puzzle.registers
    vreg = list(range(len(puzzle.starting_values))) + [None] * (
        nreg - len(puzzle.starting_values)
    )
    values = list(puzzle.starting_values)
    events = []
    used = Counter()
    for op, i, j, d in source:
        left, right = vreg[i], vreg[j]
        if left is None or right is None:
            raise ValueError("undefined")
        a, b = values[left], values[right]
        if op == "+":
            val = a + b
        elif op == "-":
            val = a - b
        elif op == "*":
            val = a * b
        elif op == "/":
            val, rem = divmod(a, b)
            if rem:
                raise ValueError("inexact")
        else:
            raise ValueError(f"unknown operator {op}")
        idx = len(values)
        values.append(val)
        events.append((op, left, right, idx))
        used[left] += 1
        used[right] += 1
        vreg[d] = idx

    slots = [None] * nreg
    for i in range(len(puzzle.starting_values)):
        slots[i] = i
    output = []
    produced = set(range(len(puzzle.starting_values)))
    for op, left, right, new in events:
        # A physical register stores one numeric value, but an SSA occurrence
        # remains distinct and has its own last-use count.
        positions = {}
        for i, occurrence in enumerate(slots):
            if occurrence is not None:
                positions.setdefault(values[occurrence], i)
        a, b = values[left], values[right]
        if a not in positions or b not in positions:
            raise AssertionError("unavailable source value")
        il, ir = positions[a], positions[b]
        used[left] -= 1
        used[right] -= 1
        produced.add(new)
        out = values[new]

        # The same result was already witnessed and remains resident.
        # Record this new virtual occurrence without charging another step.
        if out in positions:
            continue

        # Only a version that has actually been produced can keep a value live.
        # Future versions are not reservations of currently occupied storage.
        live = {values[v] for v in produced if used[v] > 0}
        slot = next((i for i, v in enumerate(slots) if v is None), None)
        if slot is None:
            slot = next(
                (i for i, v in enumerate(slots) if values[v] not in live),
                None,
            )
        if slot is None:
            raise AssertionError("no scratch register")
        output.append([op, il, ir, slot])
        slots[slot] = new

    report = validate(puzzle, output)
    if not report["valid"]:
        raise AssertionError(f"uncovered targets: {report['missing']}")
    if len(output) > len(source):
        raise AssertionError("optimizer increased instruction count")
    return output
