# Pemecahan Masalah (Troubleshooting)

Berikut adalah beberapa masalah umum yang mungkin Anda temui saat menjalankan demo dan cara mengatasinya.

## 1. `ModuleNotFoundError: No module named ...`

**Penyebab:**
Dependensi belum terinstal atau virtual environment belum diaktifkan.

**Solusi:**
1.  Pastikan virtual environment aktif (lihat [Panduan Instalasi](./02-instalasi.md)).
2.  Jalankan `pip install -r requirements.txt` lagi.
3.  Pastikan Anda menjalankan python dari environment yang sama.

## 2. `Address already in use` atau `Connection refused`

**Penyebab:**
Port yang digunakan oleh server sudah dipakai oleh program lain, atau Anda mencoba menjalankan server dua kali.

**Solusi:**
1.  Cek apakah ada terminal lain yang sedang menjalankan server yang sama. Matikan dengan `Ctrl+C`.
2.  Jika tidak ada, ubah port di file `server.py` dan `client.py` pada folder demo yang bermasalah.
    *   Contoh: Ubah `localhost:50051` menjadi `localhost:50052`.

## 3. Pyro5: `Failed to locate the nameserver`

**Penyebab:**
Client atau Server mencoba menghubungi Name Server Pyro5, tapi Name Server belum berjalan.

**Solusi:**
Pastikan Anda menjalankan Name Server terlebih dahulu di terminal terpisah sebelum menjalankan Server atau Client.
```bash
python run_demo.py pyro5 nameserver
```

## 4. gRPC: `ModuleNotFoundError: No module named 'calculator_pb2'`

**Penyebab:**
File hasil generasi protobuf (`calculator_pb2.py` dan `calculator_pb2_grpc.py`) hilang atau korup.

**Solusi:**
Regenerasi file tersebut dengan perintah:
```bash
cd grpc-demo
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
```

## 5. ZeroRPC Error pada Windows

**Masalah:**
Terkadang instalasi `zerorpc` gagal di Windows karena butuh compiler C++.

**Solusi:**
ZeroRPC membutuhkan Microsoft Visual C++ Build Tools. Jika sulit diinstal, Anda bisa melewati demo ini dan fokus pada demo lain yang pure-Python seperti XML-RPC, RPyC, atau Pyro5.

## 6. Django GraphQL Error

**Masalah:**
`no such table: books_book`

**Penyebab:**
Database belum dimigrasi.

**Solusi:**
Jalankan migrasi database:
```bash
cd graphql_demo
python manage.py migrate
```
