import threading
import os
from multiprocessing import Process, current_process
import hashlib
import string
import random

"""
Multi-processing 
real    0m19.451s
user    0m38.631s
sys     0m0.083s


Multi-threading 
real    0m35.154s
user    0m35.049s
sys     0m0.199s

No-threading
real    0m33.791s
user    0m33.764s
sys     0m0.020s

"""

def dispatcher():
    thread_name = current_process().name + str(os.getpid())
    print(f"Pid: {thread_name}")
    for _ in range(100000):
        message = "".join(random.choices(string.ascii_letters, k = 1000))
        hashlib.sha256(message.encode("utf-8")).hexdigest()



def start_processes():
    print("ID of process running main program: {}".format(os.getpid()))

    p1 = Process(target=dispatcher)
    p2 = Process(target=dispatcher)

    p1.start()
    p2.start()

    print("Waiting for processes to finish")
    p1.join()
    p2.join()


def start_threads():
    print("Id of process running main program: {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.main_thread().name))

    t1 = threading.Thread(target=dispatcher)
    t2 = threading.Thread(target=dispatcher)

    t1.start()
    t2.start()

    print("Waiting for processes to finish")
    t1.join()
    t2.join()


def single_threaded():
    for _ in range(200000):
        message = "".join(random.choices(string.ascii_letters, k=1000))
        hashlib.sha256(message.encode("utf-8")).hexdigest()



if __name__ == "__main__":
    # Uncomment one of the method call at a time and compute time.
    start_processes()
    #start_threads()
    #single_threaded()