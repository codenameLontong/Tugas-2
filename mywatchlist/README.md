# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django

[App](http://mervinapp.herokuapp.com/)

## Jelaskan perbedaan antara JSON, XML, dan HTML!

1. HyperText Markup Language, merupakan markup language yang digunakan untuk membuas suatu halaman web. HTML terdiri dari berbagai elemen yang memungkinkan kita untuk mengatur posisi berbagai konten di halaman web.
2. Sama halnya dengan HTML, Xtensible Markup Language atau yang biasa disingkat XML juga merupakan markup language. XML diciptakan untuk transport dan storing data.
3. JSON merupakan singkatan dari JavaScript Object Notation. JSON adalah format yang ringan untuk proses storing dan transport data. Pada umumnya, JSON digunakan untuk mengirim data dari server ke halaman web.

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Pada saat mendevelop sebuah platform, diperlukan adanya data yang dikirim ke database atau backend agar data yang kita simpan tidak menumpuk dan memperlambat aplikasi kita. Format data umum yang dikirim bentuknya bisa bermacam-macam, seperti yang sudah dijelaskan diatas yaitu HTML, XML, dan JSON.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

- Membuat aplikasi mywatchlist dengan `python manage.py startapp mywatchlist`
- Menambahkan atribut pada `models.py`
- Migrasi ke dalam database lokal django dengan `python manage.py makemigrations` dan `python manage.py migrate`
- Mengubah procfile dengan file json yang digunakan
- Membuat file `.json` yang berisi data-data yang ingin ditampilkan, kemudian melakukan loaddata dengan `python manage.py loaddata (FILE_NAME).json`
- Membuat template html
- Mengimplementasikan fungsi-fungsi yang menampilkan atribut-atribut yang sudah dibuat dalam bentuk html, xml, dan json dalam `views.py`
- Routing fungsi-fungsi yang ada di `views.py` di dalam `urls.py`
- Routing url aplikasi di dalam `urls.py` yang ada dalam folder `project_django`
- Membuat fungsi-fungsi dalam `tests.py` untuk melakukan unit testing
- Add, commit, dan push ke repository git perubahan yang sudah dibuat
- Membuat aplikasi baru di herokuapp
- Menyesuaikan secret variables dengan API key dan nama aplikasi dari herokuapp
- Gunakan postman untuk mengecek status

## Postman

<details><summary>HTML</summary>

![html](https://user-images.githubusercontent.com/100303130/191659836-53d43f62-487e-4f18-9d8c-12d088845dfc.jpg)

</details>

<details><summary>XML</summary>

![xml](https://user-images.githubusercontent.com/100303130/191659888-9f403164-7b82-4030-9a23-8a1865d24259.jpg)
  
</details>

<details><summary>JSON</summary>

![json](https://user-images.githubusercontent.com/100303130/191659912-12235272-ac9c-48d8-afce-b98d495a917c.jpg)

</details>
