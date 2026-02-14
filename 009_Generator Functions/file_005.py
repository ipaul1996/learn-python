# throw(exc_type, *args)
# Injects an exception at the suspension point:
# - Calling gen.throw(E, msg) resumes the generator, raising E(msg) at the paused yield.
# - If the generator catches it via try/except, it can handle and continue; otherwise it propagates out.


def safe_divider():
    try:
        while True:
            x, y = yield
            yield x / y
    except ZeroDivisionError:
        yield float("inf")  # Represents positive infinity


gen = safe_divider()
print(next(gen))  # None
print(gen.send((10, 2)))  # sends tuple, yields 5.0
print(gen.throw(ZeroDivisionError))  # inf
