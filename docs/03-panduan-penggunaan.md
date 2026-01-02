# Panduan Penggunaan

Ada dua cara untuk menjalankan demo dalam proyek ini: menggunakan script otomatis `run_demo.py` (disarankan) atau menjalankan setiap file secara manual.

## Metode 1: Menggunakan Script Otomatis (`run_demo.py`)

Kami telah menyediakan script Python `run_demo.py` di root folder untuk menyederhanakan proses menjalankan server dan client. Script ini menangani path direktori sehingga Anda tidak perlu berpindah-pindah folder.

### Format Perintah

```bash
python run_demo.py <nama_teknologi> <role>
```

*   `<nama_teknologi>`: grpc, xmlrpc, rpyc, zerorpc, pyro5, graphql
*   `<role>`: server, client, nameserver (khusus Pyro5)

### Contoh Menjalankan Demo XML-RPC

Anda membutuhkan **dua terminal** yang terbuka.

**Terminal 1 (Server):**
```bash
python run_demo.py xmlrpc server
```
*Server akan berjalan dan menunggu koneksi...*

**Terminal 2 (Client):**
```bash
python run_demo.py xmlrpc client
```
*Client akan mengirim request ke server dan menampilkan hasilnya.*

### Contoh Menjalankan Demo Pyro5 (Butuh 3 Terminal)

Pyro5 membutuhkan Name Server agar Client bisa menemukan Server.

**Terminal 1 (Name Server):**
```bash
python run_demo.py pyro5 nameserver
```

**Terminal 2 (Server):**
```bash
python run_demo.py pyro5 server
```

**Terminal 3 (Client):**
```bash
python run_demo.py pyro5 client
```

## Metode 2: Menjalankan Secara Manual

Jika Anda ingin memahami struktur folder atau script `run_demo.py` bermasalah, Anda bisa menjalankannya secara manual.

### Prinsip Dasar
1.  Masuk ke folder teknologi yang diinginkan.
2.  Jalankan file server.
3.  Jalankan file client di terminal lain.

### Contoh Manual: gRPC

**Terminal 1:**
```bash
cd grpc-demo
python server.py
```

**Terminal 2:**
```bash
cd grpc-demo
python client.py
```

### Catatan Khusus GraphQL

Demo GraphQL menggunakan Django, jadi cara jalannya sedikit berbeda karena berbasis web.

```bash
python run_demo.py graphql
```
atau manual:
```bash
cd graphql_demo
python manage.py runserver
```

Setelah server jalan, buka browser dan akses `http://127.0.0.1:8000/graphql` untuk mencoba query.
