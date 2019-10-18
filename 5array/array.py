# list.append(x)	把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
# list.extend(L)	通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
# list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
# list.remove(x)	删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
# list.pop([i])	从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
# list.clear()	移除列表中的所有项，等于del a[:]。
# list.index(x)	返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
# list.count(x)	返回 x 在列表中出现的次数。
# list.sort()	对列表中的元素进行排序。
# list.reverse()	倒排列表中的元素。
# list.copy()	返回列表的浅复制，等于a[:]。



list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

print(list1)
print(list2)
print(list3)

# 获取值
print(list1[3])

# 增加
list1 += ["1", "2"]
list.append(list1, "234")
print(list1)

# 删除
del list1[6]
print("删除第六个元素", list1)

del list3[1:3]
print("list3",list3)

del list1[4:]
print("删除第4到最后个元素", list1)

# 修改
list1[0] = "xiaoming"
print(list1)

# 查找 in not in
if "a" in list3:
    print("存在a")
else:
    print("不存在a")


if "f" not in list3:
    print("不存在f")


# 获取长度
l = len(list1)
print("长度", l)

# 获取最大值
print("最大值", max(list2))
# 获取最小值
print("最大值", min(list2))

# list 常用方法
# 在列表末尾添加新的对象
list.append(list1, "a")
list1.append("b")
print(list1)

# 统计某个元素在列表中出现的次数
print(list1.count("Runoob"))

# 在列表末尾一次性追加另一个序列中的多个值
list.extend(list1, list2)
print(list1)
print(list2)

# 从列表中找出某个值第一个匹配项的索引位置
print(list1.index("Runoob"))

# 将对象插入列表
list1.insert(3, "xiao gang")
print(list1)

# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
value = list1.pop()
print(value)
print(list1)

# 移除列表中某个值的第一个匹配项
list1.remove("xiaoming")
print(list1)

# 反向列表中元素
list2.reverse()
print(list2)

# 对原列表进行排序
list2.sort(key=None, reverse=False)
print(list2)

# 复制列表
list3 = list2.copy()
print("list3", list3)

# 清空列表
list3.clear()
print("list3", list3)


print("-------")
#将列表当做堆栈使用
stack = [3, 4, 5]
stack.append(6)
print(stack)

print(stack.pop())
print(stack.pop())

print(stack)



print("-------")

