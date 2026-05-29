"""Boundary RED skeleton — U-OUT-01~03 (output contract, Domain port Mock).

Report/08 SSOT; Domain Mock allowed; no assert on expected values in skeleton phase.
"""

from __future__ import annotations

import pytest

# from magicsquare.boundary.ui_boundary import UIBoundary
# from magicsquare.boundary.ports import DomainSolverPort
# from unittest.mock import Mock

pytestmark = pytest.mark.boundary


class TestUOut01SuccessVectorLength:
    """U-OUT-01 — success path returns int[6] (len==6)."""

    def test_u_out_01_success_returns_length_six(self) -> None:
        # Given: G1 partial grid; Mock DomainSolverPort returns [2,2,7,3,3,10]
        # When: UIBoundary.solve(matrix, solver_port=mock)
        # Then: success envelope; len(result)==6
        pytest.fail("RED: U-OUT-01 — success vector length 6")


class TestUOut02CoordinatesOneIndexed:
    """U-OUT-02 — r,c coordinates in [1,4] (1-index)."""

    def test_u_out_02_coordinates_one_indexed(self) -> None:
        # Given: G1 + Mock success vector [2,2,7,3,3,10]
        # When: UIBoundary.solve(matrix, solver_port=mock)
        # Then: r1,c1,r2,c2 each in [1,4]
        pytest.fail("RED: U-OUT-02 — coordinates 1-index in [1,4]")


class TestUOut03DomainVectorVerbatim:
    """U-OUT-03 — UI returns Domain vector verbatim (UX-05, no reorder)."""

    def test_u_out_03_domain_vector_passed_through_verbatim(self) -> None:
        # Given: G1; Mock port returns fixed int[6]
        # When: UIBoundary.solve(matrix, solver_port=mock)
        # Then: output equals mock return (no n1/n2 reshuffle)
        pytest.fail("RED: U-OUT-03 — Domain solution vector verbatim to caller")
