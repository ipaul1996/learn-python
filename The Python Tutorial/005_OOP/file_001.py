# Namespace (The Containers)
# A namespace(symbol table) in Python is simply a mapping from names (identifiers) to objects, implemented as dictionaries.
# It is the specific place in memory where a variable lives.

# Local namespace
# - Created each time a function (or method) is invoked (not when defined).
# - Holds names defined within that function (parameters, locally assigned variables).
# - Discarded when the function returns or raises an exception that is not handled within the function.
# - Note: Every recursion creates a unique, separate local namespace.


# Global namespace
# - Created when the module (file) definition is read in.
# - Holds names defined at the top level of that module (imports, functions, classes, module constants).
# - Persists until the module is unloaded or the interpreter exits.


# Class Namespace
# - Created when the class definition is executed (Python classes are executable statements).
# - Holds names defined in the class body (methods, class variables/attributes).
# - It becomes the attribute dictionary (__dict__) of the class object.
# - Unlike functions, a class namespace is NOT automatically used as a enclosing scope for the methods inside it.
#   (This is why you must use 'self.variable' or 'ClassName.variable' inside methods).


# Built‑in namespace
# - Created when the interpreter starts.
# - Contains names built into the interpreter (len, int, Exception, etc.).
# - Always available, unless explicitly shadowed by a global or local definition.
# - The built-in names actually also live in a module; this is called "builtins" module.


# Scope (The Search Rules)
# A scope defines a textual region of a Python program where a namespace is directly accessible.
# "Directly accessible" means you can use the name without a prefix (e.g., 'x' instead of 'module.x').
# Scopes are determined statically (by the structure of the code), but used dynamically (at runtime).

# The LEGB Rule (How Python connects Scope to Namespace):
# When you type a name, Python searches the namespaces in this exact order:
# - Local scope (L): Names assigned within the current function or method.
# - Enclosing scope (E): Names in any enclosing functions (for nested functions), searched from inner to outer.
# - Global scope (G): Names defined at the top level of the current module.
# - Built-in scope (B): Names preassigned in Python (such as len, int, Exception, etc.).

# If the name is not found in any of these, Python raises a NameError.
# Note: Class Namespaces do not fit the LEGB rule.


# - If you only READ a variable (print(x)), Python looks up the scopes (LEGB) to find it.
# - If you ASSIGN a variable (x = 10), Python creates a new LOCAL variable by default.
#   (This shadows any outer variable with the same name).

# THE "global" KEYWORD
# - Used inside a function to refer to a variable in the Global (Module) scope.
# - Use this if you need to ASSIGN (change) a global variable's value from inside a function.
# - "I am not creating a new local 'x', I am updating the module's 'x'."

# THE "nonlocal" KEYWORD
# - Used inside a nested function (inner) to refer to a variable in the nearest Enclosing scope.
# - It skips the Global scope. It looks strictly in the outer functions.
# - Use this to update a variable in a parent function from insidse the current function.

x = 10  # Global variable
def outer():
    y = 20  # Enclosing variable (Local to outer)

    def inner():
        global x     # Point to the top-level x
        nonlocal y   # Point to 'outer's 'y'

        x = 100      # Changes the global x
        y = 200      # Changes y in outer()
        z = 300      # New variable, local to 'inner'

        print("inner:", x, y, z)

    inner()
    print("outer:", x, y)

outer()
print("global:", x)
# Output:
# inner: 100 200 300
# outer: 100 200
# global: 100


# A function's "Global Scope" is the module where it was DEFINED,
# not the module where it is CALLED.
# When you import a function, you are importing a reference to it.
# You are NOT copying the code into your current file.
# The function still "lives" in its original module and sees that module's global variables.

"""
# module1.py
def foo():
    print(x)     # This 'x' is permanently bound to module1's global scope

x = 10


# module2.py
import module1

x = 99          # This is 'x' in module2's namespace
module1.foo()   # Prints 10, not 99!

# When foo() runs, it looks for 'x' in its own global namespace (module1).
# It does not know or care about module2's 'x'.

"""

# Assignments (like x = 5) always create or update a variable in the innermost (local) scope unless we use global or nonlocal.
# Assignments do not copy data—they just make the name point to (reference) an object.

# When we use del x, we are only removing the name x from the current (usually local) namespace.
# The object that x was pointing to still exists if there are other names or variables pointing to it.

# Any new name (from assignments, import, or def) is added to the local scope by default.
