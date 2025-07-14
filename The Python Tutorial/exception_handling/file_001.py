# There are (at least) two distinguishable kinds of errors: syntax errors (or parsing errors) and exceptions.
# A syntax error occurs when Python cannot parse your code because it violates the language rules.
# For example, missing a colon, unmatched parentheses, or incorrect indentation will cause a SyntaxError.
# Syntax errors are detected before the program runs, during the parsing stage.

# Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made 
# to execute it. Errors detected during execution are called exceptions - like a 
# ZeroDivisionError when you divide by zero. You don’t have to catch every exception, but you 
# can intercept them to handle or recover from errors.
# - Exception classes all inherit from the base class BaseException, with most user-level 
#   errors under the subclass Exception.
# - When Python detects an error (e.g. indexing out of range), it raises an exception object.
# - If uncaught, it propagates up and terminates the program, printing a traceback. The traceback 
#   shows the exception type (IndexError), message, and call stack.


def get_item(seq, index):
    return seq[index]


# Raises IndexError:
# print(get_item([1, 2, 3], 5))
"""
Traceback (most recent call last):
  File "/Users/indrajit.paul/Documents/Code/learn_python/The Python Tutorial/execption_handling/file_001.py", line 5, in <module>
    print(get_item([1, 2, 3], 5))
          ~~~~~~~~^^^^^^^^^^^^^^
  File "/Users/indrajit.paul/Documents/Code/learn_python/The Python Tutorial/execption_handling/file_001.py", line 2, in get_item
    return seq[index]
           ~~~^^^^^^^
IndexError: list index out of range
"""

print(issubclass(IndexError, LookupError))  # True
print(issubclass(LookupError, Exception))  # True
print(issubclass(Exception, BaseException))  # True
print(type(IndexError))  # <class 'type'>
print(type(LookupError))  # <class 'type'>

# catching LookupError will handle both KeyError and IndexError, while catching Exception
# handles nearly everything except system-exit events (SystemExit, KeyboardInterrupt inherit
# from BaseException directly).

# BaseException --> The root of the exception hierarchy. Normally we inherit from Exception instead.

# Exception	--> All user-level exceptions should derive from this (catches almost everything except system-exit events).

# ArithmeticError --> Base class for numeric errors.
# - ZeroDivisionError --> Raised when dividing by zero (integer or float).
# - OverflowError --> Raised when a numeric operation exceeds its defined limits.
# - FloatingPointError --> Raised for floating-point arithmetic issues.

# LookupError --> Base class for indexing and key lookup errors.
# - IndexError --> Raised when a sequence subscript is out of range.
# - KeyError --> Raised when a mapping (e.g. dict) key isn’t found.

# ValueError --> Raised when a built-in operation or function receives an argument of the right type but inappropriate value.

# TypeError --> Raised when an operation or function is applied to an object of inappropriate type.

# AttributeError --> Raised when attribute reference or assignment fails.

# ImportError --> Base for import-related failures.
# - ModuleNotFoundError --> Raised when an import fails because the module can’t be found.

# OSError --> Base for OS-related errors (file, network, etc.).
# - FileNotFoundError --> Raised when a file or directory is requested but doesn’t exist.
# - PermissionError --> Raised when trying to run an operation without the adequate access rights.
# - TimeoutError --> Raised when a system function timed out at the OS level.

# NameError --> Raised when a local or global name is not found.
# - UnboundLocalError --> Raised when a local variable is referenced before assignment.

# StopIteration --> Raised by iterators to signal no further values.

# AssertionError --> Raised when an assert statement fails.

# MemoryError --> Raised when an operation runs out of memory.

# NotImplementedError --> Raised by abstract base classes to indicate an abstract method needs an override.
