# Abstract Methods with Special Decorators (Properties, Static, Class)
# We can enforce that subclasses implement not just standard instance methods,
# but also specific data descriptors (@property) or method types (@classmethod, @staticmethod).

from abc import ABC, abstractmethod

class Shape(ABC):
    @property
    @abstractmethod
    def area(self) -> float:
        """Compute the shape’s area"""

    @classmethod
    @abstractmethod
    def description(cls) -> str:
        """Return a text description for this shape"""

    @staticmethod
    @abstractmethod
    def max_sides() -> int:
        """Return the maximum number of sides supported"""


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        return self.width * self.height

    @classmethod
    def description(cls) -> str:
        return "A rectangle is a quadrilateral with four right angles."

    @staticmethod
    def max_sides() -> int:
        return 4


r = Rectangle(2.3, 4.5)
print(r.area)
print(Rectangle.description())
print(Rectangle.max_sides)


# Multiple abstract base classes
class Flyable(ABC):
    @abstractmethod
    def fly(self) -> None: ...


class Swimmable(ABC):
    @abstractmethod
    def swim(self) -> None: ...


class Duck(Flyable, Swimmable):
    def fly(self) -> None:
        print("Duck is flying")

    def swim(self) -> None:
        print("Duck is swimming")


duck = Duck()
duck.fly()  # Duck is flying
duck.swim()  # Duck is swimming




# Abstract Methods with Default Implementation
class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        """Default logging implementation."""
        print(f"[LOG] {message}")


class FileLogger(Logger):
    def log(self, message: str) -> None:
        # Must call super() to use default implementation
        super().log(message)
        # Additional file logging logic
        with open("log.txt", "a") as f:
            f.write(f"{message}\n")


class ConsoleLogger(Logger):
    def log(self, message: str) -> None:
        # Override completely
        print(f">>> {message}")
