import socket

server_addr=('localhost',10000)

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
    client.connect(server_addr)
    client.sendall('Give me the task'.encode())
    data= client.recv(32)
    print('received: ',data.decode())
    if data.decode() == 'Here is the task':
        client.sendall('Thank you'.encode())
        data=client.recv(32)
        print('received: ',data.decode())

