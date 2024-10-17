import asyncio
import time
from datetime import datetime
from random import choice
from string import ascii_uppercase
from time import sleep, perf_counter as pc

dir= "C:/Users/Public/py_dev/multi_coros/bulktasks/code/data/in/"

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        original_return_val = func(*args, **kwargs)
        end = time.perf_counter()
        print("time elapsed in ", func.__name__, ": ", end - start, sep='')
        return original_return_val
    return wrapper


def genRandomStr():
    return(''.join(choice(ascii_uppercase) for i in range(70)))
def dat_time():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return(dt_string)
async def wfile(i):
    t0_stopwatch  = pc()
    filenamew=f"{dir}inp_file{i}.txt"
    with open(filenamew, "w") as file1:
        file1.write(f"FileName:{filenamew} \n")
        file1.write(f"Time:{dat_time()} \n")
        file1.write(f"content:{genRandomStr()} \n")
        file1.write(f"Elapsed Time:{round((pc() - t0_stopwatch), 6)}\n")


async def rfile(i):
    print(f"**************************cor-{i}*************************************")
    t0_stopwatch = pc()
    filenamer=f"{dir}inp_file{i}.txt"
    with open(filenamer, "r+") as file1:
        fread= file1.read()
        sleep(0.00001)
        fread=fread+f"Elapsed Time:{round((pc() - t0_stopwatch), 3)}\n"
        output_text = fread.replace('\\n', '\n')
        print(fread)
        return(fread)

async def test(i):
    print(f"Start Task {i}")
    await asyncio.sleep(0.1)
    print(f"Finished Task {i}")

async def main():
    listout=await asyncio.gather(*[rfile(j) for j in range(100)])
    for l in listout:
        print(l)



asyncio.run(main())