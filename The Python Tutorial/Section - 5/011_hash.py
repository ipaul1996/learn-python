"""
Hash in Python:
===============

A hash is a fixed-size (64-bit) integer value computed from an object using hash() function. It is calculated based on the data inside an object. hash(object) calls the object's __hash__() method.
- If two objects are equal (a == b), they MUST have the same hash value.
- If two objects have the same hash, they are NOT necessarily equal (collision).
- Hash value must remain CONSTANT throughout the object's lifetime. Thus mutable objects are not hashable, as their value would change so their hash

Purpose:
--------
Fast lookups (O(1) time) in hash-based collections:
- Dictionaries (dict)  →  Keys are hashed
- Sets (set)           →  Elements are hashed
- Frozen Sets (frozenset)

Hash Table Mechanism:
---------------------
Goal: We want to store the pair ("apple", 5) in a dictionary so we can find it instantly later.
1. Compute Hash Value
   - When you add a key to dict or element to set, Python calls key.__hash__()
   - This returns an integer (the hash value)
   - This integer is used to determine WHERE to store the object in memory
   - Example: hash("apple")  →  Returns an integer like 5765433627188306940

2. Find Slot (Bucket) in Internal Table
   - Python uses the hash value to calculate an index in its internal array
   - This index points to a "slot" or "bucket" where the object will be stored
   - If the slot is already occupied (called a "collision"), Python uses
     "probing" — a technique to find the next available slot
   - Example:
     hash("apple") = 5765433627188306940
     slot_index = 5765433627188306940 % table_size  →  e.g., slot 4

3. Verify Match Using Equality
   - When retrieving, Python first finds the slot using hash
   - Then it calls key.__eq__() to CONFIRM this is the correct object
   - This is needed because different objects can have the same hash (collision)


Hashable vs Unhashable Types:
-----------------------------
Hashable (Immutable):
    - int, float, bool, str, bytes
    - tuple (only if all elements are hashable)
    - frozenset
    - None
    - Custom objects (by default, unless __eq__ is overridden without __hash__)

Unhashable (Mutable):
    - list, dict, set, bytearray



Custom __hash__ Implementation:
-------------------------------
Rules when implementing __hash__ in custom classes:

1. If you override __eq__, you MUST override __hash__ (or set __hash__ = None)
2. If a == b, then hash(a) == hash(b) MUST be True
3. __hash__ should return an integer
4. Use hash() on immutable attributes only

"""


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self._x == other._x and self._y == other._y

    def __hash__(self):
        return hash((self._x, self._y))  # Tuple of immutable attributes


"""
What Happens If __eq__ Is Defined Without __hash__?
---------------------------------------------------
- Python automatically sets __hash__ = None
- The object becomes unhashable
- Cannot be used as dict key or set element
- Raises TypeError: unhashable type
"""

"""
Advanced: __hash__ for Inheritance:
-----------------------------------
- If parent defines __eq__ and __hash__, child inherits both
- If child overrides __eq__, it should also override __hash__
- If child overrides __eq__ without __hash__, child becomes unhashable
"""


class Parent:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)


class Child(Parent):
    def __eq__(self, other):  # Overrides __eq__
        return super().__eq__(other)

    # Must also override __hash__ or Child becomes unhashable!
    def __hash__(self):
        return super().__hash__()


"""
The id() vs hash() Distinction:
-------------------------------
- id(obj)   → Memory address (unique for each object instance)
- hash(obj) → Computed from object's VALUE (equal objects have equal hashes)
"""
a = "hello"
b = "hello"

print(id(a) == id(b))  # May be True (string interning) or False
print(hash(a) == hash(b))  # Always True (same value)