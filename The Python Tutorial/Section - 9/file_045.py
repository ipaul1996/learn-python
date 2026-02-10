# A Virtual Subclass is a class that is "registered" into an Abstract Base Class (ABC) 
# so that it passes isinstance() and issubclass() checks, even though it does not inherit from the ABC.
# - No Inheritance: The class does not share the ABC's Method Resolution Order (MRO).
# - No Enforcement (The "Pinky Promise"): Unlike standard inheritance, the ABC does not check 
#   if the registered class actually implements the abstract methods. It blindly trusts that you 
#   have implemented them.
# - Use Case: Useful when you need to treat a class you cannot modify (like a built-in list 
#   or a third-party class) as if it implements your specific interface.

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
