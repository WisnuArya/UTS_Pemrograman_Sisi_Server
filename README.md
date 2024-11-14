Cara Menjalankan :
1.	Pastikan sudah menginstall Django REST Framework (pip install djangorestframework)
2.	Kemudian sambungkan dengan mysql (pip install django mysqlclient)
3.	Kemudian migrasikan ke mysql (python manage.py makemigrations)
4.	Kemudian jalankan perintah ( docker-compose up –build) tunggu hingga selesai
5.	Kemudian cek pada Docker Dekstop apakah sudah muncul
6.	Jika sudah muncul ada kemungkinan dalam file inventory bagian web-1 tidak berjalan,jika tidak berjalan hentikan semua proses sebelumnya dan jalankan perintah (docker-compose up)
7.	Jika sudah,buka dengan perintah (http://localhost:8000/api/) maka akan menampilkan halaman awal
