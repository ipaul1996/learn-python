# Asynchronous (Non-Blocking) Code:
import asyncio


async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulate a non-blocking operation
    print("Data fetched!")


async def main():
    await fetch_data()  # Call the asynchronous function
    print("Continuing with other tasks...")


# Run the main function using asyncio's event loop
asyncio.run(main())
