# Generator frame retains local variable values across yield suspensions.


def accumulator():
    total = 0
    while True:
        value = yield total
        total += value


gen = accumulator()

print(next(gen))  # 0

# send(value)
# Sends a value into a paused yield expression

print(gen.send(5))  # sends 5 into yield, yields updated total 5
print(gen.send(10))  # sends 10, yields updated total 15

