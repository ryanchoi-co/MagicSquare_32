"""Boundary orchestrator — validates input and delegates to domain ports."""

from __future__ import annotations

from typing import Any

from magicsquare.boundary.dto import ValidationFailureResult
from magicsquare.boundary.ports import DomainSolverPort

_INVALID_SIZE_CODE = "INVALID_SIZE"
_INVALID_SIZE_MESSAGE = "Grid must be 4x4."


def process_grid_submission(
    grid: Any,
    solver_port: DomainSolverPort,
) -> Any:
    """Validate grid input and return failure or delegate to the domain solver.

    Args:
        grid: Raw 4×4 grid submission (``None`` or nested lists of ints).
        solver_port: Domain solver port; not invoked when validation fails.

    Returns:
        ``ValidationFailureResult`` when ``grid`` is ``None`` or ``[]``; otherwise pending.
    """
    if grid is None:
        return ValidationFailureResult(
            code=_INVALID_SIZE_CODE,
            message=_INVALID_SIZE_MESSAGE,
        )
    if len(grid) == 0:
        return ValidationFailureResult(
            code=_INVALID_SIZE_CODE,
            message=_INVALID_SIZE_MESSAGE,
        )
    raise NotImplementedError("Size validation beyond empty list is not implemented")
