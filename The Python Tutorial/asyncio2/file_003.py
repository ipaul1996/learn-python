# The asyncio event loop is the core scheduler of an asynchronous Python application.
# It continuously cycles through three main phases:
# 1. Runs ready callbacks and tasks.
# 2. Waits for I/O operations or timers to complete.
# 3. Queues up any newly ready events.
# This process repeats until all tasks are finished or the loop is explicitly stopped.

# 1. Runs ready callbacks and tasks
# The event loop maintains a FIFO "ready queue" of Handle objects.
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
