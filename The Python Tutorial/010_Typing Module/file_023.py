from typing import Callable, List, Any


def apply_to_list(data: List[int], func: Callable[[int], int]) -> List[int]:
    """Applies `func` to each element of `data`."""
    return [func(x) for x in data]


def square(x: int) -> int:
    return x * x


print(apply_to_list([1, 2, 3], square))  # [1, 4, 9]


any_call: Callable[..., Any]  # takes any args/kwargs, returns any
# The ... special form tells the checker “I’m not specifying the signature here.

no_args: Callable[[], str]  # returns a string, takes nothing


