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
    # Creating coroutine objects
    co1 = fetch_data(1,3)
    co2 = fetch_data(2,3)

    # Calling coroutines:: awaited sequentially
    result1 = await co1
    result2 = await co2
    print("CO1: ",result1)
    print("CO2: ", result2)

asyncio.run(main())

