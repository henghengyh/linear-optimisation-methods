"""JSON loading and validation for linear programming problems."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

from .exceptions import ProblemFormatError

_ALLOWED_SENSES = {"min", "max"}
_ALLOWED_RELATIONS = {"<=", ">=", "="}
_REQUIRED_TOP_LEVEL = {"name", "sense", "objective", "constraints"}


def load_problem(path: str | Path) -> dict[str, Any]:
    """Load and validate a problem from a UTF-8 JSON file."""
    file_path = Path(path)
    try:
        with file_path.open("r", encoding="utf-8") as file:
            problem = json.load(file)
    except (OSError, json.JSONDecodeError) as exc:
        raise ProblemFormatError(f"Could not read valid JSON from {file_path}: {exc}") from exc
    return validate_problem(problem)


def validate_problem(problem: Any) -> dict[str, Any]:
    """Validate the supported input shape and return the problem unchanged."""
    if not isinstance(problem, dict):
        raise ProblemFormatError("The problem must be a JSON object.")

    missing = _REQUIRED_TOP_LEVEL - problem.keys()
    if missing:
        raise ProblemFormatError(f"Missing required field(s): {', '.join(sorted(missing))}.")

    if not isinstance(problem["name"], str) or not problem["name"].strip():
        raise ProblemFormatError("'name' must be a non-empty string.")
    if problem["sense"] not in _ALLOWED_SENSES:
        raise ProblemFormatError("'sense' must be either 'min' or 'max'.")

    objective = problem["objective"]
    if not isinstance(objective, list) or not objective:
        raise ProblemFormatError("'objective' must be a non-empty list of numbers.")
    _validate_numbers(objective, "objective")

    constraints = problem["constraints"]
    if not isinstance(constraints, list) or not constraints:
        raise ProblemFormatError("'constraints' must be a non-empty list.")
    for index, constraint in enumerate(constraints):
        label = f"constraints[{index}]"
        if not isinstance(constraint, dict):
            raise ProblemFormatError(f"{label} must be an object.")
        missing_constraint = {"coefficients", "sense", "rhs"} - constraint.keys()
        if missing_constraint:
            raise ProblemFormatError(
                f"{label} is missing field(s): {', '.join(sorted(missing_constraint))}."
            )
        coefficients = constraint["coefficients"]
        if not isinstance(coefficients, list) or len(coefficients) != len(objective):
            raise ProblemFormatError(
                f"{label}.coefficients must have {len(objective)} entries, matching objective."
            )
        _validate_numbers(coefficients, f"{label}.coefficients")
        if constraint["sense"] not in _ALLOWED_RELATIONS:
            raise ProblemFormatError(f"{label}.sense must be '<=', '>=' or '='.")
        _validate_numbers([constraint["rhs"]], f"{label}.rhs")

    variables = problem.get("variables", [f"x{i + 1}" for i in range(len(objective))])
    if not isinstance(variables, list) or len(variables) != len(objective):
        raise ProblemFormatError("'variables' must be a list matching the objective length.")
    if any(not isinstance(var, str) or not var.strip() for var in variables):
        raise ProblemFormatError("Each variable name must be a non-empty string.")
    if len(set(variables)) != len(variables):
        raise ProblemFormatError("Variable names must be unique.")

    bounds = problem.get("bounds", "nonnegative")
    if bounds != "nonnegative":
        raise ProblemFormatError("Currently, only nonnegative variables are supported (bounds: 'nonnegative').")
    return problem


def _validate_numbers(values: list[Any], label: str) -> None:
    for index, value in enumerate(values):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ProblemFormatError(f"{label}[{index}] must be a number.")
        if not math.isfinite(value):
            raise ProblemFormatError(f"{label}[{index}] must be finite.")
