# Case - 1: Iterable & Iterator are different objects
class MyRange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        # Each call returns a fresh iterator
        return MyRangeIterator(self.n)


class MyRangeIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            val = self.current
            self.current += 1
            return val
        raise StopIteration


r = MyRange(5)

# Each call to iter(r) returns a new, independent iterator
itr1 = iter(r)
itr2 = iter(r)

print(
    "itr1 is itr2:", itr1 is itr2
)  # False, because they are different iterator objects

# Demonstrate that each iterator tracks its own position
print("First value from itr1:", next(itr1))  # 1
print("First value from itr2:", next(itr2))  # 1

print("Second value from itr1:", next(itr1))  # 2
print("Second value from itr2:", next(itr2))  # 2

print("Third value from itr1:", next(itr1))  # 3

# Exhaust itr1 completely
print("Remaining values from itr1:")
for val in itr1:
    print(val, end=" ")  # 4 5
print()

# itr2 is still independent and can be exhausted separately
print("Remaining values from itr2:")
for val in itr2:
    print(val, end=" ")  # 3 4 5
print()

# Explanation:
# - MyRange is an iterable: it implements __iter__ which returns a new iterator each time.
# - MyRangeIterator is the iterator: it implements __next__ and __iter__ (returns self).
# - Multiple iterators from the same iterable are independent and track their own positions.
