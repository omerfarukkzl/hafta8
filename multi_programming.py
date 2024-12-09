import threading
import time

def program1():
    for i in range(5):
        print(f"Program 1 - Döngü {i}")
        time.sleep(1)

def program2():
    for i in range(5):
        print(f"Program 2 - Döngü {i}")
        time.sleep(1)

t1 = threading.Thread(target=program1)
t2 = threading.Thread(target=program2)

t1.start()
t2.start()

t1.join()
t2.join()
