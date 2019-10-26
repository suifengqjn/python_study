
class User:
    def __new__(cls, *args, **kwargs):
        print("in new")
        return super().__new__(cls)
    def __init__(self, name):
        self.name = name

# new 是用来控制对象的生成过程，在对象生成之前
# init 是用来完善对象
# 如果new不返回对象，则不会执行init函数
if __name__ =="__main__":
    u = User(name="bob")

    print(u)