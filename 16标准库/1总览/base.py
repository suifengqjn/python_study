
import numbers


# 1. 数字的抽象积累 numbers
a = 1
print(isinstance(a, numbers.Integral))

b = 1.20
print(isinstance(b, numbers.Number))


# 2. 操作系统, 文件读写 相关 os
import os
# 获取当前目录
print(os.getcwd())

# 执行系统shell 命令
os.system("mkdir 123")


# json
import json
#序列化
js = {"a":"alice", "b":23, "c":12.4}
data = json.dumps(js)
print("json", type(data))

js = json.loads(data)
print("value", type(js))


# 对象序列化 pickle与cPickle
# cPickle模块的作用与pickle模块一样，只不过cPickle模块使用C而不是Python进行实现，因此比pickle要快好几倍。值得注意的是，cPickle不允许用户从cPickle派生子类，如果我们并不用从中派生子类的话，那么cPickle是个更好的选择。
# pickle不提供安全保证
try:
   import cPickle as pickle
except:
   import pickle

# 序列化
x = [{'a':1, 'b':2, 'c':3}, 'This is a string', 100]
str = pickle.dumps(x)
print(str)

# 反序列化
y = pickle.loads(str)
print(y)

# 写入文件 使用with 不需要关闭
with open('temp.pkl', "wb") as f:
    pickle.dump(x, f)

# 从文件读取
with open('temp.pkl', 'rb') as f:
    y = pickle.load(f)
    print("pickle.load",y)




# 数学 math
import math

print(math.cos(math.pi / 4))
print(math.log(1024, 2))


# 随机 random
import random

print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))
print(random.randrange(6))


# 网络请求 requests
import requests

res = requests.get(url="http://www.zhihu.com",params={"timeout":1})
print("status_code",res.status_code)



# 时间和日期 time 和 datetime
from datetime import date

now = date.today()
print("date",now)

# 时间戳转时间
t = date.fromtimestamp(1571882192)
print("t :", t)

from datetime import datetime

now = datetime.today()
print("datetime",now)

print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))


# 数据压缩 Python 内置了常用的数据压缩算法，比如：zlib，gzip，bz2，zipfile，tarfile
import zlib
s = b'witch which has which witches wrist watch'
s2 = zlib.compress(s)
print("zlib", len(s), len(s2))
recovers = zlib.decompress(s2)
print("zlib recover", recovers)

# 3. 文件和目录管理
import shutil
# shutil.copyfile('data.db', 'archive.db')
# shutil.move('/build/executables', 'installdir')
print(shutil.disk_usage("/Users/qianjianeng/Desktop"))

# 4. 文件通配符 glob
import glob
print(glob.glob("*.py"))



# 5. 命令行参数 sys
import sys
print(sys.argv)
print(sys.platform)
# 在命令行中执行 "python main.py one two three" 后可以得到以下输出结果
#
# ['main.py', 'one', 'two', 'three']


# 6. 错误输出重定向和程序终止
# 都封装在 sys 模块中 它们分别是： sys.stdout , sys.stdin , sys.stderr
sys.stderr.write('Warning, log file not found starting a new one\n')


# 7 字符串正则匹配和正则表达式 re
import re

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

# 性能度量 timeit 下面的代码使用了 timeit 模块中的 Timer() 对象测试一些代码的执行时间
from timeit import Timer

ti = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print(ti)