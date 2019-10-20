
# 列表推导式
# 提取1-20之间的奇数


odd_list = [i for i in range(21) if i % 2 == 1]
print(odd_list)

# 复杂逻辑情况下的应用
def handleItem(item):
    return item * item
odd_list = [handleItem(i) for i in range(21) if i % 2 == 1]
print(odd_list)
print(type(odd_list))


print("-----------")



# 生成器表达式
odd_gen =  (i for i in range(21) if i % 2 == 1)
print(type(odd_gen))
for i in odd_gen :
    print(i,end="-")

# 可以转化为list
print(list(odd_gen))

print("-----------")


#字典推导式 key value 对换

dict = {"k1":"v1","k2":"v2","k3":"v3"}
rever_dict = {value:key for key , value in dict.items()}
print(rever_dict)

