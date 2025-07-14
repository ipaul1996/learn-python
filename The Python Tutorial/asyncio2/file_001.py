# asyncio is Python’s standard library module for asynchronous I/O.
# asyncio lets you run many tasks one after another in an overlapping manner in the same thread without blocking.
# We write code that can pause at well-defined points, allowing other code to run in the same thread.
# Primary goal: handle many I/O-bound operations (networking, file I/O, timers) efficiently without blocking.

# Event loop: The scheduler that runs and switches between asynchronous tasks.

# Coroutines: Special functions defined with async def that can be pause and resume via await.
# Calling it (e.g. main()) doesn’t run its body; it just returns a coroutine object(a types.Coroutine instance)
# which can be awaited or scheduled to run by the event loop (using asyncio.run() from the top level
# or using asyncio.create_task()).

# Tasks: A wrapper for coroutines that allows them to be scheduled and run by the event loop.
# A Task is a subclass of Future and represents the execution of a coroutine.

# Awaitables: Objects that can be awaited, such as coroutines, asyncio.Future, or asyncio.Task.

# await: A keyword used inside async def function to pause execution of a coroutine until
# the awaited object is ready.

# Futures: A low-level awaitable representing a result that will become available later.
# Futures are used to signal completion or failure of asynchronous operations.

# asyncio Workflow (Step-by-step)
# 1. Define coroutines using 'async def'.
# 2. Schedule coroutines on the event loop:
#    - Use 'asyncio.run()' to run a main coroutine (entry point).
#    - Use 'asyncio.create_task()' or 'loop.create_task()' to schedule multiple coroutines concurrently.
# 3. Inside coroutines, use 'await' on I/O operations or other awaitable objects to pause execution and yield control.
# 4. The event loop monitors I/O readiness (e.g., network, file) and resumes coroutines when their awaited operations complete.
# 5. When all scheduled tasks are finished or cancelled, the event loop shuts down.
#    - 'asyncio.run()' automatically manages event loop startup and shutdown.

import asyncio


# Define an asynchronous coroutine
async def task1():
    # Simulate an I/O-bound operation with asyncio.sleep (non-blocking sleep)
    await asyncio.sleep(1.0)


# Define the main coroutine
async def main():
    print("Starting task1...")
    # Await task1: pause here until task1 completes
    await task1()  # Schedule task1 and wait for it to finish
    print("task1 completed!")


# Entry point: run the main coroutine using asyncio's event loop
# asyncio.run() creates an event loop, runs main(), and closes the loop when done.
asyncio.run(main())
