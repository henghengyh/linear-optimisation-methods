"""Tableau abstraction for each step of the Simplex Method."""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray


class Tableau:
    """Store tableau inputs as floating point arrays for safe pivot operations."""

    # Using ArrayLike gives the flexibility to implement test cases using list-of-lists
    def __init__(
        self,
        matrix: ArrayLike,
        vector: ArrayLike,
        objective: ArrayLike,
        initial_basis: list[int],
        var_names: list[str],
    ) -> None:
        
        # Create a (deep) copy of each data
        self.matrix = np.array(matrix, dtype=np.float64, copy=True) 
        self.vector = np.array(vector, dtype=np.float64, copy=True)
        self.objective = np.array(objective, dtype=np.float64, copy=True)
        self.initial_basis = list(initial_basis)
        self.var_names = list(var_names)

        top = np.column_stack((matrix, vector))
        bottom = np.append(objective, 0.0)
        self.grid: NDArray[np.float64] = np.vstack((top, bottom)).astype(np.float64)

    def get_basis(self) -> list[int]:
        """Returns the index of the matrix columns of the basis of the LPP."""
        raise NotImplementedError

    def get_solution(self) -> NDArray[np.float64]:
        """Returns a length-n solution vector with non-basic variables as 0.0"""
        raise NotImplementedError

    def objective_value(self) -> float:
        """Returns the current objective value from the RHS of the objective row."""
        raise NotImplementedError

    def is_valid_tableau(self) -> bool:
        """Ensure all RHS entries remain non-negative."""
        raise NotImplementedError

    def pivot(self, pivot_row: int, pivot_col: int) -> None:
        raise NotImplementedError

    def snapshot(self) -> tuple[NDArray[np.float64], list[int]]: 
        """return (self.grid.copy(), self.basis.copy())"""
        raise NotImplementedError
    
    def _get_pivot_column(self) -> int | None:
        """
        Returns the index of pivot column in the current Tableau. 
        Return None when no improving column exists.
        """
        raise NotImplementedError

    def _get_minimum_ratio(self, pivot_col: int) -> tuple[float, int]:
        """
        Returns (theta, row_index) of the departing variable.
        Raises UnboundedProblemError if all entries in pivot column are nonpositive.
        """
        raise NotImplementedError

    def _normalize_row(self, row: int) -> None:
        """Normalizes the row of the departing variable."""
        raise NotImplementedError

    def _eliminate_pivot_entries(self, pivot_row: int, pivot_col: int) -> None:
        """
        Eliminates non-zero entries in the pivot column except for the row
        of departing variable
        """
        raise NotImplementedError

    def _update_basis(self, pivot_row: int, entering_col: int) -> None:
        """
        Updates the basic variables record.
        """
        raise NotImplementedError
        
