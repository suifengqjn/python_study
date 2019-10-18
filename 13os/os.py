
import os

# os 包 操作文件和目录

#返回当前工作目录
d = os.getcwd()
print(d)



# 创建文件夹 如果文件夹存在，则报错

#以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)
# err= os.mkdir("tt", 0o777)
# print(err)

err = os.makedirs("a/b")
print(err)

# 递归删除目录。
err=os.removedirs("a/b")
print(err)

# 重命名文件或目录，从 src 到 dst
err =  os.rename("tt", "ttt")
print(err)
