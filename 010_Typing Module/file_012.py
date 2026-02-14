# Final
# In Python's typing system, Final allows you to indicate that a variable, attribute, or method
# should not be overridden or reassigned. This is intended for static type checkers,
# which will raise warnings if the Final contract is violated. Final has no effect at runtime.

from typing import Final

PI: Final[float] = 3.14159
MAX_RETRIES: Final[int] = 5

# PI = 3.15  # "PI" is declared as Final and cannot be reassigned


class Config:
    TIMEOUT: Final[int] = 30
    URL: Final = "https://api.example.com"


