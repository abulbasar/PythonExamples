import time
import threading
import os


"""
$ time python multi-threaded.py 
ID of process running main program: 2216
Main thread name: MainThread
Starting threads
Dispatcher thread name: t1
ID of process running dispatcher thread: 2216
Dispatcher thread name: t2
ID of process running dispatcher thread: 2216
Waiting for threads to finish

real    0m2.684s
user    0m0.039s
sys     0m0.014s


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

    t1 = threading.Thread(target=dispatcher, name='t1', args=(range(0, 50),))
    t2 = threading.Thread(target=dispatcher, name='t2', args=(range(50, 100),))

    print("Starting threads")
    t1.start()
    t2.start()

    print("Waiting for threads to finish")
    t1.join()
    t2.join()


if __name__ == "__main__":
    start()
