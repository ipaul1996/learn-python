from enum import Enum


# Custom Missing Value Handler
# _missing_(cls, value) is a classmethod called when Enum(value) lookup fails.
# - cls: The enum class itself
# - value: The value that was not found in the enum
# - Returns: An enum member to use as default, or raises ValueError/LookupError
class Mood(Enum):
    """
    An enum with a custom missing handler that returns UNKNOWN for invalid values.

    Without _missing_, Mood(5) would raise ValueError.
    With _missing_, it returns Mood.UNKNOWN instead.
    """

    HAPPY = 1
    SAD = 2
    EXCITED = 3
    UNKNOWN = 99  # Fallback member

    @classmethod
    def _missing_(cls, value):
        """
        Called when Mood(value) doesn't match any defined member.

        Args:
            cls: The Mood enum class
            value: The value that was not found (e.g., 5)

        Returns:
            Mood.UNKNOWN for any invalid value
        """
        print(f"Warning: Value {value} not found, returning UNKNOWN")
        return cls.UNKNOWN


# Example usage:
print(Mood(1))  # Mood.HAPPY (valid value, normal lookup)
print(Mood(5))  # Mood.UNKNOWN (invalid value, _missing_ called)
print(Mood(999))  # Mood.UNKNOWN (invalid value, _missing_ called)

# Verify singleton behavior still works
print(Mood.HAPPY == Mood(1))  # True (same member)
print(Mood(5) is Mood.UNKNOWN)  # True (same singleton object)


# Alternative: Raising custom errors
class StrictColor(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

    @classmethod
    def _missing_(cls, value):
        """Provide helpful error message for invalid values."""
        valid_values = [member.value for member in cls]
        raise ValueError(
            f"Invalid color value: {value}. " f"Valid values are: {valid_values}"
        )


try:
    StrictColor(999)
except ValueError as e:
    print(f"Error: {e}")
    # Error: Invalid color value: 999. Valid values are: [1, 2, 3]


# Default __str__ returns ClassName.MemberName.
# Default __repr__ shows <ClassName.MemberName: value>.
# You can override __str__ and __repr__ for custom formatting.
class FriendlyColor(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

    def __str__(self):
        return f"Color({self.name.lower()})"

    def __repr__(self):
        """Custom repr representation: includes both name and value."""
        return f"<Color.{self.name}: {self.value}>"


print(str(FriendlyColor.BLUE))  # Color(blue) (custom __str__)
print(repr(FriendlyColor.BLUE))  # <Color.BLUE: 3> (custom __repr__)
print(f"Selected: {FriendlyColor.RED}")  # Selected: Color(red)


# Enums can have:
# - Instance methods: Operate on individual members
# - Class methods: Operate on the enum class
# - Properties: Computed attributes for each member
# - Static methods: Utility functions
class Status(Enum):
    """
    A workflow status enum with custom methods and properties.

    Demonstrates:
    - @property for computed attributes
    - Instance methods for state transitions
    - Accessing all members via __class__
    """

    PENDING = 1
    RUNNING = 2
    COMPLETED = 3
    FAILED = 4

    @property
    def is_done(self):
        """Check if the status represents a finished state."""
        return self in (Status.COMPLETED, Status.FAILED)

    @property
    def is_active(self):
        """Check if the status represents an ongoing state."""
        return self in (Status.PENDING, Status.RUNNING)

    def next(self):
        """
        Get the next status in the workflow.

        Returns:
            Next Status member, or None if this is the last status.
        """
        members = list(self.__class__)  # Get all Status members
        idx = members.index(self) + 1  # Find next index
        return members[idx] if idx < len(members) else None

    def can_transition_to(self, other):
        """Check if transition to another status is valid."""
        valid_transitions = {
            Status.PENDING: [Status.RUNNING, Status.FAILED],
            Status.RUNNING: [Status.COMPLETED, Status.FAILED],
            Status.COMPLETED: [],  # Terminal state
            Status.FAILED: [],  # Terminal state
        }
        return other in valid_transitions.get(self, [])


print(Status.PENDING.is_done)  # False (not finished)
print(Status.COMPLETED.is_done)  # True (finished)
print(Status.RUNNING.is_active)  # True (ongoing)
print(Status.FAILED.is_active)  # False (finished, not active)

current = Status.PENDING
print(f"Current: {current}")  # Current: Status.PENDING
next_status = current.next()
print(f"Next: {next_status}")  # Next: Status.RUNNING

print(Status.PENDING.can_transition_to(Status.RUNNING))  # True
print(Status.COMPLETED.can_transition_to(Status.RUNNING))  # False


def process_task(current_status: Status):
    """Simulate task processing with status transitions."""
    print(f"Current status: {current_status}")

    if current_status.is_done:
        print("Task already finished!")
        return current_status

    next_status = current_status.next()
    if next_status and current_status.can_transition_to(next_status):
        print(f"Transitioning to: {next_status}")
        return next_status
    else:
        print("No valid transition available")
        return current_status


result = process_task(Status.PENDING)
# Current status: Status.PENDING
# Transitioning to: Status.RUNNING
