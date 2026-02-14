# repr, str

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        """
        Official string representation of the object, primarily for developers.
        __repr__ should return a string that, when passed to eval(), recreates the object.
        If __str__ is not defined, __repr__ is used as a fallback by str() and print().
        """
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        """
        Informal string representation of the object, intended for end users.
        __str__ should return a readable, informal string representation of the object.
        It is used by print() and str().
        If __str__ is not defined, __repr__ is used instead.
        """
        return f"({self.x}, {self.y})"


p = Point(2, 3)

# print() uses __str__ if available, otherwise falls back to __repr__
print(p)  # Output: (2, 3)

# str() explicitly calls __str__
print(str(p))  # Output: (2, 3)

# repr() explicitly calls __repr__
print(repr(p))  # Output: Point(2, 3)

# Demonstrating eval with __repr__ output
p2 = eval(repr(p))
print(p2)  # Output: (2, 3)
print(type(p2))  # Output: <class '__main__.Point'>
