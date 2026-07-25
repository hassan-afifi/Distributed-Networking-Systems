import socket
import threading
import time
import sys

class ChecksumServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.checksums = {}
        self.lock = threading.Lock()
    
    def handle_client(self, conn, addr):
        try:
            data = conn.recv(1024).decode('utf-8').strip()
            if not data:
                return
            
            if data.startswith("BE|"):
                self.handle_insert(conn, data)
            elif data.startswith("KI|"):
                self.handle_retrieve(conn, data)
            else:
                conn.send(b"ERROR")
                
        except Exception as e:
            print("Error handling client", addr, ":", e)
        finally:
            conn.close()
    
    def handle_insert(self, conn, data):
        try:
            parts = data.split('|')
            if len(parts) < 5:
                conn.send(b"ERROR")
                return
            
            file_id = int(parts[1])
            validity = int(parts[2])
            checksum_length = int(parts[3])
            checksum = parts[4]
            
            if len(checksum) != checksum_length:
                conn.send(b"ERROR")
                return
            
            expiration_time = time.time() + validity
            
            with self.lock:
                self.checksums[file_id] = {
                    'checksum': checksum,
                    'checksum_length': checksum_length,
                    'expiration': expiration_time
                }
            
            conn.send(b"OK")
            
        except Exception as e:
            print("Error in insert:", e)
            conn.send(b"ERROR")
    
    def handle_retrieve(self, conn, data):
        try:
            parts = data.split('|')
            if len(parts) < 2:
                conn.send(b"0|")
                return
            
            file_id = int(parts[1])
            current_time = time.time()
            
            with self.lock:
                if file_id in self.checksums:
                    checksum_data = self.checksums[file_id]
                    
                    if current_time > checksum_data['expiration']:
                        del self.checksums[file_id]
                        conn.send(b"0|")
                    else:
                        response = str(checksum_data["checksum_length"], "|", checksum_data["checksum"])
                        conn.send(response.encode('utf-8'))
                else:
                    conn.send(b"0|")
                    
        except Exception as e:
            print("Error in retrieve:", e)
            conn.send(b"0|")
    
    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.host, self.port))
            s.listen(5)
            print("Checksum server listening on", self.host, ":", self.port)
            
            while True:
                conn, addr = s.accept()
                client_thread = threading.Thread(
                    target=self.handle_client, 
                    args=(conn, addr)
                )
                client_thread.daemon = True
                client_thread.start()
    
host = sys.argv[1]
port = int(sys.argv[2])

server = ChecksumServer(host, port)
server.start()