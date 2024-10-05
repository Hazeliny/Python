# https://docs.python.org/3/howto/sockets.html
# https://stackoverflow.com/questions/8627986/how-to-keep-a-socket-open-until-client-closes-it
# https://stackoverflow.com/questions/10091271/how-can-i-implement-a-simple-web-server-using-python-without-using-any-libraries


from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM) # 创建TCP/IP套接字(Socket)。AF_INET表示使用IPv4，SOCK_STREAM表示使用TCP协议
    try :
	# 绑定服务器IP地址和端口号9000
        serversocket.bind(('localhost',9000))
	# 开始监听客户端连接，允许最大5个连接排队
        serversocket.listen(5)
	# 处理客户端请求，无限循环，保持服务器不断运行，等待客户端的连接请求
        while(1):
            (clientsocket, address) = serversocket.accept() # 接收客户端连接

            rd = clientsocket.recv(5000).decode() # 接收客户端请求数据，最大5000字节
            pieces = rd.split("\n") # 将请求按行分割
            if ( len(pieces) > 0 ) : print(pieces[0]) # 打印请求的第一行（通常是HTTP请求行）

		# 响应内容，返回HTML网页
            data = "HTTP/1.1 200 OK\r\n" # 响应状态行，表示请求成功
            data += "Content-Type: text/html; charset=utf-8\r\n" # 响应头，指定内容类型为HTML
            data += "\r\n"
            data += "<html><body>Hello Lin!</body></html>\r\n\r\n" # 响应正文，返回HTML页面
            clientsocket.sendall(data.encode()) # 将响应内容发送回客户端
            clientsocket.shutdown(SHUT_WR) # 关闭写操作

	# 关闭连接
    except KeyboardInterrupt :
        print("\nShutting down...\n"); # 捕获Ctrl+C中断，安全关闭服务器
    except Exception as exc :
        print("Error:\n");
        print(exc)

    serversocket.close() # 关闭服务器

print('Access http://localhost:9000')
createServer()

