import asyncio


async def genYield():
    i=0
    k=100
    while True:
        i+=1
        k+=1
        yield i,k
        await asyncio.sleep(1)
        if i == 8 :
           break
# sync function, calling async function
def get_number_i_k():
    yield asyncio.get_event_loop().run_until_complete(genYield())

taskyield = asyncio.create_task(genYield())

lisout= [{"a":i , "b":k} for i,k in  get_number_i_k() ]
for l in lisout:
    print(f"{l}")