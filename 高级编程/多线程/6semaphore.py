
import threading
import time
# threading.Semaphore 控制线程并发数量

class htmlSplider(threading.Thread):
    def __init__(self,sem, url):
        super().__init__()
        self.sem = sem
        self.url = url
    def run(self):
        time.sleep(2)
        print("get html success {}".format(self.url))
        self.sem.release()




class urlProducer(threading.Thread):
    def __init__(self,sem):
        super().__init__()
        self.sem = sem

    def run(self):

        for i in range(20):
            self.sem.acquire()
            url = "http:www.baidu.com/{}".format(i)
            html = htmlSplider(self.sem, url)
            html.start()


if __name__ == "__main__":

    # 设置最大并发线程为3
    sem = threading.Semaphore(3)
    urlp = urlProducer(sem)
    urlp.start()
