# We an require that subclasses implement not only instance methods,
# but also properties, classmethods, or staticmethods.

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
