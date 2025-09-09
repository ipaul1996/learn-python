from functools import total_ordering


class Version:
    def __init__(self, major, minor):
        self.major = major
        self.minor = minor

    def __eq__(self, other):
        if not isinstance(other, Version):
            return NotImplemented

        return (self.major, self.minor) == (other.major, other.minor)

    def __lt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented

        return (self.major, self.minor) < (other.major, other.minor)

    def __le__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self < other or self == other


v1 = Version(1, 2)
v2 = Version(2, 3)

print(v1 == v2)  # False
print(v1 < v2)  # True
print(v1 > v2)  # False

print(v1 <= v2)
