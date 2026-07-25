import socket
import struct
import sys
import select
import random

class GuessingGameServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.clients = []
        self.game_over = False
        self.target_number = 0
        self.start_new_game()
    
    def start_new_game(self):
        self.target_number = random.randint(1, 100)
        self.game_over = False
        print("New game started! Target number:", self.target_number)
    
    def unpack_client_message(self, data):
        if len(data) != 5:
            return None, None
        
        operator = chr(data[0])
        number = struct.unpack('I', data[1:5])[0] 
        return operator, number
    
    def pack_server_message(self, response_char, number=0):
        char_byte = response_char.encode('ascii')[0]
        number_bytes = struct.pack('I', number)
        return bytes([char_byte]) + number_bytes
    
    def handle_client_message(self, client_socket, data):
        if self.game_over:
            return self.pack_server_message('V')
        
        operator, number = self.unpack_client_message(data)
        if operator is None:
            return self.pack_server_message('N')
        
        if operator == '<':
            if self.target_number < number:
                return self.pack_server_message('I')
            else:
                return self.pack_server_message('N')
        elif operator == '>':
            if self.target_number > number:
                return self.pack_server_message('I')
            else:
                return self.pack_server_message('N')
        elif operator == '=':
            if self.target_number == number:
                self.game_over = True
                return self.pack_server_message('Y')
            else:
                return self.pack_server_message('K')
        else:
            return self.pack_server_message('N')
    
    def broadcast_game_over(self):
        end_message = self.pack_server_message('V')
        
        for client_socket, _ in self.clients:
            try:
                client_socket.send(end_message)
            except:
                pass
    
    def recv_full(self, sock, length):
        data = b''

        while len(data) < length:
            more = sock.recv(length - len(data))
            
            if not more:
                return None
    
            data = data + more
        
        return data

    def run(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print("Guessing Game Server running on", self.host, ":", self.port)

        while True:
            read_sockets = [self.server_socket] + [client[0] for client in self.clients]
            
            try:
                ready_to_read, _, _ = select.select(read_sockets, [], [])
            except select.error:
                break
            
            for sock in ready_to_read:
                if sock == self.server_socket:
                    client_socket, client_address = self.server_socket.accept()
                    print("New client connected:", client_address)
                    self.clients.append((client_socket, client_address))
                else:
                    try:
                        data = self.recv_full(sock, 5)
                        
                        if data:
                            if len(data) == 5:
                                response = self.handle_client_message(sock, data)
                                sock.send(response)
                                
                                if self.game_over and chr(response[0]) == 'Y':
                                    print("Game over! Client won!")
                                    self.broadcast_game_over()
                                    
                                    for client_socket, addr in self.clients:
                                        client_socket.close()
                                    self.clients = []
                                    
                                    self.start_new_game()
                            else:
                                print("Invalid message length:", len(data), "bytes")
                        else:
                            for i, (client_socket, addr) in enumerate(self.clients):
                                if client_socket == sock:
                                    print("Client disconnected:", addr)
                                    self.clients.pop(i)
                                    break
                            
                            sock.close()
                    except Exception as e:
                        print("Error with client:", e)

                        for i, (client_socket, addr) in enumerate(self.clients):
                            if client_socket == sock:
                                self.clients.pop(i)
                                break
                        
                        sock.close()
        
        self.server_socket.close()

host = sys.argv[1]
port = int(sys.argv[2])
server = GuessingGameServer(host, port)
server.run()
