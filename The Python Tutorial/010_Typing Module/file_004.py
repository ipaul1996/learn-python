# NewType: Creating Distinct Types for Static Analysis
#
# NewType is a special tool used to create distinct types from existing ones.
# Its purpose is to help static type checkers catch logical errors by adding
# semantic meaning to your types, without affecting runtime behavior.
# It's like putting different labels on identical jars of "salt" and "sugar"—the
# contents are the same, but the labels prevent you from mixing them up.


# The Problem: Lack of Semantic Distinction
# Imagine you have user IDs and order IDs. At runtime, both are just integers.
def process_user(uid: int) -> None:
    print(f"Processing user {uid}...")


def process_order(oid: int) -> None:
    print(f"Processing order {oid}...")


user_id = 123
order_id = 987

# This is a logical bug, but a static type checker won't see it
# because both `user_id` and `order_id` are just of type `int`.
process_user(order_id)  # Whoops!


# The Solution: Using NewType
# NewType creates unique types that are treated as distinct subtypes of the
# original by static type checkers. However, at runtime, they behave exactly
# like the original type. It is purely a static analysis tool with zero
# runtime overhead.

from typing import NewType

# Create distinct types for UserId and OrderId.
# The first argument is the new type's name, the second is the base type.
UserId = NewType("UserId", int)
OrderId = NewType("OrderId", int)


def process_user_v2(uid: UserId) -> None:
    print(f"Processing user {uid}...")


def process_order_v2(oid: OrderId) -> None:
    print(f"Processing order {oid}...")


# "Instantiate" the new types. At runtime, this just returns the integer.
user_id_v2 = UserId(123)
order_id_v2 = OrderId(987)

print(f"Value of user_id_v2: {user_id_v2}")
print(f"Runtime type of user_id_v2: {type(user_id_v2)}")
# Note: It's still just an int!

# This call is correct and passes the type check.
process_user_v2(user_id_v2)

# This call is a bug, and now a static type checker will raise an error!
# process_user_v2(order_id_v2)  # error: Expected type 'UserId', got 'OrderId' instead

"""
UserId Variable:
This is the alias or variable that you import and use to annotate your code. 
It holds the special "dummy" type that NewType creates.

UserId String:
This string is not used by your running Python code at all. Its sole purpose is to give 
a name to the new type that static type checkers (like Mypy) can use when they report errors. 
This ensures that the error messages are clear and human-readable.
"""
