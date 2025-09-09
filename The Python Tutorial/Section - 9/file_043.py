# Abstract Base Classes
# It is a concept from the abc module.
# Classes that can’t be instantiated directly and may include one
# or more @abstractmethod declarations—methods without implementation.
# They are intended to be used as base classes for other classes.
# They enforce that all subclasses implement the required methods.
# If a subclass does not implement all abstract methods, it too becomes
# abstract and cannot be instantiated.
# ABCs can provide concrete (fully implemented) methods as well as abstract ones.

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        """Begin moving"""

    @abstractmethod
    def stop(self):
        """Cease movement"""

    @abstractmethod
    def hello(self): ...


# ... --> It is called the Ellipsis object. They act as a placeholder for code
# that will be implemented later. Alternatively, we can use pass. But ... is often
# used for abstract methods


class Car(Vehicle):
    def start(self):
        print("Car engine on")

    def stop(self):
        print("Car engine off")

    def hello(self):
        print("Hello World!")


class Bike(Vehicle):
    def start(self):
        print("Bike engine on")


# v = Vehicle()  # TypeError: Can't instantiate abstract class Vehicle without an implementation for abstract methods 'start', 'stop'
# b = Bike() # TypeError: Can't instantiate abstract class Bike without an implementation for abstract method 'stop'
c = Car()  # OK
