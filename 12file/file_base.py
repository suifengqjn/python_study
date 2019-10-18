
import os
#open(filename, mode)
# filename：包含了你要访问的文件名称的字符串值。
# mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。
# 这个参数是非强制的，默认文件访问模式为只读(r)。

# w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。

filePth = "./1.txt"
f = open(filePth, "r")

#读取所有数据
# f.read(size) size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
content = f.read()
print("read--",content)

f.seek(0)
content1 = f.read(10)
print("read--",content1)
f.close()


#f.readline() f.readline() 会从文件中读取单独的一行。换行符为 '\n'。
# f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行
f = open(filePth, "r")
content = f.readline()
print("read line--",content)
f.close()


#f.readlines() 将返回该文件中包含的所有行。
f = open(filePth, "r")
l = f.readlines()
print("read lines--",l)
f.close()







#f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
f = open("./2.txt", "w")

num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
print(num)
# 关闭打开的文件
f.close()


# f.tell()
# f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数

f = open("./1.txt", "r")
f.seek(12,1)
location = f.tell()
print("tell",location)
f.close()


# f.seek()
# 如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
#
# from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
#
# seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
# seek(x,1) ： 表示从当前位置往后移动x个字符
# seek(-x,2)：表示从文件的结尾往前移动x个字符