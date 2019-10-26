
# 自定义类
def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"
        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company

# 使用type 动态创建
class BaseClass:
    def answer(self):
        return "i am base class"

def say(self):
    return 'i am ' + self.name
Student = type("stu", (BaseClass,), {"name":"student","say":say})
if __name__ == "__main__":
    myClass = create_class("user")
    obj = myClass()
    print(obj)

    stu = Student()
    print(stu.name)
    print(stu.say())
    print(stu.answer())


