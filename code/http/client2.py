import urllib.request

fhand = urllib.request.urlopen('http://127.0.0.1:9000/romeo.txt') # 使用urllib模块请求URL
for line in fhand:
    print(line.decode().strip()) # 逐行读取并打印服务器的响应
# 使用urllib模块通过更高级的方式发送HTTP请求，适合于更复杂的HTTP通信
# urllib 是高级HTTP库，封装了复杂的细节，适合快速、简单地进行HTTP通信
# TCP 是传输层协议，负责数据的可靠传输
# HTTP 是应用层协议，基于TCP，用于传输超文本（如网页）
