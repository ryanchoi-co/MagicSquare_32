"""User domain entity for Magic Square practice sessions."""

from __future__ import annotations

import re
from dataclasses import dataclass

from magicsquare.entity.exceptions import UserValidationError

_USER_ID_PATTERN = re.compile(r"^[a-zA-Z0-9_-]{1,32}$")
_MIN_DISPLAY_NAME_LEN = 1
_MAX_DISPLAY_NAME_LEN = 64


@dataclass(frozen=True, slots=True)
class User:
    """Identity of a player who may persist grids via the data layer.

    Aligns with repository id rules in Report/02 (1–32 alphanumeric, underscore,
    hyphen). Immutable: use ``rename`` to obtain a new instance.

    Attributes:
        user_id: Stable external identifier for save/load operations.
        display_name: Human-readable label shown at the boundary layer.
    """

    user_id: str
    display_name: str

    def __post_init__(self) -> None:
        """Validate invariants after dataclass field assignment."""
        self._validate_user_id(self.user_id)
        self._validate_display_name(self.display_name)

    @classmethod
    def create(cls, user_id: str, display_name: str) -> User:
        """Factory that builds a validated User.

        Args:
            user_id: Repository-compatible identifier.
            display_name: Non-empty display name (leading/trailing space stripped).

        Returns:
            A validated User instance.

        Raises:
            UserValidationError: If user_id or display_name violates domain rules.
        """
        return cls(user_id=user_id, display_name=display_name.strip())

    def rename(self, new_display_name: str) -> User:
        """Return a new User with an updated display name.

        Args:
            new_display_name: Replacement label; must satisfy display name rules.

        Returns:
            New User instance sharing the same user_id.

        Raises:
            UserValidationError: If new_display_name is invalid.
        """
        return User.create(user_id=self.user_id, display_name=new_display_name)

    @staticmethod
    def _validate_user_id(user_id: str) -> None:
        """Check user_id against repository id contract.

        Args:
            user_id: Candidate identifier.

        Raises:
            UserValidationError: When the id is empty or does not match the pattern.
        """
        if not user_id or not _USER_ID_PATTERN.fullmatch(user_id):
            raise UserValidationError(
                "D_USER_INVALID_ID",
                "user_id must match ^[a-zA-Z0-9_-]{1,32}$",
            )

    @staticmethod
    def _validate_display_name(display_name: str) -> None:
        """Check display_name length after strip.

        Args:
            display_name: Already-stripped display name.

        Raises:
            UserValidationError: When empty or too long.
        """
        if len(display_name) < _MIN_DISPLAY_NAME_LEN:
            raise UserValidationError(
                "D_USER_EMPTY_DISPLAY_NAME",
                "display_name must not be empty",
            )
        if len(display_name) > _MAX_DISPLAY_NAME_LEN:
            raise UserValidationError(
                "D_USER_DISPLAY_NAME_TOO_LONG",
                f"display_name must be at most {_MAX_DISPLAY_NAME_LEN} characters",
            )
