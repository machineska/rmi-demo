# Panduan Instalasi dan Persiapan

Agar semua demo dalam proyek ini dapat berjalan dengan lancar, Anda perlu menyiapkan lingkungan pengembangan (environment) yang tepat. Ikuti langkah-langkah di bawah ini secara berurutan.

## 1. Prasyarat Sistem

Pastikan komputer Anda telah terinstal:
*   **Python 3.7** atau lebih baru. Anda dapat mengecek versi Python dengan perintah:
    ```bash
    python --version
    ```
    atau
    ```bash
    python3 --version
    ```
*   **pip** (Python Package Installer). Biasanya sudah terinstal otomatis bersama Python.

## 2. Menggunakan Virtual Environment (Sangat Disarankan)

Sangat disarankan untuk menggunakan **Virtual Environment** agar dependensi proyek ini tidak bentrok dengan proyek Python lain di komputer Anda.

### Cara Membuat Virtual Environment

Buka terminal/command prompt di folder root proyek ini (`rmi-demo/`), lalu jalankan:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Setelah diaktifkan, biasanya prompt terminal Anda akan diawali dengan `(venv)`.

## 3. Instalasi Dependensi

Proyek ini memiliki file `requirements.txt` yang berisi daftar semua pustaka (library) yang dibutuhkan. Setelah virtual environment aktif, jalankan perintah berikut:

```bash
pip install -r requirements.txt
```

Tunggu hingga proses instalasi selesai.

### Apa saja yang diinstal?

Berikut adalah penjelasan singkat mengenai paket-paket utama yang diinstal:

*   **`grpcio` & `grpcio-tools`**: Library runtime dan tools untuk gRPC.
*   **`Pyro5`**: Library untuk Python Remote Objects versi 5.
*   **`rpyc`**: Library untuk Remote Python Call.
*   **`zerorpc`**: Library RPC berbasis ZeroMQ.
*   **`django`**: Framework web untuk demo GraphQL.
*   **`graphene-django`**: Library integrasi GraphQL untuk Django.

## 4. Verifikasi Instalasi

Untuk memastikan semuanya terinstal dengan benar, coba jalankan perintah bantuan dari script orkestrasi kami:

```bash
python run_demo.py --help
```

Jika muncul pesan bantuan cara penggunaan, berarti environment Anda sudah siap!
