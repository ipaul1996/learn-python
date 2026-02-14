# type()
# The built-in `type()` function returns the type (class) of the given object i.e., the class object.
# IMPORTANT: This class object is unique in memory.
# Regardless of how many instances you create (t1, t2, t3...),
# type(t1), type(t2), and the class name 'Test' all reference
# the EXACT SAME object in memory.

print(type(2))  # <class 'int'>
print(type(42.0))  # <class 'float'>

print(type("Spam"))  # <class 'str'>
print(type("42"))  # <class 'str'>

print(type(True))  # <class 'bool'>
print(type(False))  # <class 'bool'>

fruits = ["apple", "banana", "cherry"]
print(type(fruits))  # <class 'list'>

coordinates = (10.0, 20.0)
print(type(coordinates))  # <class 'tuple'>

person = {"name": "Alice", "age": 30, "city": "New York"}
print(type(person))  # <class 'dict'>

unique_numbers = {1, 2, 3, 4, 5}
print(type(unique_numbers))  # <class 'set'>

# None is commonly used to represent the absence of a value,
# such as when a function does not explicitly return anything.
print(type(None))  # <class 'NoneType'>


def example_function():
    pass


result = example_function()
print(result)  # None
print(type(result))  # <class 'NoneType'>
print(type(example_function))  # <class 'function'>


# Get the name of the type as a string using __name__ attribute
print(type(42.0).__name__)  # float


print(type(example_function))  # <class 'function'>


class Test:
    def __init__(self, x, y):
        self.x = x
        self.y = y


t = Test(1, 2)
print(type(t))  # <class '__main__.Test'>
print(type(t).__name__)  # Test


"""
1. dir() 
Provides a list of names (attributes and methods) belonging to an object or within 
the current scope. It's a quick way to see what's available.

Usage:
- dir(object) — Lists all valid attributes and methods of the object.
- dir() — Lists names in the current local scope.

Use dir() when you want a quick reminder of an object's capabilities without the details. 
It answers the question, "What names are associated with this?"

Examples:
dir(list)           # Lists all methods and attributes of list
dir(Dog)            # Lists all methods and attributes of Dog class
dir()               # Lists names in the current scope

******************************

2. help()
Displays the official documentation (the docstring) for an object, method, or module. 
It's used to understand how to use something.

Usage:
- help(object) — Shows the full documentation, including function signatures and descriptions.
- help() — Starts an interactive help utility in the Python shell.

Use help() when you need a detailed explanation of what something does, what arguments it takes, 
and what it returns. It answers the question, "How do I use this?"

Examples:
help(list)           # Info about lists
help(Dog.get_name)   # Info about a method
"""
