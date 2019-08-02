import time
import threading
import os
from queue import Queue
import random



def dispatcher(queue:Queue):
    thread_name = threading.current_thread().name
    while not queue.empty():
        print(f"{thread_name}" + queue.get())
        time.sleep(0.1)


def start():
    queue = Queue()

    t1 = threading.Thread(target=dispatcher, name='t1', args=(queue,))
    t2 = threading.Thread(target=dispatcher, name='t2', args=(queue,))

    for i in range(20):
        queue.put(f" m-{i} ")

    print("Starting threads")
    t1.start()
    t2.start()

    print("Waiting for threads to finish")
    t1.join()
    t2.join()


if __name__ == "__main__":
    start()
