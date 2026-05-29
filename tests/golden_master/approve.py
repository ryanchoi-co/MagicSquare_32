"""Approve-pattern helpers for Golden Master regression files."""

from __future__ import annotations

import difflib
import re
from pathlib import Path

from .dto import GoldenError, GoldenResult, GoldenSuccess
from .scenarios import GoldenScenario

DEFAULT_GOLDEN_PATH = Path(__file__).resolve().parents[1] / "golden_master_expected.txt"
_SECTION_SEPARATOR = "\n\n________________________________________\n\n"

_SECTION_RE = re.compile(
    r"^\[(?P<key>[a-z_0-9]+)\]\s*\n"
    r"Input:\s*\n"
    r"(?P<input>(?:\d+(?: \d+)*\n?)+)"
    r"(?P<tail>(?:Output:\n.+|Error:\n.+))",
    re.MULTILINE,
)


def read_expected_file(path: Path = DEFAULT_GOLDEN_PATH) -> str:
    """Read the full golden master baseline (``open(path).read()`` equivalent)."""
    return path.read_text(encoding="utf-8")


def write_golden_file(content: str, path: Path = DEFAULT_GOLDEN_PATH) -> None:
    """Write golden master baseline to disk."""
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = content if content.endswith("\n") else content + "\n"
    path.write_text(normalized, encoding="utf-8", newline="\n")


def read_golden_file(path: Path = DEFAULT_GOLDEN_PATH) -> dict[str, str]:
    """Parse golden file into scenario-key → body (Input + Output/Error)."""
    if not path.is_file():
        return {}
    return read_golden_file_from_document(read_expected_file(path))


def format_unified_diff(expected: str, actual: str, label: str) -> str:
    """Return unified diff with --- expected / +++ actual headers."""
    return "".join(
        difflib.unified_diff(
            expected.splitlines(keepends=True),
            actual.splitlines(keepends=True),
            fromfile="expected",
            tofile="actual",
            lineterm="",
        ),
    )


def compare_text(expected: str, actual: str, label: str) -> str | None:
    """Return diff text when *expected* and *actual* differ."""
    if expected == actual:
        return None
    header = f"--- expected ({label})\n+++ actual ({label})\n"
    return header + format_unified_diff(expected, actual, label)


def scenario_body(key: str, grid: list[list[int]], result: GoldenResult) -> str:
    """Build Input + Output/Error body without section header."""
    from .dto import format_grid_input

    return "\n".join(
        ("Input:", format_grid_input(grid), result.serialize()),
    )


def assert_golden_text(
    expected: str,
    actual: str,
    *,
    label: str,
    path: Path = DEFAULT_GOLDEN_PATH,
    auto_create: bool = False,
) -> None:
    """Compare full expected vs actual text; create baseline when missing."""
    if not path.is_file():
        if not auto_create:
            msg = (
                f"Golden master file missing: {path}. "
                "Run: python scripts/generate_golden_master.py --approve"
            )
            raise AssertionError(msg)
        write_golden_file(actual, path)
        return

    diff = compare_text(expected, actual, label)
    if diff:
        raise AssertionError(f"Golden master mismatch for {label}:\n{diff}")


def assert_golden_section(
    scenario: GoldenScenario,
    actual_body: str,
    path: Path = DEFAULT_GOLDEN_PATH,
    *,
    auto_create: bool = False,
    full_document: str | None = None,
) -> None:
    """Approve pattern for one scenario section."""
    if not path.is_file():
        if not auto_create:
            msg = (
                f"Golden master file missing: {path}. "
                "Run: python scripts/generate_golden_master.py --approve"
            )
            raise AssertionError(msg)
        if full_document is None:
            msg = "full_document required when auto_create=True"
            raise ValueError(msg)
        write_golden_file(full_document, path)
        return

    expected_sections = read_golden_file(path)
    expected_body = expected_sections.get(scenario.key)
    if expected_body is None:
        raise AssertionError(
            f"Missing expected section [{scenario.key}] in {path}",
        )
    diff = compare_text(expected_body, actual_body, scenario.test_id)
    if diff:
        raise AssertionError(
            f"[GoldenMaster][{scenario.test_id}] mismatch:\n{diff}",
        )


def assert_golden_master_document(
    actual_document: str,
    path: Path = DEFAULT_GOLDEN_PATH,
    *,
    auto_create: bool = False,
) -> None:
    """Approve pattern for the full golden master document."""
    if not path.is_file():
        if not auto_create:
            msg = (
                f"Golden master file missing: {path}. "
                "Run: python scripts/generate_golden_master.py --approve"
            )
            raise AssertionError(msg)
        write_golden_file(actual_document, path)
        return

    expected_document = read_expected_file(path)
    diff = compare_text(expected_document, actual_document, "golden_master_expected.txt")
    if diff:
        raise AssertionError(f"Golden master document mismatch:\n{diff}")


def read_golden_file_from_document(text: str) -> dict[str, str]:
    """Parse an in-memory golden document."""
    sections: dict[str, str] = {}
    for match in _SECTION_RE.finditer(text):
        key = match.group("key")
        block = (
            "Input:\n"
            f"{match.group('input').rstrip()}\n"
            f"{match.group('tail').strip()}"
        )
        sections[key] = block
    return sections


def parse_result_tail(tail: str) -> GoldenResult:
    """Parse Output/Error tail from a golden section (for unit tests)."""
    import ast

    if tail.startswith("Output:"):
        vector_text = tail.split("Output:", maxsplit=1)[1].strip()
        vector = ast.literal_eval(vector_text)
        if not isinstance(vector, list):
            msg = f"Expected list vector, got {type(vector)!r}"
            raise TypeError(msg)
        return GoldenSuccess(vector=vector)
    if tail.startswith("Error:"):
        code = tail.split("Error:", maxsplit=1)[1].strip()
        return GoldenError(code=code)
    msg = f"Unrecognized golden tail: {tail!r}"
    raise ValueError(msg)
