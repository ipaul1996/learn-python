# Covariant (covariant=True)
# Allows a generic type to accept subtypes.
# TypeVar("T_co", covariant=True)
# If Dog is a subclass of Animal, then Box[Dog] is compatible with Box[Animal].


from typing import Generic, TypeVar


class Animal:
    def speak(self) -> str:
        return "Some generic animal sound"


class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"


# Declare a covariant type variable
T_co = TypeVar("T_co", covariant=True)


class ReadOnlyBox(Generic[T_co]):
    def __init__(self, value: T_co) -> None:
        # Annotate the stored value
        self._value: T_co = value

    def get(self) -> T_co:
        # Returns the stored value (producer-only)
        return self._value


# Usage example
dog_box: ReadOnlyBox[Dog] = ReadOnlyBox(Dog())
# Covariance allows assigning a ReadOnlyBox[Dog] to ReadOnlyBox[Animal]
animal_box: ReadOnlyBox[Animal] = dog_box  # ✅

# Statically, type checker sees get() returns Animal
# At runtime, it's actually a Dog instance
pet: Animal = animal_box.get()
print(pet.speak())  # Woof!
# pet is treated as Animal but behaves like Dog at runtime
