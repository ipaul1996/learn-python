# Enum Equality and Hashing
# ==========================

# Enum members support equality comparison and hashing, which allows them to be:
# - Compared with other enum members
# - Used as dictionary keys
# - Stored in sets
# - Used in hash-based collections


# Enum.__eq__(self, other) -> bool
# Defines equality comparison between enum members.

# Key behaviors:
# - Compares by identity (singleton pattern): returns True only if both refer to the same member
# - Returns False for different enum members, even with same value
# - Returns False when comparing with non-enum values (including raw values)
# Important: Enum members are singletons - only one instance exists per member


from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 2  # Note: Same value as GREEN (creates an alias)


# Example 1: Comparing enum members by identity
print(Color.RED == Color.RED)  # True (same member, same object)
print(Color.RED is Color.RED)  # True (identity check confirms it's the same object)

# Example 2: Comparing different members
print(Color.RED == Color.GREEN)  # False (different members)
print(Color.RED is Color.GREEN)  # False

# Example 3: Accessing by value returns the same singleton
print(Color.RED == Color(1))  # True
print(Color.RED is Color(1))  # True (Color(1) returns the same RED member)
# Behind the scenes: Color(1) looks up the member with value 1, which is Color.RED
# Since enum members are singletons, it returns the exact same object


# Example 4: Comparing with raw values
print(Color.RED == 1)  # False! (enum member != its raw value)
print(Color.RED.value == 1)  # True (explicit value comparison works)
# This is a key difference from mixed-type enums (str/int Enum)


# Example 5: Alias behavior (members with same value)
print(Color.GREEN == Color.BLUE)  # True! (BLUE is an alias of GREEN)
print(Color.GREEN is Color.BLUE)  # True (aliases are the same object)
print(Color.BLUE)  # Color.GREEN (canonical name always shown)
# When values are duplicated, the first member is canonical, others are aliases


# Example 6: Enum members from different enums are never equal
class Priority(Enum):
    HIGH = 1
    LOW = 2


print(Color.RED == Priority.HIGH)  # False (different enum types)
# Even though both have value 1, they're different enum instances


# Enum.__hash__(self) -> int
# Provides a hash code so enum members can be used in hash-based collections.

# Key behaviors:
# - Returns a unique integer hash based on the member's identity
# - Hash is consistent: hash(member) always returns the same value
# - Guarantees: hash(m1) == hash(m2) if and only if m1 is m2
# - Allows enum members to be used as dict keys or in sets
# - Hash is based on id(), not on .value


class Status(Enum):
    PENDING = 0
    APPROVED = 1
    REJECTED = 2


# Example 1: Hashing enum members
print(hash(Status.PENDING))  # e.g., 8775520955344
print(hash(Status.APPROVED))  # e.g., 8775520955408 (different hash)

# Hash is consistent for the same member
hash1 = hash(Status.PENDING)
hash2 = hash(Status.PENDING)
print(hash1 == hash2)  # True (same member always has same hash)


# Example 2: Using enum members in a set
status_set = {Status.PENDING, Status.APPROVED, Status.REJECTED}
print(Status.PENDING in status_set)  # True
print(len(status_set))  # 3

# Adding duplicate members doesn't increase size (same hash)
status_set.add(Status.PENDING)
print(len(status_set))  # Still 3 (PENDING already in set)


# Example 3: Using enum members as dictionary keys
status_messages = {
    Status.PENDING: "Waiting for review",
    Status.APPROVED: "Request approved",
    Status.REJECTED: "Request denied",
}

print(status_messages[Status.APPROVED])  # "Request approved"

# Lookup by value returns the same member (same hash)
print(status_messages[Status(1)])  # "Request approved" (Status(1) is Status.APPROVED)


# Example 4: Hash is based on identity, not value
class Color2(Enum):
    RED = 1
    BLUE = 1  # Alias with same value


# Both have the same value, but hash is based on identity
# Since BLUE is an alias of RED, they have the same hash
print(hash(Color2.RED) == hash(Color2.BLUE))  # True (same object)
print(Color2.RED is Color2.BLUE)  # True (aliases are identical)


# Example 5: Comparing hashes across different enums
class Priority2(Enum):
    HIGH = 0
    LOW = 1


# Different enum types, different objects, different hashes
print(hash(Status.PENDING) == hash(Priority2.HIGH))  # False (probably)
# Even though both have value 0, they're different objects


# Example 6: Hash consistency with equality
# Fundamental Python rule: if a == b, then hash(a) must equal hash(b)
member1 = Status.PENDING
member2 = Status(0)  # Same as PENDING

print(member1 == member2)  # True (same member)
print(hash(member1) == hash(member2))  # True (required by Python)
print(member1 is member2)  # True (singleton - same object)
