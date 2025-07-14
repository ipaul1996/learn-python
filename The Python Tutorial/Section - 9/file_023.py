# Comparison Methods
# Instances … cannot be ordered … unless the class defines enough of the methods
"""
__eq__(self, other)    # equality (==)
  - x==y calls x.__eq__(y)
  - Default on object: returns True if x is y, else NotImplemented
  - Your implementation should return a boolean (or NotImplemented if the types don’t match), allowing Python to try the reflected comparison or give False.


__ne__(self, other)    # inequality (!=)
  - x!=y calls x.__ne__(y)
  - Default on object: the inverse of __eq__ (i.e. returns not x.__eq__(y) or NotImplemented).
  - If you only implement __eq__, Python will fall back to using not x==y for !=.


__lt__(self, other)    # less than (<)
  - x<y calls x.__lt__(y)
  - Should return a boolean or NotImplemented. If NotImplemented, Python may try y.__gt__(x).
  - Without this method (or its counterpart), < raises TypeError.


__le__(self, other)    # less than or equal (<=)
  - x<=y calls x.__le__(y)
  - If missing, Python does not auto-derive it from __lt__ and __eq__ unless you use functools.total_ordering.
  - If __ge__ is there it falls back to it.


__gt__(self, other)    # greater than (>)
  - x>y calls x.__gt__(y)
  - Mirrors __lt__ on the other operand if it returns NotImplemented.


__ge__(self, other)    # greater than or equal (>=)
  - x>=y calls
  - Like __le__, not auto-derived without total_ordering.
  - Of __le__ is there it falls back to __le__


For any of these methods, returning NotImplemented (instead of raising) when other isn’t a compatible type lets Python:
- Try the reflected operation on other (if it’s a subclass).
- Finally raise TypeError if nothing supports the comparison.


If you define __eq__ plus one of __lt__, __le__, __gt__, or __ge__, the decorator @functools.total_ordering will fill in the
rest, so you get full ordering support without extra boilerplate
"""


class Version:
    def __init__(self, major, minor):
        self.major, self.minor = major, minor

    def __eq__(self, other):
        # if not ... is a way to run code only when a condition is false
        if not isinstance(other, Version):
            return NotImplemented
            # It is a special built-in constant in Python. (Its type: <class 'NotImplementedType'>)
            # It tells Python that the comparison is not implemented for the given type,
            # allowing Python to try the reflected operation or handle it appropriately.
        return (self.major, self.minor) == (other.major, other.minor)

    def __lt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor) < (other.major, other.minor)


v1 = Version(1, 2)
v2 = Version(1, 3)

print(v1 == v2)  # == calls __eq__ → works.
print(v1 < v2)  # < calls __lt__ → works.

try:
    print(v1 <= v2)  # <= isn’t defined, and Python won’t auto-derive it → TypeError.
except TypeError as e:
    print(
        "Error:", e
    )  # Error: '<=' not supported between instances of 'Version' and 'Version'
