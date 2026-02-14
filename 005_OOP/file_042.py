# Method Overriding
# When a subclass defines a method with the same name as one in its superclass,
# it overrides that inherited behavior with its own implementation. At runtime,
# Python uses dynamic dispatch so that calls on subclass instances invoke the
# subclass’s version, not the parent’s. This lets subclasses tailor or extend
# base-class functionality while preserving a common interface, enabling flexible,
# polymorphic designs.
class Animal:
    def speak(self):
        print("Some generic sound")


class Dog(Animal):
    def speak(self):  # override
        print("Woof!")


class Cat(Animal):
    def speak(self):  # override
        print("Meow!")


for creature in (Animal(), Dog(), Cat()):
    creature.speak()
# Output:
# Some generic sound
# Woof!
# Meow!


# Python does not support true overloading by signature. If you write two methods
# with the same name in a class, the latter definition replaces the former.
class MathOps:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):  # This replaces the previous add!
        return x + y + z


m = MathOps()
# m.add(2, 3)       # TypeError: missing argument z
print(m.add(2, 3, 4))  # 9
