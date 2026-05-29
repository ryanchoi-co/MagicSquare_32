"""Boundary ports — abstractions for domain services invoked by orchestrators."""

from __future__ import annotations

from typing import Any, Protocol


class DomainSolverPort(Protocol):
    """Port for partial-grid resolution; mocked in boundary contract tests."""

    def resolve(self, grid: Any) -> Any:
        """Resolve two empty cells and return a placement vector or domain failure."""
        ...
