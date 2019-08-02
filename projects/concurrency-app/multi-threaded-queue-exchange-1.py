import time
import threading
import os
from queue import Queue
import random



def dispatcher(queue:Queue):
    thread_name = threading.current_thread().name
    for i in range(10):
        queue.put(f"[{thread_name}] {i}")
        time.sleep(0.1 + 0.1 * random.random())


def start():

    queue = Queue()

    t1 = threading.Thread(target=dispatcher, name='t1', args=(queue,))
    t2 = threading.Thread(target=dispatcher, name='t2', args=(queue,))

    print("Starting threads")
    t1.start()
    t2.start()

    print("Waiting for threads to finish")
    t1.join()
    t2.join()

    while not queue.empty():
        print(queue.get())




if __name__ == "__main__":
    start()
