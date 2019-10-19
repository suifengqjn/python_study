
name = 'xiaoming'
position = '讲师'
address = '北京市昌平区建材城西路金燕龙办公楼1层'

print('--------------------------------------------------')
print("三种格式化输出的方式")
print("姓名：%s " %name)
print("职位：%s " %position)
print("公司地址：%s " %address)
print("姓名：%s 职位：%s" %(name, position))
print("姓名：{} 职位：{}".format(name, position))
print('--------------------------------------------------')


# 下标
str = "中国人abc"
print(str[:2])
print(str[1:4])


print("输入：")
content= input("请输入内容：")
print(content)