# Enum

# An enumeration (Enum) is a set of symbolic names (members) bound to unique, constant values.

# Why use Enums?
# - Readability: Use meaningful names (Color.RED) instead of magic numbers (1)
# - Type Safety: Color.RED != 1 (prevents accidental comparisons with raw values)
# - Maintainability: Change the value in one place, all references update automatically
# - IDE Support: Enables auto-completion and helps catch typos at development time
# - Documentation: Self-documenting code - intent is clear from the name

# Key Characteristics:
# - Members are singletons: Color.RED is always the same object in memory
# - Members are immutable: Cannot change Color.RED's value after definition
# - Each member has two attributes: .name (string) and .value (any type)
# - Enums are iterable and maintain definition order (Python 3.6+)
# - Members can have any hashable value: int, str, tuple, etc.


from enum import Enum


class Color(Enum):
    """
    A simple enumeration representing colors with associated integer values.
    Each member is a unique, constant value that cannot be changed during runtime.
    Members are singletons - Color.RED is always the exact same object.
    """

    RED = 1
    GREEN = 2
    BLUE = 3


print(Color)  # <enum 'Color'> (the enum class object)
print(type(Color))  # <class 'enum.EnumType'> (metaclass that creates enums)


# Three ways to access enum members:
print(Color(1))  # Color.RED (by value lookup - searches for member with value 1)
print(Color.RED)  # Color.RED (by attribute - most common, direct access)
print(Color["RED"])  # Color.RED (by name lookup - useful for string-based access)

# The type of an enum member is the enum class itself
print(type(Color.RED))  # <enum 'Color'> (Color.RED is an instance of Color enum)


member = Color.RED

# Member representation and attributes
print(f"Representation: {member}")  # Color.RED
print(f"String conversion: {str(member)}")  # Color.RED
print(f"Symbolic Name: {member.name}")  # 'RED' (string, useful for serialization)
print(f"Actual Value: {member.value}")  # 1 (the constant value assigned)


# Enums are iterable. Order is guaranteed by definition order.
for color in Color:
    print(color)
"""
Output:
Color.RED
Color.GREEN
Color.BLUE
"""

# Membership testing
print(Color.RED in Color)  # True (Color.RED is a member of Color enum)
print(1 in Color)  # False (raw value 1 is not a member, only Color.RED is)

# Type safety - enum members are NOT equal to their values
print(Color.RED == 1)  # False (prevents accidental comparison with raw integers)
print(Color.RED.value == 1)  # True (if you need to compare the value explicitly)

# Identity comparison - members are singletons
print(Color.RED is Color(1))  # True (same object in memory)
print(Color.RED is Color.RED)  # True (always the same singleton)
print(id(Color.RED) == id(Color(1)))  # True (same memory address)
