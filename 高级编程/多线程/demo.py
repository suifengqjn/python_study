import time
import threading

class task1(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        count = 1
        while True:
            print("task1", time.time())
            count += 1
            if count >= 5:
                break
            time.sleep(2)

class task2(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        count = 1
        while True:
            print("task2", time.time())
            count += 1
            # if count >= 7:
            #     break
            time.sleep(3)



if __name__ == "__main__":

    t1 = task1("t1")
    t1.start()

    t2 = task2("t2")
    t2.start()


    for i in range(10):
        print(i)

        time.sleep(2)