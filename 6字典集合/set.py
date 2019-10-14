# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket)

# 快速判断元素是否在集合内
if 'orange' in basket:
    print("存在")
else:
    print("不存在")

#集合运算
a = set('abracadabra')
b = set('alacazam')

# 集合a中包含而集合b中不包含的元素
print(a - b)
# 集合a或b中包含的所有元素
print(a | b)
# 集合a和b中都包含了的元素
print(a & b)
# 不同时包含于a和b的元素
print(a ^ b)


#增
basket.add("aaa")
print(basket)
#删
basket.remove("aaa")
print(basket)