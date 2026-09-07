Nama : Nicholas

NPM : 2506537165

Kelas : PBP E


### Tugas 1

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