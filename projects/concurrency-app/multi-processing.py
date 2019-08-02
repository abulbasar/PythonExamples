import time
import threading
import os
from multiprocessing import Process


"""
$ time python multi-processing.py 
ID of process running main program: 2344
Main thread name: MainThread
Waiting for processes to finish
Dispatcher thread name: MainThread
ID of process running dispatcher thread: 2345
Dispatcher thread name: MainThread
ID of process running dispatcher thread: 2346

real    0m2.618s
user    0m0.053s
sys     0m0.021s


"""


def high_latency_method():
    time.sleep(0.05)


def dispatcher(items):
    print("Dispatcher thread name: {}".format(threading.current_thread().name))
    print("ID of process running dispatcher thread: {}".format(os.getpid()))
    for _ in items:
        high_latency_method()


def start():
    print("ID of process running main program: {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.main_thread().name))

    p1 = Process(target=dispatcher, args=(range(0, 50),))
    p2 = Process(target=dispatcher, args=(range(50, 100),))

    p1.start()
    p2.start()

    print("Waiting for processes to finish")
    p1.join()
    p2.join()

    print("Main thread finished")


if __name__ == "__main__":
    start()
