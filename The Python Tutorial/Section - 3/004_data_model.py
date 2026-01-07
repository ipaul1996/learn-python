# Python Data Model

"""
In Python everything is object.
Every object has an identity, a type and a value.

An object’s identity never changes once it has been created; you may think of it as the object’s address in memory.
The id() function returns an integer representing its identity.
The is operator compares the identity of two objects.

An object’s type determines the operations that the object supports (e.g., “does it have a length?”) and also defines the possible values for objects of that type.
The type() function returns an object’s type (which is an object itself). Like its identity, an object’s type is also unchangeable.

The value of some objects can change. Objects whose value can change are said to be mutable; objects whose value is unchangeable once they are created are called immutable. An object’s mutability is determined by its type; for instance, numbers, strings and tuples are immutable, while dictionaries and lists are mutable.
The value of an immutable container object that contains a reference to a mutable object can change when the latter’s value is changed; however the container is still considered immutable, because the collection of objects it contains cannot be changed. For example, a tuple containing a list.

Some objects contain references to other objects; these are called containers. Examples of containers are tuples, lists and dictionaries. The references are part of a container’s value. In most cases, when we talk about the value of a container, we imply the values, not the identities of the contained objects; however, when we talk about the mutability of a container, only the identities of the immediately contained objects are implied. So, if an immutable container (like a tuple) contains a reference to a mutable object, its value changes if that mutable object is changed.

Types affect almost all aspects of object behavior. Even the importance of object identity is affected in some sense: for immutable types, operations that compute new values may actually return a reference to any existing object with the same type and value, while for mutable objects this is not allowed. For example, after a = 1; b = 1, a and b may or may not refer to the same object with the value one, depending on the implementation. This is because int is an immutable type, so the reference to 1 can be reused. This behaviour depends on the implementation used, so should not be relied upon, but is something to be aware of when making use of object identity tests. However, after c = []; d = [], c and d are guaranteed to refer to two different, unique, newly created empty lists. (Note that e = f = [] assigns the same object to both e and f.)

Some objects contain references to “external” resources such as open files or windows. It is understood that these resources are freed when the object is garbage-collected, but since garbage collection is not guaranteed to happen, such objects also provide an explicit way to release the external resource, usually a close() method. Programs are strongly recommended to explicitly close such objects. The try…finally statement and the with statement provide convenient ways to do this.

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
