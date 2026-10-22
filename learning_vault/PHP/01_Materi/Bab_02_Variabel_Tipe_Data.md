---
icon: "📖"
sticker: "📖"
color: "#6366f1"
tags:
  - php
  - materi
  - fase-1
---

# 📚 Bab 2 — Variabel & Tipe Data

> **Level**: Pemula Murni (*Zero-Knowledge*) | **Prasyarat**: Bab 1 ✅ | **Estimasi Waktu**: 45–55 menit
> **Jalur Spesialisasi**: Persiapan Framework Laravel (Fase 1: Fondasi PHP Murni via CLI)

---

## 💡 Konsep Utama (Dalam Bahasa Ringkas)

**Variabel** adalah kotak berlabel yang digunakan untuk menyimpan nilai di dalam program. Di PHP, semua variabel wajib dimulai dengan tanda dollar `$`. PHP adalah bahasa **dinamis** — artinya tipe data (angka, teks, true/false) ditentukan otomatis dari nilai yang kamu isi, bukan dari deklarasi manual.

---

## 🔧 Analogi Mekanis Dunia Nyata

| Konsep Nyata | Padanan di PHP | Fungsi Mekanis |
| :--- | :--- | :--- |
| **Kotak berlabel stiker nama** | Variabel `$nama` | Wadah penyimpanan nilai; labelnya selalu diawali `$` |
| **Isi kotak: angka bulat** | Tipe `int` | Menyimpan bilangan bulat: `10`, `-3`, `100` |
| **Isi kotak: angka pecahan** | Tipe `float` | Menyimpan bilangan desimal: `3.14`, `99.9` |
| **Isi kotak: kalimat teks** | Tipe `string` | Menyimpan teks diapit `"..."` atau `'...'` |
| **Isi kotak: saklar ON/OFF** | Tipe `bool` | Hanya dua nilai: `true` (nyala) atau `false` (mati) |
| **Kotak kosong tanpa isi** | Tipe `null` | Nilai kosong/tidak ada; ditulis `null` |
| **Label ganti isi** | Reassignment `$x = 5;` lalu `$x = 99;` | Nilai variabel bisa diganti kapan saja |

---

## 📋 Peta Langkah-demi-Langkah (Dyslexia Friendly)

1. **Buat variabel**: Tulis `$namaVariabel = nilai;` — tanda `$` wajib ada di depan.
2. **Isi dengan nilai**: Nilai bisa berupa angka (`42`), teks (`"Halo"`), atau `true`/`false`.
3. **Tampilkan isi variabel**: Gunakan `echo $namaVariabel;` untuk mencetak nilainya.
4. **Gabungkan variabel & teks**: Pakai tanda titik `.` — contoh: `echo "Halo, " . $nama;`
5. **Cek tipe data**: Gunakan fungsi `gettype($variabel)` untuk melihat tipe aktifnya.
6. **Ganti nilai variabel**: Cukup tulis `$variabel = nilaiBaru;` — nilai lama otomatis tergantikan.
7. **Tutup instruksi**: Ingat titik koma `;` di akhir setiap baris perintah.

---

## 📊 Tabel Jejak Eksekusi (Aphantasia Friendly)

Perhatikan program berikut:
```php
<?php
$nama   = "Angga";
$usia   = 25;
$tinggi = 170.5;
$aktif  = true;

echo "Nama: " . $nama . "\n";
echo "Usia: " . $usia . "\n";
echo "Tipe \$aktif: " . gettype($aktif) . "\n";
```

| Step | Baris Kode | State Variabel di Memori | Tampilan Terminal |
| :---: | :--- | :--- | :--- |
| **1** | `$nama = "Angga";` | `$nama = "Angga"` (string) | *(kosong)* |
| **2** | `$usia = 25;` | `$usia = 25` (integer) | *(kosong)* |
| **3** | `$tinggi = 170.5;` | `$tinggi = 170.5` (float) | *(kosong)* |
| **4** | `$aktif = true;` | `$aktif = true` (boolean) | *(kosong)* |
| **5** | `echo "Nama: " . $nama . "\n";` | (tidak berubah) | `Nama: Angga` |
| **6** | `echo "Usia: " . $usia . "\n";` | (tidak berubah) | `Usia: 25` |
| **7** | `echo "Tipe \$aktif: " . gettype($aktif) . "\n";` | (tidak berubah) | `Tipe $aktif: boolean` |

---

## 💻 Kode Contoh PHP (Siap Jalan di PHP 8.3+)

Ketik kode di bawah ini ke dalam berkas `variabel.php`:

