import asyncio

# The asyncio event loop is the core scheduler of an asynchronous Python application.
# It continuously cycles through three main phases (each cycle is called an "iteration" of the event loop):
# 1. Runs ready callbacks and tasks.
# 2. Waits for I/O operations or timers to complete.
# 3. Queues up any newly ready events.
# This process repeats until all tasks are finished or the loop is explicitly stopped.

# STEP 1: Runs ready callbacks and tasks
# The event loop maintains a "ready queue"(collections.deque object --> a high-performance, double-ended queue)
# of Handle objects.
# _ready queue: A FIFO (First-In, First-Out) queue. The loop processes items in the order they were added.
# asyncio.Handle: A simple wrapper object that contains a callback (a regular, synchronous function) and its arguments. 
# It provides a standardized, executable unit for the loop's scheduler. The loop doesn't need to know what the function does, 
# only that it can execute the Handle via its internal _run() method.
# There are two primary sources for these handles.

# 1. Direct Callback Scheduling
# You can schedule a regular Python function to be executed as soon as possible on the next iteration of the loop. 
# This is done using the low-level loop.call_soon() method. A callback in this context refers to a standard, non-async function.

# How it works?
# a. You call loop.call_soon(my_callback, arg1, arg2).
# b. asyncio creates an asyncio.Handle that wraps my_callback and its arguments.
# c. This Handle is immediately appended to the end of the _ready queue.
# d. During the "run ready" phase, the loop will pop this Handle from the queue 
#    and execute my_callback(arg1, arg2).

# Example:
def a_regular_function(step):
    # This is a standard synchronous callback
    print(f"Executing regular function: Step {step}")

async def main():
    print("Main coroutine started.")
    loop = asyncio.get_running_loop()
    
    # Schedule two callbacks to run on the next loop iteration
    loop.call_soon(a_regular_function, 1)
    loop.call_soon(a_regular_function, 2)
    
    # We await something to allow the event loop to run its cycle
    await asyncio.sleep(0.1) 
    print("Main coroutine finished.")

asyncio.run(main())

# Execution Analysis:
# a. main() starts and gets the current event loop.
# b. loop.call_soon(..., 1) creates a Handle for a_regular_function(1) and adds it to the _ready queue.
# c. loop.call_soon(..., 2) does the same for a_regular_function(2). The _ready queue now contains two handles.
# d. main() hits await asyncio.sleep(0.1) and suspends, giving control to the event loop.
# e. The loop begins its "run ready" phase. It finds two Handles in _ready.
# f. It executes the first handle, calling a_regular_function(1).
# g. It executes the second handle, calling a_regular_function(2).
# h. The _ready queue is now empty. The loop proceeds to its next phase (waiting for the 0.1s sleep timer).


# 2. Task Resumption after await
# a. You first call an async def function, which returns a coroutine object. At this point, no code inside the function has run.
# b. You pass this coroutine object to asyncio.create_task() i.e., asyncio.create_task(coroutine). 
#    - It wraps your coroutine in a Task object.
#    - It then schedules the Task to run as soon as possible. To do this, it wraps the Task's internal startup logic in an 
#      asyncio.Handle and adds that Handle to the event loop's _ready queue.
#    - The function returns the Task object(not internal handle) immediately, which you can use to track or await its result.
# c. On the next iteration of the event loop, the loop finds the Handle for the Task in the _ready queue and executes it.
# d. The Task executes its wrapped coroutine's code until it encounters an await expression(usually on a Future). 
#    This is a suspension point.
# e. The Task checks if the awaited Future is complete. If it is not (PENDING state), the Task registers its internal 
#    ._wakeup() method as a callback to the Future's internal list of callbacks. The Task then yields control to the 
#    event loop and is considered suspended. It is no longer in the _ready queue.
# f. Later, an external event (like a timer expiring or I/O data arriving) causes the event loop to resolve the Future 
#    by calling future.set_result() or future.set_exception().
# g. The call to set_result() or set_exception() transitions the Future's state to FINISHED. This transition immediately 
#    triggers the execution of all callbacks previously registered with the Future.
# h. The Task's ._wakeup() method is executed as part of this callback sequence. The sole function of ._wakeup() is to re-schedule 
#    the Task by wrapping its execution method in a Handle and adding that Handle to the event loop's _ready queue.
# i. In the subsequent iteration of the event loop, the loop processes its _ready queue. It finds the Handle for the Task, 
#    executes it, and the Task resumes the execution of its coroutine. The code continues immediately after the await expression, 
#    and the result of the now-completed Future is returned.




# Each Handle wraps either:
#   - A callback scheduled via loop.call_soon() (to run as soon as possible),
#   - A callback scheduled via loop.call_later() (to run after a delay), or
#   - A Task that is ready to resume (e.g., after an await completes).
# On each iteration, the loop processes the ready queue:
#   - It removes each Handle in order and executes its callback or resumes the Task(until next suspension point).
#   - This continues until the ready queue is empty for that cycle.
# High-level APIs like asyncio.run() or loop.run_until_complete() drive this loop for us.


# 2. Waits for I/O events or timers
# When the ready queue is empty, the event loop waits for something new to happen:
#   - It monitors all registered I/O sources (like sockets or files) to see if they become ready for reading or writing.
#   - It also keeps track of timers (set by call_later, call_at, etc.) to see if any have finished waiting.
#   - The loop uses efficient system calls (like select, epoll, or kqueue) to wait for either an I/O event or a timer to expire.
#   - This waiting is efficient: the loop "sleeps" until something is ready, so it doesn't waste CPU time.

# 3. Moves new events to the ready queue
# When an I/O event happens (like data arrives on a socket) or a timer expires:
#   - The loop finds the callback or task that should run for that event.
#   - It wraps this callback or task in a Handle and puts it into the ready queue.
#   - This way, the next time the loop runs, these new tasks or callbacks will be picked up and executed.

# The loop repeats these steps:
#   - Run everything that’s ready.
#   - Wait for new events.
#   - Move new events to the ready queue.
# This cycle continues until all work is done or you tell the loop to stop.
