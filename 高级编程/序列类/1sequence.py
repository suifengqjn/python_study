

from collections import abc

a = [1, 2]
b = a + [3, 4] # + 两边类型必须相同
print(b)

a += (3, 4) # += 只需要满足序列类型
print(a)

a.extend(range(3))
print(a)

a.extend((4, 5))
print(a)


# append 添加一个值, 跟extend 区别很大
a.append([1, 2])
print(a)