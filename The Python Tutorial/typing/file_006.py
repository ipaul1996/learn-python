from typing import Generic, TypeVar

# Generic is a class from Python's typing module used to define generic classes.
# It allows you to create classes that can operate on different types, specified
# using TypeVar.

T = TypeVar("T")


class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value


# Here, Box can hold any type, and type safety is preserved.
# You can create Box[int], Box[str], etc.

# Usage:
int_box = Box[int](5)
str_box = Box[str]("abc")

reveal: int = int_box.get()  # type checker knows get() returns int
