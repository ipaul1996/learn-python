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
# - Supports slots=True for memory efficiency
# - Type hints for fields.

from dataclasses import dataclass, field

# Before @dataclass
class PointV0:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        if not isinstance(other, PointV0):
            return False
        return self.x == other.x and self.y == other.y


@dataclass
class PointV1:
    x: int
    y: int


p1 = PointV1(1, 2)
print(p1)  # Output: Point(x=1, y=2)


@dataclass(frozen=True, order=True)
class PointV2:
    x: float
    y: float


# Here, Point instances are immutable and support comparison via == and <.


@dataclass(frozen=True)  # Makes the object immutable
class InventoryItem:
    name: str
    unit_price: float
    quantity: int = 0  # A default value
    tags: list[str] = field(default_factory=list)  # For mutable defaults


item = InventoryItem("Banana", 0.79, 100)
# item.quantity = 99 # This would raise a FrozenInstanceError!

print(item)
# InventoryItem(name='Banana', unit_price=0.79, quantity=100, tags=[])
