from typing import TypeVar, Generic


T = TypeVar("T")

S = TypeVar("S", bound="str")


def identity(x: T) -> T:
    return x


class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get(self):
        return self.value


box1 = Box[int](5)

box2 = Box[str]("Hello")
