import asyncio
from typing import Awaitable, MutableMapping, Any

# 1. We define what our Message is (a modifiable dictionary)
Message = MutableMapping[str, Any]

# 2. This function simulates downloading data from the internet.
# Notice it is an 'async def', which means calling it creates an Awaitable.
async def wait_for_network_event() -> Message:
    print("⏳ Waiting for data over the network...")
    await asyncio.sleep(2)  # Simulate a 2-second delay

    asyncio.create_task()
    
    # After the wait, we produce the actual Message (a standard dictionary)
    return {
        "type": "websocket.receive",
        "text": "Hello from the client!"
    }

async def main():
    # --- THE AWAITABLE PHASE ---
    # Calling the function doesn't give us the dictionary right away!
    # 'pending_event' is an Awaitable[Message].
    pending_event: Awaitable[Message] = wait_for_network_event()
    
    print(f"Right now, we have an: {type(pending_event)}") 
    # Output: <class 'coroutine'>
    
    # --- THE AWAIT PHASE ---
    # We use 'await' to pause here until the 2 seconds are up and the data arrives.
    actual_message: Message = await pending_event
    
    # --- THE MUTABLE MAPPING PHASE ---
    # Now that we waited, 'actual_message' is our MutableMapping (the dictionary).
    print(f"\nNow we have a: {type(actual_message)}") 
    # Output: <class 'dict'>
    
    # Because it is a MutableMapping, we can read it AND change it
    print(f"Original text: {actual_message['text']}")
    actual_message["text"] = "I CHANGED THIS TEXT!"  # Mutating the mapping!
    actual_message["processed"] = True               # Adding a new key!
    
    print(f"Final Message: {actual_message}")

# Run the async program
asyncio.run(main())