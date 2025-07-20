# type()
# The built-in `type()` function returns the type (class) of the given object.
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


"""
1. dir() 
It lists the attributes and methods of objects, classes, or modules.
Usage:
- dir(object) — Lists all valid attributes, methods, and properties of the object.
- dir() — Lists names in the current local scope.
Useful for exploring what you can do with an object or module.
Does not show documentation, only names.

Examples:
dir(list)           # Lists all methods and attributes of list
dir(Dog)            # Lists all methods and attributes of Dog class
dir()               # Lists names in the current scope

******************************

2. help()
It displays documentation for objects, classes, functions, or modules.

Usage:
- help(object) — Shows docstring, methods, and usage info.
- help() — Starts an interactive help utility in the Python shell.

Examples:
help(list)           # Info about lists
help(Dog.get_name)   # Info about a method
"""
