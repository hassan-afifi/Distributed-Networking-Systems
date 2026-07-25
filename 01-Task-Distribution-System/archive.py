import socket
import sys
import random

server_address=('',10001)

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as server:
    server.bind(server_address)

    while True:
        data, client= server.recvfrom(256)
        data=data.decode()
        print(f'received: {data}, form: {client}')
        if data=='Search':
            x=random.randint(1,10)
            server.sendto(f'task {x}'.encode(),client)
