# class
# Classes in Python provides a way to bundle data and functionality together.
# A class is like a blueprint for creating objects (instances).
# Creating a new class means creating a new type. We can create multiple
# instances of that type.

# Python supports class inheritance, allowing a class (derived class) to inherit attributes
# and methods from one or more base classes. The derived class can override or extend the
# functionality of its base class by redefining methods.
# Normally, class members are (except for private variables using naming conventions) and all member 
# functions are virtual(i.e., can be overridden at runtime).
# There are no shorthands for referencing the object’s members from its methods: the method function is
# declared with an explicit first parameter 'self' representing the object, which is provided implicitly by the call.
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
# When a class definition is entered, a new namespace is created, and used as the local scope — thus, all
# assignments to local variables go into this new namespace.
# When a class definition is left normally (via the end), a class object is created. This is basically
# a wrapper around the contents of the namespace created by the class definition.
# The original local scope (the one in effect just before the class definition was entered) is reinstated,
# and the class object is bound here to the class name given in the class definition header.


"""
An attribute refers to any name that "belongs" to an object. When you use dot notation 
like my_object.something, you are accessing an attribute. This is called "attribute reference".

Attributes may be read-only or writable. In the latter case, assignment to attributes is possible. 
Module attributes are writable: you can write modname.the_answer = 42. Writable attributes may also be 
deleted with the del statement. For example, del modname.the_answer will remove the attribute the_answer 
from the object named by modname.


Class Objects:
Class objects support two kinds of operations: instantiation and attribute references.
1) Instantiation syntax: obj = ClassName()
   A new, unique instance object is created, and its __init__ method is called to initialize its state.
2) Attribute reference syntax: class_object.attr
   Here attr can be a value object(i.e., a data attribute) or function object(i.e., a non-data attribute).
   Here attr(be it value object or function object) defined inside the class definition.
   attr is stored in the class's __dict__. Valid attribute names are all the names that were in the class’s 
   namespace when the class object was created.
"""


class MyClass:
    """A simple example class"""

    i = 12345

    def f(self):
        return "hello world"


# Here valid attribute references are MyClass.i(returns an integer) and MyClass.f(returns a function object).
# Class attributes can also be assigned to, so we can change the value of MyClass.i by assignment or even
# replace MyClass.f with a new function.

# Instantiation syntax: obj = ClassName()
x = MyClass()
# Create a new instance of MyClass and assigns this object to the variable x.
# The instantiation operation (“calling” a class object) creates an empty object.
x1 = MyClass()
x2 = MyClass()


# Many classes like to create objects with instances customized to a specific initial state.
# This is done by defining a special method called __init__() in the class definition.
# The __init__() method is a constructor in Python, and it is automatically called when an instance of the class is created.
# The first parameter to __init__() is always self explicitly, which refers to the instance being created.
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


"""
Instance Objects:
Instance object only supports attribute reference.
Attribute reference syntax: instance_object.attr
Here attr can be a value object(i.e., a data attribute) or method object(i.e., a non-data attribute).

Data attributes need not be declared; they spring into existence when they are first assigned to,
typically via self inside the __init__ and are destroyed with the instance. They are stored in the 
instance's __dict__ i.e., each instance has its own copy of data attributes. These instnace attributes
represent state of an instance.

Method objects are functions that belong to an instance. They becomes bound to an instance when we access them.
When a non-data attribute of an instance is referenced, we call it a method reference. Hence, the 
instance’s class is searched. If the name denotes a valid class attribute that is a function object, 
references to both the instance object and the function object are packed into a method object. When 
the method object is called with an argument list, a new argument list is constructed, where the first 
argument is the instance object(self) followed by other arguments we passed and the function object is called 
with this new argument list.
Methods are used to access, modify, or perform actions using the state of an instance.

When we do an attribute reference from an instance,
1. The instance’s __dict__ is searched first. If found, the value is returned. This is typically where instance 
   data attributes are found.
2. If not found in the instance, the search continues to the class's __dict__ and then up the inheritance hierarchy 
   according to the Method Resolution Order (MRO).
   - If the attribute is found and it's a class data attribute, its shared value is returned.
   - If the attribute is found and it's a function, it creates a special bound method object as per the above process 
     and returns that.

We can access class attributes through an instance, but we cannot modify a class attribute through it. An assignment 
operation like instance.attr = value will always create or modify the attribute in the instance's __dict__, never the class's. 
If a class attribute with the same name exists, this new instance attribute will effectively shadow it for that specific instance.
But if the class data attribute is a mutable object like list or dictionary, any instance can modify it.

"""
print(x.f)  # <bound method MyClass.f of <__main__.MyClass object at 0x104d39be0>>
print(MyClass.f)  # <function MyClass.f at 0x104d044a0>
# x.f is a valid method reference, since MyClass.f is a function, but x.i is not, since MyClass.i is not.
# But x.f is not the same thing as MyClass.f — it is a method object, not a function object.

# We can call the method f in the following way,
res = x.f()
print(res)  # hello world

# Alternatively,
store = x.f
print(store())  # hello world

# x.f() is equivalent to MyClass.f(x)
# Here x is an instance of the class
print(MyClass.f(x))  # hello world
