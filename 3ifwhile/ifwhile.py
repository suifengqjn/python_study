

# Fibonacci series: 斐波纳契数列
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b

print("-----")
i = 0
while i < 100:
    if i % 3 == 0:
        print(i, end=",")
    i += 1

age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

### 退出提示
input("点击 enter 键退出")