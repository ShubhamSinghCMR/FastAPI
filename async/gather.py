import asyncio
import time

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
    
    results = await asyncio.gather(fetch_data(1,3),fetch_data(2,1),fetch_data(3,4))
    for result in results:
        print(result)

asyncio.run(main())