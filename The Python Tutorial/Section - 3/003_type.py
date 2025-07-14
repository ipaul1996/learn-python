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


# Get the name of the type as a string using __name__ attribute
print(type(42.0).__name__) # float
