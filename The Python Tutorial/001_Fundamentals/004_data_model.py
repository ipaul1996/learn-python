"""
Python Data Model
=================

Objects, Values, and Types
---------------------------

In Python, everything is an object.
Every object has three fundamental properties: identity, type, and value.


1. Object Identity
   ---------------
   An object's identity is unique and never changes once the object is created.
   Think of it as the object's memory address.

   - The id() function returns an integer representing this identity
   - The 'is' operator compares identities of two objects

   Examples:

   x = [1, 2, 3]
   y = x
   z = [1, 2, 3]

   print(id(x))         # e.g., 140234567890
   print(id(y))         # Same as id(x)
   print(id(z))         # Different from id(x)

   print(x is y)        # True (same identity)
   print(x is z)        # False (different identity)
   print(x == z)        # True (same value)


2. Object Type
   -----------
   An object's type determines:
   - What operations the object supports (e.g., "does it have a length?")
   - What values are valid for objects of that type

   - The type() function returns an object's type (which is itself an object, an unique class object)
   - An object's type is unchangeable (like its identity)

   Examples:

   x = 42
   s = "hello"
   lst = [1, 2, 3]

   print(type(x))       # <class 'int'>
   print(type(s))       # <class 'str'>
   print(type(lst))     # <class 'list'>

   print(type(int))     # <class 'type'> (type is itself an object)


3. Object Value
   ------------
   Some objects' values can change; some cannot.

   Mutable Objects:
   - Objects whose value CAN change after creation
   - Examples: lists, dictionaries, sets

   Immutable Objects:
   - Objects whose value CANNOT change after creation
   - Examples: numbers (int, float), strings, tuples

   - Mutability is determined by the object's type

   Examples:

   # Immutable: int
   x = 10
   # x cannot be changed, only reassigned to a new object
   x = 20  # x now references a different int object

   # Mutable: list
   lst = [1, 2, 3]
   lst.append(4)  # Same list object, value changed
   print(lst)     # [1, 2, 3, 4]


Containers and Mutability
--------------------------

Some objects contain references to other objects. These are called containers.
Examples: tuples, lists, dictionaries.

The references themselves are part of the container's value.

Important distinction:
- Container's value = the VALUES of contained objects (in most contexts)
- Container's mutability = the IDENTITIES of immediately contained objects

For an immutable container (like a tuple):
- You cannot change WHICH objects it contains (identities are fixed)
- But if it contains a mutable object, that object's VALUE can still change

Examples:

# Immutable container (tuple) with mutable object (list)
t = ([1, 2], 'hello')

print(id(t[0]))     # e.g., 140234567890

# Cannot change which list the tuple refers to
# t[0] = [3, 4]     # TypeError: 'tuple' does not support item assignment

# But CAN modify the list that tuple contains
t[0].append(3)
print(t)            # ([1, 2, 3], 'hello')
print(id(t[0]))     # Same identity as before

# The tuple is still considered immutable because the collection
# of objects it contains (their identities) has not changed.


Type Behavior and Object Identity
----------------------------------

For immutable types:
- Operations that compute new values MAY return a reference to an existing object
  with the same type and value
- Behavior is implementation-dependent

For mutable types:
- Each newly created object has a unique identity
- This is not allowed to be optimized away

Examples:

# Immutable type (int): may or may not share identity
a = 1
b = 1
print(a is b)  # True (CPython interns small integers)

c = 1000
d = 1000
print(c is d)  # False (typically, larger integers are not interned)

# But don't rely on this behavior!
# Use == for value comparison, 'is' only for identity checking

# Mutable type (list): guaranteed different identities
x = []
y = []
print(x is y)  # False (always different objects)

# Special case: assigning same object to multiple variables
e = f = []
print(e is f)  # True (both reference the SAME list object)


External Resources and Cleanup
-------------------------------

Some objects contain references to external resources (open files, network sockets, etc.)

These resources should be explicitly released because:
- Garbage collection is not guaranteed to happen immediately
- External resources are limited

Methods for cleanup:
- close() method: Explicitly releases the resource
- try...finally statement: Ensures cleanup even with exceptions
- with statement: Automatic cleanup (recommended)

Examples:

# Manual cleanup (not recommended)
f = open('file.txt', 'r')
try:
    data = f.read()
finally:
    f.close()  # Guaranteed to execute

# Automatic cleanup with 'with' (recommended)
with open('file.txt', 'r') as f:
    data = f.read()
# File automatically closed when leaving 'with' block


Types in Python:
----------------

1. None - A singleton object that represents the absence of a value. Truth value is False. Often used as a default return. Comparisons to None should use is or is not, not == (since None is singleton). None is immutable and hashable; its hash is constant. Its type is NoneType.
Common uses:
   - Default return value of functions that don't explicitly return anything
   - Default value for optional function parameters
   - Representing "no value" or "missing data"


2. NotImplemented - A singleton object that is used by special methods to signal that an operation is not implemented for given operand types. For example, if x.__add__(y) returns NotImplemented, Python will try y.__radd__(x) next. NotImplemented is immutable and hashable.


3. Ellipsis(...) - A singleton object that has no specific operations. It is used as:

(a)
def my_function():
    ...  # Same as pass, indicates "to be implemented"

(b)
def func(args: Tuple[int, ...]) -> None:  # Tuple of any number of ints
          pass

(c)
def some_function(x: int) -> str: ...

Ellipsis is immutable and hashable. Its type is 'ellipsis'. Written as three dots (...) or as the built-in name Ellipsis.

x = ...
print(type(x)) # <class 'ellipsis'>
print(x is Ellipsis)  # True
print(... is Ellipsis) # True
print(bool(...))      # True
print(hash(...))      # Some constant integer


4. Number - All numeric types are immutable and hashable.
    i) Integral
      a) Integers (int):
        - Precision: Arbitrary (unlimited, bounded only by available memory).
        - Supports all bitwise operations: &, |, ^, ~, <<, >>
        - Interning: Small integers (typically -5 to 256) are interned (cached) by CPython.

      b) Booleans (bool):
        - Subclass of int.
        - Values: False (0) and True (1).
        - Stringify to "True" and "False", not "1" and "0"

    ii) Real (float): Machine-level double-precision floating-point numbers. Subject to platform-specific behavior.
       Special values:
       - float('inf')   # Positive infinity
       - float('-inf')  # Negative infinity
       - float('nan')   # Not a Number

    iii) Complex (complex): A pair of floats representing real and imaginary parts.

5. Sequences - Ordered collections accessible by non-negative integer index.
    i) Immutable Sequences
        a) Strings: Sequence of Unicode code points(characters). Each character is itself a string of length 1.
        b) Tuples:
           - Created with commas (a = 1, 2 or (1, 2)). A single-item tuple requires a trailing comma ((1,)).
           - Empty tuple: t = () or t = tuple()
           - The collection of references is immutable, but referenced objects may be mutable.
           - Hashable only if all elements are hashable.
        c) Bytes:
           - Immutable array of 8-bit bytes (integers 0-255).
           -  Created with b'...' literal or bytes()

           Example:
           b = b'hello'
           print(type(b))      # <class 'bytes'>
           print(b[0])         # 104 (ASCII code for 'h')
           print(len(b))       # 5
           print(list(b))      # [104, 101, 108, 108, 111]

    ii) Mutable Sequences
       a) Lists:
          - The general-purpose, mutable sequence.
          - Can contain mixed types.
          - Created with [...] or list()
       b) Byte Arrays: Mutable counterpart to bytes.



6. Set Types - Unordered collections of unique elements. Elements should be hashable, hence immutable.
    i) Sets: Mutable, Created with {...} or set(), {} creates an empty dict, not set! Use set() for empty set.
    ii) Frozen Sets: Immutable, Can be used as dictionary keys or set elements

7. Mappings
    i) Dictionaries (dict):
       - Key-value pairs.
       - Keys must be hashable
       - Mutable.
       - Insertion order is guaranteed.
       - {} creates an empty dict.
       - Average O(1) time for lookup, insert, delete

8. Callable Types - Objects that can be invoked with the () syntax.
    i) User-defined functions: Created with def or lambda.
    ii) Instance methods: Functions bound to a class instance.
    iii) Generator functions: Functions using yield. Return a generator iterator. Saves execution state between yields.
    iv) Coroutine functions: Defined with async def. Return a coroutine object.
    v) Asynchronous generator functions: async def with yield. Return an async generator.
    vi) Built-in functions/methods: Implemented in C (e.g., len, [].append).
    vii) Classes: Calling a class creates an instance (via __new__, __init__).
    viii) Class Instances: Can be made callable by defining a __call__() method.
9. Modules:
   - A basic organizational unit of Python code.
   - Created by the import system.
   - Has a namespace implemented as a dictionary (__dict__)

   import math

   print(type(math))           # <class 'module'>
   print(math.__name__)        # 'math'
   print(math.__file__)        # Path to math module file
   print(dir(math))            # List of names in module
   print(math.pi)              # 3.141592653589793

10. Custom classes: User-defined types created with the class statement.
11. Class instances: Objects created by calling a class.
12. I/O objects: Objects representing open files or streams.
13. Internal Types: Types used internally by the Python interpreter. Code Objects, Frame Objects, Traceback Objects, Slice Objects, Static Method and Class Method Objects.
"""
