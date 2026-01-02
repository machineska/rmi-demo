# XML-RPC

**XML-RPC** adalah spesifikasi panggilan prosedur jarak jauh (RPC) yang menggunakan XML untuk menyandikan panggilannya dan HTTP sebagai protokol transportasi. Ini adalah salah satu protokol RPC paling sederhana dan tertua yang masih digunakan.

## Konsep Utama

### 1. Kesederhanaan
Filosofi utama XML-RPC adalah kesederhanaan. Spesifikasinya sangat pendek. Tidak seperti CORBA atau DCOM yang kompleks, XML-RPC dirancang untuk melakukan satu hal dengan mudah: memanggil fungsi di komputer lain.

### 2. Format XML
Semua data dikirim dalam format XML yang bisa dibaca manusia.
Contoh Request:
```xml
<methodCall>
  <methodName>examples.getStateName</methodName>
  <params>
    <param>
        <value><i4>41</i4></value>
    </param>
  </params>
</methodCall>
```

## Implementasi dalam Demo

Python memiliki dukungan bawaan untuk XML-RPC melalui modul `xmlrpc.server` dan `xmlrpc.client`, sehingga Anda tidak perlu menginstal library tambahan apa pun!

File demo terdapat di folder `xmlrpc-demo/`.

### Server (`server.py`)

Membuat server XML-RPC sangat mudah:

```python
from xmlrpc.server import SimpleXMLRPCServer

def add(x, y):
    return x + y

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(add, "add")
server.serve_forever()
```

1.  Import `SimpleXMLRPCServer`.
2.  Definisikan fungsi biasa (`add`).
3.  Buat instance server di port tertentu.
4.  Daftarkan fungsi agar bisa diakses dari luar (`register_function`).
5.  Jalankan server.

### Client (`client.py`)

Client menggunakan `ServerProxy` untuk menghubungkan diri ke server:

```python
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
result = proxy.add(2, 3)
print(result)  # Output: 5
```

Perhatikan bahwa pemanggilan `proxy.add(2, 3)` terlihat seperti pemanggilan fungsi lokal biasa, padahal itu dikirim lewat jaringan!

## Kelebihan dan Kekurangan

**Kelebihan:**
*   **Built-in**: Tidak perlu install `pip` apapun di Python standar.
*   **Mudah Debug**: Bisa menggunakan browser atau tools HTTP biasa untuk melihat trafik.
*   **Lintas Platform**: Sangat mudah diimplementasikan di bahasa apapun (PHP, Java, Perl, dll).

**Kekurangan:**
*   **Verbose**: Format XML sangat boros karakter, memakan bandwidth.
*   **Lambat**: Parsing XML memakan resource CPU dibanding format biner.
*   **Tipe Data Terbatas**: Hanya mendukung tipe data dasar (int, string, array, struct). Tidak bisa mengirim objek kompleks.
