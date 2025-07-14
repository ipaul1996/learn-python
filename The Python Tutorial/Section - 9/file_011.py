"""
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
"""

# The base class name (BaseClassName) must be accessible in the current scope
# where the derived class is defined. You can also use any valid expression
# instead of a simple name for the base class. For example, if the base class
# is defined in another module, you can specify it like this:
"""
class DerivedClassName(module_name.BaseClassName):
"""

# When a derived class is defined, Python stores its base class as part of its definition.
# Attribute and method lookups on an instance of the derived class first search the derived class itself;
# if not found, Python automatically searches up the inheritance chain through the base classes.
# This process continues recursively if there are multiple levels of inheritance.


# Derived classes can override methods from their base classes.
# When a method in the base class calls another method (even one defined in the base class),
# it may actually call an overridden version in the derived class if it exists.
# This is because method calls are always resolved using the actual type of the object.
class Base:
    def greet(self):
        self.say_hello()

    def say_hello(self):
        print("Hello from Base")


class Derived(Base):
    def say_hello(self):
        print("Hello from Derived")


d = Derived()
d.greet()  # Hello from Derived

d1 = Base()
d1.greet()  # Hello from Base
