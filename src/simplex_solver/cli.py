"""Command-line entry point for validating a problem JSON file."""

import argparse
import sys

from .exceptions import ProblemFormatError
from .parser import load_problem


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a simplex-solver problem JSON file.")
    parser.add_argument("problem", help="Path to a problem JSON file")
    args = parser.parse_args()
    try:
        problem = load_problem(args.problem)
    except ProblemFormatError as exc:
        print(f"Invalid problem: {exc}", file=sys.stderr)
        return 2
    print(f"Valid problem: {problem.name} ({problem.sense}, {len(problem.c)} variables)")
    print("Solver implementation is not available yet.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
