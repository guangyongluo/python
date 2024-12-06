import socket

# 创建socket对象
socket_server = socket.socket()

# 绑定ip地址和端口
socket_server.bind(("localhost", 8888))

# 监听端口，传入可接受的连接数
socket_server.listen()

# 等待客户端连接
# result: tuple = socket_server.accept()
# conn = result[0] # 客户端和服务端的连接对象
# address = result[1] # 客户端的地址信息

# accept是阻塞方法
conn, address = socket_server.accept()


print(f"接受到客户端的连接，客户端的信息是：{address}")

while True:
    # recv接受参数是缓冲区大小
    # recv方法返回值是一个字节数组也就是bytes对象，不是字符串，可以通过decode方法进行编码，将字节数组编程成字符串对象
    data = conn.recv(1024).decode("UTF-8")

    print(f"客户端发来的消息是：{data}")

    # 发送回复消息
    msg = input("请输入你要和客户端回复的消息：").encode("UTF-8")

    if msg == 'exit':
        break
    conn.send(msg)

conn.close()
socket_server.close()




