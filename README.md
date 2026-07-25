# Distributed Networking Systems

A collection of networking projects developed as part of a university course on distributed networking systems. This repository demonstrates practical implementations of TCP/UDP communication, concurrent client-server architectures, custom binary protocols, file transfer, network simulation, and resource allocation using Python.

---

## Projects

### 1. [Task Distribution System](01-Task-Distribution-System)
A distributed task assignment system consisting of a TCP server, TCP client, and UDP archive service. The server coordinates client requests and communicates with the archive service to retrieve tasks once predefined conditions are met.

**Concepts**
- TCP sockets
- UDP sockets
- Concurrent servers with `select`
- Client-server communication
- Distributed services

---

### 2. Guessing Game
A multiplayer client-server guessing game using a custom binary communication protocol. Multiple clients connect to a TCP server and locate a randomly generated number using a binary search strategy.

**Concepts**
- TCP sockets
- Binary protocols
- Serialization with `struct`
- Concurrent client handling
- Binary search algorithm

---

### 3. NetCopy File Transfer
A client-server file transfer application implementing reliable file transmission together with checksum verification to ensure data integrity.

**Concepts**
- TCP sockets
- File transfer
- Data integrity
- Checksum verification

---

### 4. Binary Protocols
A collection of exercises demonstrating the design, serialization, parsing, and processing of custom binary network protocols.

**Concepts**
- Binary message formats
- Serialization
- Protocol parsing
- Network packet processing

---

### 5. Circuit Allocation
Simulation of circuit allocation algorithms used in computer networks to manage limited communication resources efficiently.

**Concepts**
- Resource allocation
- Network simulation
- Routing concepts
- Algorithm implementation

---

### 6. Mininet Topology
A custom virtual network topology built using Mininet, including multiple hosts, switches, and routers configured to simulate a realistic computer network.

**Concepts**
- Mininet
- Linux networking
- Virtual network topology
- Routing
- Network simulation

---

## Technologies

- Python
- TCP/IP
- UDP
- Socket Programming
- `select()`
- `struct`
- Mininet
- Linux Networking

---

## Repository Structure

```
DistributedNetworkingSystems/
├── 01-Task-Distribution-System/
├── 02-Guessing-Game/
├── 03-NetCopy-File-Transfer/
├── 04-Binary-Protocols/
├── 05-Circuit-Allocation/
└── 06-Mininet-Topology/
```

Each project contains its own README with setup instructions and implementation details.

---

## Learning Objectives

These projects explore fundamental concepts in distributed networking, including:

- Client-server architectures
- Concurrent network programming
- TCP and UDP communication
- Binary protocol design
- File transfer mechanisms
- Network simulation
- Routing and resource allocation

---

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License**.

https://creativecommons.org/licenses/by-nc-nd/4.0/
