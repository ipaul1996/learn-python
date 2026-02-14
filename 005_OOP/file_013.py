# Python has two built-in functions that work with inheritance:

# Use isinstance() to check an instance’s type: isinstance(obj, int) will be
# True only if obj.__class__ is int or some class derived from int.
x = 5
print(isinstance(x, int))  # True


class MyInt(int):
    pass


y = MyInt()
print(isinstance(y, int))  # True

# Use issubclass() to check class inheritance: issubclass(bool, int) is True
# since bool is a subclass of int. However, issubclass(float, int) is False
# since float is not a subclass of int.

# Examples:
print(issubclass(bool, int))  # True
print(issubclass(float, int))  # False
print(issubclass(MyInt, int))  # True
