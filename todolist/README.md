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



# Tugas 5: Pengimplementasian Form dan Autentikasi Menggunakan Django

[App](http://mervinapp.herokuapp.com/todolist)


## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing _style_?

- External CSS dibuat di sebuah file `.css` baru, lalu dimasukkan dengan menggunakan elemen `<link>` ke dalam suatu halaman.
- Internal CSS dibuat di dalam sebuah elemen `<style>`, sehingga hanya berlaku pada satu halaman yang dibuat.
- Inline CSS dibuat di dalam properti `style=""` dalam sebuah elemen, sehingga hanya berlakuk pada elemen yang dimaksud.

## Jelaskan tag HTML5 yang kamu ketahui.

- `<p>`, untuk suatu teks paragraf.
- `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`, untuk judul/subjudul (*heading*).
- `<a>`, untuk membuat *link* dari suatu URL, yang biasanya sebuah halaman lain.
- `<div>`, digunakan untuk isi bagian web (*content division*).
- `<span>`, digunakan untuk membagi bagian dalam suatu tulisan (*content span*). Hampir mirip dengan `<div>`, namun `<span>` adalah elemen *inline*, dan `<div>` adalah elemen tingkat *block*.
- `<table>` (tabel keseluruhan), `<tr>` (baris/*row*), `<th>` (kepala/*head*), `<td>` (data), untuk membuat sebuah tabel.
- `<main>`, bagian utama dalam suatu halaman
- `<title>`, memberi judul pada suatu halaman. Ini yang muncul pada nama *tab* atau *window* saat dibuka.
- `<header>`, bagian atas pada suatu halaman.
- `<footer>`, bagian bawah pada suatu halaman.
- `<nav>`, navigasi pada suatu halaman.
- `<meta>`, metadata suatu halaman.
- `<head>`, menyimpan identitas, informasi, atau metadata dari suatu halaman.
- `<link>`, menghubungan suatu sumber daya, seperti *stylesheet*.
- `<script>`, menjalankan *script* yang dibutuhkan.
- `<style>`, memberikan gaya CSS secara *internal* (internal CSS).

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.

- *Universal selector*, yang akan memilih semua elemen.  
  Contohnya adalah `*`,  yang akan memilih semua elemen.
- *Type selector*, yang akan memili semua elemen dengan tipe/nama node yang sama.  
  Contohnya adalah `p`, yang akan memilih semua elemen `<p>`.
- *Class selector*, yang akan memilih semua elemen dengan kelas (*class*) yang sesuai, yang dibuat properti `class` di suatu elemen.  
  Contohnya adalah `.red`, yang akan memilih semua elemen dengan kelas `red`.
- *ID selector*, yang akan memilih semua elemen dengan ID yang sesuai, yang dibuat dari properti `id` di suatu elemen.  
  Contohnya adalah `#header`, yang akan memilih semua elemen dengan ID `header`. Idealnya, satu ID hanya ada pada satu elemen.
- *Attribute selector*, yang akan memilih semua elemen yang memiliki suatu atribut (dengan value yang sesuai, jika perlu).  
  Contohnya adalah `[disabled]`, yang akan memilih semua elemen dengan atribut `disabled`.
- *Selector list*, yang akan menggabungkan beberapa elemen untuk satu aturan.  
  Contohnya adalah `div, p`, yang akan memilih semua elemen `<div>` dan `<p>`.
- *Descendant combinator*, yang akan memilih elemen yang merupakan keturunan oleh (atau di dalam) elemen pertamanya.  
  Contohnya adalah `div p`, yang akan memilih semua elemen `<p>` yang di dalam elemen `<div>`.
- *Child combinator*, yang akan memilih leemen yang merupakan keturunan langsung/anak dari suatu elemen.
  Contohnya adalah `div > p`, hang akan memilih semua elemen `<p>` yang merupakan anak dari elemen `<div>`

## Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas.

- [x] Kustomisasi templat HTML yang telah dibuat pada [Tugas 4](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tugas/tugas-4) dengan menggunakan CSS atau CSS _framework_ (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:
- [x] Kustomisasi templat untuk halaman _login_, _register_, dan _create-task_ semenarik mungkin.
- [x] Kustomisasi halaman utama _todo list_ menggunakan _cards_.
- [x] Menambahkan bonus yaitu efek hover ketika melakukan hover pada cards di halaman utama todolist.
