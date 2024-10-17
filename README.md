Python Co-Routine Concurrency Practice different approaches:

For hundreds and thousands of concurrency co-routines, there are two different techniques that can be tailored for applications that require parallel processing.

#1 Gather: push n co-routine with fork and joint pattern, which is available in Python [asyncio.gather].

#2 Use limited m-co-routine and keep using them all the time. When one worker/co-routine completes the job, proceed with
the same co-routine, and run the next job.

For concurrency level technique #1:the level is n or zero. When n is completed, the next n starts with a new co-routines.

Concurrency level technique #2: the level all the time is n.
For reality, both techniques respect the fact we cannot run thousands of co-routines in one shot, especially for network connections or DB transactions.
To get the best performance, both techniques should be tested for the application and the better selected.
The experience shows one of these techniques for a specific application can give much better results.

Module for technique #1 is gather_with_repeat.py.

Module for technique #2 is use_n_all_the_time.py
