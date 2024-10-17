import asyncio


async def fun1_sync():
    i = 0
    while True:
        i += 1
        if i % 50000 == 0:
            print("Hello, I'm Abhishek")
            print("GFG is Great")
            await asyncio.sleep(0.01)
            return f"{i}"

async def fun2_async():
    while True:
        await asyncio.sleep(0.01)
        k =   await fun1_sync()
        print(k)

loop = asyncio.get_event_loop()
#asyncio.ensure_future(fun1_sync())
asyncio.ensure_future(fun2_async())
loop.run_forever()