"""Domain RED skeleton — D-MIS-01 (missing numbers, ascending pair).

Domain Mock forbidden. Report/08 G1 → (7, 10).
"""

from __future__ import annotations

import pytest

# from magicsquare.entity.services.missing_number_finder import find_not_exist_nums

pytestmark = pytest.mark.domain


def test_d_mis_01_g1_ascending_missing_pair() -> None:
    # Given: G1 partial grid
    # When: find_not_exist_nums(grid)
    # Then: (7, 10) ascending
    pytest.fail("RED: D-MIS-01 — G1 missing numbers (7, 10) ascending")
