#
# def 函数名（参数列表）:
#     函数体


def hello() :
   print("Hello World!")

hello()


# 计算面积函数
def area(width, height):
    return width * height

print(area(2,3.5))


# 参数为不可变对象
def ChangeInt(a):
    a = 10

b = 2
ChangeInt(b)
print(b)

#参数为不可变对象
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)


#关键字参数,顺序可以不同
def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")


#默认参数
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")



#不定长参数
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
#加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
printinfo(70, 60, 50, 11)

print("------------------------")
def printinfo2(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


printinfo2(10)
printinfo2(70, 60, 50)



#参数带两个星号 **  以字典的形式导入
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3)


#匿名函数 python 使用 lambda 来创建匿名函数 lambda 函数的语法只包含一个语句
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))




#return语句
# return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。之前的例子都没有示范如何返回数值

def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


# 调用sum函数
total = sum(10, 20)
print("函数外 : ", total)
