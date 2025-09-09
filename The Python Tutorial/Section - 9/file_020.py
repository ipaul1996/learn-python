# Object Creation Process
#
# When you call a class to create an instance:
#     obj = MyClass(arg1, arg2)
#
# Python executes the following two-step process:
#
# 1. Construction via `__new__`:
#    The __new__ method, the actual constructor, is called first. It's a static method
#    that receives the class (cls) as its first argument. Its primary job is to
#    allocate memory and return a new, uninitialized instance of that class.
#        inst = MyClass.__new__(MyClass, arg1, arg2)
#
# 2. Initialization via `__init__`:
#    If __new__ successfully returns an instance of the class, that new instance is
#    then passed as the first argument (self) to the __init__ method. This method,
#    the initializer, sets the initial state of the object. It does not return anything.
#        inst.__init__(arg1, arg2)
#
# The variable `obj` is then assigned a reference to the newly constructed and initialized instance.

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


# Use cases for overriding __new__:
# 1. To Control the Creation Process (e.g., Singleton Pattern)
#    You can return a pre-existing instance instead of a new one, or even an
#    instance of a different class. This is used to implement design patterns
#    like Singletons, where only one instance of a class should ever exist.


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating the Logger instance")
            cls._instance = super().__new__(cls)
        return cls._instance


# 2. To Customize the Creation of Immutable Types (e.g., int, str, tuple)
#    Since these objects cannot be changed after creation (`__init__`), any
#    modifications to their underlying value must be done in `__new__` before
#    the object is finalized.


# Example: An int subclass that only stores even numbers.
class EvenInt(int):
    def __new__(cls, value):
        # Coerce the input value to an integer.
        val = int(value)

        # Modify the value *before* creating the object.
        if val % 2 != 0:
            val -= 1  # Make it even by rounding down.

        # Pass the final, correct value to the parent's __new__ method.
        return super().__new__(cls, val)


# --- Demo ---
print("--- EvenInt Demo ---")
print(f"MyInt(7) is {EvenInt(7)}")  # -> 6
print(f"MyInt(10) is {EvenInt(10)}")  # -> 10

print("\n--- Singleton Demo ---")
log1 = Logger()
log2 = Logger()
print(f"Are log1 and log2 the same object? {log1 is log2}")  # -> True
