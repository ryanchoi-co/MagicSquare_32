"""Demo grids for GUI — same values as ``tests/boundary/conftest.py`` (BV-04a/b)."""

from __future__ import annotations

# BV-04a: 3 rows × 4 columns (not 4×4)
GRID_BV_04A_3_ROWS_4_COLS: list[list[int]] = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# BV-04b: 4 rows × 3 columns (not 4×4)
GRID_BV_04B_4_ROWS_3_COLS: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]
