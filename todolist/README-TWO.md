# Tugas 6: JavaScript dan AJAX

[App](http://mervinapp.herokuapp.com/todolist)


## Jelaskan perbedaan antara _asynchronous programming_ dengan _synchronous programming_
*Synchronous programming* adalah sebuah paradigm ketika hanya satu program yang dapat berjalan pada suatu waktu. Sehingga, ketika program ingin dieksekusi, program tsb perlu menunggu program sebelumnya untuk selesai dijalankan.

*Asynchronous programming* adalah sebuah paradigm ketika beberapa program dapat berjalan sekaligus, tanpa menunggu program lain untuk selesai. 



## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event adalah "interrupt" atau sinyal yang diberikan kepada sebuah *current* proses untuk dihandle oleh *current* proses tersebut. Event bisa berupa action explisit dari luar ataupun efek samping dari proses yang berlangsung.
dengan menggunakan *event-driven programming* kita bisa membuat logic dan fungsionalitas program yang lebih kompleks dan terarah. Misalnya ketika terjadi event A, maka execute proses X dan proses Y. Lebih abstraknya lagi, kita bisa membuat program kita lebih interaktif dan high-performant.
Pada tugas kali ini, contoh event yang digunakan adalah event click (mouseclick).

```js
//1
$("#button").click(.....)
//2
$(document).ready(...)
```

## Jelaskan penerapan asynchronous programming pada AJAX.

1. Ketika terjadi event, maka JavaScript akan membuat object XHR baru.
2. Objek XHR tersebut akan dikirim ke server, kemudian responsenya diterima kembali oleh JavaScript.
3. Response tersebut akan diolah, dan data laman web akan diperbarui oleh JavaScript tanpa harus me-_refresh_.

**Artinya, kita tetap bisa melakukan proses fetching data, tanpa harus memberhentikan proses yang sedang terjadi di laman web pada waktu tersebut.**

## Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas.

- [x] Implementasi `views.py` dan `urls.py` yang dibutuhkan untuk setiap panggilan AJAX yang akan dilakukan.
- [x] Mengambil data dari server dengan AJAX. Bandingkan dengan menggunakan templates Django. Buat juga sehingga daftar diambil di setiap perubahan/interaksi yang berkaitan.
- [x] Mengubah form sehingga nantinya data akan dikirim dengan menggunakan JavaScript yang tidak membutuhkan refresh.
- [x] Ubah bagian-bagian yang perlu sehingga berkaitan dengan data todolist.
- [x] Styling Modal dengan menggunakan **bootstrap**
