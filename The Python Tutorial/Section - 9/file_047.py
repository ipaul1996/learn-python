# __dict__ & vars()

# Every instance of a class (and most other objects) has a special attribute called __dict__.
# This dictionary stores the attributes of that specific instance. When you set an attribute on
# an object, like my_car.color = 'blue', you are essentially adding a key-value pair ('color': 'blue')
# to that object's __dict__. Because it's a regular dictionary, you can directly view and even
# manipulate an object's state through its __dict__.


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model


my_car = Car("Toyota", "Camry")

# Using __dict__ to inspect instance attributes
print(f"Using __dict__: {my_car.__dict__}")
# Output: {'make': 'Toyota', 'model': 'Camry'}


# The vars() function is safer way to get an object's __dict__.
# 1. Preferred Usage: While vars(obj) and obj.__dict__ typically return the same result, using vars()
# is generally preferred as it's more explicit and follows Python's "we're all consenting adults" philosophy.
# 2. Error Handling: Not all objects have a __dict__ attribute:
#     - Objects using __slots__ for memory optimization
#     - Built-in types (e.g., integers, strings)
#     - Objects with custom __getattr__ implementations
#    In these cases, vars() handles them more gracefully by raising a TypeError instead of an AttributeError.
# 3. Scope Awareness: When called without arguments, vars() returns the local symbol table (similar to locals()),
#    which is useful for debugging:
def example_function():
    x = 10
    y = 20
    print(vars())  # Shows local variables: {'x': 10, 'y': 20}


# Creating attributes using standard dot notation
my_car.year = 2023  # type: ignore

# Creating attributes directly through __dict__
my_car.__dict__["color"] = "blue"

# Both approaches update the object's state
print(f"Updated object: {vars(my_car)}")
# Output: {'make': 'Toyota', 'model': 'Camry', 'year': 2023, 'color': 'blue'}

# Note: __dict__ and vars() only show instance attributes. Class attributes are stored in the class's own __dict__
print(f"Class __dict__: {Car.__dict__}")
# Shows class attributes, methods, and other class metadata
