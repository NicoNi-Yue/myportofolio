Nama : Nicholas

NPM : 2506537165

Kelas : PBP E


### Tugas 1

NOTE : Tugas ini saya selesaikan dengan bantuan AI (Gemini Flash 3.6) dengan total sebanyak 4x prompting pengerjaan dan beberapa prompting awal untuk mencerna. Di mana saya gunakan ini sebagai pengganti googling agar pengetahuan terkait CSS ini langsung saja dijelaskan secara to-the-point tanpa harus grinding mencari secara step by step di web berbeda.

- Selengkapnya dapat dilihat di link : https://share.gemini.google/5apZG7syXXfd

1. Alur yang dilalui secara bertahap:

- Respon Permintaan / HTTP Request POST:
Mulanya ketika kita membuka browser, Browser akan mengirimkan permintaan/HTTP Request tadi ke DJango sesuai dengan URL yang ingin kita akses

- Urls.py proyek:
Pada tahap ini, urls.py proyek memeriksa awalan suatu path url lalu kemudian melakukan routing ke urls.py aplikasi 

- Urls.py aplikasi:
Di tahap ini, urls.py aplikasi mencocokkan path url yang terdaftar, lalu kemudian memanggil views.py/fungsi view untuk menangani permintaan tersebut.

- View:
View di sini berperan sebagai logika utama, yang dapat menerima request, logika, dan meminta data yang diperlukan ke fungsi model

- Model: 
Model di sini berperan dalam berkomunikasi dengan database untuk mengambil dan memproses data yang dibutuhkan. Data-data tersebut kemudian dikembalikan ke view dalam bentuk objek

- Template:
Pada view menggabungkan data dari model ke dalam file template

- Respon Dikirim / HTTP Request GET:
Template yang sudah dirender menjadi file HTML dikembalikan oleh view ke browser pengguna untuk ditampilkan

2. Menjelaskan dampak terhadap "Kemudahan pemeliharaan", ketika adanya pembaruan data yang terjadi, kita hanya perlu melakukan perubahan pada bagian database di models DJango nya saja, tanpa harus merubah struktur code HTML di template.

3. Perbedaan fungsi "makemigrations" dan "migrate" pada DJango adalah:

makemigrations : Berperan dalam menyiapkan blueprint dari perubahan yang terjadi pada models. Command ini tidak mengubah isi database melainkan membuat file migrasi baru pada folder migrations

migrate: Berperan untuk menjalankan file migrasi yang sudah dibuat pada folder migrations ke database asli.

Contoh kasus: 
Seandainya pada models education saya saat ini, saya ingin menambahkan / mengubah salah satu field di dalamnya, misalkan field logo, saya ingin mengubahnya sama seperti yang ada di experience yaitu "thumbnail".

Karena pada blueprint saat ini masih tercatat education dengan field logo, maka kita perlu menjalankan makemmigrations agar blueprint tersebut mengupdate perubahan yang terjadi, sehingga tercatat bahwa field yang terdapat pada education tidak lagi bernama "logo" melainkan "thumbnail". Namun, jika mengingat dengan fungsi migrate bahwa menjalankan file migrasi. Jika tidak kita run setelah makemigrations, maka ia akan menjalankan file migrasi yang sebelumnya, sehingga mau tidak mau, kita harus menjalankan command migrate agar field education saat ini bener-bener berubah dari "logo" menjadi "thumbnail".


