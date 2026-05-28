"""Entity-layer tests for User (DT-USER-*)."""

from __future__ import annotations

import pytest

from magicsquare.entity.exceptions import UserValidationError
from magicsquare.entity.user import User


def test_entity_user_create_valid() -> None:
    """DT-USER-01: Valid id and display_name produce a User."""
    # Arrange
    user_id = "player_01"
    display_name = "Magic Player"

    # Act
    user = User.create(user_id=user_id, display_name=display_name)

    # Assert
    assert user.user_id == user_id
    assert user.display_name == display_name


def test_entity_user_create_strips_display_name() -> None:
    """DT-USER-02: Leading and trailing spaces are stripped from display_name."""
    # Arrange
    raw_name = "  Padded Name  "

    # Act
    user = User.create(user_id="p1", display_name=raw_name)

    # Assert
    assert user.display_name == "Padded Name"


def test_entity_user_rejects_invalid_id_empty() -> None:
    """DT-USER-03: Empty user_id raises UserValidationError."""
    # Arrange / Act / Assert
    with pytest.raises(UserValidationError) as exc_info:
        User.create(user_id="", display_name="Alice")

    assert exc_info.value.code == "D_USER_INVALID_ID"


def test_entity_user_rejects_invalid_id_special_chars() -> None:
    """DT-USER-04: user_id with disallowed characters is rejected."""
    # Arrange / Act / Assert
    with pytest.raises(UserValidationError) as exc_info:
        User.create(user_id="bad id!", display_name="Bob")

    assert exc_info.value.code == "D_USER_INVALID_ID"


def test_entity_user_rejects_id_over_32_chars() -> None:
    """DT-USER-05: user_id longer than 32 characters is rejected."""
    # Arrange
    long_id = "a" * 33

    # Act / Assert
    with pytest.raises(UserValidationError) as exc_info:
        User.create(user_id=long_id, display_name="Carol")

    assert exc_info.value.code == "D_USER_INVALID_ID"


def test_entity_user_rejects_empty_display_name() -> None:
    """DT-USER-06: Blank display_name after strip is rejected."""
    # Arrange / Act / Assert
    with pytest.raises(UserValidationError) as exc_info:
        User.create(user_id="u1", display_name="   ")

    assert exc_info.value.code == "D_USER_EMPTY_DISPLAY_NAME"


def test_entity_user_rejects_display_name_too_long() -> None:
    """DT-USER-07: display_name over 64 characters is rejected."""
    # Arrange
    too_long = "x" * 65

    # Act / Assert
    with pytest.raises(UserValidationError) as exc_info:
        User.create(user_id="u2", display_name=too_long)

    assert exc_info.value.code == "D_USER_DISPLAY_NAME_TOO_LONG"


def test_entity_user_rename_returns_new_instance() -> None:
    """DT-USER-08: rename returns new User; original is unchanged."""
    # Arrange
    original = User.create(user_id="u3", display_name="Before")

    # Act
    renamed = original.rename("After")

    # Assert
    assert renamed.display_name == "After"
    assert renamed.user_id == "u3"
    assert original.display_name == "Before"


def test_entity_user_frozen_immutability() -> None:
    """DT-USER-09: User fields cannot be assigned after creation."""
    # Arrange
    user = User.create(user_id="u4", display_name="Frozen")

    # Act / Assert
    with pytest.raises(AttributeError):
        user.display_name = "Hacked"  # type: ignore[misc]
