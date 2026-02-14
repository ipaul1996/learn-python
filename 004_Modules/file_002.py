import file_001

# This does not add the names of the functions defined in file_001 directly to the current namespace;
# It only adds the module name file_001 there. Using the module name we can access the functions.
result = file_001.add(5, 3)
print(f"Result of addition: {result}")

greeting = file_001.greet("Alice")
print(greeting)

# Within a module, the module’s name (as a string) is available as the value of the global variable __name__.
print(file_001.__name__)  # file_001
print(__name__)  # __main__
# In Python, __main__ is a special built-in name. When we run a Python file directly not as
# an imported module the interpreter sets the __name__ variable in that file to "__main__".


# A module can contain executable statements as well as function definitions.
# These statements are intended to initialize the module. They are executed
# only the first time the module name is encountered in an import statement.
# They are also run if the file is executed as a script.

# Each module has its own separate space for its variables and functions,
# which is called its namespace. This means that any global variables we
# define inside a module won’t interfere with global variables in other modules or scripts.
# So, the person writing the module doesn’t have to worry about name conflicts.
# However, if we want to, we can still access or change a module’s global variables
# from outside the module by using modname.variablename

# Modules can import other modules. It is customary but not required to place all import statements
# at the beginning of a module (or script, for that matter). The imported module names, if placed at
# the top level of a module (outside any functions or classes), are added to the module’s global namespace.

import math  # Imports the entire math module. Access functions with math.function_name.

# import numpy as np  # Imports the numpy module and gives it the alias np for shorter access.

from math import (
    sqrt,
    pi,
)  # Imports only the sqrt and pi from the math module, allowing direct access without the math prefix.

from math import *

# Imports all public names from the math module into the current namespace. Can cause name conflicts.
# It is generally not recommended to use the wildcard import (from module import *)
# because it can lead to confusion about which names are defined in the current namespace.
# It does not import names that begin with an underscore (_), which are considered private.

from os.path import join  # Imports the join function from the os.path submodule.

# from mypackage import mymodule  # Imports mymodule from the package mypackage


def calculate():
    import math

    return math.sqrt(16)


# Imports can be placed inside functions; the module is only available within that scope.


# Importing a module does not execute the module’s code immediately.
# The module’s code is executed only when the module is imported for the first time.
# If we import the same module again, Python will not execute the module’s code again.
# Instead, it will use the already loaded module from memory.
# This is because Python caches imported modules in a dictionary called sys.modules.


# When we import a module named spam, Python looks for it in this order:
# First, it checks if spam is a built-in module (these are listed in sys.builtin_module_names).
# If not found, it looks for a file called spam.py in the directories listed in sys.path.
# The sys.path list is created from:
# - The folder where your script is located (or the current folder if you’re using the interactive prompt).
# - Any folders listed in the PYTHONPATH environment variable.
# - Some default folders set by Python, like the site-packages directory where extra packages are installed.


# The built-in function dir() is used to find out which names a module defines.
# It returns a sorted list of names defined by the module.
print(dir(file_001))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'greet']

# The dir() function can also be used without arguments to list the names in the current local scope.
print(dir())
"""
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', 
'__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'calculate', 'cbrt', 'ceil', 'comb', 'copysign', 
'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'file_001', 'floor', 
'fma', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'greeting', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 
'join', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'math', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 
'radians', 'remainder', 'result', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
"""