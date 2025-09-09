# Identity Operators
# In Python everything is object. Every object has three core properties: an identity, a type, and a value.
# An object’s identity is a unique identifier for it. It is guaranteed to be unique and constant for the object's lifetime. 
# You can think of it as the object’s address in memory. The built-in id() function returns this identity as an integer.

# 'is'      --> Returns True if two variables point to the same object (i.e., have the same identity).
# 'is not'  --> Returns True if two variables point to different objects.

# Note:
# - 'is' and 'is not' check for object identity, not value equality. Use '==' to compare values for equality.
#    - a is b is equivalent to id(a) == id(b). It checks if a and b are the same object.
#    - a == b checks if the values of a and b are equivalent.
#    - a and b can be different objects, yet there values can be the same.

a = [1, 2, 3]
print(f"ID of a: {id(a)}") # 4309105088

b = a  # b references the same list object as a
print(f"ID of b: {id(b)}") # 4309105088

c = [1, 2, 3]    # c is a new list object with the same contents as a
print(f"ID of c: {id(c)}") # 4308945216

print(f"a is b: {a is b}")    # True (same object)
print(f"a is c: {a is c}")    # False (different objects, even though values are equal)
print(f"a == c: {a == c}")    # True (values are equal)

# Demonstrating 'is not'
print(f"a is not c: {a is not c}")  # True


#  For optimization, Python's CPython implementation pre-allocates and reuses certain immutable objects. 
#  This behavior, known as "interning" or "caching," can make is return True unexpectedly.
#  - Integers from -5 to 256 are always cached. Any variables assigned these values will point to the same object.
#  - Short strings may also be interned.
#  - None, True, and False are singletons. There is only one instance of each, so you should always use is None, 
#    is True, or is False.
#  Warning: This caching behavior is an implementation detail. You should never rely on it. Always use == to compare 
#  values and is only when you specifically need to check for object identity.

x = 5
y = 5
print(f"x is y: {x is y}")    # True # (due to integer caching)
