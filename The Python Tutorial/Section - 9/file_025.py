# Letting @total_ordering fill in the rest

from functools import total_ordering


@total_ordering
class Version3:
    def __init__(self, major, minor):
        self.major, self.minor = major, minor

    def __eq__(self, other):
        if not isinstance(other, Version3):
            return NotImplemented
        return (self.major, self.minor) == (other.major, other.minor)

    def __lt__(self, other):
        if not isinstance(other, Version3):
            return NotImplemented
        return (self.major, self.minor) < (other.major, other.minor)


v1, v2 = Version3(1, 2), Version3(1, 3)
print(v1 < v2)  # True
print(v1 <= v2)  # True (auto-generated)
print(v1 == v2)  # False
print(v1 != v2)  # True (uses __eq__)
print(v1 > v2)  # False (auto-generated)
print(v1 >= v2)  # False (auto-generated)
