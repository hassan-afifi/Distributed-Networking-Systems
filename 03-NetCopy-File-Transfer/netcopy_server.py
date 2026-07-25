import socket
import hashlib
import sys

def receive_file_from_client(server_host, server_port, filename):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((server_host, server_port))
            s.listen(1)
            
            print("Waiting for connection on", server_host, ":", server_port, "...")
            conn, addr = s.accept()
            print("Connected to", addr)
            
            with open(filename, 'wb') as f:
                while True:
                    data = conn.recv(4096)
                    if not data:
                        break
                    f.write(data)
            
            conn.close()
            return True
            
    except Exception as e:
        print("Error receiving file:", e)
        return False

def retrieve_checksum(checksum_host, checksum_port, file_id):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((checksum_host, checksum_port))
            message = str("KI|", file_id)
            s.sendall(message.encode('utf-8'))
            response = s.recv(1024).decode('utf-8').strip()
            
            if response == "0|":
                return None
            
            parts = response.split('|')
            if len(parts) >= 2 and parts[0] != "0":
                return parts[1]
            
            return None
            
    except Exception as e:
        print("Error retrieving checksum:", e)
        return None

def calculate_md5_checksum(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

server_host = sys.argv[1]
server_port = int(sys.argv[2])
checksum_host = sys.argv[3]
checksum_port = int(sys.argv[4])
file_id = int(sys.argv[5])
filename = sys.argv[6]

try:
    print("Waiting for file transfer...")
    if not receive_file_from_client(server_host, server_port, filename):
        print("Failed to receive file")
        sys.exit(1)
    
    print("File received successfully")
    
    print("Retrieving checksum...")
    stored_checksum = retrieve_checksum(checksum_host, checksum_port, file_id)
    
    if stored_checksum is None:
        print("CSUM CORRUPTED")
        sys.exit(1)
    
    print("Calculating checksum of received file...")
    calculated_checksum = calculate_md5_checksum(filename)
    
    if stored_checksum == calculated_checksum:
        print("CSUM OK")
    else:
        print("CSUM CORRUPTED")
        print("Stored checksum:", stored_checksum)
        print("Calculated checksum:", calculated_checksum)

except Exception as e:
    print("Error:", e)
    sys.exit(1)