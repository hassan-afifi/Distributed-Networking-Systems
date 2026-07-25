# Guessing Game

A multiplayer client-server guessing game implemented in Python using TCP sockets and a custom binary communication protocol. Clients connect to the server and use a binary search strategy to identify a randomly generated number while the server manages concurrent connections and game state.

## Features

- TCP client-server communication
- Custom binary protocol
- Binary serialization using `struct`
- Concurrent client handling with `select()`
- Automatic binary search strategy
- Multiplayer support
- Game state synchronization

## Architecture

```
            TCP
+---------+      +---------+
| Client  | ---> |         |
+---------+      |         |
                 | Server  |
+---------+ ---> |         |
| Client  |      |         |
+---------+      +---------+
```

## Technologies

- Python
- TCP Sockets
- `select()`
- `struct`
- Binary Protocols

## Project Structure

```
02-Guessing-Game/
├── client.py
└── server.py
```

## Communication Protocol

Each message consists of **5 bytes**:

| Bytes | Description |
|------:|-------------|
| 1 | Operator (`>`, `<`, `=` or server response) |
| 4 | Integer value |

### Client Requests

| Operator | Meaning |
|----------|---------|
| `>` | Is the target number greater than the provided value? |
| `<` | Is the target number less than the provided value? |
| `=` | Guess the exact number |

### Server Responses

| Response | Meaning |
|----------|---------|
| `I` | Yes |
| `N` | No |
| `Y` | Correct guess |
| `K` | Incorrect final guess |
| `V` | Game has ended |

## How It Works

1. The server generates a random number.
2. Clients connect over TCP.
3. Each client performs a binary search by sending comparison requests.
4. The first client to correctly guess the number wins.
5. The server notifies the remaining clients that the game has ended.

## Learning Objectives

This project demonstrates:

- TCP socket programming
- Binary protocol design
- Data serialization
- Concurrent server implementation
- Event-driven I/O with `select()`
- Binary search algorithms
