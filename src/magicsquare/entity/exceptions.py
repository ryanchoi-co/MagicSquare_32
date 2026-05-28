"""Domain-level exceptions for entity validation."""


class UserValidationError(ValueError):
    """Raised when User identity or display fields violate domain rules."""

    def __init__(self, code: str, message: str) -> None:
        """Initialize with a stable error code and human-readable message.

        Args:
            code: Machine-readable error identifier (e.g. D_USER_INVALID_ID).
            message: Description of the validation failure.
        """
        super().__init__(message)
        self.code = code
        self.message = message
