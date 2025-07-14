import asyncio, time


async def main():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")


asyncio.run(main())
# asyncio provides a run() function to execute an async def function and all
# other coroutines called from there, like sleep() in the main() function.

