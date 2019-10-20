


class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()


class C(B):
    def __init__(self):
        print("C")
        super().__init__()
class D(C):
    def __init__(self):
        print("D")
        super().__init__()
# super 执行顺序，根据mro 继承链上的关系，而不是代码层面的上一级
if __name__ == "__main__":
    d = D()



