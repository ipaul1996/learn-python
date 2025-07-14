import asyncio
import time


async def main():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")


loop = asyncio.get_event_loop()  # Returns event loop instance for the current thread.
task = loop.create_task(main())
# create_task() schedules the coroutine to be run in the event loop.
# It returns a Task object, which can be used to monitor the status of the task
# and can also be used to obtain a result value from your completed
# coroutine. You can cancel the task with task.cancel().


loop.run_until_complete(task)
# This blocks the current thread(main thread).
# It will keep the loop running only until the given coro completes—but all other
# tasks scheduled on the loop will also run while the loop is running.

pending = asyncio.all_tasks(loop=loop)
# 

for task in pending:
    task.cancel()


group = asyncio.gather(*pending, return_exceptions=True)
# It gathers all the tasks in the loop and returns a single Future object.
# If any of the tasks raises an exception, it will be returned as part of the result
# of the Future, rather than being raised immediately.
# If return_exceptions is False, the first exception raised will be propagated to the caller.


loop.run_until_complete(group)
# Waits for all cancellations to finish, ensuring no stray coroutines remain.

loop.close()
# loop.close() is usually the final action: it must be called on a stopped loop, and
# it will clear all queues and shut down the executor. A stopped loop can be restar‐
# ted, but a closed loop is gone forever.



