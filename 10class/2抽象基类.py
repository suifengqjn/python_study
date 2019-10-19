
from collections.abc import Sized

from abc import ABCMeta,abstractmethod

# 我们再某些情况下希望判定某个对象的类型
class Person(object):
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.name)


p = Person("zhangsan")
print(isinstance(p, Sized))


# 我们需要强制某个子类必须实现某些方法,如果不采用抽象基类
# class BaseCache():
#     def get(self, key):
#         raise NotImplementedError
#     def set(self, key, value):
#         raise NotImplementedError
#
# # 继承 BaseCache
# class RedisCache(BaseCache):
#     def get(self, key):
#         print(key)
#
# redis = RedisCache
# redis.get("a")

#
# 1、如果子类在继承后一定要实现的方法，可以在父类中指定metaclass为abc模块的ABCMeta
# 类，并在指定的方法上标准abc模块的@abcstractmethod来达到目的。
# 2、一旦定义了这样的父类，父类就不能实例化了，否则会抛出TypeError异常。
# 3、继承的子类如果没有实现@abcstractmethod标注的方法，在实例化使也会抛出TypeError异常

class BaseCache(metaclass=ABCMeta):
    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(self, key, value):
       pass

# 继承 BaseCache
class RedisCache(BaseCache):
    def get(self, key):
        print(key)
    def set(self, key, value):
        print(key, value)

redis = RedisCache()
redis.get(key="a")