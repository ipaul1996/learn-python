# Generator in for-loop
def squares(n):
    for i in range(n):
        yield i * i


gen = squares(5)

# The for loop automatically calls __iter__() and __next__() until StopIteration.
# - Calls iter(obj) → triggers obj.__iter__() → gets an iterator.
# - Repeatedly calls next(iterator) → triggers iterator.__next__() → retrieves the next value.
# - Stops when a StopIteration exception is raised, which signals the end of the generator's sequence.
for val in gen:
    print(val)

gen1 = squares(3)

print("************************")

try:
    while True:
        value = next(gen1)
        print(value)
except StopIteration:
    print("Generator exhausted-StopIteration raised.")
