import asyncio
import time
import random

async def fetch_data(pid, delay):
    start_time = time.time()  
    print(f"Started fetching data for {pid} at {start_time}")
    
    await asyncio.sleep(delay)
    
    end_time = time.time()
    print(f"Completely fetched data for {pid} at {end_time}")
    
    print(f"Time taken for {pid}: {end_time - start_time:.2f} seconds")
    
    return {
        'value': "fetched data",
        'pid': pid
    }

async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i in range(1,4):
            delay = random.randint(1,5)
            task = tg.create_task(fetch_data(i,delay))
            tasks.append(task)
    for task in tasks:
        print(task.result())


asyncio.run(main())

