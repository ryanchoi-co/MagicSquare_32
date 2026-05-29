"""Reference capture logic for Golden Master bootstrap (tests/scripts only).

Implements Report/02 solver contract: Step A (small→first blank) then Step B.
Not imported by production ``src/`` packages.
"""

from __future__ import annotations

from .dto import GoldenError, GoldenResult, GoldenSuccess


class _UnsolvableDomainError(Exception):
    """Test-only signal when both placement steps fail."""


_MAGIC_CONSTANT = 34
_GRID_SIZE = 4


def row_major_blanks_one_indexed(grid: list[list[int]]) -> list[tuple[int, int]]:
    """Return empty cells in row-major order using 1-indexed coordinates."""
    return [
        (row_idx + 1, col_idx + 1)
        for row_idx in range(_GRID_SIZE)
        for col_idx in range(_GRID_SIZE)
        if grid[row_idx][col_idx] == 0
    ]


def missing_pair(grid: list[list[int]]) -> tuple[int, int]:
    """Return missing numbers (n_small, n_large) for a partial grid."""
    present = {
        grid[r][c] for r in range(_GRID_SIZE) for c in range(_GRID_SIZE) if grid[r][c] != 0
    }
    missing = sorted(set(range(1, 17)) - present)
    return missing[0], missing[1]


def attempt_placement(
    grid: list[list[int]],
    first: int,
    second: int,
) -> list[int] | None:
    """Try placing *first* then *second* at row-major blanks; return int[6] or None."""
    blanks = [
        (row_idx, col_idx)
        for row_idx in range(_GRID_SIZE)
        for col_idx in range(_GRID_SIZE)
        if grid[row_idx][col_idx] == 0
    ]
    if len(blanks) != 2:
        return None
    (r1, c1), (r2, c2) = blanks
    trial = [row[:] for row in grid]
    trial[r1][c1] = first
    trial[r2][c2] = second
    if _is_magic(trial):
        return [r1 + 1, c1 + 1, first, r2 + 1, c2 + 1, second]
    return None


def step_a_succeeds(grid: list[list[int]]) -> bool:
    """Return True when Step A (small-first) completes a magic square."""
    n_small, n_large = missing_pair(grid)
    return attempt_placement(grid, n_small, n_large) is not None


def step_a_fails(grid: list[list[int]]) -> bool:
    """Return True when Step A does not complete a magic square."""
    return not step_a_succeeds(grid)


def _blank_count(grid: list[list[int]]) -> int:
    return sum(1 for row in grid for cell in row if cell == 0)


def _duplicate_non_zero(grid: list[list[int]]) -> bool:
    seen: set[int] = set()
    for row in grid:
        for cell in row:
            if cell == 0:
                continue
            if cell in seen:
                return True
            seen.add(cell)
    return False


def _is_magic(grid: list[list[int]]) -> bool:
    for row in grid:
        if sum(row) != _MAGIC_CONSTANT:
            return False
    for col in range(_GRID_SIZE):
        if sum(grid[row][col] for row in range(_GRID_SIZE)) != _MAGIC_CONSTANT:
            return False
    if sum(grid[i][i] for i in range(_GRID_SIZE)) != _MAGIC_CONSTANT:
        return False
    if sum(grid[i][_GRID_SIZE - 1 - i] for i in range(_GRID_SIZE)) != _MAGIC_CONSTANT:
        return False
    values = [grid[r][c] for r in range(_GRID_SIZE) for c in range(_GRID_SIZE)]
    return set(values) == set(range(1, 17))


def _solve_two_blanks(grid: list[list[int]]) -> list[int]:
    if _blank_count(grid) != 2:
        msg = "exactly 2 empty cells required"
        raise ValueError(msg)
    n_small, n_large = missing_pair(grid)
    step_a = attempt_placement(grid, n_small, n_large)
    if step_a is not None:
        return step_a
    step_b = attempt_placement(grid, n_large, n_small)
    if step_b is not None:
        return step_b
    raise _UnsolvableDomainError("no valid magic square completion")


def capture_reference(grid: list[list[int]]) -> GoldenResult:
    """Return Golden Master DTO for a raw 4×4 grid using reference rules."""
    if len(grid) != _GRID_SIZE or any(len(row) != _GRID_SIZE for row in grid):
        return GoldenError(code="INVALID_SIZE")
    blank_total = _blank_count(grid)
    if blank_total != 2:
        return GoldenError(code="INVALID_BLANK_COUNT")
    for row in grid:
        for cell in row:
            if cell != 0 and (cell < 1 or cell > 16):
                return GoldenError(code="INVALID_VALUE_RANGE")
    if _duplicate_non_zero(grid):
        return GoldenError(code="DUPLICATE_NUMBER")
    try:
        vector = _solve_two_blanks(grid)
    except _UnsolvableDomainError:
        return GoldenError(code="NO_VALID_MAGIC_SQUARE")
    return GoldenSuccess(vector=vector)
