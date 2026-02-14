# The `operator` module provides function equivalents for many built-in Python operators.
# These functions allow you to use operators (such as arithmetic, comparison, logical, and sequence operations) 
# as first-class callable objects. This is especially useful for functional programming, sorting, mapping, and 
# when passing operators as arguments to higher-order functions.

"""
- Arithmetic Operators:
  - `add(a, b)` – Addition (`a + b`)
  - `sub(a, b)` – Subtraction (`a - b`)
  - `mul(a, b)` – Multiplication (`a * b`)
  - `truediv(a, b)` – Division (`a / b`)
  - `floordiv(a, b)` – Floor division (`a // b`)
  - `mod(a, b)` – Modulo (`a % b`)
  - `pow(a, b)` – Power (`a ** b`)
  - `neg(a)` – Negation (`-a`)
  - `pos(a)` – Unary plus (`+a`)
  - `abs(a)` – Absolute value (`abs(a)`)

- Comparison Operators:
  - `eq(a, b)` – Equal (`a == b`)
  - `ne(a, b)` – Not equal (`a != b`)
  - `lt(a, b)` – Less than (`a < b`)
  - `le(a, b)` – Less than or equal (`a <= b`)
  - `gt(a, b)` – Greater than (`a > b`)
  - `ge(a, b)` – Greater than or equal (`a >= b`)

- Logical/Bitwise Operators:
  - `and_(a, b)` – Logical AND (`a and b`)
  - `or_(a, b)` – Logical OR (`a or b`)
  - `not_(a)` – Logical NOT (`not a`)
  - `xor(a, b)` – Bitwise XOR (`a ^ b`)
  - `invert(a)` – Bitwise inversion (`~a`)
  - `lshift(a, b)` – Left shift (`a << b`)
  - `rshift(a, b)` – Right shift (`a >> b`)

- Sequence and Object Operators:
  - `getitem(obj, key)` – Get item (`obj[key]`)
  - `setitem(obj, key, value)` – Set item (`obj[key] = value`)
  - `delitem(obj, key)` – Delete item (`del obj[key]`)
  - `contains(obj, item)` – Membership test (`item in obj`)
  - `length_hint(obj)` – Estimate length

- Attribute and Method Operators:
  - `attrgetter(attr)` – Get attribute
  - `itemgetter(item)` – Get item
  - `methodcaller(name, ...)` – Call method by name

These are the most commonly used functions in the

"""

import operator

result = operator.add(2, 3)  # 5
difference = operator.sub(10, 4)  # 6
product = operator.mul(5, 3)  # 15
quotient = operator.truediv(8, 2)  # 4.0
remainder = operator.mod(9, 4)  # 1
power = operator.pow(2, 5)  # 32


is_equal = operator.eq("a", "b")
is_greater = operator.gt(7, 3)  # True
is_less_or_equal = operator.le(2, 2)  # True


my_list = [10, 20, 30]
item = operator.getitem(my_list, 1)  # 20
operator.setitem(my_list, 1, 99)  # my_list becomes [10, 99, 30]
contains_item = operator.contains(my_list, 99)  # True


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"


p = Person("Alice")
get_name = operator.attrgetter("name")
name = get_name(p)  # "Alice"

call_greet = operator.methodcaller("greet")
greeting = call_greet(p)  
