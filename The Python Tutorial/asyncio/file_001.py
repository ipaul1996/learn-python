# Synchronous (Blocking) Code:
import time


def fetch_data():
    print("Fetching data...")
    time.sleep(2)  # Simulate a blocking operation
    print("Data fetched!")


data = fetch_data()

print("Continuing with other tasks...")
# This code will block the main thread until fetch_data is complete.
# If you want to run this in an asynchronous context, you would need to use asyncio.
