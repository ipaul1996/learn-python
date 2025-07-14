class O:
    pass


class A(O):
    pass


class B(O):
    pass


class D(A, B):
    pass


print(
    D.__mro__
)  # (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.O'>, <class 'object'>)

"""
      object
        |
------- O ------
A               B
        D
"""
