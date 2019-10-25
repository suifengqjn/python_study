
import logging

# 带参数的情况
# 一个参数
def use_logging(func):

    def wrapper(name):
        logging.warning("%s is running" % func.__name__)
        return func(name)
    return wrapper


# 多个参数
def use_logging2(func):

    def wrapper(*args):
        logging.warning("%s is running" % func.__name__)
        return func(*args)
    return wrapper

# 关键字参数
def use_logging3(func):
    def wrapper(*args, **kwargs):
        # # args是一个数组，kwargs一个字典
        logging.warning("%s is running" % func.__name__)
        print("use_logging3", args, kwargs)
        return func(*args, **kwargs)
    return wrapper


# 带参数的装饰器
def use_logging4(level:str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warning("%s is running" % func.__name__)
            elif level == "error":
                logging.error("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator







@use_logging3
def foo(name, age):
    print("foo", name, age)

@use_logging4(level="error")
def foo2(name='foo'):
    print("i am %s" % name)

if __name__ == "__main__":


    foo("xiaoming", 12)

    foo2("aaaa")
