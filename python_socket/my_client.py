import socket

socket_client = socket.socket()

socket_client.connect(("localhost", 8888))

while True:
    msg = input("请输入发给服务端的消息：")
    if msg == "exit":
        break
    socket_client.send(msg.encode("UTF-8"))

    recv_data = socket_client.recv(1024)
    print(f"服务端返回：{recv_data.decode('UTF-8')}")

socket_client.close()