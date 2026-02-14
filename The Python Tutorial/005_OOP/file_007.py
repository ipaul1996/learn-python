# A function object defined externally can be assigned to a class attribute.
# When accessed via an instance, it will behave as a method. Here the first
# paramter of the function must accept an instance.
def f1(self, x, y):
    return min(x, x + y)


class C:
    # Assign external function f1 to the class attribute f
    f = f1

    def g(self):
        return "hello world"

    # Assign function g to another class attribute within the class
    h = g
