
import string

str = "today is a beautiful day"
print(str)


print(str[1:4])

print(str[:3])

print(str[3:])

#字符串有两种类型，一种是str，一种是unicode
#要正确判读一个对象是不是字符串，要有basestring，因为basestring是str和unicode的基类，包含了普通字符串和unicode类型。

#判断是不是字符串
# v = isinstance(str,string.basestring)
# print(v)


