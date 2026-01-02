# RPyC (Remote Python Call)

**RPyC** adalah library Python yang kuat untuk *Remote Procedure Call*. Berbeda dengan XML-RPC atau gRPC yang dirancang untuk interoperabilitas antar bahasa, RPyC dirancang khusus untuk **Python-to-Python**.

## Konsep Utama

### 1. Transparansi Penuh
Fitur "killer" dari RPyC adalah transparansinya. Anda bisa mengakses atribut objek remote, memanggil method, bahkan melakukan slicing list remote seolah-olah benda itu ada di komputer lokal Anda. RPyC menangani semua "sihir" jaringan di belakang layar.

### 2. Arsitektur Simetris
Dalam RPyC, perbedaan antara Client dan Server bisa menjadi kabur. Client bisa melayani request dari Server, dan sebaliknya.

## Implementasi dalam Demo

File demo terdapat di folder `rpyc-demo/`.

### Server (`server.py`)

RPyC menggunakan konsep `Service`. Anda membuat class yang mewarisi `rpyc.Service`.

```python
import rpyc

class CalculatorService(rpyc.Service):
    def exposed_add(self, x, y):
        return x + y

    def exposed_subtract(self, x, y):
        return x - y

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(CalculatorService, port=18861)
    t.start()
```

*   **Penting**: Hanya method yang diawali dengan `exposed_` yang bisa diakses dari luar. Ini adalah fitur keamanan dasar RPyC.

### Client (`client.py`)

```python
import rpyc

conn = rpyc.connect("localhost", 18861)
result = conn.root.add(5, 3)
print(result)
```

*   `conn.root` adalah entry point ke service remote.
*   Perhatikan kita memanggil `add`, bukan `exposed_add`. RPyC otomatis memetakan nama tersebut.

## Kelebihan dan Kekurangan

**Kelebihan:**
*   **Sangat Pythonic**: Terasa sangat natural bagi developer Python.
*   **Powerful**: Mendukung callback, exception propagation (error di server muncul di client), dan object proxying.
*   **Fleksibel**: Bisa digunakan untuk clustering, testing remote, dll.

**Kekurangan:**
*   **Keamanan**: Karena sangat powerful (bisa akses internal Python), RPyC harus diamankan dengan hati-hati jika digunakan di jaringan publik.
*   **Spesifik Python**: Tidak bisa digunakan jika Client ditulis dalam Java atau JavaScript.
