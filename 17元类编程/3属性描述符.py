
import numbers

# 实现下面任意一个方法就是属性描述符
# 属性描述符：对属性进行赋值的时候进行类型判断
class IntField:
    # 数据描述符
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("not int type")
        if value < 0:
            return ValueError("need > 0")
        self.value = value
    def __delete__(self, instance):

        pass

class NotDataField:
    # 非数据描述符
    def __get__(self, instance, owner):
        return self.value

class User:
    age = IntField()

if __name__ == "__main__" :
    user = User()

    user.age = 12
    print(user.age)

    # 还能这样访问属性值
    print(getattr(User, "age"))
    # error
    # user.age = "12"
    # print(user.age)