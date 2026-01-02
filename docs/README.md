# Dokumentasi Proyek Demo RMI/RPC

Selamat datang di dokumentasi lengkap proyek Demo RMI/RPC. Proyek ini dibuat untuk tujuan edukasi, mendemonstrasikan berbagai teknologi *Remote Method Invocation* (RMI) dan *Remote Procedure Call* (RPC) menggunakan bahasa pemrograman Python.

Dokumentasi ini disusun untuk membantu Anda memahami konsep, melakukan instalasi, menjalankan demo, hingga memahami detail teknis dari setiap teknologi yang digunakan.

## 📚 Daftar Isi

1.  [**Pengantar**](./01-pengantar.md)
    *   Apa itu Sistem Terdistribusi?
    *   Apa itu RPC dan RMI?
    *   Mengapa ada banyak teknologi berbeda?

2.  [**Panduan Instalasi**](./02-instalasi.md)
    *   Prasyarat Sistem
    *   Setup Virtual Environment (Sangat Disarankan)
    *   Instalasi Dependensi

3.  [**Panduan Penggunaan**](./03-panduan-penggunaan.md)
    *   Menggunakan Script Otomatis `run_demo.py`
    *   Menjalankan Demo secara Manual
    *   Tips Menjalankan Server dan Client

4.  [**Detail Teknologi**](./technologies/README.md)
    *   [gRPC (Google Remote Procedure Call)](./technologies/01-grpc.md)
    *   [XML-RPC](./technologies/02-xmlrpc.md)
    *   [RPyC (Remote Python Call)](./technologies/03-rpyc.md)
    *   [ZeroRPC](./technologies/04-zerorpc.md)
    *   [Pyro5 (Python Remote Objects)](./technologies/05-pyro5.md)
    *   [GraphQL (dengan Django)](./technologies/06-graphql.md)

5.  [**Pemecahan Masalah (Troubleshooting)**](./04-pemecahan-masalah.md)
    *   Masalah Koneksi dan Port
    *   Masalah Dependensi
    *   Error Spesifik Teknologi

6.  [**Perbandingan Teknologi**](./05-perbandingan.md)
    *   Tabel Perbandingan Fitur
    *   Kapan Menggunakan Apa?
    *   Analisis Performa

## 🚀 Mulai Cepat

Jika Anda sudah tidak sabar untuk mencoba, berikut langkah singkatnya:

1.  Pastikan Python 3.7+ terinstall.
2.  Install dependensi: `pip install -r requirements.txt`
3.  Jalankan salah satu demo, misalnya XML-RPC:
    *   Terminal 1: `python run_demo.py xmlrpc server`
    *   Terminal 2: `python run_demo.py xmlrpc client`

Selamat belajar!
