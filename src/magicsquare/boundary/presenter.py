"""Boundary presenters — map DTOs to user-visible strings (Screen Layer)."""

from __future__ import annotations

from magicsquare.boundary.dto import ValidationFailureResult

_PENDING_SOLVER_MESSAGE = (
    "Grid size is valid (4×4). "
    "Empty-cell count, value range, and solver are not implemented yet."
)


def format_validation_failure(result: ValidationFailureResult) -> str:
    """Return the PRD failure message for display (AC-FR-01-01 contract).

    Args:
        result: Structured boundary validation failure.

    Returns:
        Exact ``message`` field for GUI / CLI display.
    """
    return result.message


def format_solver_pending() -> str:
    """Return message when size validation passes but solve path is not wired."""
    return _PENDING_SOLVER_MESSAGE
