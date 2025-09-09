# Private Variables

# Single underscore (_var):
# A single underscore before a variable name (e.g., _my_var) is a convention to indicate
# that it is intended for internal use only. It is not enforced by Python, so it can still
# be accessed from outside the class.

# Double underscore (__var):
# A double underscore before a variable name (e.g., __my_var) triggers name mangling.
# Python changes the name of the variable internally to _ClassName__my_var, making it harder
# (but not impossible) to access from outside the class.


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
