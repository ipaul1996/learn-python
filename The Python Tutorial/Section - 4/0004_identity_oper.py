# Identity Operators
# In Python everything is object. Every object has an identity, a type and a value. 
# An object’s identity never changes once it has been created; we may think of it as 
# the object’s address in memory. The id() function returns an integer representing its identity.

# 'is'      --> Returns True if two variables point to the same object (i.e., have the same identity).
# 'is not'  --> Returns True if two variables point to different objects.

# Note:
# - 'is' and 'is not' check for object identity, not value equality.
# - Use '==' to compare values for equality.
# - For immutable types (like int, float, bool, str, tuple), Python may cache/reuse objects for efficiency,
#   so 'is' may sometimes return True for seemingly separate objects.


a = [1, 2, 3]
b = a            # b references the same list object as a
c = [1, 2, 3]    # c is a new list object with the same contents as a

print(f"a is b: {a is b}")    # True (same object)
print(f"a is c: {a is c}")    # False (different objects, even though values are equal)
print(f"a == c: {a == c}")    # True (values are equal)

x = 5
y = 5
print(f"x is y: {x is y}")    # True

# Demonstrating 'is not'
print(f"a is not c: {a is not c}")  # True
print(f"x is not y: {x is not y}")  # False