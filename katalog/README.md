Link : 'https://tugas2jeremy.herokuapp.com/'

## 1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya 
dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

![image](https://user-images.githubusercontent.com/100303130/190314079-9752c14b-2846-4e4d-b045-3f9731f1049e.png)

Pertama, client akan merequest yang nantinya akan diterima oleh urls.py, kemudian akan dilanjutkan ke views.py yang akan melakukan
memproses request yang sudah masuk. Bila ada proses yang membutuhkan database, akan dilakukan pemanggilan query ke models kemudian
database akan mengembalikan hasilnya ke views. Jika permintaan sudah selesai diproses, maka hasilnya akan dipetakan ke templates (berkas html) yang akan 
diperlihatkan ke client.

## 2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual envinronment kita gunakan agar tidak terjadi bentrok dengan versi lain yang ada pada komputer. Venv akan mengisolasi package dan dependecies
dari aplikasi. Kita dapat tetap membuat aplikasi web berbasis Django tanpa menggunakan venv, namun versi python dan libraries yang digunakan harus 
diperhatikan agar tidak terjadi bentrok antara versi-versi yang berbeda.

## 3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
- Melakukan migrasi dengan `python manage.py makemigrations` dan `python manage.py migrate`
- Membuat fungsi di `views.py` yang ditujukan untuk menerima parameter request dan mereturn render dengan context
- Menambahkan iterasi dari list yang ada pada `views.py` dalam `katalog.html` untuk menampilkan katalog yang sudah ada di dalam folder fixtures
- Menambahkan path di `urls.py` dari katalog untuk fungsi `show_catalog` yang ada di `views.py`
- Menambahkan path `urls.py` dari katalog di dalam `urls.py` dari project_django
- Melakukan add, commit, dan push perubahan yang dilakukan ke github
- Membuat aplikasi baru di heroku
- Menambahkan nama aplikasi dan API key sebagai secret variable di dalam repository secret
- Mendeploy website
