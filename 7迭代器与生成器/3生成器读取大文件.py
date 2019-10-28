
 # 需求：文件大小500G 一行

 # f = open()
 # for line in f:
 #     print(line)


def myreadlines(f, newline):
  buf = ""
  while True:
    while newline in buf:
      pos = buf.index(newline)
      yield buf[:pos]
      buf = buf[pos + len(newline):]
    chunk = f.read(4096)

    if not chunk:
      #说明已经读到了文件结尾
      yield buf
      break
    buf += chunk

with open("input.txt") as f:
    for line in myreadlines(f, "{|}"):
        print (line)