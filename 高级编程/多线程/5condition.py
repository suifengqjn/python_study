import threading

# #
class Xiaoai(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="xiaoai")
        self.cond = cond
    #重写父类方法
    def run(self):
        with self.cond:
            self.cond.wait()
            print("{}: b".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}: d".format(self.name))
            self.cond.notify()






class Tianmao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="tianmao")
        self.cond = cond

    def run(self):
        with self.cond:

            print("{}: a".format(self.name))
            self.cond.notify()
            self.cond.wait()


            print("{}: c".format(self.name))
            self.cond.notify()
            self.cond.wait()





if __name__ == "__main__":

    #在调用with cond之后才能调用wait或者notify方法
    condition = threading.Condition()
    xiaoai = Xiaoai(condition)
    tianmao = Tianmao(condition)

    # 线程start 之后，执行 run方法
    xiaoai.start()
    print("11")
    tianmao.start()


