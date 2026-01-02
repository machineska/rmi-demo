# Pengantar: Sistem Terdistribusi, RPC, dan RMI

Sebelum terjun ke dalam kode dan implementasi, penting untuk memahami konsep dasar yang mendasari teknologi yang didemonstrasikan dalam proyek ini.

## Apa itu Sistem Terdistribusi?

Sistem terdistribusi adalah sekumpulan komputer independen yang tampak bagi penggunanya sebagai satu sistem yang koheren. Bayangkan sebuah aplikasi besar seperti Google atau Facebook; mereka tidak berjalan di satu komputer raksasa, melainkan di ribuan komputer yang saling berkomunikasi.

Tantangan utama dalam sistem terdistribusi adalah **komunikasi**. Bagaimana program A di Komputer 1 bisa meminta program B di Komputer 2 untuk melakukan sesuatu dan mendapatkan hasilnya? Di sinilah RPC dan RMI berperan.

## RPC (Remote Procedure Call)

**RPC** atau Panggilan Prosedur Jarak Jauh adalah protokol yang memungkinkan sebuah program komputer untuk menyebabkan subrutin atau prosedur dieksekusi di ruang alamat lain (biasanya di komputer lain dalam jaringan bersama) tanpa programmer harus secara eksplisit mengkodekan detail interaksi jaringan tersebut.

Sederhananya:
*   **Lokal**: Anda memanggil fungsi `hitung_gaji(id_karyawan)` yang ada di file yang sama atau library yang diimpor.
*   **Remote (RPC)**: Anda memanggil fungsi `hitung_gaji(id_karyawan)`, tapi fungsi itu sebenarnya dijalankan di server yang berada di gedung lain atau negara lain. RPC menyembunyikan kerumitan jaringan sehingga pemanggilan fungsi terasa seperti pemanggilan fungsi lokal biasa.

### Cara Kerja RPC Sederhana
1.  **Client** memanggil stub klien (prosedur lokal).
2.  **Client Stub** mengemas parameter ke dalam pesan (marshalling) dan memanggil OS untuk mengirim pesan.
3.  **OS Client** mengirim pesan ke OS Server.
4.  **OS Server** memberikan paket ke stub server.
5.  **Server Stub** membongkar parameter (unmarshalling) dan memanggil prosedur server.
6.  **Server** mengeksekusi prosedur dan mengembalikan hasil ke stub server.
7.  Proses berulang secara terbalik untuk mengembalikan hasil ke Client.

## RMI (Remote Method Invocation)

**RMI** adalah versi berorientasi objek dari RPC. Jika RPC berfokus pada fungsi/prosedur, RMI berfokus pada **Objek**.

Dalam RMI:
*   Anda tidak hanya memanggil fungsi, tetapi Anda memanggil **method** pada sebuah **objek** yang hidup di mesin lain.
*   Objek tersebut memiliki state (keadaan) dan behavior (perilaku).
*   RMI seringkali mendukung fitur-fitur OOP seperti inheritance, polymorphism, dan garbage collection terdistribusi.

Contoh teknologi RMI di Python adalah **Pyro5** (Python Remote Objects) dan **RPyC**.

## Mengapa Ada Banyak Teknologi Berbeda?

Dalam proyek ini, Anda akan melihat gRPC, XML-RPC, ZeroRPC, dll. Mengapa kita butuh begitu banyak? Karena setiap teknologi memiliki trade-off (kompromi):

1.  **Interoperabilitas Bahasa**:
    *   **XML-RPC** dan **gRPC** dirancang agar Client bisa ditulis dalam Python dan Server dalam Java (atau kombinasi bahasa lain).
    *   **Pyro5** dan **RPyC** sangat spesifik Python (Python-to-Python), yang memungkinkan fitur-fitur canggih yang tidak mungkin dilakukan antar bahasa berbeda (seperti mengirim objek Python kompleks).

2.  **Performa**:
    *   **XML-RPC** menggunakan XML yang teks-based, sehingga pesannya besar dan parsing-nya lambat.
    *   **gRPC** menggunakan Protocol Buffers (biner), yang sangat ringkas dan cepat.
    *   **ZeroRPC** menggunakan ZeroMQ dan MessagePack, fokus pada kecepatan tinggi.

3.  **Kemudahan Penggunaan**:
    *   **XML-RPC** sangat mudah dipahami (Anda bisa membaca paket datanya).
    *   **gRPC** butuh definisi file `.proto` dan kompilasi kode, lebih rumit di awal tapi lebih aman (type-safe).

Dengan memahami perbedaan ini, Anda bisa memilih alat yang tepat untuk pekerjaan Anda.
