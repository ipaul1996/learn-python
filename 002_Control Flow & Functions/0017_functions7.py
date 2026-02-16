# Nested Functions and Closures

# Nested functions are functions defined inside other functions.
# Closures allow inner functions to "remember" and access variables from their
# enclosing scope, even after the outer function has finished execution.

# Key Concepts:
# - Nested functions are created at runtime (when the outer function executes)
# - Closures capture state without using classes or global variables
# - Variables are stored in cell objects and accessible via __closure__
# - The nonlocal keyword allows modification of enclosure scope variables
# - Variable lookup follows LEGB order (Local, Enclosing, Global, Built-in)


def outer_function(x):
    """Outer function that defines an inner helper function."""
    scale_factor = 2  # Local to outer_function

    def inner_function(y):
        """Inner function can access outer function's variables."""
        # 'scale_factor' and 'x' are "free variables" here
        return (y * x) + scale_factor

    return inner_function(10)


result = outer_function(5)
print(result)  # 52 (calculation: (10 * 5) + 2)
# inner_function is NOT accessible from global scope


# Each call to outer_function creates a NEW inner_function object
def create_function():
    def helper():
        return "hello"

    return helper  # Note: We're not calling helper(), just returning it


func1 = create_function()
func2 = create_function()

print(func1 is func2)  # False (different function objects)
print(func1())  # "hello"
print(func2())  # "hello"


# A closure is created when:
# 1. An inner function references variables from its enclosing scope
# 2. The inner function is returned or passed around
# 3. The outer function has finished executing

# The inner function "closes over" the variables it needs, preserving them
# even after the outer function's execution is complete.


def make_multiplier(factor):
    """
    Factory function that creates multiplier functions.

    Returns a function that multiplies its argument by 'factor'.
    'factor' is captured in a closure.
    """

    def multiplier(number):
        # 'factor' is a free variable (from enclosing scope)
        return number * factor

    return multiplier  # Return the function object, not a call to it


# Create two different multiplier functions with different states
double = make_multiplier(2)  # Captures factor=2
triple = make_multiplier(3)  # Captures factor=3

print(double(5))  # 10 (5 * 2)
print(triple(5))  # 15 (5 * 3)
print(double(10))  # 20 (10 * 2)
print(triple(10))  # 30 (10 * 3)


# Function objects have a __closure__ attribute that contains the cell objects
# holding the values of free variables.
# - __closure__: Tuple of cell objects (or None if no closure)
# - Each cell has a cell_contents attribute containing the actual value


def make_adder(x):
    """Create a function that adds x to its argument."""

    def adder(y):
        return x + y

    return adder


add_5 = make_adder(5)

print(add_5(3))  # 8

if isinstance(add_5.__closure__, tuple):
    # The cell object (container)
    print(add_5.__closure__[0])
    # Output: <cell at 0x...: int object at 0x...>

    # The actual value inside
    print(add_5.__closure__[0].cell_contents)
    # Output: 5
else:
    print("This function has no closure.")

# The code object tells us which variables are local and which are captured.
# 'co_freevars': Variables used but not defined locally (captured)
print(add_5.__code__.co_freevars)  # ('x',)

# 'co_varnames': Local variables and arguments
print(add_5.__code__.co_varnames)  # ('y',)
