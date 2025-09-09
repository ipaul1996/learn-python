from enum import Enum


# Custom Missing Handler
class Mood(Enum):
    HAPPY = 1
    SAD = 2
    UNKNOWN = 99

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


print(Mood(5))  # Mood.UNKNOWN

# Enum members are singletons: Color.RED is Color.RED is always True
print(Mood.HAPPY == Mood(1))  # True


# Default __str__ returns ClassName.MemberName.
# Default __repr__ shows <ClassName.MemberName: value>.
class FriendlyColor(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

    def __str__(self):
        return f"Color({self.name.lower()})"


print(str(FriendlyColor.BLUE))  # Color(blue)


# Enums can include methods and @property:
class Status(Enum):
    PENDING = 1
    RUNNING = 2
    COMPLETED = 3

    @property
    def is_done(self):
        return self is Status.COMPLETED

    def next(self):
        members = list(self.__class__)
        idx = members.index(self) + 1
        return members[idx] if idx < len(members) else None


print(Status.PENDING.is_done)  # False
print(Status.COMPLETED.is_done)  # True
print(Status.RUNNING.next())  # Status.COMPLETED
