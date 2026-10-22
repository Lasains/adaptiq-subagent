---
icon: "📖"
sticker: "📖"
color: "#6366f1"
tags:
  - php
  - materi
  - fase-2
---

# 📚 Bab 09: String & Manipulasi Teks

> **Level**: Menengah (*Fase 2: Pemrosesan & Sanitasi Data Teks*)  
> **Prasyarat**: Bab 08 (Array Lanjutan), Bab 07 (Fungsi)  
> **Estimasi Waktu**: 25–30 Menit  
> **Target Eksekusi**: PHP 8.3+ via CLI (`php nama_file.php`)  
> **Relevansi Web / Laravel**: Sangat Tinggi (Validasi form pendaftaran, pembuatan slug URL, & pembersihan input)  

---

## 💡 Konsep Utama (Dalam Bahasa Ringkas)

Hampir seluruh data yang dimasukkan pengguna lewat form website (seperti nama, email, atau nomor HP) diterima oleh PHP dalam bentuk teks (**String**).  
Seringkali teks tersebut kotor, memiliki spasi liar di ujungnya, atau menggunakan huruf besar-kecil yang tidak beraturan.  
**Manipulasi String** adalah keterampilan menggunakan fungsi bawaan PHP untuk membersihkan, mencari, memotong, dan mengubah teks menjadi data yang siap disimpan rapi ke dalam database.

---

## 🔧 Analogi Mekanis Dunia Nyata

| Situasi Nyata                      | Padanan di PHP                  | Penjelasan Mekanis                                                                  |
| :--------------------------------- | :------------------------------ | :---------------------------------------------------------------------------------- |
| **Gunting Pemotong Rumput Liar**   | `trim($teks)`                   | Memangkas spasi tak terlihat yang terselip di awal dan akhir teks.                  |
| **Pengecatan Ulang Huruf Seragam** | `strtolower()` / `strtoupper()` | Mengubah seluruh huruf menjadi kecil (untuk email) atau kapital (untuk kode promo). |
| **Pisau Pemotong Roti Tawar**      | `explode(",", $teks)`           | Membelah satu kalimat panjang menjadi potongan-potongan array berdasarkan pemisah.  |
| **Lem Perekat Potongan Kertas**    | `implode(" - ", $array)`        | Merekatkan kembali potongan array menjadi satu baris kalimat utuh.                  |
| **Sensor Pendeteksi Kata Kunci**   | `str_contains($teks, "kata")`   | Memeriksa apakah suatu kata ada di dalam kalimat (Fitur Modern PHP 8).              |

---

## 📋 Peta Langkah-demi-Langkah (Dyslexia Friendly)

1. **Membersihkan Teks Input Pengguna**:
   - Selalu gunakan `trim($input)` untuk menghapus spasi yang tidak sengaja terketik di ujung kiri/kanan.
2. **Menstandarkan Format Huruf**:
   - `strtolower($email)` ➔ Jadikan huruf kecil semua (contoh: `User@Email.Com` ➔ `user@email.com`).
   - `ucwords($nama)` ➔ Awali setiap kata dengan huruf kapital (contoh: `budi santoso` ➔ `Budi Santoso`).
3. **Membongkar Teks Jadi Array (`explode`)**:
   - Format: `explode(tanda_pemisah, kalimat)`.
   - Contoh: memecah hobi `"baca,renang,koding"` menjadi array `["baca", "renang", "koding"]`.
4. **Mencari Kata Modern di PHP 8**:
   - `str_contains($teks, "@")` ➔ Menghasilkan `true` jika mengandung simbol `@`.
   - `str_starts_with($teks, "08")` ➔ Menghasilkan `true` jika diawali nomor `"08"`.
   - `str_replace("lama", "baru", $teks)` ➔ Mengganti kata tertentu secara otomatis.

---

## 📊 Tabel Jejak Eksekusi Logika (Aphantasia Friendly)

Perhatikan program pembuatan URL ramah SEO (*Slug*) berikut:

