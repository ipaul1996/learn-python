# In Python’s typing system, TypeVar can be invariant, covariant, or contravariant

# Invariant (default):
# The type variable can only be exactly the specified type.
# TypeVar("T") is invariant.
# Box[int] is not compatible with Box[float] or vice versa.
# A Box[Apple] is not a Box[Fruit], because you could insert an
# orange into a Box[Fruit], which wouldn’t belong in a pure apple box.

from typing import Generic, TypeVar

T = TypeVar("T")  # invariant by default


class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value


int_box = Box[int](5)
float_box = Box[float](3.14)


# int_box and float_box are not interchangeable:
def process_int_box(box: Box[int]):
    print(box.value)


process_int_box(int_box)  # OK
# process_int_box(float_box)  # Type checker error!
