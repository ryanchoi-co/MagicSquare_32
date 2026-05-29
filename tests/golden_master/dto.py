"""Golden Master result DTO and text serialization."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True)
class GoldenSuccess:
    """Successful solver placement vector."""

    vector: list[int]

    def serialize(self) -> str:
        return f"Output:\n{self.vector!r}"


@dataclass(frozen=True)
class GoldenError:
    """Structured validation or solver failure."""

    code: str

    def serialize(self) -> str:
        return f"Error:\n{self.code}"


GoldenResult = Union[GoldenSuccess, GoldenError]


def format_grid_input(grid: list[list[int]]) -> str:
    """Render a 4×4 grid as four space-separated rows."""
    return "\n".join(" ".join(str(cell) for cell in row) for row in grid)


def serialize_scenario_block(key: str, grid: list[list[int]], result: GoldenResult) -> str:
    """Serialize one scenario section for the golden master file."""
    lines = [f"[{key}]", "Input:", format_grid_input(grid), result.serialize()]
    return "\n".join(lines)
