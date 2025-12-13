"""
Python Enum Enhancements: auto() and @unique decorator

The enum module provides two useful utilities for creating enumerations more efficiently
and safely: auto() for automatic value assignment and @unique for ensuring value uniqueness.
"""

from enum import Enum, auto, unique


class Status(Enum):
    """
    Using auto() to automatically assign values to enum members.
    auto() generates sequential integer values starting from 1.
    This is useful when you care about distinct values but not their specific numeric values.
    """

    PENDING = auto()
    RUNNING = auto()
    COMPLETED = auto()


# auto() generates values: 1, 2, 3, etc.
print([member.value for member in Status])  # Output: [1, 2, 3]


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
