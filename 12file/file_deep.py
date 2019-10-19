#
#
# open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。
#
# open(file, mode='r')
# 完整的语法格式为：
#
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# 参数说明:
#
# file: 必需，文件路径（相对或者绝对路径）。
# mode: 可选，文件打开模式
# buffering: 设置缓冲
# encoding: 一般使用utf8
# errors: 报错级别
# newline: 区分换行符
# closefd: 传入的file参数类型
# opener:

#常用model
# t	文本模式 (默认)。
# x	写模式，新建一个文件，如果该文件已存在则会报错。
# +	打开一个文件进行更新(可读可写)。
# r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。

#file 对象常用方法
# 1
# file.close()
#
# 关闭文件。关闭后文件不能再进行读写操作。
#
# 2
# file.flush()
#
# 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
#
# 3
# file.fileno()
#
# 返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
#


# 6
# file.read([size])
#
# 从文件读取指定的字节数，如果未给定或为负则读取所有。
#
# 7
# file.readline([size])
#
# 读取整行，包括 "\n" 字符。
#
# 8
# file.readlines([sizeint])
#
# 读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。
#
# 9
# file.seek(offset[, whence])
#
# 设置文件当前位置
#
# 10
# file.tell()
#
# 返回文件当前位置。
#

# 12
# file.write(str)
#
# 将字符串写入文件，返回的是写入的字符长度。
#
# 13
# file.writelines(sequence)
#
# 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。