# An enumeration (Enum) is a set of symbolic names (members) bound to unique, 
# constant values. Enums improve readability, maintainability, and type-safety 
# compared to plain constants (e.g., integers or strings).


from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color(1))  # Color.RED
print(Color.RED)  # Color.RED
print(Color["RED"])  # Color.RED

print(Color.RED.name)  # RED
print(Color.RED.value)  # 1

for color in Color:
    print(color)

"""
Color.RED
Color.GREEN
Color.BLUE
"""

print(Color) # <enum 'Color'>
print(list(Color)) # [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]
print(Color.RED in Color)  # True

print(Color.__members__) # {'RED': <Color.RED: 1>, 'GREEN': <Color.GREEN: 2>, 'BLUE': <Color.BLUE: 3>}
print("RED" in Color.__members__)  # True
