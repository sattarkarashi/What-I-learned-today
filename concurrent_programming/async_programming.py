import asyncio
from random import randint
import time
import aiohttp
import json

'''
For I/O-bound tasks, async programming is a good choice.
'''

async def get_items():
    print("Getting items")
    await asyncio.sleep(3)
    print("Items received")
    return randint(1, 100) 

async def get_posts(url:str, id:int) -> dict:
    full_url = f"{url}/{id}"
    print(f"Getting post from {full_url}")
    async with aiohttp.ClientSession() as session:
        response = await session.get(full_url)
        response = await response.text()
        return json.loads(response)



async def main():
    # print("Starting main program")
    # start = time.perf_counter()
    # items = await asyncio.gather(*[get_items() for _ in range(2)])
    # print(f"Items: {items}")
    # duration = time.perf_counter() - start
    # print(f"Ending main program in {duration} seconds.")

    url = "https://jsonplaceholder.typicode.com/posts"
    start = time.perf_counter()
    posts = await asyncio.gather(*[get_posts(url, id) for id in range(1, 100)])
    print(f"Posts: {posts}")
    duration = time.perf_counter() - start
    print(f"Ending main program in {duration} seconds.")

if __name__ == "__main__":
    asyncio.run(main())