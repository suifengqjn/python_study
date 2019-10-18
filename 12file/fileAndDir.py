import os

# 文件重命名
os.rename("oldname", "newname")

# 文件删除
os.remove("path")



# 文件夹基本操作
#创建文件夹

os.mkdir("张三")

#获取当前目录
os.getcwd()


#改变默认目录

os.chdir("../")

#获取目录列表
os.listdir("./")

#删除文件夹
os.rmdir("张三")