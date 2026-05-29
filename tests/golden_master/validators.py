"""Golden Master contract validators — int[6], row-major, Step A/B rules."""

from __future__ import annotations

from .dto import GoldenError, GoldenResult, GoldenSuccess
from .reference import (
    attempt_placement,
    missing_pair,
    row_major_blanks_one_indexed,
    step_a_fails,
    step_a_succeeds,
)

_GRID_SIZE = 4


def assert_int6_format(vector: list[int]) -> None:
    """Output must be exactly six integers."""
    assert len(vector) == 6, f"Expected int[6], got len={len(vector)}: {vector!r}"
    assert all(isinstance(value, int) for value in vector), (
        f"All elements must be int: {vector!r}"
    )


def assert_one_index_coordinates(vector: list[int]) -> None:
    """Coordinates r,c must be 1-indexed in [1, 4]."""
    r1, c1, _n1, r2, c2, _n2 = vector
    for name, value in (("r1", r1), ("c1", c1), ("r2", r2), ("c2", c2)):
        assert 1 <= value <= _GRID_SIZE, f"{name}={value} out of 1-index range [1,4]"


def assert_row_major_blank_order(grid: list[list[int]], vector: list[int]) -> None:
    """Placement coordinates follow row-major empty-cell scan order."""
    expected = row_major_blanks_one_indexed(grid)
    r1, c1, _n1, r2, c2, _n2 = vector
    assert (r1, c1) == expected[0], (
        f"First blank must be row-major {expected[0]}, got ({r1},{c1})"
    )
    assert (r2, c2) == expected[1], (
        f"Second blank must be row-major {expected[1]}, got ({r2},{c2})"
    )


def assert_small_first_combination(grid: list[list[int]], vector: list[int]) -> None:
    """Step A: n_small at first blank, n_large at second blank."""
    n_small, n_large = missing_pair(grid)
    _r1, _c1, n1, _r2, _c2, n2 = vector
    assert (n1, n2) == (n_small, n_large), (
        f"Step A expects (n_small,n_large)=({n_small},{n_large}), got ({n1},{n2})"
    )
    assert step_a_succeeds(grid), "GM-TC-01 requires Step A success"


def assert_reverse_fallback_combination(grid: list[list[int]], vector: list[int]) -> None:
    """Step B: Step A fails, reverse placement succeeds."""
    n_small, n_large = missing_pair(grid)
    _r1, _c1, n1, _r2, _c2, n2 = vector
    assert step_a_fails(grid), "GM-TC-02 requires Step A failure before reverse"
    assert (n1, n2) == (n_large, n_small), (
        f"Step B expects (n_large,n_small)=({n_large},{n_small}), got ({n1},{n2})"
    )
    reverse_vector = attempt_placement(grid, n_large, n_small)
    assert reverse_vector == vector, (
        f"Reverse fallback vector mismatch: expected {reverse_vector!r}"
    )


def assert_success_contract(grid: list[list[int]], vector: list[int]) -> None:
    """Full success-path contract for Golden Master."""
    assert_int6_format(vector)
    assert_one_index_coordinates(vector)
    assert_row_major_blank_order(grid, vector)


def assert_error_contract(result: GoldenResult, expected_code: str) -> None:
    """Failure envelope must carry the Golden Master error code."""
    assert isinstance(result, GoldenError), (
        f"Expected GoldenError({expected_code!r}), got {result!r}"
    )
    assert result.code == expected_code, (
        f"Error code mismatch: expected {expected_code!r}, got {result.code!r}"
    )


def assert_success_result(grid: list[list[int]], result: GoldenResult) -> list[int]:
    """Assert success DTO and return vector."""
    assert isinstance(result, GoldenSuccess), f"Expected success, got {result!r}"
    assert_success_contract(grid, result.vector)
    return result.vector
