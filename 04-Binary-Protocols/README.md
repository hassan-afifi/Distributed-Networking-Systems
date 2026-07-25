# Binary Protocols

A Python project demonstrating the creation and parsing of custom binary data structures using the `struct` module. The project illustrates how structured binary messages can be serialized, stored, and reconstructed according to predefined binary layouts.

## Overview

Binary protocols are commonly used in networking, embedded systems, and file formats because they provide compact and efficient data representation.

This project consists of two programs:

- A protocol generator that serializes structured data into a binary file.
- A protocol parser that deserializes binary data according to different protocol layouts.

## Features

- Binary serialization
- Binary deserialization
- Custom protocol layouts
- File-based binary storage
- Packing and unpacking structured data
- Multiple protocol formats

## Technologies

- Python
- `struct`
- Binary file I/O

## Project Structure

```
04-Binary-Protocols/
│
├── protocol_generator.py
├── protocol_parser.py
└── README.md
```

## Components

### `protocol_generator.py`

Creates binary records using user-specified `struct` format strings and stores the serialized data in a binary file.

### `protocol_parser.py`

Reads binary files, determines the expected record size, and reconstructs the original values using predefined binary formats.

## Example Binary Layouts

Examples of supported fields include:

| Type | Description |
|------|-------------|
| `?` | Boolean |
| `c` | Character |
| `i` | Integer |
| `f` | Floating-point number |
| `9s` | Fixed-length string |

## How It Works

1. A format string defines the binary layout.
2. Values are packed into a binary representation.
3. The binary data is written to a file.
4. The parser reads the file.
5. The original values are reconstructed by unpacking the binary data.

## Learning Objectives

This project demonstrates:

- Binary serialization
- Data encoding and decoding
- Custom protocol design
- Binary file formats
- Python's `struct` module
- Fixed-size binary records
