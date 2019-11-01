
# 线程池
#主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
#当一个线程完成的时候我们主线程能立即知道
#futures可以让多线程和多进程编码接口一致

from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
from concurrent.futures import Future
from multiprocessing import Pool
import time

def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times


executor = ThreadPoolExecutor()
#通过submit函数提交执行的函数到线程池中, submit 是立即返回
# task1 = executor.submit(get_html(2))
# task2 = executor.submit(get_html(5))
# print(task1.Result())

# task1.Done()  立即返回，不会等到线程执行结束
# task1.Result() 阻塞，直到线程结束
# task1.Cancel() 线程未开始前可以取消

if __name__ == "__main__":
    urls = [3,2,4]

    all_task = [executor.submit(get_html, (url)) for url in urls]
    # for future in as_completed(all_task):
    #     data = future.result()
    #     print("get {} page".format(data))

    wait(all_task, return_when=FIRST_COMPLETED) # 等待直到第一个任务结束
    print("----done")

    time.sleep(5)

    # 通过executor的map获取已经完成的task的值
    print("executor.map")
    for data in executor.map(get_html, urls):
        print("get {} page".format(data))