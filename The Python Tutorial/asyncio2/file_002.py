import asyncio


# Let's define a coroutine
async def work():
    print("Work started")
    await asyncio.sleep(1.0)  # Suspension point
    print("Work done")
    return 42


# If we do work() here, it will not run it's body, instead it will return a coroutine object.
# Until we await this coroutine object or wrap it in a Task, nothing in work actually executes.

print(type(work()))  # <class 'coroutine'>

# Syntax: result = await some_awaitable
# - Pauses the current coroutine at that line.
# - Schedules the awaited object (another coroutine, Task, or Future).
# - Returns control to the event loop so it can run other tasks.
# - When the awaited object completes, resumes right after await, returning its value.


async def main():
    # Create the coroutine object
    coro_obj = work()

    # Await it directly
    result = await coro_obj

    print("Result:", result)


# Entry point: run the main coroutine using asyncio's event loop
# asyncio.run() creates an event loop, runs main(), and closes the loop when done.
asyncio.run(main())
