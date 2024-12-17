import asyncio

# Shared resource
shared_resource=0

# lock
lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_resource

    async with lock:
        # Critical section begins
        print("Shared resource before modification: ",shared_resource)
        shared_resource+=1
        await asyncio.sleep(2)
        print("Shared resource after modification: ",shared_resource)
        # Critical section ends

async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(1,4)))
        
asyncio.run(main())