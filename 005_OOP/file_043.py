# Abstract Base Classes (ABC)

# An Abstract Base Class (ABC) is a class that:
# - Cannot be instantiated directly - you cannot create instances of it
# - Defines a contract - specifies methods that subclasses must implement
# - May contain abstract methods - method declarations without implementation
# - May contain concrete methods - fully implemented methods that subclasses inherit

# ABCs enforce that all subclasses implement required methods. If a subclass does not
# implement all abstract methods, it too becomes abstract and cannot be instantiated.
# Python's abc module provides the infrastructure for defining ABCs.

from abc import ABC, abstractmethod

# ABC: Base class for defining abstract base classes
# abstractmethod: Decorator to mark methods as abstract


class Vehicle(ABC):
    """Abstract base class for all vehicles."""

    def __init__(self) -> None:
        self.is_running = False

    @abstractmethod
    def start(self):
        """Begin moving"""
        pass

    @abstractmethod
    def stop(self):
        """Cease movement"""
        pass

    @abstractmethod
    def get_speed(self) -> int:
        """Return current speed in km/h."""
        ...

    # Concrete method - inherited by all subclasses
    def status(self) -> str:
        return "Running" if self.is_running else "Stopped"


# ... --> It is called the Ellipsis object (a builtin singleton object). They act as a
# placeholder for code that will be implemented later. Alternatively, we can use pass.
# But ... is often used for abstract methods and pass is used for concrete methods, which
# intentionally does nothing.


class Car(Vehicle):
    def start(self):
        print("Car engine on")

    def stop(self):
        print("Car engine off")

    def get_speed(self):
        return 5


class Bike(Vehicle):
    def start(self):
        print("Bike engine on")


# vehicle = Vehicle()  # TypeError: Can't instantiate abstract class Vehicle without an implementation for abstract methods 'start', 'stop', 'get_speed'
# bike = Bike() # TypeError: Can't instantiate abstract class Bike without an implementation for abstract method 'stop'
car = Car()  # OK


print(isinstance(car, Vehicle))  # True
print(isinstance(car, Car))      # True
print(issubclass(Car, Vehicle))  # True
