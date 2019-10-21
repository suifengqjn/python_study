import string

str = "  today is a beautiful day  "
print(str)

# 截取
print(str[1:4])

print(str[:3])

print(str[3:])

if ("H" in str):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

# 切割
arr = str.split(" ", -1)
print(arr)

# 拼接
s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b")  # 字符串序列
print(s1.join(seq))
print(s2.join(seq))

# 开头
v = str.startswith("today")
print(v)

# 结尾
v2 = str.endswith("day")
print(v2)

# trim
# 去掉左边的空格
print(str.lstrip())
# 去掉右边的空格
print(str.rstrip())

# 字符串有两种类型，一种是str，一种是unicode
# 要正确判读一个对象是不是字符串，要有basestring，因为basestring是str和unicode的基类，包含了普通字符串和unicode类型。

# replace
str = str.replace("today", "yestoday", -1)
print(str)

#是否是数字
print(str.isdigit())


# format
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))

#如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))


v = 123
strv = repr(v)
print(v, type(strv))


