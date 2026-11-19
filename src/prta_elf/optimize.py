"""Exact causal provenance optimization of an existing valid program.

This is a safe baseline improvement, NOT a demonstrated PRTA solver.
It retains every first witnessed target construction and its dependencies,
then compacts register references to preserve behavior.
"""
from .core import Puzzle, trace, validate


def prune_provenance(puzzle: Puzzle, program: list[list]) -> list[list]:
    validate(puzzle, program)  # reject illegal input before optimization
    _, first = trace(puzzle, program)
    last_writer: list[int | None] = [None] * puzzle.registers
    deps: list[tuple[int | None, int | None]] = []
    for op, i, j, dst in program:
        deps.append((last_writer[i], last_writer[j]))
        last_writer[dst] = len(deps) - 1
    needed: set[int] = set()
    agenda = [step for step in first.values() if step >= 0]
    while agenda:
        t = agenda.pop()
        if t in needed: continue
        needed.add(t)
        agenda.extend(d for d in deps[t] if d is not None)
    reduced = [ins.copy() for k, ins in enumerate(program) if k in needed]
    validate(puzzle, reduced)
    return reduced
