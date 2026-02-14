# In Python, data hiding is based on convention rather than strict enforcement.
# All attributes are accessible and modifiable from outside the class.
# Programmers use naming conventions (like a leading underscore) to indicate
# that certain attributes are intended for internal use only.
# However, these are not enforced by the language, so it's the developer's
# responsibility to respect these conventions. Additionally, new attributes
# can be added to objects at runtime unless explicitly prevented.

class MyClass:
    def __init__(self, value):
        self.value = value  # public attribute


obj = MyClass(10)
print(obj.value)  # Accessing attribute from outside (allowed)

obj.value = 20  # Modifying attribute from outside (allowed)
print(obj.value)

obj.new_attr = 99  # type: ignore # Adding a new attribute from outside (allowed)
print(obj.new_attr)  # type: ignore
