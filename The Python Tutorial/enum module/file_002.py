from enum import Enum, auto, unique


class Status(Enum):
    PENDING = auto()
    RUNNING = auto()
    COMPLETED = auto()


# auto() → generates an integer starting at 1 and increments automatically.

print([member.value for member in Status])  # [1, 2, 3]


@unique
class Direction(Enum):
    NORTH = 1
    WEST = 2
    SOUTH = 3
    EAST = 4

# @unique(enum_class) decorator ensures all values are distinct, raising ValueError otherwise.