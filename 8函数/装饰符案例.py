
import logging


# 需求 ，执行一个方法的之后，打印日志，不能对该方法进行修改
# 如果不用装饰器 只能这么实现
def use_logging(func):

    def wrapper():
        logging.warning("%s is running" % func.__name__)
        return func()   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper

def foo():
    print('i am foo')

foo = use_logging(foo)  # 因为装饰器 use_logging(foo) 返回的时函数对象 wrapper，这条语句相当于  foo = wrapper
foo()                   # 执行foo()就相当于执行 wrapper()


# 使用@语法糖
# 有了 @ ，我们就可以省去foo = use_logging(foo)这一句了，直接调用 foo() 即可得到想要的结果。
def use_logging2(func):

    def wrapper():
        logging.warning("%s is running" % func.__name__)
        return func()
    return wrapper

@use_logging2
def foo2():
    print("i am foo2")

foo2()






# 使用案例
class myDecorator(object):

    def __init__(self, f):
        print ("inside myDecorator.__init__()")
        self.f = f

    def __call__(self):
        print ("inside myDecorator.__call__()")
        self.f()

@myDecorator
def aFunction():
    print ("inside aFunction()")

print ("Finished decorating aFunction()")


aFunction()

# 以上，初始化时 aFunction 会变成myDecorator类的一个实例，
# 通过重载()操作符的办法，这样子aFunction实际上就变成了myDecorator.()操作了。
# 于是从外型上看，这还是一个普通的函数的调用，但其实暗地里你可以做出很多不为人知的操作的

print("------------------")

#或者如果不想使用类，也可以使用内部函数的办法。如下的代码和上面的同样的效果
def entryExit(f):
    def new_f():
        print ("Entering", f.__name__)
        f()
        print ("Exited", f.__name__)
    return new_f

@entryExit
def func1():
    print ("inside func1()")


func1()