# Multiple Inheritance and __slots__:
# No Multiple Inheritance of Slots: Mixing two slot-only classes without compatible slots
# can lead to conflicts.
# When you define a class with __slots__, you’re asking Python to lay out each instance
# with exactly those attributes (and no __dict__). If you inherit from two such classes
# that both use __slots__, Python must create a combined memory layout. But if those layouts
# conflict, you get an error.
class A:
    __slots__ = ("x",)  # A instances have exactly one slot: 'x'


class B:
    __slots__ = ("y",)  # B instances have exactly one slot: 'y'


# Attempt multiple inheritance of two slot-only classes:
# class C(A, B): pass  # TypeError: multiple bases have instance lay-out conflict


# Alternative: Avoid using __slots__ in one of the base classes to prevent layout conflicts.
class D:
    pass  # No __slots__, so instances have a __dict__


class E(A, D):
    __slots__ = ("y",)  # Only one parent (A) uses __slots__

    def __init__(self, x, y):
        self.x = x
        self.y = y


# Usage:
e = E(10, 20)
print(e.x, e.y)
