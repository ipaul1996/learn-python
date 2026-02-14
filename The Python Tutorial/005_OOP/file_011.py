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

# When a derived class is defined, Python stores its base class as part of its definition (derived class's `__bases__` attribute). Data attribute and method lookups on an instance of the derived class first search the derived class itself;
# if not found, Python automatically searches up the inheritance chain through the base classes.
# This process continues recursively if there are multiple levels of inheritance (as per MRO).


# A derived class can override methods defined in its base class.
# When a method in a base class calls another method via `self`, the call is not fixed to the base class's version.
# Instead, Python dynamically looks up the method on the actual object's class at runtime.
# This means a base class method might end up calling an overridden version from a derived class.
# This powerful feature is a core part of polymorphism, known as dynamic dispatch.
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
