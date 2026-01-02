# gRPC (Google Remote Procedure Call)

**gRPC** adalah framework RPC open-source berkinerja tinggi yang dikembangkan oleh Google. Ini adalah salah satu teknologi RPC paling populer saat ini, terutama untuk arsitektur Microservices.

## Konsep Utama

### 1. Protocol Buffers (Protobuf)
gRPC menggunakan **Protocol Buffers** sebagai Interface Definition Language (IDL) dan format pertukaran pesan dasarnya. Protobuf adalah mekanisme untuk menserialisasi data terstruktur (seperti XML, tapi lebih kecil, lebih cepat, dan lebih sederhana).

Anda mendefinisikan struktur data dan layanan di file `.proto`, lalu menggunakan compiler `protoc` untuk menghasilkan kode sumber akses data dalam bahasa pilihan Anda (Python, Java, Go, dll).

### 2. HTTP/2
gRPC dibangun di atas HTTP/2, yang memberikan keuntungan performa signifikan dibandingkan HTTP/1.1:
*   **Multiplexing**: Banyak request bisa dikirim lewat satu koneksi TCP.
*   **Header Compression**: Mengurangi overhead data.
*   **Server Push**: Server bisa mengirim data ke client tanpa diminta.

## Implementasi dalam Demo

File demo terdapat di folder `grpc-demo/`.

### Struktur File `.proto` (`calculator.proto`)

```protobuf
syntax = "proto3";

package calculator;

service Calculator {
  rpc Add (Number) returns (Number) {}
  rpc Subtract (Number) returns (Number) {}
}

message Number {
  float value = 1;
}
```

*   `service Calculator`: Mendefinisikan layanan dengan dua metode: `Add` dan `Subtract`.
*   `message Number`: Mendefinisikan struktur data yang dipertukarkan.

### Proses Code Generation

Sebelum menjalankan kode Python, kita harus "menerjemahkan" file `.proto` menjadi kode Python. Perintahnya:

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
```

Ini menghasilkan dua file:
1.  `calculator_pb2.py`: Kode untuk serialisasi pesan (`Number`).
2.  `calculator_pb2_grpc.py`: Kode untuk client stub dan server servicer.

### Server (`server.py`)

Server mengimplementasikan class `CalculatorServicer` yang dihasilkan dari protobuf.

```python
class Calculator(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        # ... logika penambahan ...
        return calculator_pb2.Number(value=result)
```

### Client (`client.py`)

Client membuat "Stub" (perwakilan lokal dari server remote).

```python
channel = grpc.insecure_channel('localhost:50051')
stub = calculator_pb2_grpc.CalculatorStub(channel)
response = stub.Add(calculator_pb2.Number(value=10))
```

## Kelebihan dan Kekurangan

**Kelebihan:**
*   Sangat efisien (binary serialization).
*   Strongly-typed (mengurangi bug tipe data).
*   Dukungan banyak bahasa (polyglot).

**Kekurangan:**
*   Kurang human-readable (format biner).
*   Proses development sedikit lebih panjang (edit proto -> compile -> code).
