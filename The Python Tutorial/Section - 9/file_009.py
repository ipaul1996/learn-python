# When a method refers to a name that isn’t defined inside the method (or as a parameter or attribute),
# Python looks for it in the global namespace of the module where the method was defined.
# Classes do not introduce a new global scope. Even though methods live inside a class body,
# their global variables come from the enclosing module, not from the class.

import math  # imported into the module’s global scope

PI = 3.14159  # module-level constant


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # 'PI' and 'math' are looked up in the module, not on Circle!
        return PI * (self.radius**2)

    def circumference(self):
        # we can also use math.pi if we prefer
        return 2 * math.pi * self.radius
