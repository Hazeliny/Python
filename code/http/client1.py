import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 创建一个TCP套接字
mysock.connect(('127.0.0.1', 9000)) # 连接到服务器地址 127.0.0.1 和端口 9000
cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode() # 发送GET请求
mysock.send(cmd)

# 接收服务器返回的数据
while True:
    data = mysock.recv(512) # 每次接收512字节
    if len(data) < 1:
        break # 如果数据为空，表示接收结束
    print(data.decode(),end='') # 打印接收到的数据

mysock.close() # 关闭连接
# 通过socket模块发送HTTP GET请求并接收响应，直接与服务器进行TCP通信
# socket 是一个底层模块，允许你直接处理网络连接和通信，适合需要控制所有细节的网络编程
# TCP 是传输层协议，负责数据的可靠传输
# HTTP 是应用层协议，基于TCP，用于传输超文本（如网页）
