
import sys
list = [1, 2, 3, 4]
# 创建迭代器对象
it = iter(list)
# 输出迭代器的下一个元素
print(next(it))
print(next(it))



# 迭代器对象可以使用常规for语句进行遍历：
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象

print(" ")
#也可以使用 next() 函数：
list = [1, 2, 3, 4]
while True:
    try:
        print(next(it), end=" ")
    except StopIteration:
        sys.exit()








