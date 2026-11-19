"""Literal constructive arithmetic and competition validator.

No arithmetic is performed on an undefined register, and each instruction
is checked before changing the machine's state.
"""
from __future__ import annotations
import csv
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Puzzle:
    id: str
    starting_values: tuple[int, ...]
    targets: tuple[int, ...]
    value_limit: int
    registers: int
    family: str = "unknown"


def load_puzzles(path: str | Path) -> dict[str, Puzzle]:
    with open(path, newline="", encoding="utf-8") as stream:
        rows = csv.DictReader(stream)
        return {
            row["id"]: Puzzle(
                id=row["id"],
                starting_values=tuple(json.loads(row["starting_values"])),
                targets=tuple(json.loads(row["targets"])),
                value_limit=int(row["value_limit"]),
                registers=int(row["registers"]),
                family=row.get("family", "unknown"),
            ) for row in rows
        }


def load_programs(path: str | Path) -> dict[str, list[list]]:
    with open(path, newline="", encoding="utf-8") as stream:
        return {r["id"]: json.loads(r["program"]) for r in csv.DictReader(stream)}


def validate(puzzle: Puzzle, program: list[list], max_instructions: int | None = None) -> dict:
    if len(puzzle.starting_values) > puzzle.registers:
        raise ValueError("too many starting values")
    if any(not (1 <= x <= puzzle.value_limit) for x in puzzle.starting_values):
        raise ValueError("starting value outside bounds")
    registers: list[int | None] = list(puzzle.starting_values) + [None] * (puzzle.registers - len(puzzle.starting_values))
    goals = set(puzzle.targets)
    covered = set(x for x in registers if x in goals)
    if max_instructions is not None and len(program) > max_instructions:
        raise ValueError("instruction limit exceeded")
    for step, ins in enumerate(program):
        if not isinstance(ins, list) or len(ins) != 4:
            raise ValueError(f"step {step}: bad instruction shape")
        op, i, j, dst = ins
        if op not in {"+", "-", "*", "/"}:
            raise ValueError(f"step {step}: unrecognized operator {op!r}")
        if not all(type(k) is int and 0 <= k < puzzle.registers for k in (i, j, dst)):
            raise ValueError(f"step {step}: register out of bounds")
        a, b = registers[i], registers[j]
        if a is None or b is None:
            raise ValueError(f"step {step}: undefined source")
        if op == "+": value = a + b
        elif op == "-":
            if a <= b: raise ValueError(f"step {step}: nonpositive subtraction")
            value = a - b
        elif op == "*": value = a * b
        else:
            q, r = divmod(a, b)
            if r != 0: raise ValueError(f"step {step}: inexact division")
            value = q
        if not 1 <= value <= puzzle.value_limit:
            raise ValueError(f"step {step}: result outside permitted range")
        registers[dst] = value
        if value in goals: covered.add(value)
    missing = sorted(goals - covered)
    return {"id": puzzle.id, "valid": not missing, "instruction_count": len(program),
            "covered": len(covered), "target_count": len(goals), "missing": missing}


def trace(puzzle: Puzzle, program: list[list]) -> tuple[list[int], dict[int, int]]:
    """Trace all produced numbers and the first event covering each target."""
    state: list[int | None] = list(puzzle.starting_values) + [None] * (puzzle.registers - len(puzzle.starting_values))
    first = {v: -1 for v in puzzle.starting_values if v in puzzle.targets}
    generated = []
    for t, (op, i, j, dst) in enumerate(program):
        a, b = state[i], state[j]
        if a is None or b is None: raise ValueError(f"step {t}: undefined source")
        value = {"+": lambda: a+b, "-": lambda: a-b, "*": lambda: a*b, "/": lambda: a//b}[op]()
        state[dst] = value
        generated.append(value)
        if value in puzzle.targets and value not in first: first[value] = t
    return generated, first
