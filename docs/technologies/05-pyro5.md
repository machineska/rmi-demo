# Pyro5 (Python Remote Objects)

**Pyro5** adalah generasi terbaru dari library Python Remote Objects yang legendaris. Ini memungkinkan Anda membangun aplikasi di mana objek dapat berbicara satu sama lain melalui jaringan, dengan panggilan method yang terlihat seperti panggilan lokal.

## Konsep Utama

### 1. Objek Terdistribusi Sejati
Berbeda dengan RPC biasa yang "memanggil fungsi", Pyro memaparkan **objek**. Client memegang proxy ke objek yang hidup di server. Perubahan state pada objek di server akan tetap ada untuk panggilan berikutnya.

### 2. Name Server
Pyro menggunakan komponen khusus yang disebut **Name Server**.
*   Server mendaftarkan objeknya ke Name Server dengan nama logis (misal: "example.calculator").
*   Client bertanya ke Name Server: "Di mana objek bernama 'example.calculator'?".
*   Name Server memberikan alamat (URI) objek tersebut ke Client.
*   Ini membuat Server bisa pindah IP/Port tanpa mengubah kode Client, asalkan Server mendaftar ulang ke Name Server.

## Implementasi dalam Demo

File demo terdapat di folder `pyrofive/`.

### Langkah 1: Jalankan Name Server
Sebelum menjalankan server atau client, Name Server harus aktif.
```bash
python -m Pyro5.nameserver
```

### Server (`server.py`)

```python
import Pyro5.api

@Pyro5.api.expose
class Calculator(object):
    def add(self, x, y):
        return x + y

def main():
    daemon = Pyro5.api.Daemon()             # Membuat daemon Pyro
    ns = Pyro5.api.locate_ns()              # Mencari Name Server
    uri = daemon.register(Calculator)       # Mendaftarkan class sebagai objek Pyro
    ns.register("example.calculator", uri)  # Mendaftarkan URI objek ke Name Server
    print("Siap.")
    daemon.requestLoop()                    # Mulai loop event
```

Decorator `@Pyro5.api.expose` penting untuk menandai class/method mana yang boleh diakses dari luar.

### Client (`client.py`)

```python
import Pyro5.api

calculator = Pyro5.api.Proxy("PYRONAME:example.calculator")
print(calculator.add(5, 6))
```

Client menggunakan string khusus `PYRONAME:nama_objek` untuk memberitahu Pyro agar mencari alamat objek tersebut lewat Name Server.

## Kelebihan dan Kekurangan

**Kelebihan:**
*   **Abstraksi Tinggi**: Sangat mudah mengelola objek terdistribusi.
*   **Discovery Otomatis**: Name Server memudahkan manajemen lokasi layanan.
*   **Fitur Kaya**: Mendukung one-way calls, batch calls, dan timeout.

**Kekurangan:**
*   **Kompleksitas Infrastruktur**: Butuh menjalankan Name Server terpisah.
*   **Overhead**: Sedikit lebih lambat dibanding ZeroRPC atau gRPC karena fitur-fiturnya yang kaya.
*   **Python-centric**: Fokus utamanya adalah ekosistem Python.
