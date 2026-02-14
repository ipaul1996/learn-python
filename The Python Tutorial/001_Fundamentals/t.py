x = 10.0
name = "Alice"
is_active = True
fruits = ["Mango", "Guava", "Lichhi"]
numbers = (10.0,)
person = {"name": "indrajit", "age": 29}

nothing = None


a, b, c = 1, 2, 3

a, *b, c, d = 1, 2, 3
print(a, b, c, d)

x = 1
y = -1

x, y = y, x

p = {"x": 100, "y": 200, "z": 300}

k1, k2, k3 = p
print(k1, k2, k3)

print(p.keys())
print(p.values())
print(p.items())


class Test:
    def __init__(self, x, y):
        self.x = x
        self.y = y


t = Test(1, 2)
print(type(t))  # <class '__main__.Test'>
print(type(t).__name__)  # Test
print(type(type(t).__name__))  # <class 'str'>

t1 = Test(1, 2)
t2 = Test(3, 4)

# Do t1 and t2 share the exact same class object?
print(type(t1) is type(t2))  # True
