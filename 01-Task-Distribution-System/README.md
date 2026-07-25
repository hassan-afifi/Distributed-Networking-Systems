# Task Distribution System

A distributed task assignment system implemented in Python using both TCP and UDP sockets. The application consists of a TCP server, a TCP client, and a UDP archive service that work together to distribute tasks once predefined conditions are met.

## Features

- TCP client-server communication
- UDP archive service
- Concurrent client handling using `select()`
- Task distribution workflow
- Request-response messaging
- Simple distributed architecture

## Architecture

```
                
+--------+   TCP   +--------+
| Client | <-----> | Server |
+--------+         +--------+
                       |
                       | UDP
                       |
                       ▼
              +----------------+
              | Archive Server |
              +----------------+
```

## Technologies

- Python
- TCP Sockets
- UDP Sockets
- `select()`
- Client-Server Architecture

## Project Structure

```
01-Task-Distribution-System/
├── client.py
├── server.py
└── archive.py
```

## How It Works

1. The client connects to the TCP server.
2. The client requests a task.
3. The server tracks incoming requests.
4. Once the configured condition is satisfied, the server contacts the archive service using UDP.
5. The archive server returns a randomly selected task.
6. The server delivers the task to the client.

## Learning Objectives

This project demonstrates:

- TCP communication
- UDP communication
- Concurrent server design
- Inter-process communication
- Distributed system fundamentals
