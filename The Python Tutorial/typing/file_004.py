# Literal Types
# Restrict a variable or parameter to exact literal values
from typing import Literal


def set_mode(mode: Literal["r", "w", "a"]) -> None:
    # 'mode' must be exactly 'r', 'w', or 'a'
    print(f"Opening file in {mode} mode")

set_mode('r')
# set_mode('x') # Error
