import time

"""
$ time python single-threaded.py 

real    0m5.376s
user    0m0.025s
sys     0m0.010s

"""


def high_latency_method():
    time.sleep(0.05)


def start():
    for _ in range(100):
        high_latency_method()


if __name__ == "__main__":
    start()
