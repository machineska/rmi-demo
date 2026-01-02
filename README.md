# RMI/RPC Demo Project

This project demonstrates various Remote Method Invocation (RMI) and Remote Procedure Call (RPC) technologies implemented in Python. It showcases different approaches to distributed computing and inter-process communication.

## 📋 Table of Contents

- [Overview](#overview)
- [Technologies Demonstrated](#technologies-demonstrated)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Demos](#demos)
  - [1. gRPC Demo](#1-grpc-demo)
  - [2. XML-RPC Demo](#2-xml-rpc-demo)
  - [3. RPyC Demo](#3-rpyc-demo)
  - [4. ZeroRPC Demo](#4-zerorpc-demo)
  - [5. Pyro5 Demo](#5-pyro5-demo)
  - [6. GraphQL Demo](#6-graphql-demo)
- [Running the Demos](#running-the-demos)
- [One-Command Run](#one-command-run)
- [Troubleshooting](#troubleshooting)
- [Comparison of Technologies](#comparison-of-technologies)

## 🎯 Overview

This project is designed for educational purposes to demonstrate different RMI/RPC technologies available in Python. Each demo implements a simple calculator service with basic arithmetic operations (addition and subtraction) to showcase how different technologies handle remote method invocation.

## 🛠 Technologies Demonstrated

1. **gRPC** - Google's high-performance RPC framework
2. **XML-RPC** - Simple RPC protocol using XML over HTTP
3. **RPyC** - Remote Python Call framework
4. **ZeroRPC** - RPC library based on ZeroMQ and MessagePack
5. **Pyro5** - Python Remote Objects framework
6. **GraphQL** - Query language and runtime for APIs (using Django)

## 📁 Project Structure

```
rmi-demo/
├── grpc-demo/              # gRPC implementation
│   ├── calculator.proto    # Protocol buffer definition
│   ├── calculator_pb2.py   # Generated Python classes
│   ├── calculator_pb2_grpc.py # Generated gRPC classes
│   ├── server.py          # gRPC server
│   ├── client.py          # gRPC client
│   └── Readme.md          # gRPC compilation command
├── xmlrpc-demo/           # XML-RPC implementation
│   ├── server.py          # XML-RPC server
│   └── client.py          # XML-RPC client
├── rpyc-demo/             # RPyC implementation
│   ├── server.py          # RPyC server
│   └── client.py          # RPyC client
├── zerorpc-demo/          # ZeroRPC implementation
│   ├── server.py          # ZeroRPC server
│   └── client.py          # ZeroRPC client
├── pyrofive/              # Pyro5 implementation
│   ├── server.py          # Pyro5 server
│   └── client.py          # Pyro5 client
├── graphql_demo/          # Django GraphQL implementation
│   ├── graphql_demo/      # Django project settings
│   ├── books/             # Django app with Book model
│   ├── manage.py          # Django management script
│   └── Readme.md          # GraphQL query examples
├── requirements.txt       # Project dependencies
└── main.py               # Sample Python script (not used in demos)
```

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🚀 Installation

1. Clone or download this project
2. Navigate to the project directory
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Dependencies

The project requires the following Python packages:
- `Pyro5` - For Pyro5 RMI
- `rpyc` - For RPyC framework
- `zerorpc` - For ZeroRPC implementation
- `grpcio` - For gRPC runtime
- `grpcio-tools` - For gRPC development tools
- `django` - For GraphQL demo backend
- `graphene-django` - For GraphQL integration with Django

## 🎮 Demos

### 1. gRPC Demo

**Technology**: Google's high-performance, open-source RPC framework that uses Protocol Buffers.

**Features**:
- Type-safe communication using Protocol Buffers
- High performance with HTTP/2
- Supports multiple programming languages
- Built-in authentication, load balancing, and more

**Files**:
- `calculator.proto`: Defines the service interface and message types
- `server.py`: Implements the Calculator service
- `client.py`: Connects to server and calls remote methods

**How it works**:
1. Protocol buffer definition specifies the service interface
2. Generated Python code provides client and server stubs
3. Server implements the service methods
4. Client creates a channel and calls remote methods

### 2. XML-RPC Demo

**Technology**: Simple RPC protocol that uses XML to encode calls and HTTP as transport.

**Features**:
- Built into Python standard library
- Human-readable XML format
- Simple to implement and debug
- Cross-platform compatibility

**Files**:
- `server.py`: Creates XML-RPC server with exposed functions
- `client.py`: Connects to server using ServerProxy

**How it works**:
1. Server registers functions to be called remotely
2. Client creates a proxy object pointing to the server
3. Remote function calls are serialized to XML and sent over HTTP

### 3. RPyC Demo

**Technology**: Remote Python Call - transparent and symmetric distributed computing.

**Features**:
- Transparent remote object access
- Symmetric architecture (both ends can serve)
- Built-in security features
- Supports object serialization

**Files**:
- `server.py`: Defines service class with exposed methods
- `client.py`: Connects and calls remote methods

**How it works**:
1. Server defines a service class inheriting from rpyc.Service
2. Methods prefixed with "exposed_" are available remotely
3. Client connects and accesses methods through conn.root

### 4. ZeroRPC Demo

**Technology**: RPC library based on ZeroMQ and MessagePack for fast communication.

**Features**:
- High performance with ZeroMQ transport
- Efficient MessagePack serialization
- Asynchronous communication support
- Language agnostic

**Files**:
- `server.py`: Creates ZeroRPC server with Calculator class
- `client.py`: Connects and calls remote methods

**How it works**:
1. Server binds a class to a TCP endpoint
2. Client connects to the endpoint
3. Method calls are serialized with MessagePack and sent over ZeroMQ

### 5. Pyro5 Demo

**Technology**: Python Remote Objects - distributed object technology for Python.

**Features**:
- True distributed objects
- Name server for object discovery
- Automatic proxy generation
- Security features and SSL support

**Files**:
- `server.py`: Registers Calculator class with Pyro daemon
- `client.py`: Locates and uses remote object

**How it works**:
1. Server registers object with Pyro daemon and name server
2. Client locates object by name through name server
3. Transparent method calls on remote objects

**Note**: Requires running Pyro name server: `python -m Pyro5.nameserver`

### 6. GraphQL Demo

**Technology**: Query language and runtime for APIs, implemented with Django and Graphene.

**Features**:
- Flexible query language
- Single endpoint for all operations
- Strong type system
- Real-time subscriptions support

**Files**:
- `models.py`: Defines Book model
- `schema.py`: GraphQL schema with queries and mutations
- `settings.py`: Django configuration with GraphQL setup
- `urls.py`: URL routing including GraphQL endpoint

**How it works**:
1. Django models define data structure
2. GraphQL schema maps models to GraphQL types
3. Queries and mutations provide data access operations
4. GraphiQL interface available for testing

## 🏃‍♂️ Running the Demos

### General Pattern

For most demos (except GraphQL and Pyro5):
1. Start the server in one terminal
2. Run the client in another terminal

### Specific Instructions

#### gRPC Demo
```bash
# Generate Python code from proto file (if needed)
cd grpc-demo
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto

# Run server
python server.py

# Run client (in another terminal)
python client.py
```

#### XML-RPC Demo
```bash
cd xmlrpc-demo
# Terminal 1
python server.py

# Terminal 2
python client.py
```

#### RPyC Demo
```bash
cd rpyc-demo
# Terminal 1
python server.py

# Terminal 2
python client.py
```

#### ZeroRPC Demo
```bash
cd zerorpc-demo
# Terminal 1
python server.py

# Terminal 2
python client.py
```

#### Pyro5 Demo
```bash
# Terminal 1 - Start name server
python -m Pyro5.nameserver

# Terminal 2 - Start server
cd pyrofive
python server.py

# Terminal 3 - Run client
python client.py
```

#### GraphQL Demo
```bash
cd graphql_demo
# Run migrations (first time only)
python manage.py makemigrations
python manage.py migrate

# Start Django server
python manage.py runserver

# Access GraphiQL interface at: http://localhost:8000/graphql/
```

**Sample GraphQL Queries**:

Query all books:
```graphql
{
  allBooks {
    title
    author
    publishedYear
  }
}
```

Create a new book:
```graphql
mutation {
  createBook(title: "1984", author: "George Orwell", publishedYear: 1949) {
    book {
      title
      author
      publishedYear
    }
  }
}
```

## 🟢 One-Command Run

Gunakan skrip terpadu:

```bash
python run_demo.py grpc server    # terminal 1
python run_demo.py grpc client    # terminal 2

python run_demo.py xmlrpc server  # terminal 1
python run_demo.py xmlrpc client  # terminal 2

python run_demo.py pyro5 nameserver  # terminal 1
python run_demo.py pyro5 server      # terminal 2
python run_demo.py pyro5 client      # terminal 3

python run_demo.py graphql           # menjalankan server Django
```

## 🧰 Troubleshooting

- Dependencies belum terpasang: jalankan `pip install -r requirements.txt`.
- Port sudah dipakai: ubah port di file server terkait atau hentikan proses lain.
- Pyro5 perlu nameserver: jalankan `python -m Pyro5.nameserver` terlebih dahulu.
- gRPC stub tidak cocok: regenerasi dengan `python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto` di folder `grpc-demo`.
- ZeroRPC gagal menghubungkan: pastikan server berjalan dan alamat `tcp://127.0.0.1:4242` dapat diakses.

## 🐳 Docker Compose (opsional)

Menjalankan beberapa server sekaligus:

```bash
docker compose up -d
```

Layanan yang aktif: XML-RPC (9000), RPyC (18861), ZeroRPC (4242).

## 🧪 Benchmark (opsional)

Uji latensi sederhana:

```bash
python benchmarks/benchmark.py --iterations 200 --target all
```

## ⚖️ Comparison of Technologies

| Technology | Performance | Ease of Use | Language Support | Use Case |
|------------|-------------|-------------|------------------|----------|
| **gRPC** | Very High | Medium | Multi-language | Microservices, high-performance APIs |
| **XML-RPC** | Low | Very Easy | Multi-language | Simple integrations, legacy systems |
| **RPyC** | High | Easy | Python-focused | Python distributed applications |
| **ZeroRPC** | Very High | Medium | Multi-language | High-throughput, low-latency services |
| **Pyro5** | High | Easy | Python-only | Python distributed objects |
| **GraphQL** | Medium | Medium | Multi-language | Flexible APIs, frontend-backend communication |

### When to Use Each Technology

- **gRPC**: When you need high performance, type safety, and multi-language support
- **XML-RPC**: For simple integrations where human readability is important
- **RPyC**: For Python-centric distributed applications requiring transparency
- **ZeroRPC**: When maximum performance and minimal latency are critical
- **Pyro5**: For Python applications needing true distributed object capabilities
- **GraphQL**: For flexible APIs where clients need to specify exactly what data they want

## 🎓 Educational Value

This project demonstrates:
- Different approaches to remote method invocation
- Trade-offs between performance, simplicity, and features
- Protocol design considerations (binary vs. text, synchronous vs. asynchronous)
- Service discovery mechanisms
- Serialization strategies

Each technology represents different design philosophies and is suitable for different use cases in distributed systems development.
