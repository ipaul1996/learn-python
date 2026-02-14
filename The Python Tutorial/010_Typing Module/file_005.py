from typing import TypeVar

# TypeVar is a function from Python's typing module used to define generic types
# for type hints. It allows you to write functions, classes, or methods that can
# operate on multiple types while preserving type safety.

T = TypeVar("T")  # unconstrained
# T is a type variable that can represent any type. When you use it in a function
# like identity, the type is inferred based on the argument passed.


S = TypeVar("S", bound=str)  # must be subtype of str
# S can only be a str or a subclass of str.


def identity(x: T) -> T:
    return x


a: int = identity(5)  # type of T is inferred as int
b: str = identity("hello")  # type of T is inferred as str
