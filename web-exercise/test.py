import asyncio
import time


async def main():
    sleep_task = None

    async def activator():
        nonlocal sleep_task
        sleep_task = asyncio.create_task(asyncio.sleep(1))

    async def waitor():
        await asyncio.shield(sleep_task)

    activator_task = asyncio.create_task(activator())
    waitor_task = asyncio.create_task(waitor())
    waitor_task2 = asyncio.create_task(waitor())
    await asyncio.sleep(0.5)
    waitor_task.cancel()
    await asyncio.sleep(0)
    print(sleep_task.done())
    await waitor_task2


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
