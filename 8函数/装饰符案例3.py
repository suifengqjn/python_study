

#类装饰器
# 装饰器不仅可以是函数，还可以是类，相比函数装饰器，
# 类装饰器具有灵活度大、高内聚、封装性等优点。
# 使用类装饰器主要依靠类的__call__方法，当使用 @ 形式将装饰器附加到函数上时，就会调用此方法
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')

@Foo
def bar():
    print ('bar')

bar()



# 装饰器顺序
# @a
# @b
# @c
# def f ():
#     pass
#
#
# f = a(b(c(f)))