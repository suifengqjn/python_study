dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print(dict)

# 内置函数
print(len(dict))
print(str(dict))
print(type(dict))

# 内置方法
# 返回指定键的值，如果值不在字典中返回default值
v = dict.get("a", "default")
print(v)

# 如果键在字典dict里返回true，否则返回false
# 检测键 Age 是否存在
if 'Age' in dict:
    print("键 Age 存在")
else:
    print("键 Age 不存在")

# 检测键 Sex 是否存在
if 'Cecil' in dict:
    print("键 Sex 存在")
else:
    print("键 Sex 不存在")

# 以列表返回可遍历的(键, 值) 元组数组
print(dict.items())

# 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
dict.setdefault("aa", "bb")
print(dict)

# 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。

v = dict.pop("aa")
print("pop", v)

# 遍历
for k, v in dict.items():
    print("k=%s mv=%s" %(k, v))

# 所有的key
print("keys", dict.keys())

# 所有的value
print("values", dict.values())

# 取值
print(dict["Alice"])

# 增
dict["bob"] = 12334
print(dict)

# 删

# 删除键
del dict["bob"]
print(dict)

# 清空字典
dict.clear()
print("clear", dict)

# 删除字典
del dict
print(dict)


