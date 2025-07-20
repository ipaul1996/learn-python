# Contravariant (contravariant=True)
# Allows a generic consumer type to accept supertypes.
# TypeVar("T_contra", contravariant=True)
# If Animal is a superclass of Dog, then Box[Animal] is compatible with Box[Dog].

from typing import TypeVar, Protocol


class Animal:
    def speak(self) -> str:
        return "Some generic animal sound"


class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"


T_contra = TypeVar("T_contra", contravariant=True)


class Consumer(Protocol[T_contra]):
    def consume(self, item: T_contra) -> None: ...


class AnimalFeeder:
    def consume(self, item: Animal) -> None:
        print(f"Feeding animal: {item.speak()}")


# Contravariance allows this assignment:
dog_feeder: Consumer[Dog] = AnimalFeeder()  # Allowed!

dog = Dog()
dog_feeder.consume(dog)  # Feeding animal: Woof!
