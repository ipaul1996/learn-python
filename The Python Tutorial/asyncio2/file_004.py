# task = asyncio.create_task(some_coroutine())
# Wraps the coroutine in a new Task and schedules it to run concurrently with other tasks in the event loop.
# Returns immediately with a Task object that can be inspected or cancelled.
# Common Task methods and properties:
# - done(): Returns True if the task is finished (completed or cancelled).
# - cancelled(): Returns True if the task was cancelled.
# - result(): Returns the result if the task completed successfully, or raises an exception if it failed.
# - exception(): Returns the exception raised by the task, or None if it completed successfully.
# - cancel(): Requests cancellation of the task. If running, it will be cancelled at the next await point.
# - add_done_callback(callback): Adds a callback to be called when the task is done.
# - get_name(): Returns the task's name.
# - set_name(name): Sets the task's name.

# Task Lifecycle:
# 1. Created: A Task is created when you wrap a coroutine with asyncio.create_task(coro) or loop.create_task(coro).
# 2. Pending: The Task is waiting to be run by the event loop (scheduled, but not yet started).
# 3. Running: The Task is actively executing its coroutine until it hits an await expression, completes, or is cancelled.
# 4. Suspended: At an await point, the Task pauses and yields control back to the event loop, waiting for the awaited operation to finish.
# 5. Resumed: When the awaited operation completes, the Task is put back into the ready queue and continues running from where it left off.
# 6. Done: The Task is finished and marked as done. This can happen in three ways:
#    a. Completed: The coroutine returns normally, and the Task stores the result.
#    b. Failed: The coroutine raises an exception, and the Task stores the exception.
#    c. Cancelled: If cancel() is called, the Task raises asyncio.CancelledError at the next await point, allowing cleanup before being marked as cancelled.
# Once a Task is done, its result or exception can be retrieved, and any callbacks added with add_done_callback() are called.

import asyncio


async def worker(name, delay):
    print(f"{name} start")
    for i in range(100000):
        pass
    await asyncio.sleep(delay)
    print(f"{name} done")
    return name


async def main():
    t1 = asyncio.create_task(worker("Prem", 3.0))
    t2 = asyncio.create_task(worker("Aashraya", 1.5))

    print("Worker scheduled")
    results = await asyncio.gather(t1, t2)
    print("Result:", results)


asyncio.run(main())
"""
Worker scheduled
Prem start
Aashraya start
Aashraya done
Prem done
Result: ['Prem', 'Aashraya']
"""