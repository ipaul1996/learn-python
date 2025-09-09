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


Reason:
A: C -> A -> X -> Y -> O
B: C -> B -> Y -> X -> O
# But C needs to merge these, and can't put both X before Y and Y before X at the same time.
# This means Python can't resolve the order in which to search for methods, so it raises an error.

"""
