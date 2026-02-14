# Write a generator count_up(n) that yields integers 0 through n-1.
# Instantiate and manually call next() to retrieve first three values, then exhaust via a for loop.


def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1


gen_obj = count_up(5)
print(gen_obj)  # <generator object count_up at 0x100ca9d80>

print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))

for j in range(2):
    print(next(gen_obj))


