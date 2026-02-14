# 1. Syntax Errors (Parsing Errors)
# - Occur BEFORE execution, during the "parsing" stage.
# - Cause: Violating the grammar rules of Python (e.g., missing `:`, unmatched `()`, wrong indentation).
# - Result: The program never starts.

# 2. Exceptions (Runtime Errors)
# - Occur DURING execution.
# - Cause: The syntax is correct, but the operation is impossible (e.g., dividing by zero, opening a missing file).
# - Result: Python raises an "Exception Object". If not handled (caught), the program crashes with a Traceback.


# BaseException  <-- The absolute root (Do NOT catch this blindly!)
#  ├── SystemExit        <-- Raised by sys.exit()
#  ├── KeyboardInterrupt <-- Raised by Ctrl+C
#  └── Exception         <-- The root for all User-Code errors. CATCH THIS.
#       ├── ArithmeticError
#       │    ├── ZeroDivisionError  (1 / 0)
#       │    ├── OverflowError      (Number too big)
#       │    └── FloatingPointError
#       │
#       ├── LookupError   <-- Parent for "Finding things" errors
#       │    ├── IndexError    (Seq[99] - sequence out of range)
#       │    ├── KeyError      (Dict['bad_key'] - key not found)
#       │
#       ├── ValueError    (Right type, wrong content. e.g., int("hello"))
#       ├── TypeError     (Wrong type. e.g., "hello" + 5)
#       ├── AttributeError (obj.missing_method)
#       ├── NameError     (variable_not_defined)
#       │    └── UnboundLocalError
#       │
#       ├── OSError       <-- Parent for System/IO errors
#       │    ├── FileNotFoundError
#       │    ├── PermissionError
#       │    ├── TimeoutError
#       │
#       ├── StopIteration (Signal that an iterator is empty)
#       ├── MemoryError
#       └── NotImplementedError


# Critical Distinction: BaseException vs Exception
# - BaseException: Includes system-exiting events like SystemExit and KeyboardInterrupt.
#   Rule: Avoid `except BaseException`. If you do this, you might stop your script
#   from exiting when you hit Ctrl+C or call sys.exit().

# - Exception: The base class for all standard errors.
#   Rule: Use `except Exception` when you want to catch "everything that might go wrong in my code"
#   without blocking the user from stopping the program.


# Common Error Categories

# 1. ArithmeticError (Math Issues)
#    - ZeroDivisionError: Division or modulo by zero.
#    - OverflowError: Result is too large to be represented (mostly in floats/complex).

# 2. LookupError (Container Issues)
#    - IndexError: Asking for index 5 in a list of length 3.
#    - KeyError: Asking for key 'apple' in a dict that only has 'banana'.
#    * Pro Tip: Catch `LookupError` to handle both cases in one block.

# 3. Type & Value Errors (Data Issues)
#    - TypeError: "I can't add a String to an Integer". The operation is invalid for this object type.
#    - ValueError: "I expect a number-string like '5', but you gave me 'apple'".
#      The type is correct (string), but the content is inappropriate.

# 4. definition Errors
#    - NameError: Trying to use a variable `x` that hasn't been defined yet.
#    - AttributeError: Trying to access `obj.score` when `obj` has no such attribute.
#    - NotImplementedError: Used in abstract classes to say "Child class MUST define this".

# 5. OS & Environment (The Outside World)
#    - OSError: The parent for file/network errors.
#    - FileNotFoundError: "I can't find 'data.txt'".
#    - PermissionError: "I found 'secret.txt', but I'm not allowed to read it".


# Code Verification of Hierarchy
print(issubclass(IndexError, LookupError))  # True
print(issubclass(LookupError, Exception))  # True
print(issubclass(Exception, BaseException))  # True (Grandparent)


def get_item(seq, index):
    return seq[index]


# print(get_item([1, 2, 3], 5))

"""
Traceback (most recent call last): 
  # 1. The Stack Trace (The Path)
  # Shows the chain of function calls that led to the error.
  # Read from BOTTOM to TOP to trace the cause.
  File "script.py", line 5, in <module>
    print(get_item([1, 2, 3], 5))
          ~~~~~~~~^^^^^^^^^^^^^^
  File "script.py", line 2, in get_item
    return seq[index]
           ~~~^^^^^^^
           
  # 2. The Exception Type & Message (The What)
  IndexError: list index out of range
  # Type: IndexError
  # Message: list index out of range
"""
