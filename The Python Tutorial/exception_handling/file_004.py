# A custom exception in Python is a user-defined error type that you create
# by subclassing the built-in Exception class (or one of its subclasses).
# Custom exceptions help you signal specific error conditions in your code,
# making error handling clearer and more meaningful.
# Best Practices:
# - Name classes with Error suffix.
# - Inherit from Exception or a more specific built-in subclass.
# - Keep constructors simple—store only what handlers need.


class NegativeNumberError(Exception):
    """Raised when a negative number is encountered where it's not allowed."""

    pass


def square_root(x):
    if x < 0:
        raise NegativeNumberError("Cannot take square root of a negative number")
    return x**0.5


try:
    print(square_root(-9))
except NegativeNumberError as e:
    print("Custom exception caught:", e)

# ************************************************************


class AppError(Exception):
    """Base for all application-specific errors."""


class DatabaseError(AppError):
    pass


class NetworkError(AppError):
    pass


# Catch all app errors via except AppError:.
# Or handle specific subtypes (DatabaseError) separately.

# ************************************************************


class ConfigError(Exception):
    def __init__(self, path: str, msg: str):
        # constructor receiving two pieces of data:
        # path: where the error occurred (e.g. file name).
        # msg: what went wrong (e.g. "invalid JSON").

        super().__init__(
            f"{msg} (in {path})"
        )  # Calls the base Exception’s constructor with a single string argument.
        self.path = path
        self.msg = msg


class ValidationError(Exception):
    def __init__(self, field: str, msg: str):
        # field: the name of the field that failed validation
        # msg: description of what went wrong
        super().__init__(f"Validation error in '{field}': {msg}")
        self.field = field
        self.msg = msg
