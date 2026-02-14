# Use Case - 1: Factory Method
# Alternate constructors that create instances in different ways.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2025 - birth_year
        return cls(name, age)

    def __str__(self):
        return f"{self.name} is {self.age} years old"


p1 = Person("Tithi", 23)
print(p1)  # Tithi is 23 years old

p2 = Person.from_birth_year("IP", 1996)
print(p2)  # IP is 29 years old
