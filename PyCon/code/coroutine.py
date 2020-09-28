import asyncio

async def coroutine1() :
    print("co1 first entry point")
    await asyncio.sleep(1)
    print("co1 second entry point")

async def coroutine2() :
    print("co2 first entry point")
    await asyncio.sleep(2)
    print("co2 second entry point")

loop = asyncio.get_event_loop()
loop.create_task(coroutine1())
loop.create_task(coroutine2())
loop.run_forever()
