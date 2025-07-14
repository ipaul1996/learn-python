# A virtual subclass in Python is a class that is registered as a subclass
# of an Abstract Base Class (ABC) without actually inheriting from it.
# The ABC does not enforce that the registered class actually implements the abstract methods.
# It is up to the developer to ensure this.

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class MyDuck:
    def start(self):
        pass

    def stop(self):
        pass


Vehicle.register(MyDuck)

print(isinstance(MyDuck(), Vehicle))  # True
print(issubclass(MyDuck, Vehicle))  # True
