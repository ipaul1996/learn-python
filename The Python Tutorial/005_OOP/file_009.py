# In Python, class blocks do not create a new enclosing scope for name resolution. The global scope of
# a function (including methods) is always the module in which it is defined, not the class it is contained within.
# This means that when a method references a name that is not local (not defined within the method itself, not a
# parameter, and not an instance or class attribute via self or cls), Python's LEGB (Local, Enclosing, Global, Built-in)
# rule looks for it in the module's global namespace.

PI = 3.14159  # module-level constant

class Circle:

    PI = 3.14

    def print_pi(self):
        print(PI)


c = Circle()
c.print_pi()  # 3.14159
print(c.PI)  # 3.14
print(Circle.PI)  # 3.14
