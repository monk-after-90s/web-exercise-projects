import asyncio, aiohttp


async def get(session, url=""):
    async with session.get(url) as resp:
        (await resp.text())


async def main():
    start_time = asyncio.get_running_loop().time()
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[asyncio.create_task(get(session)) for _ in range(500)])
    end_time = asyncio.get_running_loop().time()
    print(f'spent_seconds:{end_time - start_time}')


asyncio.run(main())
