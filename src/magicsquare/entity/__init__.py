"""Domain entities and value objects."""

from magicsquare.entity.exceptions import UserValidationError
from magicsquare.entity.user import User

__all__ = ["User", "UserValidationError"]
