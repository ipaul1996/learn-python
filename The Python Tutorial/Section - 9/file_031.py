# Dataclasses
# Dataclasses are a feature in Python (introduced in Python 3.7)
# that make it easier to create classes for storing data without
# writing a lot of boilerplate code. By using the @dataclass decorator,
# Python automatically adds special methods like __init__, __repr__, and __eq__
# to your class.

# Key features / benefits of dataclasses:
# - Automatically generates __init__, __repr__, __eq__, and other methods.
# - Reduces boilerplate code for simple data containers.
# - Supports default values and type annotations.
# - Can be made immutable with frozen=True.
# - Supports ordering comparisons with order=True.
# - Type hints for fields.

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


p1 = Point(1, 2)
print(p1)  # Output: Point(x=1, y=2)


@dataclass(frozen=True, order=True)
class PointV2:
    x: float
    y: float


# Here, Point instances are immutable and support comparison via == and <.
