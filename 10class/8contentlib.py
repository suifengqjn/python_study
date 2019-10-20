
#上下文管理器，原理就是通过with语句

import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print("open file")
    yield {"name":"alice"}
    print("close file")

with file_open("123.txt") as f:
    print("read file data")
