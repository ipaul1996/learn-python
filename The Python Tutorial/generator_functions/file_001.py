# A generator function is defined like a normal function but uses yield to 
# produce a sequence of values lazily(as soon as we call it does not provide a value, until next is called).
# On invocation, it returns a generator object, not immediate execution.
# The yield keyword transforms a function into a generator.

"""
def gen_func(...):
    # setup
    yield value1        # suspend, emit value1
    # intermediate code
    yield value2        # suspend again
    # teardown or return
"""

# Calling gen = gen_func() does not run body; instead, it creates a generator frame object 
# that stores code, initializes local variables, and sets the instruction pointer to the 
# start of the function, ready to resume execution when next() is called.
# next(gen) executes until first yield, returns its value, and suspends at that point.
# Each next(gen) resumes execution from the last yield, with all local variables and control flow preserved, 
# continuing until the next yield, function return, or a StopIteration exception is raised.

