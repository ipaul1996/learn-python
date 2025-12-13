import datetime as dt

today = dt.date.today()

print(today.year, today.month, today.day)


def count_up(n):
    i = 0
    while i <= n:
        yield i
        i += 1


gen_obj = count_up(2)
print(gen_obj)

print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
