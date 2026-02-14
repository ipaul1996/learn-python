# Literal Types
# Restrict a variable or parameter to exact literal values
from typing import Literal


def set_mode(mode: Literal["r", "w", "a"]) -> None:
    # 'mode' must be exactly 'r', 'w', or 'a'
    print(f"Opening file in {mode} mode")


set_mode("r")
# set_mode('x') # Error


def set_status(code: Literal[200, 404, 500]) -> None:
    """Accept only HTTP status codes 200, 404, or 500."""
    print(f"Status set to {code}")


set_status(200)

# set_status(403) # Invalid (type checker error):



