# coding=utf-8
# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 9999

# 绑定端口号
err = serversocket.bind(("", port))
if err != None:
    raise err
else:
    print("listening {}".format(port))

# 设置最大连接数，超过后排队
serversocket.listen(5)


while True:
    client, addr = serversocket.accept()
    # 建立客户端连接
    data = client.recv(1024)
    print("收到消息",data.decode("utf8"))
    msg = '欢迎访问菜鸟教程！' + "\r\n"
    client.send(msg.encode('utf-8'))
    client.close()
