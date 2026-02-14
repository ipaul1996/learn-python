# @staticmethod
# A decorator (@staticmethod) that turns a method into a plain
# function stored in a class’s namespace. It neither receives the
# instance (self) nor the class (cls) automatically.
class MathHelpers:

    @staticmethod
    def multiply(a, b):
        return a * b


r1 = MathHelpers.multiply(3, 4)
print(r1)

helper = MathHelpers()
r2 = helper.multiply(3, 4)
print(r2)
