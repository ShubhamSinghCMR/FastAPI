import asyncio

# Shared resource
shared_resource = 0

# Semaphore with a limit of 2 (allows up to 2 coroutines to access the critical section at the same time)
semaphore = asyncio.Semaphore(2)

async def modify_shared_resource():
    global shared_resource

    async with semaphore:
        # Critical section begins
        print(f"Shared resource before modification: {shared_resource}")
        shared_resource += 1
        await asyncio.sleep(2) 
        print(f"Shared resource after modification: {shared_resource}")
        # Critical section ends

async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(1, 6)))

asyncio.run(main())
