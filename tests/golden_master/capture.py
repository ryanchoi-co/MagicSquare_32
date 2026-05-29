"""Capture actual solver output for Golden Master scenarios."""

from __future__ import annotations

from .approve import scenario_body
from .dto import GoldenResult, serialize_scenario_block
from .reference import capture_reference
from .scenarios import ALL_SCENARIOS, GoldenScenario


def capture_scenario(scenario: GoldenScenario) -> GoldenResult:
    """Capture API result DTO for one scenario."""
    return capture_reference(scenario.grid)


def capture_scenario_section(scenario: GoldenScenario) -> str:
    """Serialize one scenario block including ``[key]`` header."""
    result = capture_scenario(scenario)
    return serialize_scenario_block(scenario.key, scenario.grid, result)


def capture_scenario_body(scenario: GoldenScenario) -> str:
    """Serialize Input + Output/Error body for file comparison."""
    result = capture_scenario(scenario)
    return scenario_body(scenario.key, scenario.grid, result)


def capture_all_scenarios() -> str:
    """Serialize every catalog scenario into one golden master document."""
    blocks = [
        serialize_scenario_block(scenario.key, scenario.grid, capture_scenario(scenario))
        for scenario in ALL_SCENARIOS
    ]
    return "\n\n________________________________________\n\n".join(blocks) + "\n"
