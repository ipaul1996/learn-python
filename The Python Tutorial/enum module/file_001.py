# An enumeration (Enum) is a set of symbolic names (members) bound to unique,
# constant values. Enums provide meaningful names for constants, improving
# code readability, maintainability, and type safety compared to using plain
# constants (e.g., integers or strings).

from enum import Enum


class Color(Enum):
    """
    A simple enumeration representing colors with associated integer values.
    Each member is a unique, constant value that cannot be changed during runtime.
    """

    RED = 1
    GREEN = 2
    BLUE = 3


# Different ways to access enum members:
print(Color(1))  # Color.RED (by value)
print(Color.RED)  # Color.RED (by attribute)
print(Color["RED"])  # Color.RED (by name)


# Accessing member properties:
print(Color.RED.name)  # RED (the symbolic name as string)
print(Color.RED.value)  # 1 (the underlying constant value)


# Iterating through all enum members:
for color in Color:
    print(color)
"""
Output:
Color.RED
Color.GREEN
Color.BLUE
"""


# Key Concepts Explained:

# Color.RED → The actual enum member object (a singleton instance of the Color class)
# RED → The symbolic name (accessible via .name attribute)
# 1 → The concrete value (accessible via .value attribute)


# Additional Enum Properties and Methods:
print(Color)  # <enum 'Color'> (the enum class itself)
print(list(Color))  # [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>] (all members)
print(Color.RED in Color)  # True (membership test)

# The __members__ attribute provides a mapping of names to members:
print(Color.__members__)
# Output: {'RED': <Color.RED: 1>, 'GREEN': <Color.GREEN: 2>, 'BLUE': <Color.BLUE: 3>}

# Checking if a name exists in the enum:
print("RED" in Color.__members__)  # True


# Important Enum Characteristics:

# 1. Enums ensure type safety - Color.RED is not equal to the integer 1
print(Color.RED == 1)  # False

# 2. Enum members are singletons - same member is always the same object
print(Color.RED is Color(1))  # True
