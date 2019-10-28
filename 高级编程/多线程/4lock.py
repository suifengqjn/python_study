
from threading import Lock
import threading
total = 0
lock = Lock()
def add():
    global total
    global lock
    for i in range(10000000):
        lock.acquire()
        total += 1
        lock.release()

def desc():
    global total
    global lock
    for i in range(10000000):
        lock.acquire()
        total -=1
        lock.release()


# Lock 不能连续两次acquire
# RLock 可以连续多次acquire acquire 和 release 次数也要相同
if __name__ == "__main__":

    thread1 = threading.Thread(target=add)
    thread2 = threading.Thread(target=desc)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(total)