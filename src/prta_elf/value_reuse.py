"""Exact value-occurrence compiler for existing Elf Calculator programs.

An original register name is not a permanent identity: it denotes the value
written there most recently. This compiler reconstructs the chronological
value ledger, compiles each live value into an available register, and avoids
rebuilding a value when an identical value is already resident. Every emitted
construction remains one real, scored calculator instruction.

This is not a verified PRTA rotation rule. It is a conventional shared-value
baseline against which prospective PRTA contact moves should be measured.
"""
from __future__ import annotations

from collections import Counter
from .core import Puzzle, validate


def _value(op: str, a: int, b: int) -> int:
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/":
        q, r = divmod(a, b)
        if r: raise ValueError("inexact division in source program")
        return q
    raise ValueError(f"unknown operator: {op}")


def reuse_values(puzzle: Puzzle, program: list[list]) -> list[list]:
    """Recompile valid source by reusing current equal-value occurrences.

    The input is treated as a fixed arithmetic event sequence. Earlier target
    coverage remains witnessed even after its storage is reused. A result
    already present in another register can be inherited by the virtual output
    without executing an instruction. A target first reached by an event must
    still be produced, unless it is already present in an existing register.

    A forward event may be erased only when no future source depends on it and
    its result has already been covered, so we first remove dead provenance.
    The result is independently validated and is never longer than the input.
    """
    from .optimize import prune_provenance
    if not validate(puzzle, program)["valid"]:
        raise ValueError("source must cover all targets")
    program = prune_provenance(puzzle, program)

    virtual: list[int | None] = list(puzzle.starting_values) + [None] * (puzzle.registers - len(puzzle.starting_values))
    events: list[tuple[str, int, int, int]] = []
    future: Counter[int] = Counter()
    for op, i, j, dst in program:
        a, b = virtual[i], virtual[j]
        if a is None or b is None: raise ValueError("undefined virtual source")
        value = _value(op, a, b)
        events.append((op, a, b, value))
        future[a] += 1
        future[b] += 1
        virtual[dst] = value

    physical: list[int | None] = list(puzzle.starting_values) + [None] * (puzzle.registers - len(puzzle.starting_values))
    result: list[list] = []
    covered = set(puzzle.starting_values) & set(puzzle.targets)
    targets = set(puzzle.targets)

    for op, a, b, out in events:
        positions = {value: idx for idx, value in enumerate(physical) if value is not None}
        if a not in positions or b not in positions:
            raise AssertionError("failed to preserve a future-needed source")
        i, j = positions[a], positions[b]
        future[a] -= 1
        future[b] -= 1

        positions = {value: idx for idx, value in enumerate(physical) if value is not None}
        if out in positions:
            covered.add(out) if out in targets else None
            continue

        # Prefer dead value slots, including a just-consumed operand.
        # Keeping all existing live values prevents later aliasing failures.
        slot = next((k for k, v in enumerate(physical) if v is None), None)
        if slot is None:
            slot = next((k for k, v in enumerate(physical) if future[v] <= 0), None)
        if slot is None:
            raise AssertionError("no scratch register for a live output")
        result.append([op, i, j, slot])
        physical[slot] = out
        if out in targets: covered.add(out)

    report = validate(puzzle, result)
    if not report["valid"]: raise AssertionError(f"uncovered: {report['missing']}")
    if len(result) > len(program): raise AssertionError("reuse increased instruction count")
    return result


def safe_reuse_values(puzzle: Puzzle, program: list[list]) -> tuple[list[list], str]:
    """Return a legal non-worsening program even when register packing fails.

    Any failed allocator attempt is discarded completely, then a proven
    provenance-only program is independently validated. Illegal source
    programs still raise ValueError instead of being silently accepted.
    """
    from .optimize import prune_provenance
    try:
        return reuse_values(puzzle, program), "value_reuse"
    except AssertionError:
        return prune_provenance(puzzle, program), "provenance_fallback"
