# Wrong design: Using mutable objects as class variables
class Dog:

    tricks = []  # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog("Fido")
e = Dog("Buddy")

d.add_trick("roll over")
e.add_trick("play dead")

print(d.tricks)  # ['roll over', 'play dead'] # unexpectedly shared by all dogs

# Right design: Using instance variables for mutable objects
class Dog2:

    def __init__(self, name):
        self.name = name
        self.tricks = []  # correct: unique list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d2 = Dog2("Fido")
e2 = Dog2("Buddy")

d2.add_trick("roll over")
e2.add_trick("play dead")

print(d2.tricks)  # ['roll over']
print(e2.tricks)  # ['play dead']


