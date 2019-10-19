sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

for i in range(len(sites)):
    print("index", i)

# 遍历数字序列，可以使用内置range()函数

for i in range(5):
    print(i)

for i in range(6, 9):
    print(i)

# 也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
for i in range(0, 10, 3):
    print(i)

for index in range(len(sites)):
    print(sites[index])


for i in range(2, 3+1):
    print("----",i)


