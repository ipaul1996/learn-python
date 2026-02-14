# Use Case - 3:
# Polymorphic Constructors: In inheritance hierarchies,
# returning instances of the subclass that called the method.
class Animal:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, name):
        return cls(name)


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# Polymorphic constructor usage:
dog = Dog.create("Buddy")
cat = Cat.create("Whiskers")

print(dog.speak())  # Buddy says Woof!
print(cat.speak())  # Whiskers says Meow!
