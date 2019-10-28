
# gil global interpreter lock
# python 中的一个线程对应c语言中的一个线程
# gil 使得同一个时刻只有一个线程在一个cpu上执行字节码 无法将多个线程映射到多个cpu上
#
# import dis
#
# def add(a):
#     a = a+1
#     return a
# print(dis.dis(add))

# gil 在执行过程中会释放，不是线程安全
# gil 会根据执行的字节码行数和io操作 主动释放
import threading
total = 0
def add():
    global total
    for i in range(10000000):
        total += 1

def desc():
    global total
    for i in range(10000000):
        total -=1

if __name__ == "__main__":

    thread1 = threading.Thread(target=add)
    thread2 = threading.Thread(target=desc)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(total)