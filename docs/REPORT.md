# Input format and example results

## JSON format

A problem file is a JSON object with these fields:

| Field | Type | Meaning |
| --- | --- | --- |
| `name` | string | Human-readable problem name. |
| `sense` | string | `"min"` or `"max"`. |
| `objective` | array of numbers | Objective coefficient for each variable. |
| `constraints` | array of objects | Constraint rows. Each has `coefficients`, `sense`, and `rhs`. |
| `variables` | array of strings, optional | Variable names in objective order; defaults to `x1`, `x2`, etc. |
| `bounds` | string, optional | Currently must be `"nonnegative"`; defaults to that value. |

Each constraint's `coefficients` array must have the same length as `objective`. Constraint `sense` may be `"<="`, `">="`, or `"="`. All coefficient and right-hand-side values must be finite numbers. Variables are assumed nonnegative. The parser rejects malformed JSON, missing fields, inconsistent dimensions, unsupported bounds, and invalid values.

Mathematically, each row is interpreted as

\[
 a_{i1}x_1 + \cdots + a_{in}x_n \; (\le,\ge,=) \; b_i,
 \qquad x_j \ge 0.
\]

## Example: diet cost

`examples/diet_problem.json` minimizes `0.5 food_a + 0.8 food_b`, meeting two minimum requirements while limiting each food to at most 10 units. The constraint intersection gives `food_a = 2.4` and `food_b = 3.2`, with minimum cost `3.76`. This is the expected optimum.

## Example: unbounded objective

`examples/unbounded_case.json` maximizes `x1 + x2` subject to `x1 - x2 <= 2` and nonnegativity. Setting `x1 = x2 = t` is feasible for every `t >= 0`, while the objective `2t` grows without bound. The expected result is **unbounded**.

## Current implementation boundary

At this setup stage, the package validates input and the command line confirms whether a JSON file is structurally valid. The optimization algorithms have not been implemented yet, so the example results above are mathematical expected results, not output produced by the program.
