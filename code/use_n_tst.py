import asyncio
from test_ctl import Ctl_test
# coroutine w
tst_ctl = Ctl_test()
async def single_job_coro_tst(cor_id, ctl):
    while True:
        value = tst_ctl.get_next_inp_tst()
        print(f'>>> corName:cor{cor_id} inp_value{value} ')
        if value == None: return
        # block for a moment
        #await asyncio.sleep(1)
        await asyncio.sleep(0.01)
        out_value= { "corName":f"cor{cor_id}", "value":value}
        tst_ctl.set_next_out_tst(out_value)
        # report the value
        print(f'>out_value ')


# exec main coroutine
async def exec():
    # create many tasks
    coro_jobs = [asyncio.create_task(single_job_coro_tst(i, tst_ctl)) for i in range(10)]
    # wait for all tasks to complete
    done, pending = await asyncio.wait(coro_jobs)
    print(f"Done={done}  Pending={pending}")
    # report results
    print('All done')


# start the asyncio program
asyncio.run(exec())
print(tst_ctl.lis_out)