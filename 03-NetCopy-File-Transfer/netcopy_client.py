import socket
import hashlib
import sys

def calculate_md5_checksum(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def send_file_to_server(server_host, server_port, filename):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_host, server_port))
            
            with open(filename, 'rb') as f:
                while True:
                    data = f.read(4096)
                    if not data:
                        break
                    s.sendall(data)
            
            s.shutdown(socket.SHUT_WR)
            
    except Exception as e:
        print("Error sending file to server:", e)
        return False
    return True

def store_checksum(checksum_host, checksum_port, file_id, checksum, validity=60):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((checksum_host, checksum_port))
            
            checksum_length = len(checksum)
            message = str("BE|", file_id, "|", validity, "|", checksum_length, "|", checksum)

            s.sendall(message.encode('utf-8'))
            response = s.recv(1024).decode('utf-8').strip()
            
            return response == "OK"
            
    except Exception as e:
        print("Error storing checksum:", e)
        return False

server_host = sys.argv[1]
server_port = int(sys.argv[2])
checksum_host = sys.argv[3]
checksum_port = int(sys.argv[4])
file_id = int(sys.argv[5])
filename = sys.argv[6]

try:
    print("Calculating checksum...")
    checksum = calculate_md5_checksum(filename)
    print("Checksum:", checksum)
    
    print("Sending file to netcopy server...")
    if not send_file_to_server(server_host, server_port, filename):
        print("Failed to send file")
        sys.exit(1)
    
    print("Storing checksum...")
    if not store_checksum(checksum_host, checksum_port, file_id, checksum):
        print("Failed to store checksum")
        sys.exit(1)
    
    print("File transfer and checksum storage completed successfully")
    
except FileNotFoundError:
    print("Error: File", filename, "not found")
    sys.exit(1)
except Exception as e:
    print("Error:", e)
    sys.exit(1)
