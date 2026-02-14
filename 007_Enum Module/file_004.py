# Enum.__eq__(self, other) -> bool
# Defines equality comparison between enum members.
# - self: the enum member instance.
# - other: another enum member or value to compare.
# Compares by identity: returns True only when other is the same singleton member (self is other).
# For cross-type or unmatched values, returns False.


from enum import Enum


class Color(Enum):
    RED = 1
    BLUE = 2


# Compare by value/identity
print(Color.RED == Color(1))  # True
print(Color.RED == Color.BLUE)  # False
# # Behind the scenes, Enum.__eq__ checks for the same member identity:
# Color.RED is Color(1) evaluates to True because Color(1) returns the
# singleton RED member.

# Enum.__hash__(self) -> int
# Provides a hash code so enum members can be used in sets or as dict keys.
# self: the enum member instance.
# Returns a unique integer hash based on the enum’s identity.
# Consistent across program run for the same enum member.
# Ensures that hash(member1) == hash(member2) iff member1 is member2.


class Status(Enum):
    OK = 0
    ERROR = 1


# Use in dict or set
status_set = {Status.OK, Status.ERROR}
print(hash(Status.OK), Status.OK in status_set)  # 1678056344083980682 True
