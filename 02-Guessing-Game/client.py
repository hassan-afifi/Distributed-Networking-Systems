import socket
import struct
import sys

class GuessingGameClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.game_active = True
    
    def connect(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            print("Connected to server", self.host, ":", self.port)
            return True
        except Exception as e:
            print("Failed to connect:", e)
            return False
    
    def pack_client_message(self, operator, number):
        char_byte = operator.encode('ascii')[0]
        number_bytes = struct.pack('I', number)
        return bytes([char_byte]) + number_bytes
    
    def unpack_server_message(self, data):
        if len(data) != 5:
            return None
        response_char = chr(data[0])
        return response_char
    
    def send_guess(self, operator, number):
        try:
            message = self.pack_client_message(operator, number)
            self.socket.send(message)
            response = self.socket.recv(5)
            response_char = self.unpack_server_message(response)
            return response_char
        except Exception as e:
            print("Error communicating with server:", e)
            return None
    
    def binary_search_game(self):
        low = 1
        high = 100
        
        while self.game_active and low <= high:
            if self.game_active and low == high:
                print("Final guess: number =", low)
                response = self.send_guess('=', low)
            else:
                mid = (low + high) // 2
                print("Guessing: number >", mid)
                response = self.send_guess('>', mid)

            if response is None:
                break

            if response == 'I':
                print("  Response: Yes, number >", mid)
                low = mid + 1
            elif response == 'N':
                print("  Response: No, number <=", mid)
                high = mid - 1
            elif response == 'Y':
                print("Congratulations! You won!")
                self.game_active = False
            elif response == 'K':
                print("Game over! Wrong guess with '=' operator!")
                self.game_active = False
            elif response == 'V':
                print("Game ended by server!")
                self.game_active = False
    
    def run(self):
        if not self.connect():
            return
        
        try:
            self.binary_search_game()
        except KeyboardInterrupt:
            print("\nClient interrupted by user")
        finally:
            self.socket.close()
            print("Disconnected from server")

host = sys.argv[1]
port = int(sys.argv[2])
client = GuessingGameClient(host, port)
client.run()
