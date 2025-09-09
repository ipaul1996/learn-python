class Dog:

    kind = "canine"  # class data attributes shared by all instances

    def __init__(self, name):
        self.name = name  # instance data attributes are unique to each instance


d = Dog("Fido")
e = Dog("Buddy")

print(d.kind)  # shared by all dogs
print(e.kind)  # shared by all dogs

print(d.name)  # unique to d
print(e.name)  # unique to e


