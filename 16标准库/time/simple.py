import time



t = time.time()

print (t)                       #原始时间数据
print (int(t))                  #秒级时间戳
print (int(round(t * 1000)))    #毫秒级时间戳
print (int(round(t * 1000000))) #微秒级时间戳

print("------")

print("当前时间",time.time())


localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)


localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)


# 格式化日期
# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

print(3*1**3)

x = True
y = False
z = False

if x or y and z:
    print("yes")
else:
    print("no")
