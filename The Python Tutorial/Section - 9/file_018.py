class O:
    pass


class X(O):
    pass


class Y(O):
    pass


class A(X, Y):
    pass  # demands X before Y


class B(Y, X):
    pass  # demands Y before X

"""
class C(A, B):
    pass
    
TypeError: Cannot create a consistent method resolution order (MRO) for bases X, Y
"""
