def f1(arg):
    print ("f1")
    rl = arg()
    print (rl)
    return rl + "f1"

# @符作符相当于 f1(f2())
# 会最先执行
# 执行到下面的代码时候，f2 已经不存在

# 实际上前面那些个 @ 操作符完成了这么一个操作：
# f2 = f1(f2())
# f2已经被覆盖为 f1(f2) 的返回值了。
# 运行时f2的结果已经固化，使用参数也不会重新计算，或者说根本无法使用参数

@f1
def f2(arg = ""):
    print ("f2")
    return arg + "f2r"

print ("start")
print (f2)
#print f2("1") 出错
#print f1(None)

print("-----------------")
