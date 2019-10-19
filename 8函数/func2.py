
# 缺省参数
def printInfo(name, age = 20):
    print(name, age)


printInfo("张三")


# 不定长参数
def printinfo(arg1, *vartuple):
    # 打印任何传入的参数
    print(arg1)
    for var in vartuple:
        print(var)

printinfo(10)
printinfo(70, 60, 50)


# 匿名函数
sum = lambda arg1, arg2: arg1 + arg2

print("Value of total : ", sum(10, 20))

print("Value of total : ", sum(20, 20))
