Nama : Nicholas

NPM : 2506537165

Kelas : PBP E

### Tugas 1 (Recovered)

NOTE : Tugas ini saya selesaikan dengan bantuan AI (Gemini Flash 3.6) dengan total sebanyak 4x prompting pengerjaan dan beberapa prompting awal untuk mencerna. Di mana saya gunakan ini sebagai pengganti googling agar pengetahuan terkait CSS ini langsung saja dijelaskan secara to-the-point tanpa harus grinding mencari secara step by step di web berbeda.

Berikut 4 prompting yang saya gunakan:

- (Memberikan style.css dari template yang diberikan dari tutorial 1 untuk menjelaskan cara kerjanya. Gaya pembicaraan di prompt ini agak ada percakapan karena saya masukkan mode "Personal Intelligence")
"La, tolong bantu aku. Coba dong untuk disetiap kata/variabel di awal ini cara kerjanya bagaimana, serta apa fungsi-fungsinya, semisal 'display: inline-block'" 

- Kira-kira apakah mungkin dibentuk fitur Light mode / Dark mode tanpa Javascript? (Dan pada akhirnya, aku abaikan prompt ini karena Javascript-nya diletakkan di dalam html dengan elemen <script>)

- (Memberikan image web yang menggambarkan border terputus ke bawah, memberikan screenshot css) "Di part ini selalu kepotong terus, apakah solusinya ini terletak pada object-fit kah? pengaruh padding kah? atau ada yang perlu diubah di bagian class skill-card (Parentnya span)?" (Dan, setelah dibalas object-fit yang dari tadi saya amati, saya kira itu untuk fit segala isi di dalam area/kotak tersebut, ternyata itu berlaku untuk Image/Video. Sehingga, Gemini Flash 3.6 memberikan solusi terkait display: flex, flex-wrap: wrap. atau display: inline-block. Pada akhirnya, saya memilih display: inline-block)

- "Kasih deskripsi utk skill card eSports dong awkakwk, bahkan hal begini pun ku tanya ke kamu zzz" (No idea...)

- Selengkapnya dapat dilihat di link : https://share.gemini.google/gMRFrOlFhlN0

1. Iya, saya menggunakan <section> pada tugas Individu 1, namun tidak untuk <article> dan <aside>. Dengan menggunakan elemen <section>, saya merasa lebih gampang untuk memahami dan membayangkan/membangun web-nya. Hanya sekedar melihat template dari Tutorial 1 dan inspect, fungsi dari elemen section ini cukup terbayangkan. Section ini membantu saya untuk bisa menentukan setiap bagian yang ingin dibentuk, contohnya di dalam portofolio ini, saya ingin memasukkan "skill", "project", "academy", ataupun "achievement" di dalamnya, nah dari 4 sub poin ini aku bisa langsung menempatkan keempatnya ke dalam body, di mana setiap subpoin tersebut berada di setiap section dengan id yang telah ditentukan.

Namun, alasan mengapa saya tidak menggunakan article dan aside, karena saya hanya memanfaatkan langsung apa yang ada di template (mengamati langsung), dan tidak kepikiran atau mengetahui kalo fitur/elemen sejenis itu ada.

2. Dalam mengatur CSS ini, tantangan yang saya dapatkan ialah ketika ingin membuat teks ini tidak saling berpotongan/terpecah ke bawah, atau bordernya terputus, serta card-card yang telah saya susun untuk 3 kolom tidak berbentuk aneh (not balance [seperti gepeng bentuknya]). Ketika saya ingin mengevaluasi bagaimana cara untuk memperbaikinya, saya melakukan bruteforce secara tidak langsung, tadinya saya eksperimen dengan menguji setiap command yang ada di sana, seperti mengubah setiap value dan melihat perubahannya. Dan pada akhirnya, perlahan juga sudah mulai memahami apa command yang pas ketika ingin membuat sesuatu di bagian bawahnya (tambahan). 

Namun, terkait penyesuaian yang ada di Mobile dan Dekstop saya masih belum terlalu yakin dengan cara kerjanya, saya hanya sekedar mengubah segala fitur menjadi flex, agar tidak sering terjadi kehancuran pada susunan div tersebut.

3. Terlalu banyak batasan dalam kondisi static web. Misalnya, ketika saya ingin menambah/mengedit isi portofolio yang ada di dalamnnya. Saya terbatas untuk mengubahnya, di mana saya harus mengeditnya kembali dari vscodenya lagi dibandingkan saya mengubahnya angsung di web dengan adanya fitur "Edit", "Tambah", ataupun "Hapus". Sehingga, setiap kali aku ingin membuat perubahan, aku harus begitu terus berulang kali, terus harus melakukan "redeploy" terus menerus, dan hal seperti itu cukuplah merepotkan.

### Tugas 2

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


### Tugas 3
NOTE : Tugas ini saya selesaikan dengan bantuan AI (Gemini Flash 3.6) dengan total sebanyak 3x prompting pengerjaan dan beberapa prompting awal untuk mencerna. Di mana saya gunakan ini sebagai pengganti googling agar pengetahuan terkait CSS ini langsung saja dijelaskan secara to-the-point tanpa harus grinding mencari secara step by step di web berbeda.

- Selengkapnya dapat dilihat di link : https://share.gemini.google/NuOxF0JwFl4I

1. Alasan utama kita pakai ModelForm di Django dibandingkan bikin form HTML secara manual itu karena efisiensi serta keamanan. 

Dengan menggunakan ModelForm, Django bakal otomatis membuat layout form dan menangani validasi data sesuai dengan atribut yang ada di models.py. Benefitnya di sini juga kita ga perlu lagi menulis tag <input> manual di HTML ataupun bikin logika validasi satu per satu, bahkan untuk simpan data ke database pun cukup panggil form.save().

Sedangkan untuk {% csrf_token %}, itu wajib dimasukkan ke dalam form untuk melindungi aplikasi kita dari serangan Cross-Site Request Forgery (CSRF). Token acak dan unique ini memastikan bahwa request POST yang masuk benar-benar berasal dari pengguna sah melalui form di situs kita, bukan dari situs jahat pihak ketiga.

2. JSON lebih disukai ketimbang XML di aplikasi web modern karena JSON jauh lebih ringkas, ringan, dan tidak verbose. XML kebanyakan pake tag pembuka dan penutup sprti HTML <buah> </buah> <nama> </nama> <umur> </umur>. Selain itu, JSON didukung oleh JS. Proses parsing data JSON juga jauh lebih cepat dan gampang dilakukan, and vice versa.

3. Alur pengembalian data JSON dan serialization: 
- Alurnya dimulai ketika client melakukan request ke URL tertentu, 
- Django mengarahkannya ke fungsi view. 
- Di dalam view, kita mengambil data dari database melalui model Django. 
- Data yang diambil ini bentuknya masih berupa objek Python atau QuerySet. Di sinilah proses serialization dibutuhkan. 

Objek model Django itu merupakan struktur data kompleks yang tidak bisa langsung ditransmisikan lewat protokol HTTP, karena HTTP cuma bisa mengirim teks atau data sederhana. Serialization bertugas memproses dan mengubah objek Python tersebut menjadi format teks terstruktur yang universal, yaitu JSON. Setelah datanya diubah ke bentuk JSON, view akan membungkusnya ke dalam JsonResponse untuk dikirimkan kembali ke client.