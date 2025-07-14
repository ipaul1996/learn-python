# class
# Classes in Python provides a way to bundle data and functionality together.
# A class is like a blueprint for creating objects (instances).
# Creating a new class means creating a new type. We can create multiple
# instances of that type.

# Each class instance can have attributes attached to it for maintaining its state.
# Class instances can also have methods (defined by its class) for modifying its state.
# Methods define behaviors that the object will show, while attributes store data within class instances.
# Instance attributes are unique to each object(state of the object), while class attributes are shared
# across all instances of the class.
# Attributes and methods are collectively referred to as members of a class or object.

# Python supports class inheritance, allowing a class (derived class) to inherit attributes
# and methods from one or more base classes. The derived class can override or extend the
# functionality of its base class by redefining methods.
# Normally, class members are public and all member functions are virtual(i.e., can be overridden at runtime).
# there are no shorthands for referencing the object’s members from its methods: the method function is
# declared with an explicit first argument representing the object, which is provided implicitly by the call.
"""
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
"""
# Class definitions, like function definitions must be executed before they have any effect.
# We can place a class definition in a branch of an if statement, or inside a function.
# In general, the statements inside a class definition are function definitions.
# When a class definition is entered, a new namespace is created, and used as the local scope — thus, all
# assignments to local variables go into this new namespace.
# When a class definition is left normally (via the end), a class object is created. This is basically
# a wrapper around the contents of the namespace created by the class definition;
# The original local scope (the one in effect just before the class definition was entered) is reinstated,
# and the class object is bound here to the class name given in the class definition header.


# Class objects support two kinds of operations: attribute references and instantiation.
# Attribute reference syntax: obj.attrName
# Valid attribute names are all the names that were in the class’s namespace when the class object was created.
class MyClass:
    """A simple example class"""

    i = 12345

    def f(self):
        return "hello world"


# Here valid attribute references are MyClass.i(returns an integer) and MyClass.f(returns a function object).
# Class attributes can also be assigned to, so you can change the value of MyClass.i by assignment.
# Class attributes can also be assigned to, so we can change the value of MyClass.i or even replace MyClass.f with a new function.

# Instantiation syntax: obj = ClassName()
x = MyClass()
# Create a new instance of MyClass and assigns this object to the local variable x.
# The instantiation operation (“calling” a class object) creates an empty object.
x1 = MyClass()
x2 = MyClass()


# Many classes like to create objects with instances customized to a specific initial state.
# This is done by defining a special method called __init__() in the class definition.
# The __init__() method is a constructor in Python, and it is automatically called when an instance of the class is created.
# The first argument to __init__() is always self explicitly, which refers to the instance being created.
# The __init__() method can have additional parameters to initialize the instance's attributes.
class ComplexNumber:
    """A class to represent complex numbers."""

    def __init__(self, real=0.0, imag=0.0):
        """Initialize the complex number with real and imaginary parts."""
        self.real = real
        self.imag = imag


# Creating an instance of ComplexNumber
c1 = ComplexNumber(3, 4)  # Creates a complex number 3+4i
c2 = ComplexNumber()  # Creates a complex number 0+0i (default values)
# Accessing attributes of the instance
print(f"c1: {c1.real} + {c1.imag}i")
print(f"c2: {c2.real} + {c2.imag}i")


# The only operations understood by instance objects are attribute references.
# There are two kinds of valid instance attribute names: data attributes and methods.
# Data attributes need not be declared; like local variables, they spring into existence when they are first assigned to.
# The other kind of attribute is a method, which is a function that belongs to an object.
# All attributes of a class that are function objects define corresponding methods of its instances.
# So, x.f is a valid method reference, since MyClass.f is a function, but x.i is not, since MyClass.i is not.
# But x.f is not the same thing as MyClass.f — it is a method object, not a function object.
print(x.f)  # <bound method MyClass.f of <__main__.MyClass object at 0x104d39be0>>
print(MyClass.f)  # <function MyClass.f at 0x104d044a0>

# We can call the method f in the following way,
res = x.f()
print(res)  # hello world

# Alternatively,
store = x.f
print(store())  # hello world

# x.f() is equivalent to MyClass.f(x)
print(MyClass.f(x))  # hello world

# In general, calling a method with a list of n arguments is equivalent to calling the corresponding
# function with an argument list that is created by inserting the method’s instance object before the first argument.

# How method works?
# When a non-data attribute of an instance is referenced, the instance’s class is searched.
# If the name denotes a valid class attribute that is a function object, references to both the
# instance object and the function object are packed into a method object. When the method object
# is called with an argument list, a new argument list is constructed from the instance object
# and the argument list, and the function object is called with this new argument list.



