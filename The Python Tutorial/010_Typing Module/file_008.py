# Combine multiple type vars:

from typing import TypeVar

T = TypeVar("T")
U = TypeVar("U")


def pair(first: T, second: U) -> tuple[T, U]:
    return (first, second)


# Inferred as pair[str, int]
p: tuple[str, int] = pair("age", 30)
