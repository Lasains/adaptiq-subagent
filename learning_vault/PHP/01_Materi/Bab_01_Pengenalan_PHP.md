---
icon: "📖"
sticker: "📖"
color: "#6366f1"
tags:
  - php
  - materi
  - fase-1
---

# 📚 Bab 1 — Pengenalan PHP & Program Pertama

> **Level**: Pemula Murni (*Zero-Knowledge*) | **Prasyarat**: Tidak ada | **Estimasi Waktu**: 40–50 menit  
> **Jalur Spesialisasi**: Persiapan Framework Laravel (Fase 1: Fondasi PHP Murni via CLI)

---

## 💡 Konsep Utama (Dalam Bahasa Ringkas)

PHP adalah bahasa pemrograman yang bertugas memberikan **instruksi terstruktur kepada komputer**. Komputer membaca dan menjalankan kode baris demi baris, dari atas ke bawah. Pada tahap awal ini, kita belajar menjalankan PHP melalui terminal (CLI) agar kamu fokus menguasai logika dan sintaksis dasar tanpa terdistraksi rumitnya web browser, sebelum nantinya melangkah ke framework Laravel.

---

## 🔧 Analogi Mekanis Dunia Nyata

Bagi pemula yang membutuhkan gambaran nyata dan mekanis tanpa abstraksi rumit:

| Konsep Nyata | Padanan di PHP | Fungsi Mekanis |
| :--- | :--- | :--- |
| **Saklar Utama Mesin** | Tag `<?php` | Menyalakan penerjemah PHP agar mulai membaca instruksi di bawahnya. |
| **Pengeras Suara / Printer** | Perintah `echo` | Mengirimkan teks atau data untuk ditampilkan ke layar terminal. |
| **Tanda Titik di Akhir Kalimat** | Titik Koma `;` | Menandakan batas akhir dari satu kalimat instruksi kerja. |
| **Catatan Pribadi di Kertas** | Komentar `// ...` | Catatan untuk dibaca pemrogram manusia; mesin PHP mengabaikannya. |

---

## 📋 Peta Langkah-demi-Langkah (Dyslexia Friendly)

1. **Membuat Berkas Kode**: Berkas program PHP wajib disimpan dengan akhiran (ekstensi) `.php`, misalnya `halo.php`.
2. **Menyalakan Saklar PHP**: Tulis `<?php` di baris paling atas dokumen. Tanpa tag ini, komputer tidak akan menganggapnya sebagai kode program.
3. **Mengirim Perintah Cetak**: Gunakan perintah `echo` diikuti teks di dalam tanda petik ganda `"..."`.
4. **Memberi Karakter Baris Baru**: Tambahkan simbol `\n` di ujung teks agar cetakan berikutnya turun ke baris baru.
5. **Menggabungkan Dua Teks**: Gunakan tanda titik `.` (*string concatenation*) untuk merangkai dua teks terpisah.
6. **Menutup Instruksi**: Akhiri setiap perintah dengan tanda titik koma `;`.
7. **Menjalankan Program**: Buka terminal dan ketik perintah `php nama_berkas.php`.

---

## 📊 Tabel Jejak Eksekusi (Aphantasia Friendly)

Perhatikan program sederhana berikut:
```php
<?php
echo "Halo, Dunia!\n";
echo "Belajar PHP " . "untuk Laravel!\n";
```

Berikut alur eksekusi mekanis langkah demi langkah di dalam memori dan layar:

| Step | Baris Kode | Yang Dikerjakan Mesin | Tampilan Layar Terminal |
| :---: | :--- | :--- | :--- |
| **1** | `<?php` | Mesin PHP aktif dan siap menerima instruksi | *(Layar masih kosong)* |
| **2** | `echo "Halo, Dunia!\n";` | Mengirim teks `"Halo, Dunia!"` lalu menurunkan kursor 1 baris | `Halo, Dunia!` |
| **3** | `echo "Belajar PHP " . "untuk Laravel!\n";` | Menggabungkan kedua teks menjadi `"Belajar PHP untuk Laravel!"` lalu mencetaknya | `Belajar PHP untuk Laravel!` |
| **4** | *(Akhir berkas)* | Tidak ada instruksi lagi; proses berhenti | *(Selesai)* |

