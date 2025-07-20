from typing import NewType


def print_user(u: int) -> None:
    pass


def print_order(o: int) -> None:
    pass


user_id = 5
order_id = 678

print_user(order_id)  # bug
# Here static type checker won’t catch that mixing up two plain ints is wrong—because
# both parameters are just int.

# To resolve this issue we can use NewType

UserId = NewType("UserId", int)
OrderId = NewType("OrderId", int)

# NewType creates simple unique types with almost zero runtime overhead.
# NewType(name, tp) is considered a subtype of tp by static type checkers.
# At runtime, NewType(name, tp) returns a dummy callable that simply returns its argument.
# NewType is purely a static‐type aid.


def print_user_v2(u: UserId) -> None:
    pass


def print_order_v2(o: OrderId) -> None:
    pass


uid = UserId(5)
oid = OrderId(678)

print(uid)  # 5
print(type(uid))  # <class 'int'>

print_user_v2(uid)  # OK
# print_user_v2(oid) # Type-checker error!
