# Object Creation
# When we write the following,
# obj = MyClass(arg1, arg2)

# 1. Allocate memory & create the bare instance by calling
#    inst = MyClass.__new__(MyClass, arg1, arg2)

# 2. Initialize that instance by calling
#    MyClass.__init__(inst, arg1, arg2)

# Finally, inst is returned to you.

# __new__
# is a special method in Python that controls how a new object is created before __init__ initializes it.
# Signature: def __new__(cls, *args, **kwargs) -> instance
# It receives the class (cls) and must return an instance (usually by calling super().__new__(cls) or object.__new__(cls)).

# If you don’t override it, __new__ comes from object:
"""
def __new__(cls, *args, **kwargs):
    # allocate raw memory for instance of cls
    return <new, empty instance of cls>
"""


# Custom __new__ looks like the following:
class MyClass:
    def __new__(cls, *args, **kwargs):
        # 1. allocate instance:
        inst = super().__new__(cls)
        # 2. (optional) tweak inst before init…
        return inst


# Use cases:
# - Control what instance is created (e.g., return a cached object or a subclass).
# - Customize creation of immutable objects (like int, str, or tuple), since their values can't be changed after creation.


class MyInt(int):
    def __new__(cls, value):
        # always return even numbers
        val = int(value)
        if val % 2:
            val -= 1
        return super().__new__(cls, val)


# demo
print(MyInt(7))  # → 6
print(MyInt(10))  # → 10
