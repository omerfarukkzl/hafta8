import multiprocessing
import os

def process1():
    print(f"Process 1, PID: {os.getpid()}")

def process2():
    print(f"Process 2, PID: {os.getpid()}")

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=process1)
    p2 = multiprocessing.Process(target=process2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
