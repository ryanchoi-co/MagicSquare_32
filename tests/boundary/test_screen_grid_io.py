"""Unit tests for screen grid I/O (no Qt)."""

from __future__ import annotations

import pytest

from magicsquare.boundary.screen.grid_io import (
    GridCellParseError,
    parse_cell_text,
    read_grid_from_cell_texts,
)


class TestParseCellText:
    def test_empty_is_zero(self) -> None:
        assert parse_cell_text("") == 0
        assert parse_cell_text("   ") == 0

    def test_zero_and_sixteen(self) -> None:
        assert parse_cell_text("0") == 0
        assert parse_cell_text("16") == 16

    def test_rejects_non_numeric(self) -> None:
        with pytest.raises(GridCellParseError):
            parse_cell_text("abc")

    def test_rejects_seventeen(self) -> None:
        with pytest.raises(GridCellParseError):
            parse_cell_text("17")


class TestReadGridFromCellTexts:
    def test_four_by_four_empty_is_all_zeros(self) -> None:
        rows = [[""] * 4 for _ in range(4)]
        assert read_grid_from_cell_texts(rows) == [[0] * 4 for _ in range(4)]

    def test_rejects_wrong_row_count(self) -> None:
        with pytest.raises(ValueError, match="4 rows"):
            read_grid_from_cell_texts([["1"] * 4] * 3)
