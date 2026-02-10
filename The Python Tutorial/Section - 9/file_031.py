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
# - Fields without defaults must come before fields with defaults.
# - Never use mutable objects as defaults directly, use field(default_factory=...) instead.
# - Memory Efficiency: For Python 3.10+, `slots=True` can be used to generate a
#   __slots__ attribute, resulting in faster attribute access and lower memory usage.
# - Advanced Field Control: The `field()` function allows for fine-grained
#   control over each attribute, such as providing mutable default values
#   using `default_factory`.

# How It Works
# - The @dataclass decorator inspects the class's __annotations__ dictionary.
# - It finds all attributes with type hints.
# - It generates methods and injects them into the class.

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


# ---------------------------------------------------------------
"""
field() Parameters:
- default - Default value for the field
- default_factory - Function that returns default value (for mutable types)
- init - Include in __init__? (default: True)
- repr - Include in __repr__? (default: True)
- compare - Include in __eq__ and ordering? (default: True)
- hash - Include in __hash__? (default: None uses compare value)
- metadata - Dictionary for storing arbitrary metadata


Dataclass Decorator Parameters:
@dataclass(
    init=True,        # Generate __init__?
    repr=True,        # Generate __repr__?
    eq=True,          # Generate __eq__?
    order=False,      # Generate __lt__, __le__, __gt__, __ge__?
    unsafe_hash=False,# Generate __hash__?
    frozen=False      # Make instances immutable?
)
class Example:
    value: int

    

We must view the @dataclass decorator not as a runtime enforcer, but as a compile-time code generator.
When we define a dataclass, the decorator scans our class for variable annotations. It then generates 
methods like __init__, __repr__, and __eq__ and attaches them to our class. Crucially, the generated __init__ 
method performs raw assignment. It does not inspect the value we pass in, nor does it look at the type hint 
to decide if a cast is necessary. It simply takes the object reference we provide and binds it to the instance 
attribute. Thus no runtime data validation or data conversion is possible. For that we need pydantic v2.

"""
