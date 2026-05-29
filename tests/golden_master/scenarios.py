"""Golden Master scenario catalog — GM-TC-01~05 input grids."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GoldenScenario:
    """One approval scenario: test ID, stable key, and 4×4 input grid."""

    test_id: str
    key: str
    grid: list[list[int]]


GM_TC_01_NORMAL_SUCCESS = GoldenScenario(
    test_id="GM-TC-01",
    key="normal_success",
    grid=[
        [16, 0, 2, 0],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ],
)

GM_TC_02_REVERSE_SUCCESS = GoldenScenario(
    test_id="GM-TC-02",
    key="reverse_success",
    grid=[
        [16, 2, 3, 13],
        [5, 11, 10, 8],
        [9, 7, 0, 12],
        [4, 14, 15, 0],
    ],
)

GM_TC_03_INVALID_BLANK_COUNT = GoldenScenario(
    test_id="GM-TC-03",
    key="invalid_blank_count",
    grid=[
        [1, 2, 3, 4],
        [5, 0, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ],
)

GM_TC_04_DUPLICATE_NUMBER = GoldenScenario(
    test_id="GM-TC-04",
    key="duplicate_number",
    grid=[
        [16, 2, 3, 13],
        [5, 11, 10, 8],
        [9, 7, 5, 12],
        [4, 14, 0, 0],
    ],
)

GM_TC_05_NO_VALID_MAGIC_SQUARE = GoldenScenario(
    test_id="GM-TC-05",
    key="no_valid_magic_square",
    grid=[
        [16, 2, 3, 13],
        [5, 11, 10, 8],
        [9, 7, 0, 12],
        [4, 14, 0, 15],
    ],
)

ALL_SCENARIOS: tuple[GoldenScenario, ...] = (
    GM_TC_01_NORMAL_SUCCESS,
    GM_TC_02_REVERSE_SUCCESS,
    GM_TC_03_INVALID_BLANK_COUNT,
    GM_TC_04_DUPLICATE_NUMBER,
    GM_TC_05_NO_VALID_MAGIC_SQUARE,
)

SCENARIO_BY_TEST_ID: dict[str, GoldenScenario] = {
    scenario.test_id: scenario for scenario in ALL_SCENARIOS
}

SCENARIO_BY_KEY: dict[str, GoldenScenario] = {scenario.key: scenario for scenario in ALL_SCENARIOS}
