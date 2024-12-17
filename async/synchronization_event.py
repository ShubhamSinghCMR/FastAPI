import asyncio

# Create an Event object
event = asyncio.Event()

async def wait_for_event(task_name):
    print(f"{task_name} waiting for the event to be set...")
    await event.wait()  # Wait until the event is set
    print(f"{task_name} resumed after the event was set!")

async def trigger_event():
    print("Triggering the event in 2 seconds...")
    await asyncio.sleep(2)
    event.set()  # Set the event to allow other tasks to proceed

async def main():
    # Create coroutines that will wait for the event
    task1 = asyncio.create_task(wait_for_event("Task 1"))
    task2 = asyncio.create_task(wait_for_event("Task 2"))
    
    # Start a coroutine that triggers the event
    await trigger_event()

    # Wait for the tasks to complete
    await asyncio.gather(task1, task2)

asyncio.run(main())
