import asyncio
import os.path
from time import sleep, perf_counter as pc

inp_dir= "C:/Users/Public/py_dev/multi_coros/bulktasks/code/data/in/"
out_file= "C:/Users/Public/py_dev/multi_coros/bulktasks/code/data/out/gather_all_files.txt"
listOfFiles = [f for f in os.listdir(inp_dir) ]
out_file= open(out_file, 'w')

async def write_out(lines):
    out_file.writelines(lines)
    out_file.writelines("End---------------------------------------------------------------------------------------------------------file\n")

def get_next():
    if len(listOfFiles) == 0 : return None
    return listOfFiles.pop()

async def read_file(fn):
    t0_stopwatch = pc()
    filenamer=f"{inp_dir}{fn}"
    with open(filenamer, "r+") as file1:
        fread= file1.read()
        sleep(0.00001)
        fread=fread+f"Read_Elapsed Time:{round((pc() - t0_stopwatch), 3)}\n"
        output_text = fread.replace('\\n', '\n')
        print(fread)
        return(fread)


async def single_job_coro(cor_id):
        run_num=1
        t0_stopwatch = pc()
        next_file = get_next()
        if next_file == None: return
        #print(f'====>corName:cor{cor_id} file_name{next_file} ')
        out_lines_read= await read_file(next_file)
        out_lines_read = out_lines_read + f"write_Elapsed Time:{round((pc() - t0_stopwatch), 5)}\n"
        output_text = out_lines_read.replace('\\n', '\n')
        await write_out(f'====>corName:cor{cor_id} with read file name:{next_file}\n'+
                       f"cor:{cor_id}  Run_Number:{run_num}\n" + out_lines_read)
        await asyncio.sleep(0.01)           #mandatory** to give  others chance  to run
        #sleep(0.1)
        run_num+=1

async def exec():
    ist=0
    incr=10
    ied=ist+incr
    while True:
        print(f"ist:{ist} ied:{ied}")
        # create many coros jobs
        done =await asyncio.gather(*[single_job_coro(i) for i in range(ist,ied)])
        #print(f"Done={done} ")
        # done, pending = await asyncio.wait([single_job_coro)
        #listoutx= asyncio.gather(*[single_job_coro(i) for i in range(ist, ied)])
        # report results
        ist=ied
        incr=10
        ied=ist+incr
        if ied > len(listOfFiles): ied= len(listOfFiles)

        if ist >= len(listOfFiles): break




# start the asyncio program
t0_stopwatch = pc()
asyncio.run(exec())
out_file.close()
print('All done')
print(f"see { out_file.name}")
print(f"Total Elapsed Time for All Jobs:{round((pc() - t0_stopwatch), 5)}\n")