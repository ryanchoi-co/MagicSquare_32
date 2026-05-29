"""Domain RED skeleton — D-VAL-01~06 (MagicSquareValidator / is_magic_square).

Domain Mock forbidden. G0-based variants per Report/08.
"""

from __future__ import annotations

import pytest

# from magicsquare.entity.services.magic_square_validator import is_magic_square

pytestmark = pytest.mark.domain


def test_d_val_01_g0_complete_grid_returns_true() -> None:
    # Given: G0 complete magic square
    # When: is_magic_square(grid)
    # Then: True
    pytest.fail("RED: D-VAL-01 — G0 complete grid → true")


def test_d_val_02_g0_row_sum_mismatch_returns_false() -> None:
    # Given: G0 with one row sum broken (≠ M=34)
    # When: is_magic_square(grid)
    # Then: False
    pytest.fail("RED: D-VAL-02 — row sum mismatch → false")


def test_d_val_03_g0_col_sum_mismatch_returns_false() -> None:
    # Given: G0 with one column sum broken
    # When: is_magic_square(grid)
    # Then: False
    pytest.fail("RED: D-VAL-03 — column sum mismatch → false")


def test_d_val_04_g0_diag_sum_mismatch_returns_false() -> None:
    # Given: G0 with main or anti diagonal sum broken
    # When: is_magic_square(grid)
    # Then: False
    pytest.fail("RED: D-VAL-04 — diagonal sum mismatch → false")


def test_d_val_05_g0_duplicate_or_out_of_set_returns_false() -> None:
    # Given: G0-based full grid with duplicate non-zero or value 17
    # When: is_magic_square(grid)
    # Then: False
    pytest.fail("RED: D-VAL-05 — duplicate or out of {1..16} → false")


def test_d_val_06_g0_zero_in_full_grid_returns_false() -> None:
    # Given: G0 with one cell replaced by 0
    # When: is_magic_square(grid)
    # Then: False
    pytest.fail("RED: D-VAL-06 — zero in complete grid → false")
