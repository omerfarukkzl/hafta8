import threading
import multiprocessing
import os

def thread_task():
    print(f"Thread ID: {threading.get_ident()}")

def process_task():
    print(f"Process ID: {os.getpid()}")

def multiprogramming_example():
    threads = [threading.Thread(target=thread_task) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

def multiprocessing_example():
    processes = [multiprocessing.Process(target=process_task) for _ in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

if __name__ == '__main__':
    print("Multiprogramming:")
    multiprogramming_example()
    print("Multiprocessing:")
    multiprocessing_example()
