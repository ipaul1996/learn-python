# Comparison Methods
# Instances cannot be ordered unless the class defines enough of the methods.

"""
__eq__(self, other)    # equality (==)
  - x == y calls x.__eq__(y).
  - If x.__eq__(y) returns NotImplemented, Python tries y.__eq__(x).
  - Default on object (the supermost class): Returns True if x is y (Identity Check).
  - Fallback: If both sides return NotImplemented, the '==' operator falls back to an
    identity check ('is'), returning False if they are not the same object.
  - Your implementation should return a boolean or NotImplemented (to try the reflected comparison).


__ne__(self, other)    # inequality (!=)
  - x != y calls x.__ne__(y).
  - Default on object: Delegates to __eq__ and inverts the result.
  - Fallback: If both sides return NotImplemented, the '!=' operator falls back to
    identity check ('is not'), returning True if they are not the same object.
  - If you only implement __eq__, Python will fall back to using not x==y for !=.


__lt__(self, other)    # less than (<)
  - x < y calls x.__lt__(y).
  - Reflection: If x.__lt__(y) returns NotImplemented, Python attempts y.__gt__(x).
  - Default: Raises TypeError if neither object implements the comparison.



__gt__(self, other)    # greater than (>)
  - x > y calls x.__gt__(y).
  - Reflection: If x.__gt__(y) returns NotImplemented, Python attempts y.__lt__(x).
  - Default: Raises TypeError.


__le__(self, other)    # less than or equal (<=)
  - x <= y calls x.__le__(y).
  - Reflection: If x.__le__(y) returns NotImplemented, Python attempts y.__ge__(x).
  - Pitfall: This is NOT automatically derived from 'not >' or '< or =='. You must implement it
    explicitly or use functools.total_ordering.
  - Default: Raises TypeError.

  
__ge__(self, other)    # greater than or equal (>=)
  - x >= y calls x.__ge__(y).
  - Reflection: If x.__ge__(y) returns NotImplemented, Python attempts y.__le__(x).
  - Pitfall: This is NOT automatically derived from 'not <' or '> or =='. You must implement it
    explicitly or use functools.total_ordering.
  - Default: Raises TypeError.

  
The Subclass Priority Rule:
  - When you write x < y, Python normally:
    1. Calls x.__lt__(y) first
    2. If that returns NotImplemented, tries the REFLECTED method: y.__gt__(x)
  - If 'other' is a subclass of 'self' (and not the same class), Python calls the
    REFLECTED method on 'other' before calling the method on 'self'.
  - Example: For x < y, if type(y) is a subclass of type(x), Python tries y.__gt__(x) first.
  - This allows subclasses to override comparison behavior defined in their base classes. This prevents 
    parent class logic from "winning" when a more specialized subclass has defined its own comparison behavior.


If you define __eq__ plus one of __lt__, __le__, __gt__, or __ge__, the decorator @functools.total_ordering will 
fill in the rest, so you get full ordering support without extra boilerplate.

"""


class Version:
    def __init__(self, major, minor):
        self.major, self.minor = major, minor

    def __eq__(self, other):
        # if not ... is a way to run code only when a condition is false
        if not isinstance(other, Version):
            return NotImplemented

        return (self.major, self.minor) == (other.major, other.minor)

    def __lt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor) < (other.major, other.minor)


v1 = Version(1, 2)
v2 = Version(1, 3)

print(v1 == v2)  # == calls __eq__ → works.
print(v1 < v2)   # < calls __lt__  → works.

try:
    print(v1 <= v2)  # type: ignore # <= isn’t defined, and Python won’t auto-derive it → TypeError.
except TypeError as e:
    print(
        "Error:", e
    )  # Error: '<=' not supported between instances of 'Version' and 'Version'


class Foo:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, Foo):
            return NotImplemented
        return self.value == other.value


f1 = Foo(4)

print(v1 == f1)
"""
NotImplemented:
It is a built-in singleton object in Python. (Its type: <class 'NotImplementedType'>)
It signals Python, I don’t know how to handle this operation with the given operand,
allowing Python to try the reflected operation or handle it appropriately.

How NotImplemented Works?
When we do a == b, the interpreter:
1. Calls a.__eq__(b).
2. If that method returns any value other than NotImplemented, that value is the result of the expression.
3. If a.__eq__(b) returns NotImplemented, Python then attempts the reflected operation by calling b.__eq__(a).
4. If b.__eq__(a) returns a value other than NotImplemented, that is the result.
5. If both methods return NotImplemented, Python falls back to a default behavior. For == and !=, this is a simple 
   identity check (a is b). For ordering operators (<, >, etc.), it raises a TypeError.
"""
