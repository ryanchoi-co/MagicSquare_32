"""Golden Master approval regression — GM-TC-01~05 Magic Square solver output."""

from __future__ import annotations

import os
from pathlib import Path

import pytest

from .approve import (
    assert_golden_master_document,
    assert_golden_section,
    read_expected_file,
)
from .capture import (
    capture_all_scenarios,
    capture_scenario,
    capture_scenario_body,
)
from .scenarios import (
    GM_TC_01_NORMAL_SUCCESS,
    GM_TC_02_REVERSE_SUCCESS,
    GM_TC_03_INVALID_BLANK_COUNT,
    GM_TC_04_DUPLICATE_NUMBER,
    GM_TC_05_NO_VALID_MAGIC_SQUARE,
)
from .validators import (
    assert_error_contract,
    assert_reverse_fallback_combination,
    assert_small_first_combination,
    assert_success_result,
)

pytestmark = [pytest.mark.golden_master, pytest.mark.boundary]


def _auto_create_enabled() -> bool:
    return os.environ.get("GOLDEN_MASTER_AUTO_CREATE") == "1"


class TestGoldenMasterMagicSquareDocument:
    """Full-file approve: ``open(expected).read()`` vs captured document."""

    def test_golden_master_expected_file_matches_capture(
        self,
        golden_master_path: Path,
    ) -> None:
        """[GoldenMaster] Compare entire golden_master_expected.txt baseline."""
        actual = capture_all_scenarios()
        expected = (
            read_expected_file(golden_master_path)
            if golden_master_path.is_file()
            else ""
        )
        assert_golden_master_document(
            actual,
            golden_master_path,
            auto_create=_auto_create_enabled(),
        )
        if golden_master_path.is_file():
            assert expected == actual or _auto_create_enabled()


class TestGoldenMasterMagicSquareCases:
    """Per-scenario GM-TC approval tests with contract validation."""

    def test_gm_tc_01_normal_combination_success(
        self,
        golden_master_path: Path,
    ) -> None:
        """[GoldenMaster][GM-TC-01] Step A (small-first) success → int[6]."""
        scenario = GM_TC_01_NORMAL_SUCCESS
        result = capture_scenario(scenario)
        vector = assert_success_result(scenario.grid, result)
        assert_small_first_combination(scenario.grid, vector)
        assert_golden_section(
            scenario,
            capture_scenario_body(scenario),
            golden_master_path,
            auto_create=_auto_create_enabled(),
            full_document=capture_all_scenarios(),
        )

    def test_gm_tc_02_reverse_combination_success(
        self,
        golden_master_path: Path,
    ) -> None:
        """[GoldenMaster][GM-TC-02] Step A fails → reverse Step B success."""
        scenario = GM_TC_02_REVERSE_SUCCESS
        result = capture_scenario(scenario)
        vector = assert_success_result(scenario.grid, result)
        assert_reverse_fallback_combination(scenario.grid, vector)
        assert_golden_section(
            scenario,
            capture_scenario_body(scenario),
            golden_master_path,
            auto_create=_auto_create_enabled(),
            full_document=capture_all_scenarios(),
        )

    def test_gm_tc_03_invalid_blank_count(
        self,
        golden_master_path: Path,
    ) -> None:
        """[GoldenMaster][GM-TC-03] Error contract: INVALID_BLANK_COUNT."""
        scenario = GM_TC_03_INVALID_BLANK_COUNT
        result = capture_scenario(scenario)
        assert_error_contract(result, "INVALID_BLANK_COUNT")
        assert_golden_section(
            scenario,
            capture_scenario_body(scenario),
            golden_master_path,
            auto_create=_auto_create_enabled(),
            full_document=capture_all_scenarios(),
        )

    def test_gm_tc_04_duplicate_number(
        self,
        golden_master_path: Path,
    ) -> None:
        """[GoldenMaster][GM-TC-04] Error contract: DUPLICATE_NUMBER."""
        scenario = GM_TC_04_DUPLICATE_NUMBER
        result = capture_scenario(scenario)
        assert_error_contract(result, "DUPLICATE_NUMBER")
        assert_golden_section(
            scenario,
            capture_scenario_body(scenario),
            golden_master_path,
            auto_create=_auto_create_enabled(),
            full_document=capture_all_scenarios(),
        )

    def test_gm_tc_05_no_valid_magic_square(
        self,
        golden_master_path: Path,
    ) -> None:
        """[GoldenMaster][GM-TC-05] Error contract: NO_VALID_MAGIC_SQUARE."""
        scenario = GM_TC_05_NO_VALID_MAGIC_SQUARE
        result = capture_scenario(scenario)
        assert_error_contract(result, "NO_VALID_MAGIC_SQUARE")
        assert_golden_section(
            scenario,
            capture_scenario_body(scenario),
            golden_master_path,
            auto_create=_auto_create_enabled(),
            full_document=capture_all_scenarios(),
        )
