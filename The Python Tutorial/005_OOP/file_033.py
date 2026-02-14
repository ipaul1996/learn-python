# __slots__
# By default, each class in Python has a __dict__ attribute for every instance,
# which stores instance attributes dynamically. This allows you to add new attributes
# to objects at runtime, but it also uses more memory.
# When you define __slots__ (a class level attribute) in a class, you tell Python to only allocate space for a
# fixed set of attributes, removing the per-instance __dict__ and saving memory.


class Point:
    __slots__ = ("x", "y")  # Only allow 'x' and 'y' attributes

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(1, 2)

p.x = 10  # OK
print(p.x)

p.y = 20  # OK
print(p.y)

# p.z = 30 # AttributeError: 'Point' object has no attribute 'z' and no __dict__ for setting new attributes


# Subclasses without their own __slots__ get a __dict__ as usual.
# If a subclass defines __slots__, its slots are appended to those of its base classes.
class ColoredPointWithSlots(Point):
    __slots__ = (
        "color",
    )  # The comma makes this a tuple; without it, it's just a string

    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.color = color  # Allowed because 'color' is in __slots__


cp = ColoredPointWithSlots(3, 4, "blue")
print(cp.x, cp.y, cp.color)  # 3 4 blue

# cp.z = 5 # AttributeError: 'ColoredPointWithSlots' object has no attribute 'z' and no __dict__ for setting new attributes
