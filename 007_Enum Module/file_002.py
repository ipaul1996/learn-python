"""
Python Enum Enhancements: auto() and @unique decorator

The enum module provides two useful utilities for creating enumerations more efficiently
and safely:
1. auto() - Automatic value assignment
2. @unique - Ensures all values are distinct (no duplicates/aliases)
"""

from enum import Enum, auto, unique


# auto() generates sequential values automatically, starting from 1.

# Benefits:
# - No need to manually assign values
# - Avoids value conflicts when adding new members
# - Makes code cleaner when exact values don't matter
# - Automatically increments (1, 2, 3, ...)


class Status(Enum):
    """
    Using auto() to automatically assign values to enum members.
    auto() generates sequential integer values starting from 1.
    This is useful when you care about distinct values but not their specific numeric values.
    """

    PENDING = auto()  # Gets value 1
    RUNNING = auto()  # Gets value 2
    COMPLETED = auto()  # Gets value 3


# auto() generates values: 1, 2, 3, etc.
print([member.value for member in Status])  # Output: [1, 2, 3]
print(Status.PENDING.value)  # 1
print(Status.RUNNING.value)  # 2
print(Status.COMPLETED.value)  # 3


class Priority(Enum):
    """
    You can mix auto() with manually assigned values.
    auto() continues from the last assigned value.
    """

    LOW = 1
    MEDIUM = auto()  # Gets 2 (continues from LOW)
    HIGH = auto()  # Gets 3
    CRITICAL = 10  # Manually set to 10
    URGENT = auto()  # Gets 11 (continues from CRITICAL)


print([member.value for member in Priority])
# [1, 2, 3, 10, 11]


# The @unique decorator ensures all enum values are distinct.
# It prevents accidental creation of aliases (members with same value).

# Benefits:
# - Catches bugs at class definition time (not runtime)
# - Enforces strict uniqueness when aliases are not desired
# - Makes intent clear: "these values MUST be different"


@unique
class Direction(Enum):
    """
    Using the @unique class decorator to ensure all enum values are distinct.
    This prevents accidental duplicate values in the enumeration.
    If duplicate values are detected, a ValueError is raised during class creation.
    """

    NORTH = 1
    WEST = 2
    SOUTH = 3
    EAST = 4


# The @unique decorator ensures all values are distinct
# Trying to create duplicates would raise a ValueError:

try:

    @unique
    class InvalidDirection(Enum):
        NORTH = 1
        SOUTH = 2
        ALSO_NORTH = 1  # This would cause ValueError: duplicate values found

except ValueError as e:
    print(f"Error: {e}")
