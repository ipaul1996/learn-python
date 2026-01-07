# The keyword def introduces a function definition. It must be followed by the
# function name and the parenthesized list of formal parameters. The statements
# that form the body of the function start at the next line, and must be indented.
# The first statement of the function body can optionally be a string literal;
# this string literal is the function’s documentation string, or docstring.


def greet(name):
    """Greet a person by name."""
    print(f"Hello, {name}!")


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def factorial(n):
    """Return the factorial of a non-negative integer n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Parameter: A variable listed inside the parentheses in the function definition.
# Example: In def add(a, b):, a and b are parameters.

# Argument: The value that is sent to the function when it is called.
# Example: In add(2, 3), 2 and 3 are arguments.


"""
How Arguments Are Passed in Python?
-----------------------------------

Python does NOT use "pass by value" or "pass by reference" like C/C++.
Python uses "Pass by Object Reference" (also called "Pass by Assignment").

1. Variables are names that reference objects.
2. When you pass a variable, you pass the reference to the object.
3. The function receives a copy of the reference, not a copy of the object.

Therefore,
- Immutable objects (int, str, tuple): Function cannot modify original
- Mutable objects (list, dict, set): Function CAN modify original

"""

# Immutable - original unchanged
def modify_int(n):
    n = n + 1  # Creates NEW object, rebinds local variable
    return n


x = 10
modify_int(x)
print(x)  # 10 (unchanged)


# Mutable - original changed
def modify_list(lst):
    lst.append(4)  # Modifies SAME object


my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 4] (changed!)


# Rebinding vs Mutating
def rebind(lst):
    lst = [4, 5, 6]  # Rebinds local variable to NEW object (original unaffected)


def mutate(lst):
    lst.append(4)  # Mutates the SAME object


# The execution of a function introduces a new symbol table used for the
# local variables of the function. More precisely, all variable assignments
# in a function store the value in the local symbol table specific to a particular execution;
# whereas variable references first look in the local symbol table, then in the local symbol tables
# of enclosing functions, then in the global symbol table, and finally in the table
# of built-in names. This is called LEGB rule(Local → Enclosing → Global → Built-in).
# Thus, global variables and variables of enclosing functions cannot be
# directly assigned a value within a function (unless, for global variables,
# named in a global statement, or, for variables of enclosing functions,
# named in a nonlocal statement), although they may be referenced.

# Note: While global/enclosing variables cannot be directly reassigned without global/nonlocal,
# mutating them is possible without these declarations if they are mutable objects (e.g., lists, dictionaries).
# This is because mutation does not rebind the variable name; it
# modifies the object the name already references.

x = "global x"
y = "global y"


def outer():
    x = "outer x"
    y = "outer y"

    def inner():
        nonlocal x
        x = "inner x"
        print("inner:", x)
        y = "inner y"
        print("inner:", y)

    inner()
    print("outer:", x)
    print("outer:", y)


def change_global():
    global x
    x = "changed global x"
    y = "changed global y"


outer()
print("global before change_global:", x, y)
change_global()
print("global after change_global:", x, y)
"""
Output:

inner: inner x
inner: inner y
outer: inner x
outer: outer y

global before change_global: global x global y
global after change_global: changed global x global y
"""