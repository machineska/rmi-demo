# Gunakan Python 3.11 Slim sebagai base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependensi sistem yang dibutuhkan
# build-essential: untuk compile beberapa paket python
# libzmq3-dev: dibutuhkan oleh ZeroRPC (ZeroMQ)
# netcat-openbsd: opsional, berguna untuk debugging network
RUN apt-get update && apt-get install -y \
    build-essential \
    libzmq3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh source code ke dalam image
COPY . .

# Command default (bisa di-override di docker-compose)
CMD ["python", "main.py"]
