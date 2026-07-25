import socket
import select
import sys

server_addr=('',10000)


archive_addr=('localhost',10001)

if len(sys.argv)<2:
    print('error no limit was given')
    exit(1)

limit= int(sys.argv[1])
if limit < 1 or limit >5:
    print('error limit should be between 1 & 5')
    exit(2)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(server_addr)
    server.listen(1)
    inputs=[server]

    while True:
        r,_,_= select.select(inputs,[],[])
        for s in r:
            if s is server:
                client,clinet_addr=s.accept()
                inputs.append(client)
                print('client connected',clinet_addr)
            else:
                data=s.recv(32).decode()
                if not data:
                    inputs.remove(s)
                    s.close()
                    print('disconnected')
                else:
                    if data== 'Give me the task':
                        limit -=1
                        if limit <=0:
                            
                           with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as client:
                               client.sendto('Search'.encode(),archive_addr)
                               data,_ =client.recvfrom(256)
                               print('Received from: ', clinet_addr, ' data: ',data.decode())
                             
                           s.sendall(f'Here is the task'.encode())
                        else:
                            s.sendall('not ready'.encode())
                    elif data=='Thank you':
                       s.sendall('Welcome'.encode())
