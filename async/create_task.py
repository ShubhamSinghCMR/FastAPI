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
    task1 = asyncio.create_task(fetch_data(1,4))
    task2 = asyncio.create_task(fetch_data(2,1))
    task3 = asyncio.create_task(fetch_data(3,2))

    # result1 = await task1
    result2 = await task2
    print("Result2: ",result2)
    result3 = await task3
    # print("Result1: ",result1)
    # print("Result2: ",result2)
    print("Result3: ",result3)

asyncio.run(main())