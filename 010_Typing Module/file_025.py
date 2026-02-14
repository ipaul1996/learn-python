# TypedDict, NotRequired, Required
from typing import TypedDict, NotRequired, Required

# A TypedDict type represents dictionary objects with a specific set of string keys, and with specific
# value types for each valid key. Each string key can be either required (it must be present)
# or non-required (it doesn’t need to exist). It allows static type checkers to verify the structure
# of dict-like objects. At runtime, it's a normal dict.
# There are two ways of defining TypedDict types. The first uses a class-based syntax.
# The second is an alternative assignment-based syntax


# 1. Basic TypedDict definition (all required keys):
class User(TypedDict):
    id: int
    name: str


# Note: This is not a regular Python class, but a type annotation for dicts.
# The 'id' and 'name' specify required dictionary keys and their types.
# At runtime, 'User' is a subclass of dict[So, we can create instances like User(id=5, name="Eve")], used only for type checking.


# Usage:
user1: User = {"id": 1, "name": "Alice"}
# Missing or wrong-type keys will be flagged by MyPy/Pyright:
# user_bad: User = {"id": "1", "name": "Bob"}  # id must be int
# user_missing: User = {"id": 2}                    # missing 'name'


# 2. Making Keys Optional with NotRequired:
class Product(TypedDict):
    sku: str
    name: str
    price: float
    description: NotRequired[str]  # description may be omitted


prod1: Product = {"sku": "A100", "name": "Widget", "price": 9.99}
prod2: Product = {
    "sku": "B200",
    "name": "Gadget",
    "price": 19.99,
    "description": "New!",
}

# 3. Controlling required vs. optional with 'total' and 'Required'
#    - total=True (default): all keys listed are required unless marked NotRequired
#    - total=False: all keys are optional unless marked Required

# Base defines x and y as optional (total=False)
Base = TypedDict("Base", {"x": int, "y": int}, total=False)


# IMPORTANT: You CANNOT change requirement status of inherited keys
# Option 1: Define independently
class Point(TypedDict, total=True):
    x: int
    y: int
    z: int


# Option 2: Using Required
class PointV2(TypedDict, total=False):
    x: Required[int]
    y: Required[int]
    z: Required[int]


pt1: Point = {"x": 2, "y": 3, "z": 5}
# pt2: Point = {"z": 5} # Invalid


# 4. Inheritance and merging:
class Employee(User):
    role: str


ej: Employee = {"id": 10, "name": "Dana", "role": "Engineer"}


# 5. Type operations:
# TypedDict instances behave like normal dicts at runtime:
d = User(id=5, name="Eve")
print(d.keys(), d.values())

# They do NOT support item assignment type enforcement at runtime,
# only static type checking helps you.
