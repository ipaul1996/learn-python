# Classes in Python provides a way to bundle data and functionality together.
# A class is like a blueprint for creating objects (instances).
# Creating a new class means creating a new type of object. We can create multiple
# instances of that type.
# Each instance of a class can have its own attributes, known as instance attributes, which store data unique to that object.
# These attributes represent the state of the object.
# Classes can also define methods—functions that belong to the class—which operate on instance attributes.
# Methods are used to access, modify, or perform actions using the state of an instance.
# Python supports class inheritance, allowing a class (derived class) to inherit attributes and methods from one or more base classes.
# The derived class can override or extend the functionality of its base class by redefining methods.
# In Python, class members (attributes and methods) are public by default, except for private variables using naming conventions.
# All methods explicitly take the instance as the first argument, usually named 'self'.
# Classes are themselves objects in Python, allowing dynamic creation and modification.
# Built-in types can be extended by user-defined classes.
# Special methods (like arithmetic operators and subscripting) can be redefined for class instances to customize their behavior.


# A namespace in Python is simply a mapping from names (identifiers) to objects, implemented as dictionaries.
# Namespaces are used to ensure that names in a program do not conflict with each other.

# Local namespace
# - Created when a function (or method) is invoked.
# - Holds names defined within that function (parameters, locally assigned variables).
# - Discarded when the function returns or raises an exception that is not handled within the function.
# - Recursive invocations each have their own local namespace.

# Global namespace
# - Created when the module definition is read in.
# - Holds names defined at the top level of that module (module variables, function and class definitions).
# - Persists until the module is unloaded or the interpreter exits.


# Built‑in namespace
# - Created when the interpreter starts.
# - Contains names built into the interpreter (len, int, Exception, etc.).
# - Always available, unless explicitly shadowed by a global or local definition.
# - The built-in names actually also live in a module; this is called builtins.


# Scope
# A scope defines the region of a Python program where a namespace is directly accessible.
# “Directly accessible” means that an unqualified reference to a name will search for that name in the current namespace.
# Scopes are determined statically (by the structure of the code), but used dynamically (at runtime).
# At any point during execution, Python uses a well-defined order to resolve names, known as the "LEGB" rule:
# - Local scope: Names assigned within the current function or method.
# - Enclosing scope: Names in any enclosing functions (for nested functions), searched from inner to outer.
# - Global scope: Names defined at the top level of the current module.
# - Built-in scope: Names preassigned in Python (such as len, int, Exception, etc.).
# Python searches these scopes in the above order when resolving names.

# If we use the global keyword inside a function, we tell Python to use the variable from the module’s global scope 
# (outside all functions), not create a new local variable.

# If we want to modify a variable from an enclosing function (not global, but not local either), use the nonlocal keyword.

# If we don’t use global or nonlocal, assigning to a variable inside a function will always create a new local variable, 
# even if a variable with the same name exists outside.

x = 10  # Global variable
def outer():
    y = 20  # Enclosing variable

    def inner():
        global x
        nonlocal y
        x = 100      # Changes the global x
        y = 200      # Changes y in outer()
        z = 300      # Local to inner()
        print("inner:", x, y, z)

    inner()
    print("outer:", x, y)

outer()
print("global:", x)
# Output:
# inner: 100 200 300
# outer: 100 200
# global: 100

# At the top level of a file, the local scope is the same as the global scope — the module’s namespace.
# In a class, local scope = class’s own namespace (for class attributes and methods).


# Scopes are determined by where code is written (textually), not where or how it’s called.
# If you define a function in a module, its global scope is always that module’s namespace—even 
# if you call the function from somewhere else or using a different name.

"""
# module1.py
def foo():
    print(x)

x = 10


# module2.py
import module1

x = 99
module1.foo()  # Prints 10, not 99!
# Even though you call foo() from module2, it looks for x in module1’s global namespace, 
# because that’s where foo was defined.

"""

# Assignments (like x = 5) always create or update a variable in the innermost (local) scope unless we use global or nonlocal.
# Assignments do not copy data—they just make the name point to (reference) an object.

# When we use del x, we are only removing the name x from the current (usually local) namespace.
# The object that x was pointing to still exists if there are other names or variables pointing to it.

# Any new name (from assignments, import, or def) is added to the local scope by default.


# The global statement tells Python that a variable inside a function should refer to the variable 
# in the global (module-level) scope, not create a new local variable.
# This lets you change the global variable from inside the function.

# The nonlocal statement tells Python that a variable inside a nested function should refer to a variable 
# in the nearest enclosing (but not global) function’s scope.
# This lets you change a variable from an outer function inside an inner function.









# An attribute is any name that comes after a dot.
# For example, in z.real, 'real' is an attribute of the object z.
# When you write modname.funcname, 'modname' is a module object and 'funcname' is an attribute of that module.

# Attributes may be read-only or writable. In the latter case, assignment to attributes is possible. 
# Module attributes are writable: you can write modname.the_answer = 42. Writable attributes may also be 
# deleted with the del statement. For example, del modname.the_answer will remove the attribute the_answer 
# from the object named by modname.


