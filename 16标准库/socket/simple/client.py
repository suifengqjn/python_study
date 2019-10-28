# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
client.connect(("", port))

# 发送
client.send("我是客户端:你好".encode("utf8"))

# 接收小于 1024 字节的数据
msg = client.recv(1024)
client.close()

print (msg.decode('utf-8'))