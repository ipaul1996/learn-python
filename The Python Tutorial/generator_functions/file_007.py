# Generator chaining
def squares(limit):
    for i in range(limit):
        yield i * i


def filter_even(gen):
    for val in gen:
        if val % 2 == 0:
            yield val


gen = filter_even(squares(5))

print(list(gen))  # [0, 4, 16]
