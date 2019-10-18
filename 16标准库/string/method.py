mystr = 'hello world itcast and itcastcpp'

# find
# 检测 str 是否包含在 mystr中
index = mystr.find("hello")
if index >= 0 :
    print("存在", index)


# index
# 跟find()方法一样，只不过如果str不在 mystr中会报一个异常.
index = mystr.index("o")
print("index", index)


# count
# 返回 str在start和end之间 在 mystr里面出现的次数
count = mystr.count("o")
print("count", count)



# replace
# 把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.

mystr = mystr.replace("hello", "tom hello")
print(mystr)


# split
# 以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
arr=mystr.split(" ")
print("split", arr)


# capitalize
# 把字符串的第一个字符大写
print("capitalize", mystr.capitalize())



# startswith endswith
# 检查字符串是否是以 obj 开头, 是则返回 True，否则返回 False
print(mystr.startswith("tom"))

# upper
# 转换 mystr 中的小写字母为大写
print("upper", mystr.upper())


# ljust  /rjust /center
# 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
print("begin",mystr.ljust(60),"end")


# lstrip /rstrip
# 删除 mystr 左边的空格
print("       abc".lstrip())



#
# partition
# 把mystr以str分割成三部分,str前，str和str后
print("partition",mystr.partition("itcast"))


# splitlines
# 按照行分隔，返回一个包含各行作为元素的列表
str2 = "abc\nbac"
print(str2.splitlines())


# isalnum
# 如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False


#
# isalpha
# 如果 mystr 所有字符都是字母 则返回 True,否则返回 False



# isdigit
# 如果 mystr 只包含数字则返回 True 否则返回 False.


# join
# mystr 中每个字符后面插入str,构造出一个新的字符串