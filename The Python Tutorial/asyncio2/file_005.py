import asyncio


async def slow_worker():
    print("Started slow worker...")
    try:
        await asyncio.sleep()
    except asyncio.CancelledError:
        print("Slow worker was cancelled")
        raise
    print("Slow worker finished")


async def main():
    task = asyncio.create_task(slow_worker())
    await asyncio.sleep(1)
    print("Cancelling task...")
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Caught task cancellation in main")


asyncio.run(main())
