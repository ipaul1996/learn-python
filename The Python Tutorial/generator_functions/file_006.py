# gen.close()
# - Calling gen.close() raises GeneratorExit inside the generator at its paused yield.
# - If generator performs cleanup and returns (or does nothing), close() returns None.
# - If generator catches GeneratorExit or yields again, a RuntimeError is raised.


def listener():
    try:
        while True:
            data = yield
            print("Received: ", data)
    except GeneratorExit:
        print("Cleaning up & exiting")


gen = listener()
next(gen)
gen.send("hello")
gen.close()
