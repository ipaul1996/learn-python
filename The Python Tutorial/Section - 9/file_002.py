# class
# 1. Purpose: Bundling
# - Classes allow you to group Data (attributes/state) and Functionality (methods/behavior)
#   into a single unit.
# - This keeps related logic together (Encapsulation).

# 2. The "Type" Concept
# - A Class is a "Blueprint": It defines the structure.
# - An Object is an "Instance": It is the actual house built from that blueprint.
# - Creating a new class effectively creates a new custom Data Type in Python
#   (just like 'int' or 'str', but defined by you).


# 3. Inheritance
# - A class (Derived/Child) can inherit attributes and methods from another class (Base/Parent) or multiple classes.
# - Syntax: class Child(Parent): ..., Child(Parent1, Parent2): ...

# 4. Overriding Methods
# - In Python, all the methods of the parent class can be overridden by the child class at the runtime.
# - Python always calls the most specific version of the method at runtime (Dynamic Dispatch).

# 5. Member Access (Privacy)
# - Python enforces privacy via convention rather than strict access control. Thus it does not have strict 'private' or 'protected' keywords like Java.
#   - _variable (single underscore): "Treat this as private/internal."
#   - __variable (double underscore): Name mangling (harder to access, but not impossible).

# 6. There are no shorthands for referencing the object’s members from its methods: the method function is
# declared with an explicit first parameter 'self' representing the object, which is provided implicitly by python
# during the call.


# CLASS DEFINITION LIFECYCLE (Execution)
"""
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
"""

# STEP 1: EXECUTION START
# - A class definition is an executable statement, not just a declaration.
# - It must be "run" by the interpreter to exist.
# - This means you can put classes inside 'if' blocks or functions to create them dynamically.

# STEP 2: NAMESPACE CREATION
# - When Python enters 'class Name:', it creates a new empty namespace (dictionary).
# - This acts as the Local Scope for the code inside the class body.
# - Any assignment (x = 1) or function definition (def foo...) is stored in this namespace.

# STEP 3: CLASS OBJECT CREATION
# - When the class body finishes executing:
#   1. Python takes the populated namespace.
#   2. It creates a "Class Object" (the type itself).
#   3. It wraps the namespace inside this Class Object (accessible via __dict__).

# STEP 4: BINDING
# - The original scope (outside the class) is reinstated.
# - This object is assigned (bound) to the identifier 'ClassName' in the
#   current enclosing scope (local or global).


"""
An attribute refers to any name that "belongs" to an object. When you use dot notation 
like my_object.something, you are accessing an attribute. This is called "attribute reference".

Attributes may be read-only or writable. In the latter case, assignment to attributes is possible. 
Module attributes are writable: you can write modname.the_answer = 42. Writable attributes may also be 
deleted with the del statement. For example, del modname.the_answer will remove the attribute the_answer 
from the object named by modname.


Class objects support two kinds of operations: instantiation and attribute references.
1) Instantiation syntax: obj = ClassName()
   A new, unique instance object is created, and its __init__ method is called to initialize its state.
2) Attribute reference syntax: class_object.attr
   Here attr can be a value object(i.e., a data attribute) or function object(i.e., a non-data attribute).
   Here attr(be it value object or function object) defined inside the class definition.

   Initially: Valid attribute names are those defined in the class body 
   (stored in the class's __dict__ upon creation).
   Post-Creation: You can ASSIGN new attributes to the class object at any time.
   Example: MyClass.new_var = 100 adds 'new_var' to the class namespace.
   You can also modify or delete existing attributes.
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

Data attributes represent the unique state of a specific instance. They spring into existence when 
they are first assigned to.
- Typically assigned inside __init__() using 'self' during instantiation.
  Example: self.name = "Alice" creates the 'name' attribute when the instance is born.
- Can be created in any instance method at any point during the object's lifetime.
  Example: A method might do self.new_attr = value only when certain conditions are met.
- From Outside the Class: Can be added to an instance from external code at any time.
  Example: obj.dynamic_attr = 42 creates a new attribute on that specific instance on-the-fly.
Each instance maintains its own __dict__, so dynamically added attributes
belong only to that specific instance and do not affect other instances or the class itself.


Method objects are runtime wrappers that bind a generic function to a specific instance. This 
binding occurs dynamically at the moment you access the attribute. When you reference a non-data 
attribute on an instance (e.g., obj.method), Python searches the instance’s class. If the attribute 
found is a function object, Python does not return it directly. Instead, it packages both the instance 
object and the function object together into a new bound method object. When you invoke this method 
object, it acts as an adapter. It constructs a final argument list by inserting the bound instance 
(as self) at the very beginning, followed by any arguments you provided. It then executes the underlying 
function using this complete argument list.

class Handler:
    def process(self, data):
        return f"Processed {data}"


obj = Handler()
method_obj = obj.process

print(method_obj)           # <bound method Handler.process of <__main__.Handler object at 0x10326e120>>
print(method_obj.__self__)  # <__main__.Handler object at 0x10326e120>
print(method_obj.__func__)  # <function Handler.process at 0x103287480>
# When you call: method_obj("data")
# Python executes: method_obj.__func__(method_obj.__self__, "data")

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

# We can call the method f in the following way,
res = x.f()
print(res)  # hello world

# Alternatively,
store = x.f
print(store())  # hello world

# x.f() is equivalent to MyClass.f(x)
# Here x is an instance of the class
print(MyClass.f(x))  # hello world
