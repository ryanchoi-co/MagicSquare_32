"""Boundary RED tests for AC-FR-01-01 — grid size precondition (INVALID_SIZE).

AC-FR-01-01, PRD §8.1 INVALID_SIZE — 4×4 선행 검증; Boundary 구현 전 RED.
"""

from __future__ import annotations

from typing import Any
from unittest.mock import Mock

import pytest

from .conftest import (
    AC_FR_01_01,
    AC_FR_01_01_INVALID_SIZE_GRIDS,
    FORBIDDEN_NON_SIZE_ERROR_CODES,
    GRID_3X4,
    GRID_4X3,
    GRID_FOUR_EMPTY_ROWS,
    INVALID_SIZE_CODE,
    INVALID_SIZE_MESSAGE,
    OUT_OF_SCOPE_SINGLE_EMPTY_4X4,
    OUT_OF_SCOPE_VALID_PARTIAL_4X4,
    OUT_OF_SCOPE_VALUE_17_4X4,
    PRD_SECTION_INVALID_SIZE,
)

pytestmark = pytest.mark.boundary


def _submit_grid(grid: Any, solver_port: Mock) -> Any:
    """Invoke boundary orchestrator (RED: module not implemented yet)."""
    try:
        from magicsquare.boundary.orchestrator import process_grid_submission
    except ModuleNotFoundError as exc:
        pytest.fail(f"{AC_FR_01_01} RED: boundary orchestrator missing — {exc}")
    return process_grid_submission(grid=grid, solver_port=solver_port)


def _validation_failure_type() -> type[Any]:
    try:
        from magicsquare.boundary.dto import ValidationFailureResult
    except ModuleNotFoundError as exc:
        pytest.fail(f"{AC_FR_01_01} RED: ValidationFailureResult DTO missing — {exc}")
    return ValidationFailureResult


def _domain_solver_port_type() -> type[Any]:
    try:
        from magicsquare.boundary.ports import DomainSolverPort
    except ModuleNotFoundError as exc:
        pytest.fail(f"{AC_FR_01_01} RED: DomainSolverPort missing — {exc}")
    return DomainSolverPort


def _make_solver_port() -> Mock:
    port_type = _domain_solver_port_type()
    solver_port = Mock(spec=port_type)
    solver_port.resolve = Mock()
    return solver_port


