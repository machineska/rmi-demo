# ZeroRPC

**ZeroRPC** adalah framework RPC modern, ringan, dan cepat yang dibangun di atas dua teknologi hebat: **ZeroMQ** dan **MessagePack**.

## Konsep Utama

### 1. ZeroMQ (ZMQ)
ZeroMQ adalah library networking performa tinggi yang memberikan ilusi "socket on steroids". Ia menangani antrian pesan, koneksi ulang otomatis, dan pola komunikasi kompleks (seperti Pub-Sub) dengan sangat efisien. ZeroRPC menggunakan ZeroMQ sebagai lapisan transportnya.

### 2. MessagePack
MessagePack adalah format pertukaran data biner yang efisien. Ini seperti JSON tapi lebih cepat dan lebih kecil. ZeroRPC menggunakan MessagePack untuk menserialisasi data.

## Implementasi dalam Demo

File demo terdapat di folder `zerorpc-demo/`.

### Server (`server.py`)

```python
import zerorpc

class Calculator(object):
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

s = zerorpc.Server(Calculator())
s.bind("tcp://0.0.0.0:4242")
s.run()
```

Sangat bersih, bukan? Anda cukup membuat class Python biasa, lalu memberikannya ke `zerorpc.Server`.

### Client (`client.py`)

```python
import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")
print(c.add(10, 20))
```

## Kelebihan dan Kekurangan

**Kelebihan:**
*   **Performa Tinggi**: Kombinasi ZMQ dan MessagePack membuatnya sangat cepat.
*   **API Sederhana**: Kode server dan client sangat minimalis.
*   **Polyglot**: Ada library ZeroRPC untuk Node.js, Python, dan bahasa lain, sehingga bisa saling komunikasi.

**Kekurangan:**
*   **Dependensi Sistem**: Membutuhkan instalasi library C++ ZeroMQ di sistem operasi (meskipun `pip install zerorpc` biasanya menangani ini dengan binary wheels, terkadang bisa bermasalah di Windows).
*   **Fitur Terbatas**: Tidak se-kaya fitur gRPC (misalnya tidak ada streaming bidireksional yang canggih secara bawaan di level API high-level).
