# Circuit Allocation

A network resource allocation simulator implemented in Python. The program processes connection requests over time, allocates network circuits based on available link capacities, and releases resources when connections terminate.

## Overview

The simulator models a communication network in which endpoints are connected via switches and links with limited capacities. Incoming traffic demands are allocated to predefined circuits if sufficient bandwidth is available.

The network topology, possible routing paths, and simulation events are loaded from a JSON configuration file.

## Features

- JSON-based network configuration
- Event-driven simulation
- Circuit allocation and deallocation
- Bandwidth management
- Capacity verification
- Multiple routing paths
- Chronological event processing

## Technologies

- Python
- JSON
- Graph-based network modeling

## Project Structure

```
05-Circuit-Allocation/
│
├── circuit_allocator.py
├── sample_network.json
└── README.md
```

## Input Configuration

The JSON configuration describes:

- Network endpoints
- Switches
- Links and capacities
- Available circuits
- Simulation duration
- Traffic demands

## Simulation Workflow

1. Load the network topology.
2. Read all traffic demands.
3. Convert demands into allocation and deallocation events.
4. Sort events chronologically.
5. Attempt to allocate each demand to a valid circuit.
6. Reduce available link capacities.
7. Release capacities when demands expire.
8. Report successful and unsuccessful allocations.

## Example Topology

```
     A ----- S1 ----- S4 ----- D
             |         |
             |         |
             S3 ----- S2
             |
             |
             C
```

## Output

For each simulation event, the program reports whether a circuit allocation succeeded or failed and when resources are released.

Example:

```
1. demand allocation: A<->C st:1 - successful
2. demand allocation: B<->C st:2 - successful
3. demand deallocation: A<->C st:5
```

## Networking Concepts Demonstrated

- Circuit switching
- Bandwidth allocation
- Capacity management
- Event-driven simulation
- Network topology modeling
- Resource scheduling
- Routing over predefined paths

## Learning Objectives

This project demonstrates how communication networks allocate finite resources over time while maintaining link capacity constraints and supporting concurrent traffic demands.
