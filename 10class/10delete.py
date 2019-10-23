
#python 中垃圾回收的算法是引用计数

a = object()
b = a
del a
print(b)
print(a)

# 类似 dealloc 方法
class A:
    def __del__(self):
        pass