O = object
# Base class of the class hierarchy, super-most class.

# Why an MRO(Method Resolution Order) at all?
# When you do c.method(), Python must know exactly where to look first, second, third… so that:
# - You never revisit the same class twice (no infinite loops).
# - You honor each class’s declared precedence.
# - You get one single, unambiguous chain of “who-to-check-next.”

# In single inheritance this is trivial—you walk up the chain. But as soon as you have multiple bases,
# you must merge several chains together without ever contradicting any of them. That’s where C3 linearization
# comes in, enforcing three core rules all at once:

# 1. Class precedence rule (“children before parents”): In the MRO list of C, you will always see C itself before
# any of the classes it directly inherits from. When you call c.foo(), Python starts by looking in C itself.
# Only if it doesn’t find foo there will it move on to its bases.


# 2. Local precedence ordering (“direct bases keep your order”): If you declare class C(A, B):,
# then in C.__mro__ A must come before B. You, the programmer,
# explicitly said “C extends A then B.” Python must honor the order you wrote.


# 3. Monotonicity (“never break ancestor chains”): If in any base’s own MRO you see X before Y,
# then in the final MRO for C, X must still come before Y.

# Together, these three properties ensure a single, unambiguous search path for method/attribute 
# lookup, and when they can’t all be satisfied the C3 merge fails with a TypeError: Cannot create 
# a consistent method resolution order (MRO) for bases….


class A:
    pass


class B(A):
    pass


print(B.__mro__)  # (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)


class X:
    pass


class Y:
    pass


class C(X, Y):
    pass


print(
    C.__mro__
)  # (<class '__main__.C'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>)
