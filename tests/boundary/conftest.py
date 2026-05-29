"""Shared fixtures and constants for Boundary UT-* / AC-FR-01-01 tests."""

from __future__ import annotations

from typing import Any

import pytest

AC_FR_01_01 = "AC-FR-01-01"
PRD_SECTION_INVALID_SIZE = "PRD §8.1 INVALID_SIZE"

INVALID_SIZE_CODE = "INVALID_SIZE"
INVALID_SIZE_MESSAGE = "Grid must be 4x4."

# UT-01 / BV-04a: 3 rows × 4 columns
GRID_3X4: list[list[int]] = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# BV-04b: 4 rows × 3 columns
GRID_4X3: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]

# BV-03: four rows, zero columns per row
GRID_FOUR_EMPTY_ROWS: list[list[int]] = [[]] * 4

# AC-FR-01-01 catalog only — must not include valid partial 4×4 (AC-FR-01-02+)
AC_FR_01_01_INVALID_SIZE_GRIDS: tuple[Any, ...] = (
    None,
    [],
    GRID_FOUR_EMPTY_ROWS,
    GRID_3X4,
    GRID_4X3,
)

# Out of scope for AC-FR-01-01 (AC-FR-01-02~05 / FR-02~05); must stay out of RED suite
OUT_OF_SCOPE_VALID_PARTIAL_4X4: list[list[int]] = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

OUT_OF_SCOPE_SINGLE_EMPTY_4X4: list[list[int]] = [
    [1, 2, 3, 4],
    [5, 0, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

OUT_OF_SCOPE_VALUE_17_4X4: list[list[int]] = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 17],
]

FORBIDDEN_NON_SIZE_ERROR_CODES: frozenset[str] = frozenset(
    {
        "EMPTY_COUNT",
        "VALUE_RANGE",
        "DUPLICATE",
        "NO_SOLUTION",
        "UI_ERR_EMPTY_COUNT",
        "UI_ERR_VALUE_RANGE",
        "UI_ERR_DUPLICATE",
        "UI_ERR_NO_SOLUTION",
    }
)


@pytest.fixture
def invalid_size_code() -> str:
    """PRD §8.1 INVALID_SIZE code constant."""
    return INVALID_SIZE_CODE


@pytest.fixture
def invalid_size_message() -> str:
    """PRD §8.1 INVALID_SIZE message constant."""
    return INVALID_SIZE_MESSAGE