class TestAcFr0101NormalFailureReturn:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — 정상 실패 반환 (Happy Path of Failure)."""

    def test_none_grid_returns_validation_failure_result_type(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — failure DTO type."""
        # Given
        grid = None
        solver_port = _make_solver_port()
        failure_type = _validation_failure_type()

        # When
        result = _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        assert isinstance(result, failure_type)

    def test_none_grid_returns_invalid_size_code(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — code field."""
        # Given
        grid = None
        solver_port = _make_solver_port()

        # When
        result = _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        assert result.code == INVALID_SIZE_CODE

    def test_none_grid_returns_exact_prd_message(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — message field."""
        # Given
        grid = None
        solver_port = _make_solver_port()

        # When
        result = _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        assert result.message == INVALID_SIZE_MESSAGE

    def test_none_grid_returns_failure_not_success_tuple(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — no int[6] success vector."""
        # Given
        grid = None
        solver_port = _make_solver_port()

        # When
        result = _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        assert not isinstance(result, (list, tuple))

    def test_none_grid_failure_exposes_code_and_message_attributes(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — structured failure fields."""
        # Given
        grid = None
        solver_port = _make_solver_port()

        # When
        result = _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        assert getattr(result, "code", None) == INVALID_SIZE_CODE
        assert getattr(result, "message", None) == INVALID_SIZE_MESSAGE


class TestAcFr0101BoundaryValues:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — 경계값 (크기 불일치 / 결손 격자)."""

    def test_empty_list_returns_invalid_size_code(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — grid=[]."""
        # Given
        grid: list[list[int]] = []
        solver_port = _make_solver_port()

        # When
        result = _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        assert result.code == INVALID_SIZE_CODE

    def test_four_empty_rows_returns_invalid_size_code(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — grid=[[]]*4."""
        # Given
        grid = GRID_FOUR_EMPTY_ROWS
        solver_port = _make_solver_port()

        # When
        result = _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        assert result.code == INVALID_SIZE_CODE

    def test_3x4_grid_returns_invalid_size_code(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — UT-01 3×4."""
        # Given
        grid = GRID_3X4
        solver_port = _make_solver_port()

        # When
        result = _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        assert result.code == INVALID_SIZE_CODE

    def test_4x3_grid_returns_invalid_size_code(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — BV-04b 4×3."""
        # Given
        grid = GRID_4X3
        solver_port = _make_solver_port()

        # When
        result = _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        assert result.code == INVALID_SIZE_CODE

    @pytest.mark.parametrize("grid", AC_FR_01_01_INVALID_SIZE_GRIDS)
    def test_invalid_size_catalog_grids_return_invalid_size_code(
        self,
        grid: Any,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — catalog consistency."""
        # Given
        solver_port = _make_solver_port()

        # When
        result = _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        assert result.code == INVALID_SIZE_CODE
        assert result.message == INVALID_SIZE_MESSAGE


class TestAcFr0101Isolation:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — Domain resolve() 격리 (mock/spy)."""

    def test_none_grid_resolve_not_called_assert_not_called(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — resolve 0회 (None)."""
        # Given
        grid = None
        solver_port = _make_solver_port()

        # When
        _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        solver_port.resolve.assert_not_called()

    def test_empty_list_resolve_not_called(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — resolve 0회 ([])."""
        # Given
        grid: list[list[int]] = []
        solver_port = _make_solver_port()

        # When
        _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        solver_port.resolve.assert_not_called()

    def test_3x4_grid_resolve_not_called(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — resolve 0회 (3×4)."""
        # Given
        grid = GRID_3X4
        solver_port = _make_solver_port()

        # When
        _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        solver_port.resolve.assert_not_called()

    def test_none_grid_resolve_call_count_zero(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — call_count == 0."""
        # Given
        grid = None
        solver_port = _make_solver_port()

        # When
        _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        assert solver_port.resolve.call_count == 0

    def test_four_empty_rows_resolve_call_count_zero(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — call_count == 0 ([[]]*4)."""
        # Given
        grid = GRID_FOUR_EMPTY_ROWS
        solver_port = _make_solver_port()

        # When
        _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        assert solver_port.resolve.call_count == 0


class TestAcFr0101MessageExactness:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — 메시지·코드 문자 단위 동일성."""

    def test_none_grid_message_exact_char_match(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — message equality."""
        # Given
        grid = None
        solver_port = _make_solver_port()
        expected = "Grid must be 4x4."

        # When
        result = _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        assert result.message == expected
        assert list(result.message) == list(expected)

    def test_none_grid_code_exact_char_match(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — code equality."""
        # Given
        grid = None
        solver_port = _make_solver_port()
        expected = "INVALID_SIZE"

        # When
        result = _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        assert result.code == expected
        assert list(result.code) == list(expected)

    def test_empty_list_message_exact_char_match(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — [] message."""
        # Given
        grid: list[list[int]] = []
        solver_port = _make_solver_port()

        # When
        result = _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        assert result.message == INVALID_SIZE_MESSAGE

    def test_3x4_grid_message_exact_char_match(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — 3×4 message."""
        # Given
        grid = GRID_3X4
        solver_port = _make_solver_port()

        # When
        result = _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        assert result.message == INVALID_SIZE_MESSAGE

    def test_prd_constants_match_result_fields_for_none_grid(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — (code, message) tuple."""
        # Given
        grid = None
        solver_port = _make_solver_port()

        # When
        result = _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        assert (result.code, result.message) == (
            INVALID_SIZE_CODE,
            INVALID_SIZE_MESSAGE,
        )


class TestAcFr0101ScopeLimit:
    """AC-FR-01-01 — AC-FR-01-02~05 / FR-02~05 케이스 포함 금지."""

    def test_scope_catalog_excludes_valid_partial_4x4_grid(self) -> None:
        """AC-FR-01-01 — F-OK-01 style 4×4 not in RED catalog."""
        # Given / When / Then
        assert OUT_OF_SCOPE_VALID_PARTIAL_4X4 not in AC_FR_01_01_INVALID_SIZE_GRIDS

    def test_scope_catalog_excludes_single_empty_cell_4x4(self) -> None:
        """AC-FR-01-01 — AC-FR-01-02 empty-count case excluded."""
        # Given / When / Then
        assert OUT_OF_SCOPE_SINGLE_EMPTY_4X4 not in AC_FR_01_01_INVALID_SIZE_GRIDS

    def test_scope_catalog_excludes_value_17_4x4(self) -> None:
        """AC-FR-01-01 — AC-FR-01-03 value-range case excluded."""
        # Given / When / Then
        assert OUT_OF_SCOPE_VALUE_17_4X4 not in AC_FR_01_01_INVALID_SIZE_GRIDS

    @pytest.mark.parametrize("grid", AC_FR_01_01_INVALID_SIZE_GRIDS)
    def test_scope_failure_code_not_other_contract_codes(
        self,
        grid: Any,
    ) -> None:
        """AC-FR-01-01 — only INVALID_SIZE, never FR-02~05 codes."""
        # Given
        solver_port = _make_solver_port()

        # When
        result = _submit_grid(grid=grid, solver_port=solver_port)

        # Then
        assert result.code == INVALID_SIZE_CODE
        assert result.code not in FORBIDDEN_NON_SIZE_ERROR_CODES

    def test_scope_module_targets_ac_fr_01_01_only(self) -> None:
        """AC-FR-01-01 — excluded AC ids documented; no FR-02~05 tests here."""
        # Given
        excluded = (
            "AC-FR-01-02",
            "AC-FR-01-03",
            "AC-FR-01-04",
            "AC-FR-01-05",
            "FR-02",
            "FR-03",
            "FR-04",
            "FR-05",
        )

        # When / Then
        assert AC_FR_01_01 == "AC-FR-01-01"
        assert PRD_SECTION_INVALID_SIZE.endswith("INVALID_SIZE")
        for ac_id in excluded:
            assert ac_id != AC_FR_01_01
