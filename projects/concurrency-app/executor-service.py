from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import current_process
import os
import hashlib
import string
import random

"""
Thread-pool service
real    0m33.562s
user    0m33.466s
sys     0m0.174s

Process-pool service
real    0m16.995s
user    0m33.751s
sys     0m0.101s


"""

def dispatcher(n):
    thread_name = current_process().name + str(os.getpid())
    print(f"Pid: {thread_name}")
    results = []
    for _ in range(n):
        message = "".join(random.choices(string.ascii_letters, k = 1000))
        hash = hashlib.sha256(message.encode("utf-8")).hexdigest()
        results.append(hash)
    return results


def using_thread_pool_service():
    results = []
    with ThreadPoolExecutor(max_workers=2) as executor:
        future1 = executor.submit(dispatcher, 100000)
        future2 = executor.submit(dispatcher, 100000)
        print("Waiting for response")
        results += future1.result()
        results += future2.result()
    print(len(results))


def using_process_pool_service():
    results = []
    with ProcessPoolExecutor(max_workers=2) as executor:
        future1 = executor.submit(dispatcher, 100000)
        future2 = executor.submit(dispatcher, 100000)
        print("Waiting for response")
        results += future1.result()
        results += future2.result()
    print(len(results))


if __name__ == "__main__":
    # Uncomment one of the method call at a time and compute time.
    #using_thread_pool_service()
    using_process_pool_service()
    #no_threaded()