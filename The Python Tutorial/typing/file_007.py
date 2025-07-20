from typing import Generic, TypeVar

T = TypeVar("T")
S = TypeVar("S", bound=str)  # S must be a str or subclass


class LabeledBox(Generic[T, S]):
    def __init__(self, value: T, label: S):
        self.value = value
        self.label = label

    def describe(self) -> str:
        return f"{self.label}: {self.value}"


# Usage:
int_labeled_box = LabeledBox[int, str](42, "Answer")
float_labeled_box = LabeledBox[float, str](3.14, "Pi")

print(int_labeled_box.describe())  # Output: Answer: 42
print(float_labeled_box.describe())  # Output: Pi: 3.14

# The following would raise a type checker error:
# bad_box = LabeledBox[int, int](99, 100)
