# Python has no strict access control (no 'private' or 'protected' keywords).
# Nothing prevents clients from modifying attributes directly; data hiding is
# entirely based on convention and programmer discipline. 

# Weak Internal Use Indicator (_): A single leading underscore (e.g., _variable) is a semantic signal to
# other programmers that an attribute is an implementation detail and part of the non-public API.
# The interpreter does not enforce this.

# Name Mangling for Collision Avoidance (__): A double leading underscore (e.g., __variable) triggers
# "name mangling". The interpreter textually replaces this with _ClassName__variable to prevent
# namespace collisions in subclasses. It makes access harder (you must use
# the mangled name), but it does not make the data truly private.


class MyClass:
    def __init__(self):
        self.public_var = "I am public"
        self._internal_var = "I am for internal use (by convention)"
        self.__mangled_var = "I am name-mangled to avoid conflicts"

    def get_mangled(self):
        """A public method to provide controlled access to the mangled variable."""
        return self.__mangled_var


obj = MyClass()

# Public attributes are meant for direct access.
print(obj.public_var)  # Accessible

# Internal-use attributes are accessible, but it's a violation of convention.
print(obj._internal_var)

# Direct access to a name-mangled attribute will fail with an AttributeError.
try:
    print(obj.__mangled_var)
except AttributeError as e:
    print(f"\nAttempting to access obj.__mangled_var failed:")
    print(f" -> {e}")

# You can still access the mangled variable if you know the mangled name. (Discouraged)
print("\nAccessing the mangled name directly (not recommended):")
print(obj._MyClass__mangled_var)  # type: ignore

# The preferred approach is to use a public method if access is needed.
print("\nAccessing via a public getter method:")
print(obj.get_mangled())
