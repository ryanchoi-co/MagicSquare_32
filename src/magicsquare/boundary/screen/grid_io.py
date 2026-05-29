"""Parse 4×4 grid values from UI cell text (no Qt imports)."""

from __future__ import annotations


class GridCellParseError(ValueError):
    """Raised when a cell cannot be parsed as 0 or 1–16."""

    def __init__(self, row: int, col: int, raw: str) -> None:
        """Initialize with 1-indexed coordinates and raw cell text."""
        super().__init__(f"Invalid value at ({row},{col}): {raw!r}")
        self.row = row
        self.col = col
        self.raw = raw


def parse_cell_text(text: str) -> int:
    """Parse one cell: empty → 0; otherwise integer 0 or 1–16.

    Args:
        text: Raw widget text.

    Returns:
        Grid cell value.

    Raises:
        GridCellParseError: Non-numeric or out-of-range value.
    """
    stripped = text.strip()
    if stripped == "":
        return 0
    if not stripped.isdigit():
        raise GridCellParseError(0, 0, text)
    value = int(stripped)
    if value < 0 or value > 16:
        raise GridCellParseError(0, 0, text)
    return value


def read_grid_from_cell_texts(rows: list[list[str]]) -> list[list[int]]:
    """Convert 4×4 cell text rows to ``list[list[int]]`` for the orchestrator.

    Args:
        rows: Four rows of four cell strings (1-indexed errors in exceptions).

    Raises:
        GridCellParseError: Any cell fails ``parse_cell_text``.
        ValueError: Row or column count is not four.
    """
    if len(rows) != 4:
        raise ValueError("Grid must have exactly 4 rows.")
    grid: list[list[int]] = []
    for row_idx, row in enumerate(rows, start=1):
        if len(row) != 4:
            raise ValueError("Each row must have exactly 4 columns.")
        parsed_row: list[int] = []
        for col_idx, text in enumerate(row, start=1):
            try:
                parsed_row.append(parse_cell_text(text))
            except GridCellParseError as exc:
                raise GridCellParseError(row_idx, col_idx, text) from exc
        grid.append(parsed_row)
    return grid