```php
<?php
$judulArtikel = "  Belajar PHP 8 Modern untuk Pemula!  ";

// 1. Bersihkan spasi ujung
$bersih = trim($judulArtikel);

// 2. Kecilkan semua huruf
$hurufKecil = strtolower($bersih);

// 3. Buang tanda seru
$tanpaTanda = str_replace("!", "", $hurufKecil);

// 4. Ubah spasi menjadi tanda strip (-)
$slug = str_replace(" ", "-", $tanpaTanda);

echo "URL: " . $slug . "\n";
```

Berikut alur transformasi teks langkah-demi-langkah:

| Step | Operasi / Baris Kode | State Variabel Sebelum | Aksi Mesin PHP | State Variabel Sesudah |
| :---: | :--- | :--- | :--- | :--- |
| **1** | Inisialisasi `$judulArtikel` | - | Menyimpan string dengan spasi depan/belakang | `"  Belajar PHP 8 Modern untuk Pemula!  "` |
| **2** | `trim($judulArtikel)` | Teks dengan spasi luar | Memotong spasi di kedua ujung luar | `$bersih = "Belajar PHP 8 Modern untuk Pemula!"` |
| **3** | `strtolower($bersih)` | Huruf kapital bercampur | Mengubah seluruh alfabet menjadi huruf kecil | `$hurufKecil = "belajar php 8 modern untuk pemula!"` |
| **4** | `str_replace("!", "", ...)` | Mengandung tanda `!` | Menghapus karakter tanda seru | `$tanpaTanda = "belajar php 8 modern untuk pemula"` |
| **5** | `str_replace(" ", "-", ...)` | Memiliki spasi pemisah | Mengganti setiap spasi kosong dengan strip `-` | `$slug = "belajar-php-8-modern-untuk-pemula"` |
| **6** | `echo ...` | - | Mencetak hasil ke layar terminal | `URL: belajar-php-8-modern-untuk-pemula` |

---

## 💻 Kode Contoh PHP (Siap Jalan di PHP 8.3+)

Simpan kode ini dengan nama `sanitasi_string.php` lalu jalankan via CLI:

```php
<?php

// 1. Sanitasi Input Pendaftaran Akun
$rawNama = "   budi santoso pratama   ";
$rawEmail = "  BUDI.Santoso@GMAIL.COM  ";
$rawTelepon = "0812-3456-7890";

// Bersihkan dan format nama
$namaValid = ucwords(trim($rawNama));

// Bersihkan dan kecilkan email
$emailValid = strtolower(trim($rawEmail));

// Hapus tanda strip pada nomor telepon agar hanya tersisa angka
$teleponValid = str_replace("-", "", $rawTelepon);

echo "=== Data Pengguna Bersih ===\n";
echo "Nama    : " . $namaValid . "\n";
echo "Email   : " . $emailValid . "\n";
echo "Telepon : " . $teleponValid . "\n\n";

// 2. Fitur Pencarian Kata Modern (PHP 8.0+)
echo "=== Validasi Akun ===\n";
if (str_contains($emailValid, "@gmail.com")) {
    echo "- Email menggunakan domain Google Mail.\n";
}

if (str_starts_with($teleponValid, "08")) {
    echo "- Nomor telepon valid format Indonesia (diawali 08).\n";
}

// 3. Mengubah Kalimat Menjadi Tag Array (explode & implode)
$tagsString = "php, backend, laravel, coding";
$tagArray = explode(", ", $tagsString); // Pecah jadi array

echo "\nJumlah Tag: " . count($tagArray) . "\n";
echo "Tag Pertama: " . $tagArray[0] . "\n";
echo "Gabung Ulang dengan Pagar: #" . implode(" #", $tagArray) . "\n";
```

### Hasil Keluaran Terminal:
```text
=== Data Pengguna Bersih ===
Nama    : Budi Santoso Pratama
Email   : budi.santoso@gmail.com
Telepon : 081234567890

=== Validasi Akun ===
- Email menggunakan domain Google Mail.
- Nomor telepon valid format Indonesia (diawali 08).

Jumlah Tag: 4
Tag Pertama: php
Gabung Ulang dengan Pagar: #php #backend #laravel #coding
```

---

## ⚠️ Jebakan Umum

