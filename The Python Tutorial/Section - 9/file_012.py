# When you override a method in a derived class, sometimes you want to
# do everything the base class method does, plus add something extra.
# To do this, you can call the base class’s version of the method directly
# from your derived class method.
# You do this by writing:
# BaseClassName.methodname(self, arguments)
# This lets you run the base class’s code, then add your own code before or after it.


class Base:
    def greet(self):
        print("Hello from Base")


class Derived(Base):
    def greet(self):
        # Call the base class method first
        Base.greet(self)

        # Add extra behavior
        print("...and hello from Derived")


d = Derived()
d.greet()
# Output:
# Hello from Base
# ...and hello from Derived
