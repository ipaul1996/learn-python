# Dataclasses

# Dataclasses, introduced in Python 3.7, are a powerful feature that
# simplifies the creation of classes intended primarily for storing data.
# By using the @dataclass decorator, you can avoid writing repetitive
# boilerplate code, as Python will automatically generate special methods
# like __init__, __repr__, __eq__, and others based on the class's type-annotated attributes.

# Key features / benefits of dataclasses:
# - Reduces Boilerplate: Automatically generates essential dunder methods:
#   - __init__: To initialize the object.
#   - __repr__: For a developer-friendly string representation.
#   - __eq__: For value-based equality comparison (instance_a == instance_b).
# - Type-Driven: Uses type hints to define fields, promoting clearer and more robust code.
# - Immutable Instances: The decorator argument `frozen=True` makes instances
#   read-only, raising an error if you try to modify a field after creation.
# - Ordering: The argument `order=True` automatically generates comparison methods
#   (__lt__, __le__, __gt__, __ge__), allowing instances to be sorted.
# - Memory Efficiency: For Python 3.10+, `slots=True` can be used to generate a
#   __slots__ attribute, resulting in faster attribute access and lower memory usage.
# - Advanced Field Control: The `field()` function allows for fine-grained
#   control over each attribute, such as providing mutable default values
#   using `default_factory`.

from dataclasses import dataclass, field

# --------------------------------------------------------------------------


# Before @dataclass
# A standard class requires writing the initializer, representation,
# and equality methods manually.
class PointV0:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"PointV0(x={self.x}, y={self.y})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, PointV0):
            return False
        return self.x == other.x and self.y == other.y


p0_1 = PointV0(1.5, 2.0)
p0_2 = PointV0(1.5, 2.0)
print(f"Before: {p0_1}")
print(f"Equality check: {p0_1 == p0_2}")  # True, because we wrote __eq__

# --------------------------------------------------------------------------


# With @dataclass
# The decorator handles all the boilerplate code for you.
@dataclass
class PointV1:
    x: float
    y: float


p1_1 = PointV1(1.5, 2.0)
p1_2 = PointV1(1.5, 2.0)
print(f"\nAfter: {p1_1}")  # __repr__ is auto-generated
print(f"Equality check: {p1_1 == p1_2}")  # __eq__ is auto-generated

# --------------------------------------------------------------------------


# Dataclass with Ordering
# By setting order=True, dataclasses can be sorted or compared.
# The comparison is done field by field, from top to bottom.
@dataclass(order=True)
class Person:
    name: str
    age: int


p_a = Person("Alice", 30)
p_b = Person("Bob", 25)

print(
    f"\nOrdering: {p_b < p_a}"
)  # True, because 25 < 30 (compares `age` as `name` is equal alphabetically)

# --------------------------------------------------------------------------

# Immutable Dataclass with Mutable Default
# frozen=True prevents modification after an object is created.
# Use field(default_factory=...) for mutable defaults like lists or dicts
# to ensure each instance gets its own copy.
@dataclass(frozen=True)
class InventoryItem:
    name: str
    unit_price: float
    quantity: int = 0  # A simple default value
    tags: list[str] = field(default_factory=list)  # Correct way for mutable defaults


item = InventoryItem("Banana", 0.79, 100, tags=["fruit", "yellow"])
# item.quantity = 99  # This would raise a dataclasses.FrozenInstanceError!

# Even though the class is frozen, you can still modify the mutable `tags` list
item.tags.append("grocery")

print(f"\nImmutable item: {item}")
# InventoryItem(name='Banana', unit_price=0.79, quantity=100, tags=['fruit', 'yellow', 'grocery'])
