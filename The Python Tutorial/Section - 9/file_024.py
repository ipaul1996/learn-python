from file_023 import Version


class Version2(Version):
    def __le__(self, other):
        if not isinstance(other, Version2):
            return NotImplemented
        return self < other or self == other

    def __ne__(self, other):
        # Python 3 would use not __eq__, but we can define it explicitly
        if not isinstance(other, Version2):
            return NotImplemented
        return not self == other


v1, v2 = Version2(1, 2), Version2(1, 3)

print(v1 <= v2)  # True
print(v1 != v2)  # True
print(v1 >= v2)  # False, falls back to __le__