```php
<?php

// ── BAGIAN 1: Mendeklarasikan Variabel ──────────────────────────────
$nama      = "Angga";         // string: teks selalu diapit tanda petik
$usia      = 25;               // integer: angka bulat, tanpa petik
$tinggi    = 170.5;            // float: angka desimal, pakai titik
$sudahKerja = true;            // boolean: true (ya) atau false (tidak)
$hobi      = null;             // null: kotak kosong, belum ada isi

// ── BAGIAN 2: Menampilkan Nilai Variabel ─────────────────────────────
echo "=== Data Diri ===\n";
echo "Nama    : " . $nama . "\n";       // sambung teks + variabel pakai titik .
echo "Usia    : " . $usia . "\n";
echo "Tinggi  : " . $tinggi . " cm\n";

// ── BAGIAN 3: Cek Tipe Data dengan gettype() ────────────────────────
echo "\n=== Tipe Data ===\n";
echo "Tipe \$nama      : " . gettype($nama)       . "\n";  // string
echo "Tipe \$usia      : " . gettype($usia)       . "\n";  // integer
echo "Tipe \$tinggi    : " . gettype($tinggi)     . "\n";  // double (alias float)
echo "Tipe \$sudahKerja: " . gettype($sudahKerja) . "\n";  // boolean
echo "Tipe \$hobi      : " . gettype($hobi)       . "\n";  // NULL

// ── BAGIAN 4: Mengganti Nilai Variabel (Reassignment) ────────────────
$usia = 26;                    // nilai lama (25) ditimpa nilai baru (26)
echo "\nUlang Tahun! Usia sekarang: " . $usia . "\n";
```

### Cara Menjalankan di Terminal:
```bash
php variabel.php
```

### Hasil Keluaran Terminal:
```text
=== Data Diri ===
Nama    : Angga
Usia    : 25
Tinggi  : 170.5 cm

=== Tipe Data ===
Tipe $nama      : string
Tipe $usia      : integer
Tipe $tinggi    : double
Tipe $sudahKerja: boolean
Tipe $hobi      : NULL

Ulang Tahun! Usia sekarang: 26
```

> **Catatan**: PHP menyebut tipe `float` sebagai `double` di output `gettype()`. Keduanya sama saja — angka desimal.

---

## ⚠️ Jebakan Umum

| Kesalahan | Contoh Salah ❌ | Contoh Benar ✅ | Penjelasan |
| :--- | :--- | :--- | :--- |
| **Lupa tanda `$`** | `nama = "Angga";` | `$nama = "Angga";` | Tanpa `$`, PHP mengira `nama` adalah sebuah konstanta, bukan variabel. Akan error. |
| **Teks tanpa tanda petik** | `$nama = Angga;` | `$nama = "Angga";` | Tanpa petik, PHP mengira `Angga` adalah nama konstanta/fungsi yang tidak ada. |
| **Angka pakai tanda petik** | `$usia = "25";` | `$usia = 25;` | Bisa jalan, tapi tipenya jadi `string`, bukan `integer`. Bahaya saat dihitung. |
| **Nama variabel pakai spasi** | `$nama depan = "Angga";` | `$namaDepan = "Angga";` | Nama variabel tidak boleh mengandung spasi. Gunakan *camelCase*. |
| **Lupa titik koma `;`** | `$nama = "Angga"` | `$nama = "Angga";` | Menghasilkan `Parse error`. Setiap baris perintah wajib diakhiri `;`. |

---

## 🧩 Kuis Mini Interaktif

Kerjakan kuis ini di berkas [Kuis_Bab_02.md](../03_Jawaban_Kuis/Kuis_Bab_02.md).

### Soal 1 — Pilihan Ganda (10 poin)
Perhatikan kode berikut:
```php
<?php
$nilai = "100";
echo gettype($nilai);
```
Apa yang ditampilkan di terminal?
- **A)** `integer`
- **B)** `string`
- **C)** `double`
- **D)** `boolean`

### Soal 2 — Jejak Eksekusi (25 poin)
Lengkapi tabel jejak eksekusi untuk program di bawah ini:
```php
<?php
$stok = 50;
echo "Stok awal: " . $stok . "\n";
$stok = $stok - 10;
echo "Stok setelah terjual: " . $stok . "\n";
```

| Step | Baris Kode | State `$stok` | Tampilan Terminal |
| :---: | :--- | :--- | :--- |
| 1 | `$stok = 50;` | *(isi sendiri)* | *(isi sendiri)* |
| 2 | `echo "Stok awal: " . $stok . "\n";` | *(isi sendiri)* | *(isi sendiri)* |
| 3 | `$stok = $stok - 10;` | *(isi sendiri)* | *(isi sendiri)* |
| 4 | `echo "Stok setelah terjual: " . $stok . "\n";` | *(isi sendiri)* | *(isi sendiri)* |

### Soal 3 — Temukan Bug (30 poin)
Kode berikut mengalami error. Temukan **minimal 2 kesalahan** dan tulis kode perbaikannya!
```php
<?php
$produk = Laptop
$harga  = "15000000"
$ready  = ya;
echo "Produk : " . produk . "\n";
echo "Harga  : " . $harga . "\n";
```

### Soal 4 — Coding Mini (35 poin)
Buat program PHP bernama `biodata.php` yang mendeklarasikan **5 variabel** berikut dan menampilkan semuanya dengan `echo`:
1. `$nama` — nama panggilanmu (string)
2. `$kota` — kota asalmu (string)
3. `$umur` — umurmu sekarang (integer)
4. `$tinggiBadan` — tinggi badanmu dalam cm (float)
5. `$sudahBelajarPHP` — apakah kamu sudah mulai belajar PHP? (boolean: `true`)

Output yang diharapkan (sesuaikan dengan datamu):
```text
=== Biodata Saya ===
Nama          : Angga
Kota Asal     : Jakarta
Umur          : 25
Tinggi Badan  : 170.5 cm
Belajar PHP   : 1
```
> 💡 **Hint**: PHP menampilkan `true` sebagai `1` dan `false` sebagai string kosong saat di-echo.
