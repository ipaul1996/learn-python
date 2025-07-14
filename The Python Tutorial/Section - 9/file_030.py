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
        self._protected_var = "I am protected (by convention)"
        self.__private_var = "I am private (name mangled)"

    def get_private(self):
        return self.__private_var


obj = MyClass()
print(obj.public_var)  # Accessible
print(obj._protected_var)  # Accessible, but discouraged
# print(obj.__private_var)  # AttributeError: 'MyClass' object has no attribute '__private_var'

# Accessing the name-mangled private variable directly (not recommended)
print(obj._MyClass__private_var)  # Accessible via name mangling

print(obj.get_private())  # Preferred way to access private data
