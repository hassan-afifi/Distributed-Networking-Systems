# Mininet Topology

A custom network topology implemented with Mininet to simulate a routed network consisting of multiple hosts, Linux Bridge switches, and software routers. The project demonstrates virtual network construction, IP forwarding, and network emulation in a Linux environment.

## Overview

This project creates a virtual network using Mininet by defining hosts, switches, routers, and their interconnections programmatically. The topology can be launched locally, providing an interactive environment for testing connectivity, routing behavior, and network configurations without requiring physical networking hardware.

## Features

- Custom Mininet topology
- Multiple hosts, switches, and routers
- Linux Bridge switches
- IP forwarding on router nodes
- Interactive Mininet CLI
- Programmatic topology creation
- Easily extensible network design

## Technologies

- Python
- Mininet
- Linux Bridge
- Linux Networking
- IP Routing

## Project Structure

```text
06-Mininet-Topology/
│
├── topology.py
└── README.md
```
## Configuration

After launching the topology, the commands in `network_configuration.txt` can be executed within the Mininet CLI to configure the network.

The configuration file includes:

- IP address assignment
- Default gateway configuration
- Static routing
- NAT port forwarding using `iptables`
- Firewall rules for packet filtering

This separates the topology definition from the network configuration, following a modular approach commonly used in network administration.

## Network Components

The topology includes:

- 6 Hosts
- 5 Linux Bridge switches
- 3 Software routers
- Multiple interconnected network segments

## How It Works

1. Initializes the Mininet environment.
2. Creates hosts, Linux Bridge switches, and router nodes.
3. Enables IP forwarding on the router nodes.
4. Establishes links between all network devices.
5. Builds and starts the virtual network.
6. Launches the Mininet CLI for interactive experimentation.
7. Stops the network when the CLI session ends.

## Running the Project

Start the topology with:

```bash
sudo python topology.py
```

Once the topology is running, the Mininet CLI becomes available:

```bash
mininet>
```

Example commands:

```bash
pingall
nodes
links
net
```

## Networking Concepts Demonstrated

- Network virtualization
- Custom topology design
- Layer 2 switching
- Layer 3 routing
- IP forwarding
- Linux Bridge configuration
- Network emulation using Mininet

## Learning Objectives

This project demonstrates how virtual network topologies can be created and tested using Mininet. It provides hands-on experience with network emulation, routing, switching, and software-defined network experimentation in a controlled environment.
