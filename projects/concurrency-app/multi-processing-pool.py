import time
import threading
import os
from multiprocessing import Pool, current_process


"""
$ time python multi-processing-pool.py 
ID of process running main program: 2199
Main thread name: MainThread
Dispatcher thread name: MainThread
ID of process running dispatcher thread: 2201
Dispatcher thread name: MainThread
ID of process running dispatcher thread: 2200

real    0m2.683s
user    0m0.068s
sys     0m0.036s

"""


def high_latency_method():
    time.sleep(0.05)


def dispatcher(items):
    print("Dispatcher thread name: {}".format(current_process().name))
    print("ID of process running dispatcher thread: {}".format(os.getpid()))
    for _ in items:
        high_latency_method()


def start():
    print("ID of process running main program: {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.main_thread().name))
    process_pool = Pool(2)
    process_pool.map(dispatcher, (range(0, 50), range(50, 100)))


if __name__ == "__main__":
    start()
