
# pass 不会 crash
# raise 类似于手动panic
# finally 最终一定会执行

try:
    # 打开一个不存在的文件
    open('123.txt' ,'r')
except IOError as err:
    print("panic",err)
except ValueError:
    print("value err")
except NameError as err:

    pass

try:
    print(num)
except:
    print("err", "num eroor")
finally:
    print("executing finally clause")


try:
    num = 100
    print(num)
except NameError as err:
    print(err)
else:
    print('没有捕获到异常，真高兴')
finally:
    print('我一定会执行的哦')


# 跳过异常
arr = [1, 2, 3]
try:
    v = arr[5]
    print(v)
except Exception as e:
    print(e)
    pass