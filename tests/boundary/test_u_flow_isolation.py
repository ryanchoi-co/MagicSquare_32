"""Boundary RED skeleton — U-FLOW-02 extended (invalid → execute/resolve 0).

Extends Story 1 AC beyond AC-FR-01-01 size-only suite.
Report/08 SSOT; spy on DomainSolverPort.execute (or resolve) — comment only in skeleton.
"""

from __future__ import annotations

import pytest

# from magicsquare.boundary.ui_boundary import UIBoundary
# from magicsquare.boundary.ports import DomainSolverPort
# from unittest.mock import Mock

pytestmark = pytest.mark.boundary


class TestUFlow02InvalidNeverCallsExecute:
    """U-FLOW-02 — validation failure must not call domain execute."""

    def test_u_flow_02_null_matrix_execute_call_count_zero(self) -> None:
        # Given: matrix=null; solver_port=Mock(spec=DomainSolverPort); spy execute
        # When: UIBoundary.solve(matrix, solver_port=mock)
        # Then: mock.execute.call_count == 0
        pytest.fail("RED: U-FLOW-02 — null input → execute 0 calls")

    def test_u_flow_02_e002_empty_count_execute_call_count_zero(self) -> None:
        # Given: matrix with wrong empty count (E002 path)
        # When: UIBoundary.solve(matrix, solver_port=mock)
        # Then: mock.execute.call_count == 0
        pytest.fail("RED: U-FLOW-02 — E002 path → execute 0 calls")

    def test_u_flow_02_e005_duplicate_execute_call_count_zero(self) -> None:
        # Given: matrix with duplicate non-zero (E005 path)
        # When: UIBoundary.solve(matrix, solver_port=mock)
        # Then: mock.execute.call_count == 0
        pytest.fail("RED: U-FLOW-02 — E005 path → execute 0 calls")
