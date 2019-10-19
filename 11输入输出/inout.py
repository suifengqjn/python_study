

#str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。


s = 'Hello, Runoob'

print(str(s))
print(repr(s))

print(str(1/2))


# 字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
#还有类似的方法, 如 ljust() 和 center()。
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用
    print(repr(x*x*x).rjust(4))


# format
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))



#读取键盘输入
str = input("请输入：")
print ("你输入的内容是: ", str)