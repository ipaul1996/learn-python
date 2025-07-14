from typing import Optional, Any

# Variable Annotation
age: int = 30
names: list[str] = ["Alice", "Bob"]
config: dict[str, int] = {"retries": 3}
coords: list[tuple[int, int]] = [(0, 2), (3, 5)]
name: str  # uninitialized, defaults to None at runtime
point: tuple[float, float] = (0.0, 0.0)
primes: set[int] = {2, 3, 5}

# Any: disables all checking for that variable.
data: Any = "Could be anything"
data = 42
data = [1, 2, 3]


# Function Annotations
def greet(name: str) -> str:
    return "Hello " + name


# Function Returning Multiple Possible Types
def parse_id(val: str) -> int | None:
    try:
        return int(val)
    except ValueError:
        return None


# Alternative,
def parse_id_v2(val: str) -> Optional[int]:
    try:
        return int(val)
    except ValueError:
        return None


# Optional[int]: shorthand for X | None.
