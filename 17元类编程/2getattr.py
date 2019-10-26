
# __getattr__ : 查找不到属性的时候会调用
# __getattribute__: 调用任意属性都会进入此方法
from datetime import date, datetime

class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
    def __getattr__(self, item):
        return "not found {}".format(item)

    def __getattribute__(self, item):
        return item

class person:
    def __init__(self, items):
        self.items = items
    def __getattr__(self, item):
        return self.items[item]
if __name__ == "__main__" :
    user = User("bob", date(year=1992, month=3, day=14))

    print(user.age)


    per = person({"name":"a", "age":"15"})
    print(per.name)
    print(per.age)