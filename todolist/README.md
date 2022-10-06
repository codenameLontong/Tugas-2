# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

[App](https://mervinapp.herokuapp.com/todolist)

## Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`? 

`{% csrf_token %}` dapat mencegah serangan CSRF yang akan membuat penyerang tidak mungkin melakukan permintaan HTTP yang secara sepenuhnya valid yang cocok untuk diumpankan ke pengguna korban. Oleh karena itu, platform akan semakin aman dari serangan pihak luar, baik yang disengaja maupun tidak.
Pada django, jika kita tidak memuat `{% csrf_token %}`, maka request POST yang kita kirim tidak akan memiliki token. Django akan mereturn http status code 403, yakni forbidden, karena menganggap request yang kita kirim `malicious`.

## Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.

Bisa. Untuk dapat membuat HTML form secara manual, kita perlu membuat elemen `<form>` dengan action endpoint yang sesuai dan method pada POST. Jangan lupa  juga untuk sertakan `<label>` dengan atribut `name` dan `for` yang merujuk ke field Model yang sama.

```python
from todolist.models import *;
from django.forms import *;

class TaskForm(ModelForm):
    class Meta:
        model = Task;
        fields = ["title", "description"]
```


## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

View akan membaca request dari client dan dari request tersebut diambil parameter dan valuenya. Kemudian data akan diambil dari request POST tersebut dan distore ke dalam variable.Lalu, user membuat objek baru pada template dengan parameter merupakan data-data yang sudah diambil. Setelah itu, redirect akan dikembalikan ke halaman todolist. Data yang baru dimasukkan akan muncul

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

- Membuat aplikasi baru dengan command `python manage.py startapp todolist`
- Add new routing untuk url dari todolist pada `urls.py`
- Menambahkan model yang diperlukan pada `models.py`
- Melakukan proses migrasi dengan `python manage.py make migrations` dan `migrate`
- Implementasi fungsi untuk register, login, dan logout pada `views.py`
- Membuat tabel untuk menampilkan data dan tombol logout dan create task pada page utama dari todolist
- Membuat page untuk membuat data baru dengan `create_task`
- Membuat fungsi baru pada `views.py` untuk membuat data baru
- Membuat fungsi baru pada `views.py` untuk mengganti status data dan menghapus data
- Routing fungsi-fungsi yang sudah dibuat pada `views.py` di dalam `urls.py` dari todolist
- Push perubahan yang dilakukan pada repositories

