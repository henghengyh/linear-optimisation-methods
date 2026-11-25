# simplex-solver

A Python implementation of the **Simplex Method** and **Two-Phase Method** for solving linear programming problems. I’m building this project to strengthen my understanding of linear optimization and to create a practical, well-documented example of my Python, algorithm design, and testing skills.

The solver is being developed as a learning project. Its goal is to show the steps behind a solution—not just return an answer—while keeping the code organized into reusable modules.

## Project status

**Status: In development**

The repository structure and implementation plan are defined. Features below describe the intended behavior; they should not be considered complete until implemented and covered by tests.

## What it will do

- Parse linear programming problems from JSON.
- Solve supported problems using the Simplex Method.
- Use the Two-Phase Method when an initial feasible basis is not readily available.
- Report whether a problem has an optimal solution, is infeasible, or is unbounded, where these cases are supported.
- Provide a command-line interface for solving example problems.
- Include tests for ordinary cases and important edge cases.

## Mathematical scope

The initial scope is linear programs in standard form:

``maximize cᵀx subject to Ax = b, x ≥ 0.``

The project will document how supported input forms are converted to standard form, including handling of constraint directions and right-hand-side signs. The implementation and documentation will make clear which forms are supported as development progresses.

## Planned architecture

```text
simplex-solver/
├── .github/workflows/ci.yml
├── docs/REPORT.md
├── examples/
│   ├── diet_problem.json
│   └── unbounded_case.json
├── src/simplex_solver/
│   ├── __init__.py
│   ├── cli.py
│   ├── exceptions.py
│   ├── formatters.py
│   ├── parser.py
│   ├── solver.py
│   └── tableau.py
├── tests/
│   ├── __init__.py
│   ├── test_edge_cases.py
│   ├── test_simplex.py
│   └── test_two_phase.py
├── .gitignore
├── pyproject.toml
└── README.md
```

| Module | Responsibility |
| --- | --- |
| `parser.py` | Read and validate problem definitions. |
| `tableau.py` | Represent and update the simplex tableau and basis. |
| `solver.py` | Implement the Simplex and Two-Phase algorithms. |
| `exceptions.py` | Define clear errors for invalid or unsupported problems. |
| `formatters.py` | Present solutions and solver status in a readable form. |
| `cli.py` | Connect problem input, solving, and output for command-line use. |

## Development plan

### Stage 1: Project foundation

- [x] Set up the `src`-based Python package and project metadata.
- [x] Define the JSON input format and validate problem data.
- [x] Add example problems and document their expected results.

### Stage 2: Simplex Method

- [ ] Implement tableau construction and pivot operations.
- [ ] Implement entering- and leaving-variable selection.
- [ ] Solve maximization problems with an initial feasible basis.
- [ ] Detect and report unbounded cases.
- [ ] Add unit tests for pivots, known examples, and edge cases.

### Stage 3: Two-Phase Method

- [ ] Build Phase I to find a feasible basis using artificial variables.
- [ ] Detect infeasible problems from the Phase I result.
- [ ] Transition from Phase I to Phase II and optimize the original objective.
- [ ] Add tests for feasible and infeasible problems and Phase transitions.

### Stage 4: Usability and documentation

- [ ] Add the command-line interface and readable solution output.
- [ ] Write `docs/REPORT.md` to explain the algorithm, design decisions, and limitations.
- [ ] Document installation, input format, examples, and known limitations.

### Stage 5: Quality checks

- [ ] Configure GitHub Actions to run the test suite.
- [ ] Check formatting, error messages, and behavior on degenerate or cycling-prone examples.
- [ ] Review the README and examples against the implemented behavior.

## Example problems

- `examples/diet_problem.json` is planned as a bounded optimization example.
- `examples/unbounded_case.json` is planned to demonstrate unboundedness detection.

The exact JSON schema and commands will be documented here once the parser and CLI are implemented.

## Running the project

Installation and command-line instructions will be added after the package configuration and CLI are in place. For now, the repository is a work in progress; see the development plan above for the intended implementation sequence.

## Learning goals

- Understand how pivot operations transform a simplex tableau.
- See how basis selection affects each iteration.
- Understand why Phase I is needed when a feasible starting basis is unavailable.
- Practice translating mathematical edge cases into explicit program behavior and tests.
- Build a small Python package with a clear interface, examples, and automated checks.

## License

No license has been selected yet. Until one is added, reuse and redistribution are not granted by this repository.