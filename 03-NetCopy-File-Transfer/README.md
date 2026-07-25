# NetCopy File Transfer

A distributed file transfer system implemented in Python that verifies file integrity using MD5 checksums. The project consists of three independent services that work together to transfer files and validate that the received file has not been corrupted during transmission.

## Overview

The system demonstrates how multiple network services can cooperate to perform a reliable file transfer. Before sending a file, the client calculates its MD5 checksum and stores it on a dedicated checksum server. After the transfer is complete, the receiving server retrieves the stored checksum and compares it with the checksum of the received file to verify its integrity.

## Features

- Transfer files over TCP
- Automatic MD5 checksum generation
- File integrity verification
- Dedicated checksum management service
- Multi-service client-server architecture
- Concurrent checksum server using threads
- Error handling for failed transfers and checksum validation

## Architecture

```
+----------------+  TCP   +----------------+
| NetCopy Client | -----> | NetCopy Server |
+----------------+        +----------------+
         |
         | TCP
         | 
         ▼
+-----------------+
| Checksum Server |
+-----------------+
```

### Workflow

1. The client calculates the MD5 checksum of the selected file.
2. The client uploads the file to the NetCopy server.
3. The client stores the checksum on the Checksum Server.
4. The NetCopy server receives and saves the file.
5. The NetCopy server requests the stored checksum.
6. The received file's checksum is calculated and compared.
7. The server reports whether the file was transferred successfully or corrupted.

## Technologies

- Python
- TCP Sockets
- Multithreading (`threading`)
- MD5 Hashing (`hashlib`)
- File I/O

## Project Structure

```
03-NetCopy-File-Transfer/
│
├── netcopy_client.py
├── netcopy_server.py
├── checksum_server.py
└── README.md
```

### Components

#### `netcopy_client.py`

- Calculates the MD5 checksum of the file
- Uploads the file to the NetCopy server
- Stores the checksum on the Checksum Server

#### `netcopy_server.py`

- Receives files from clients
- Retrieves the stored checksum
- Calculates the checksum of the received file
- Verifies file integrity

#### `checksum_server.py`

- Stores checksums associated with file identifiers
- Handles checksum retrieval requests
- Supports expiration of stored checksum entries
- Uses a separate thread for each client connection

## Running the Project

Start the checksum server:

```bash
python checksum_server.py <host> <port>
```

Start the NetCopy server:

```bash
python netcopy_server.py <server_host> <server_port> <checksum_host> <checksum_port> <file_id> <output_file>
```

Run the client:

```bash
python netcopy_client.py <server_host> <server_port> <checksum_host> <checksum_port> <file_id> <input_file>
```

## Example

```bash
python checksum_server.py localhost 9000

python netcopy_server.py localhost 8000 localhost 9000 1 received.txt

python netcopy_client.py localhost 8000 localhost 9000 1 document.txt
```

If the checksums match, the server reports:

```
CSUM OK
```

Otherwise:

```
CSUM CORRUPTED
```

## Networking Concepts Demonstrated

- TCP socket programming
- Distributed client-server architecture
- File transfer protocols
- Cryptographic hashing for integrity verification
- Concurrent server implementation
- Network communication between independent services
- Error detection and validation

## Learning Objectives

This project demonstrates how distributed applications can combine multiple services to perform reliable file transfers while ensuring data integrity through checksum verification.
