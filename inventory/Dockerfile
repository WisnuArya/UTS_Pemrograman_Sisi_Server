# Gunakan image Python sebagai base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Install dependensi
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh aplikasi ke dalam container
COPY . .

# Expose port 8000
EXPOSE 8000

# Perintah untuk menjalankan aplikasi
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]