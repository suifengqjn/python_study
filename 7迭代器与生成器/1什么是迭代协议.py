

# 迭代器是什么
# 迭代器是访问集合内元素的一种方式，一般用来遍历数据
# 迭代器和用下标访问的方式不一样，迭代器是不能返回的

# 只要实现 __iter__ 就是可迭代的 成为迭代器还需要实现 __next__
from collections.abc import Iterable,Iterator


list = [1, 2, 3, 4]
# 创建迭代器对象
it = iter(list)
print(isinstance(it, Iterable))
print(isinstance(it, Iterator))
