"""Shared fixtures for Golden Master approval tests."""

from __future__ import annotations

from pathlib import Path

import pytest

from .approve import DEFAULT_GOLDEN_PATH


@pytest.fixture
def golden_master_path() -> Path:
    """Path to the version-controlled golden master baseline."""
    return DEFAULT_GOLDEN_PATH
