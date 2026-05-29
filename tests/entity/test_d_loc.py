"""Domain RED skeleton — D-LOC-01 (blank coordinates, row-major).

Domain Mock forbidden. Report/08 G1 fixture (tests/conftest.py when enabled).
"""

from __future__ import annotations

import pytest

# from magicsquare.entity.services.empty_cell_locator import find_blank_coords

pytestmark = pytest.mark.domain


def test_d_loc_01_g1_row_major_blank_coords() -> None:
    # Given: G1 partial grid
    # When: find_blank_coords(grid)
    # Then: [(2,2), (3,3)] 1-index order
    pytest.fail("RED: D-LOC-01 — G1 row-major blanks (2,2) then (3,3)")