---

## 💻 Kode Contoh PHP (Siap Jalan di PHP 8.3+)

Ketik kode di bawah ini ke dalam berkas `halo.php`:

```php
<?php

// 1. Baris komentar: Komputer tidak membaca baris ini.
// Gunakan ini untuk memberi catatan penjelas pada kodemu.

// 2. Perintah echo pertama: Mencetak sapaan ke layar
echo "Halo! Selamat datang di dunia pemrograman PHP.\n";

// 3. Perintah echo kedua: Menampilkan target belajar kita
echo "Misi kita: Menguasai fondasi PHP murni untuk persiapan Laravel.\n";

// 4. Perintah echo ketiga: Menggabungkan dua potongan teks dengan titik (.)
echo "PHP versi modern " . "itu cepat dan menyenangkan!\n";
```

### Cara Menjalankan di Terminal:
```bash
php halo.php
```

### Hasil Keluaran Terminal:
```text
Halo! Selamat datang di dunia pemrograman PHP.
Misi kita: Menguasai fondasi PHP murni untuk persiapan Laravel.
PHP versi modern itu cepat dan menyenangkan!
```

---

## ⚠️ Jebakan Umum

| Kesalahan | Contoh Salah ❌ | Contoh Benar ✅ | Penjelasan Kesalahan |
| :--- | :--- | :--- | :--- |
| **Lupa Tag Pembuka** | `echo "Halo";` | `<?php`<br>`echo "Halo";` | Tanpa `<?php`, kode hanya akan dianggap sebagai teks biasa dan tidak diproses. |
| **Lupa Titik Koma** | `echo "Halo Dunia"` | `echo "Halo Dunia";` | Menghasilkan error `Parse error: syntax error`. Setiap instruksi wajib ditutup `;`. |
| **Teks Tanpa Petik** | `echo Halo;` | `echo "Halo";` | Teks murni wajib diapit tanda petik tunggal `'...'` atau ganda `"..."`. |
| **Salah Simbol Sambung** | `echo "A" + "B";` | `echo "A" . "B";` | Di PHP, penyambung teks menggunakan simbol titik `.`, bukan tanda tambah `+`. |

---

## 🧩 Kuis Mini Interaktif

Kerjakan kuis ini di berkas [Kuis_Bab_01.md](../03_Jawaban_Kuis/Kuis_Bab_01.md).

### Soal 1 — Pilihan Ganda (10 poin)
Apa yang terjadi jika kamu lupa menuliskan tag `<?php` pada baris pertama berkas PHP?
- **A)** Program langsung menampilkan error merah di terminal.
- **B)** Teks kode akan dicetak mentah begitu saja ke terminal tanpa dieksekusi sebagai program.
- **C)** Komputer otomatis memperbaikinya dan program tetap berjalan normal.
- **D)** Komputer mati mendadak.

### Soal 2 — Jejak Eksekusi (25 poin)
Lengkapi tabel jejak eksekusi untuk kode di bawah ini:
```php
<?php
echo "Langkah Satu\n";
echo "Langkah " . "Dua\n";
```
*Tuliskan isi baris terminal yang muncul pada Step 1, Step 2, dan Step 3 di lembar kuis.*

### Soal 3 — Temukan Bug (30 poin)
Perhatikan kode berikut yang mengalami error:
```php
<?php
echo "Saya siap belajar PHP"
echo Laravel . " Mantap!\n";
```
*Temukan minimal 2 kesalahan sintaksis pada kode di atas dan berikan kode perbaikannya!*

### Soal 4 — Coding Mini (35 poin)
Buat program PHP mandiri bernama `perkenalan.php` yang ketika dijalankan di terminal menampilkan:
1. Nama panggilanmu.
2. Targetmu: Belajar PHP dari nol untuk persiapan framework Laravel.
3. Ide aplikasi web yang ingin kamu buat setelah menguasai Laravel.
