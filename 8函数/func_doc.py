
# 文档注释

def printLine(char, times):
    """打印多行分隔符
    :param char: 分隔符
    :param times: 次数
    """
    c = 0
    while c < times:
        print(char, times)
        c += 1

printLine("-", 5)


a = "asda"
if __name__ == "__main__":

    a = "abcd"
    if 'a' in a:
        a = 'cbddd'
    else:
        a = "bb"

    print(a)

