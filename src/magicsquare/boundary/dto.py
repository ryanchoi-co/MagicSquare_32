"""Boundary data transfer objects for success and validation failure responses."""

from __future__ import annotations

from pydantic import BaseModel


class ValidationFailureResult(BaseModel):
    """Structured failure returned when grid input fails boundary preconditions.

    Attributes:
        code: Machine-readable failure code (e.g. ``INVALID_SIZE``).
        message: Human-readable message matching PRD contract exactly.
    """

    code: str
    message: str
