"""Boundary RED skeleton — U-IN-04~08 (input validation).

U-IN-01~03 covered by tests/boundary/test_ac_fr_01_01_invalid_size.py (do not duplicate).
Report/08 SSOT; no production asserts in skeleton phase.
"""

from __future__ import annotations

import pytest

# from magicsquare.boundary.input_validator import InputValidator

pytestmark = pytest.mark.boundary


class TestUIn04ZeroEmptyCells:
    """U-IN-04 — empty count: zero blanks → E002."""

    def test_u_in_04_zero_empty_cells_returns_e002(self) -> None:
        # Given: 4×4 matrix with count(0)==0 (no empty cells)
        # When: InputValidator.validate(matrix)
        # Then: Failure envelope E002 (not implemented in skeleton)
        pytest.fail("RED: U-IN-04 — zero blanks → E002")


class TestUIn05ThreeEmptyCells:
    """U-IN-05 — empty count: three blanks → E002."""

    def test_u_in_05_three_empty_cells_returns_e002(self) -> None:
        # Given: 4×4 matrix with count(0)==3
        # When: InputValidator.validate(matrix)
        # Then: Failure envelope E002
        pytest.fail("RED: U-IN-05 — three blanks → E002")


class TestUIn06ValueBelowRange:
    """U-IN-06 — value range: cell -1 → E004."""

    def test_u_in_06_minus_one_returns_e004(self) -> None:
        # Given: 4×4 with exactly two zeros and one cell -1
        # When: InputValidator.validate(matrix)
        # Then: Failure envelope E004
        pytest.fail("RED: U-IN-06 — value -1 → E004")


class TestUIn07ValueAboveRange:
    """U-IN-07 — value range: cell 17 → E004."""

    def test_u_in_07_seventeen_returns_e004(self) -> None:
        # Given: 4×4 with exactly two zeros and one cell 17
        # When: InputValidator.validate(matrix)
        # Then: Failure envelope E004
        pytest.fail("RED: U-IN-07 — value 17 → E004")


class TestUIn08DuplicateNonZero:
    """U-IN-08 — duplicate non-zero → E005."""

    def test_u_in_08_duplicate_nonzero_returns_e005(self) -> None:
        # Given: 4×4 with duplicate non-zero (e.g. two cells with 5)
        # When: InputValidator.validate(matrix)
        # Then: Failure envelope E005
        pytest.fail("RED: U-IN-08 — duplicate non-zero → E005")
