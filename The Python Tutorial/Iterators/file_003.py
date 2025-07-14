# Case - 2: Iterable & Iterator is the same object
class CountUp:
    def __init__(self, max_value):
        self.max = max_value

    def __iter__(self):
        self.current = 1
        return self
    
    def __next__(self):
        if self.current <= self.max:
            value = self.current
            self.current += 1
            return value
        raise StopIteration
    
for num in CountUp(3):
    print(num)
# The for loop calls iter(CountUp(3)) → runs __iter__(), resetting current to 1.
# Then repeatedly calls __next__() until StopIteration is raised.