| Kesalahan | Contoh Salah ❌ | Contoh Benar ✅ | Penjelasan Teknis |
| :--- | :--- | :--- | :--- |
| **Menghitung Panjang Teks** | `count("Halo Dunia")` | `strlen("Halo Dunia")` | `count()` hanya untuk Array. Untuk mengukur panjang teks karakter, gunakan `strlen()`. |
| **Lupa Menampung Hasil String** | `trim($nama);` (berharap `$nama` berubah sendiri) | `$nama = trim($nama);` | Fungsi string di PHP **tidak mengubah variabel aslinya secara langsung**, melainkan menghasilkan teks baru yang harus ditampung kembali. |
| **Urutan Parameter `explode`** | `explode($kalimat, ",")` | `explode(",", $kalimat)` | Formatnya: **(tanda pemisah, kalimat asal)**. Jangan sampai terbalik! |
| **Pencarian Huruf Besar/Kecil** | `str_contains("Budi", "budi")` ➔ `false` | `str_contains(strtolower($teks), "budi")` | `str_contains` bersifat *case-sensitive* (peka huruf kapital). Samakan dulu ke huruf kecil jika ingin pencarian bebas kapital. |

---

## 🧩 Kuis Mini Interaktif

Kerjakan kuis ini di berkas [Kuis_Bab_09.md](../03_Jawaban_Kuis/Kuis_Bab_09.md).

### Soal 1 — Pilihan Ganda (10 poin)
Perhatikan baris kode berikut:
```php
<?php
$hobi = "makan,tidur,koding";
$hasil = explode(",", $hobi);
echo $hasil[2];
```
Apa teks yang dicetak di terminal?
- **A)** `makan`
- **B)** `tidur`
- **C)** `koding`
- **D)** `makan,tidur,koding`

### Soal 2 — Jejak Eksekusi (25 poin)
Lengkapi tabel jejak eksekusi untuk program sanitasi kode kupon diskon berikut:
```php
<?php
$rawKupon = "  diskon-merdeka-50  ";

$step1 = trim($rawKupon);
$step2 = strtoupper($step1);
$step3 = str_replace("-", "_", $step2);
$apakahDiskon = str_starts_with($step3, "DISKON");

echo "Kupon : " . $step3 . "\n";
echo "Valid : " . ($apakahDiskon ? "YA" : "TIDAK") . "\n";
```

| Step | Baris Kode | State `$step1` | State `$step2` | State `$step3` | Tampilan Terminal |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | `$step1 = trim(...)` | ? | Belum ada | Belum ada | Kosong |
| **2** | `$step2 = strtoupper(...)` | ? | ? | Belum ada | Kosong |
| **3** | `$step3 = str_replace(...)`| ? | ? | ? | Kosong |
| **4** | `echo Kupon` | - | - | - | ? |
| **5** | `echo Valid` | - | - | - | ? |

### Soal 3 — Temukan Bug (30 poin)
Kode validator email dan username berikut memiliki **2 kesalahan**. Temukan bug tersebut dan perbaiki kodenya agar berjalan dengan benar:
```php
<?php
$username = "  john_doe_99  ";

// 1. Ingin memotong spasi liar dari username dan mengecek panjang karakter
trim($username); // Mengapa $username di bawah tetap memiliki spasi?
$panjang = count($username); // Mengapa baris ini melempar TypeError fatal error?

echo "Username : " . $username . "\n";
echo "Panjang  : " . $panjang . " karakter\n";
```

### Soal 4 — Coding Mini (35 poin)
Buat program PHP bernama `pembuat_slug.php` yang:
1. Mendeklarasikan fungsi `generateSlug(string $judul): string` yang melakukan pembersihan bertahap:
   - Memotong spasi di kedua ujung teks (`trim`).
   - Mengubah seluruh huruf menjadi huruf kecil (`strtolower`).
   - Mengganti spasi `" "` menjadi tanda strip `"-"` (`str_replace`).
   - Mengembalikan teks slug yang sudah jadi (*return*).
2. Panggil fungsi tersebut dengan judul:
   `"  Tutorial Belajar PHP 8 Lengkap  "`
3. Cetak hasil perbandingan judul asli dan slug jadinya ke terminal dengan format:
```text
=== Pembuat URL Slug Otomatis ===
Judul Asli : "  Tutorial Belajar PHP 8 Lengkap  "
Slug URL   : tutorial-belajar-php-8-lengkap
```

