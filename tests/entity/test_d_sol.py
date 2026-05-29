"""Domain RED skeleton — D-SOL-01~04 (TwoCellSolver / solution).

Domain Mock forbidden. Report/08 G1/G2/G3.
"""

from __future__ import annotations

import pytest

# from magicsquare.entity.services.two_cell_solver import solution

pytestmark = pytest.mark.domain


def test_d_sol_01_g1_step_a_success_vector() -> None:
    # Given: G1 partial grid
    # When: solution(grid)
    # Then: [2, 2, 7, 3, 3, 10]
    pytest.fail("RED: D-SOL-01 — G1 Step A success vector")


def test_d_sol_02_g2_step_b_only_success_vector() -> None:
    # Given: G2 partial grid [PLACEHOLDER — grid TBD]
    # When: solution(grid)
    # Then: [3, 3, 6, 4, 4, 1]
    pytest.fail("RED: D-SOL-02 — G2 TBD")


def test_d_sol_03_g3_both_steps_fail_unsolvable() -> None:
    # Given: G3 partial grid [PLACEHOLDER — grid TBD]
    # When: solution(grid)
    # Then: UnsolvableDomainError (or NO_VALID_COMPLETION)
    pytest.fail("RED: D-SOL-03 — G3 both placements fail")


def test_d_sol_04_g1_output_length_and_one_index_coords() -> None:
    # Given: G1 partial grid
    # When: solution(grid)
    # Then: len==6; r,c in [1,4]
    pytest.fail("RED: D-SOL-04 — G1 output length 6 and 1-index coords")
