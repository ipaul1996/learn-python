from typing import Callable

# A Callable type in the typing module describes any object you can “call”
# (like a function or an object implementing __call__).

# A callable that takes two ints and returns a float
f: Callable[[int, int], float]


"""
Syntax Breakdown:

Callable[[Arg1Type, Arg2Type, …], ReturnType]

- The outer Callable[...] tells the type checker “this is something you can call.”
- The first argument, a list of types [Arg1Type, Arg2Type, …], specifies the positional parameters 
the callable expects (in order). Use an empty list [] if it takes no positional arguments.
- The second argument, ReturnType, is the type the callable returns.
- There is no place here to annotate *args/**kwargs — for that you’d use ParamSpec or Protocol.

"""

# Declare a variable that can hold any function taking two ints and returning an int
adder: Callable[[int, int], int]


def add(a: int, b: int) -> int:
    return a + b


def mul(a: int, b: int) -> int:
    return a * b


adder = add
print(adder(2, 3))  # 5

adder = mul
print(adder(2, 3))  # 6
