---
icon: "📖"
sticker: "📖"
color: "#6366f1"
tags:
  - php
  - materi
  - fase-2
---

# 📚 Bab 08: Array Lanjutan & Fungsi Pengolah Data

> **Level**: Menengah (*Fase 2: Struktur Data & Transformasi*)  
> **Prasyarat**: Bab 06 (Array Dasar & Foreach), Bab 07 (Fungsi)  
> **Estimasi Waktu**: 25–30 Menit  
> **Target Eksekusi**: PHP 8.3+ via CLI (`php nama_file.php`)  
> **Relevansi Web / Laravel**: Sangat Tinggi (Digunakan setiap hari untuk manipulasi data database)  

---

## 💡 Konsep Utama (Dalam Bahasa Ringkas)

Mengolah data array menggunakan perulangan `foreach` manual terkadang membutuhkan banyak baris kode.  
PHP menyediakan **fungsi bawaan array tingkat lanjut** yang mampu menyaring, memotong, dan mengubah isi data secara otomatis dalam 1 baris.  
Alat-alat ini memungkinkan kita mengambil satu kolom spesifik (`array_column`), menyaring data yang memenuhi kriteria (`array_filter`), dan mentransformasi seluruh isi array (`array_map`).

---

## 🔧 Analogi Mekanis Dunia Nyata

| Situasi Nyata | Padanan di PHP | Penjelasan Mekanis |
| :--- | :--- | :--- |
| **Penyaring Pasir Kasar / Saringan Kopi** | `array_filter($data, fungsiCek)` | Hanya meloloskan butiran yang memenuhi syarat ukuran/kriteria tertentu. |
| **Mesin Stempel Pabrik Otomatis** | `array_map(fungsiUbah, $data)` | Menerapkan satu tindakan perubahan yang sama persis ke setiap barang di ban berjalan. |
| **Memetik Satu Kolom di Tabel Excel** | `array_column($data, "harga")` | Memotong dan mengekstrak hanya satu kolom tertentu menjadi daftar 1 dimensi. |
| **Pemeriksa Daftar Hadir Tamu** | `in_array("Ali", $daftar)` | Mengecek dengan cepat apakah suatu nilai ada di dalam daftar (`true`/`false`). |

---

## 📋 Peta Langkah-demi-Langkah (Dyslexia Friendly)

1. **Mengekstrak Satu Kolom (`array_column`)**:
   - Jika kamu punya array 2D katalog dan hanya ingin daftar harga:
   - `$semuaHarga = array_column($katalog, "harga");`
   - Hasilnya adalah array 1 dimensi: `[350000, 150000, 25000, ...]`.
2. **Menyaring Data (`array_filter`)**:
   - Berikan array dan aturan saringannya.
   - Contoh: menyaring angka genap atau barang yang masih ada stok.
3. **Mentransformasi Data (`array_map`)**:
   - Mengubah setiap elemen tanpa perlu membuat array penampung baru.
   - Contoh: menambahkan PPN 11% ke seluruh harga barang.
4. **Mencari Keberadaan Data (`in_array`)**:
   - Format: `in_array(nilai_yang_dicari, $daftarArray)`.
   - Menghasilkan nilai boolean `true` jika ketemu, atau `false` jika tidak ada.

---

## 📊 Tabel Jejak Eksekusi Logika (Aphantasia Friendly)

Perhatikan proses ekstraksi dan penyaringan data berikut:

```php
<?php
$produk = [
    ["nama" => "Buku",   "harga" => 15000],
    ["nama" => "Pensil", "harga" => 3000],
    ["nama" => "Tas",    "harga" => 80000],
];

// 1. Ekstrak hanya kolom harga
$daftarHarga = array_column($produk, "harga");

// 2. Jumlahkan totalnya secara instan
$totalHarga = array_sum($daftarHarga);

echo "Total: Rp " . $totalHarga . "\n";
```

Berikut alur mekanis mesin PHP membaca data:

| Step | Baris Kode | Bentuk Data Asal | Proses Mesin | Hasil yang Disimpan |
| :---: | :--- | :--- | :--- | :--- |
| **1** | `$produk = [...]` | Array 2 Dimensi (3 baris, 2 kolom) | Mendaftarkan 3 barang ke memori | `$produk` terdefinisi |
| **2** | `array_column($produk, "harga")` | Mengambil label `"harga"` dari tiap baris | Memetik: baris 1 (`15000`), baris 2 (`3000`), baris 3 (`80000`) | Array 1D: `[15000, 3000, 80000]` disimpan ke `$daftarHarga` |
| **3** | `array_sum($daftarHarga)` | Array 1 Dimensi `[15000, 3000, 80000]` | Menjumlahkan: `15000 + 3000 + 80000` | Angka integer `98000` disimpan ke `$totalHarga` |
| **4** | `echo ...` | - | Mencetak hasil ke layar terminal | `Total: Rp 98000` |

---

## 💻 Kode Contoh PHP (Siap Jalan di PHP 8.3+)

Simpan kode ini dengan nama `array_lanjutan.php` lalu jalankan via CLI:

```php
<?php

$karyawan = [
    ["nama" => "Doni", "divisi" => "IT",       "gaji" => 8000000],
    ["nama" => "Siti", "divisi" => "Finance",  "gaji" => 7500000],
    ["nama" => "Riko", "divisi" => "IT",       "gaji" => 9000000],
    ["nama" => "Maya", "divisi" => "Marketing", "gaji" => 6500000],
];

// 1. array_column: Ambil daftar nama saja
$daftarNama = array_column($karyawan, "nama");
echo "=== Daftar Nama Karyawan ===\n";
echo implode(", ", $daftarNama) . "\n\n";

// 2. in_array: Cek apakah nama 'Siti' ada di daftar
if (in_array("Siti", $daftarNama)) {
    echo "Status: Siti tercatat sebagai karyawan aktif.\n\n";
}

// 3. array_filter: Saring hanya karyawan dari divisi 'IT'
$karyawanIT = array_filter($karyawan, function ($orang) {
    return $orang["divisi"] === "IT";
});

echo "=== Tim Divisi IT ===\n";
foreach ($karyawanIT as $dev) {
    echo "- " . $dev["nama"] . " (Gaji: Rp " . number_format($dev["gaji"], 0, ',', '.') . ")\n";
}

// 4. Hitung total gaji tim IT menggunakan gabungan fungsi
$gajiIT = array_column($karyawanIT, "gaji");
$totalGajiIT = array_sum($gajiIT);
echo "Total Beban Gaji Divisi IT: Rp " . number_format($totalGajiIT, 0, ',', '.') . "\n";
```

### Hasil Keluaran Terminal:
```text
=== Daftar Nama Karyawan ===
Doni, Siti, Riko, Maya

Status: Siti tercatat sebagai karyawan aktif.

=== Tim Divisi IT ===
- Doni (Gaji: Rp 8.000.000)
- Riko (Gaji: Rp 9.000.000)
Total Beban Gaji Divisi IT: Rp 17.000.000
```

---

## ⚠️ Jebakan Umum

| Kesalahan | Contoh Salah ❌ | Contoh Benar ✅ | Penjelasan Teknis |
| :--- | :--- | :--- | :--- |
| **`array_column` pada Array 1D** | `array_column([1, 2, 3], "harga")` | Hanya gunakan untuk Array 2D (array bersarang) | Array 1 dimensi tidak punya kolom bernama, hasilnya akan berupa array kosong `[]`. |
| **Urutan Parameter `in_array`** | `in_array($daftar, "Doni")` | `in_array("Doni", $daftar)` | Urutannya: **(apa yang dicari, wadah pencarian)**. Tertukar urutan akan menghasilkan `false`. |
| **Indeks Tersisa di `array_filter`** | Menganggap indeksnya urut 0, 1, 2 | Gunakan `array_values($hasil)` jika butuh indeks reset | `array_filter` mempertahankan nomor indeks lama dari data yang lolos. |
| **Return di `array_filter`** | Lupa menulis `return` di fungsi saringan | Wajib `return true;` atau `return false;` | Tanpa `return`, PHP menganggap hasilnya `null` (falsy), sehingga semua data akan terbuang. |

---

## 🧩 Kuis Mini Interaktif

Kerjakan kuis ini di berkas [Kuis_Bab_08.md](../03_Jawaban_Kuis/Kuis_Bab_08.md).

### Soal 1 — Pilihan Ganda (10 poin)
Perhatikan baris kode berikut:
```php
<?php
$data = [
    ["id" => 1, "kota" => "Bandung"],
    ["id" => 2, "kota" => "Surabaya"],
];

$hasil = array_column($data, "kota");
echo $hasil[1];
```
Apa teks yang dicetak di terminal?
- **A)** `Bandung`
- **B)** `Surabaya`
- **C)** `2`
- **D)** Error

### Soal 2 — Jejak Eksekusi (25 poin)
Lengkapi tabel jejak eksekusi untuk program pengolahan nilai berikut:
```php
<?php
$siswa = [
    ["nama" => "Ali",  "skor" => 80],
    ["nama" => "Budi", "skor" => 60],
    ["nama" => "Cici", "skor" => 90],
];

$daftarSkor = array_column($siswa, "skor");
$lulus = array_filter($daftarSkor, function ($skor) {
    return $skor >= 75;
});

$totalSkorLulus = array_sum($lulus);
$jumlahLulus = count($lulus);
echo "Jumlah Lulus: " . $jumlahLulus . "\n";
echo "Total Skor  : " . $totalSkorLulus . "\n";
```

| Step | Baris Kode | State `$daftarSkor` | State `$lulus` | Nilai Dicetak Terminal |
| :---: | :--- | :--- | :--- | :--- |
| **1** | `$siswa = [...]` | Belum ada | Belum ada | Kosong |
| **2** | `array_column($siswa, "skor")` | ? | Belum ada | Kosong |
| **3** | `array_filter(...)` | ? | ? | Kosong |
| **4** | `echo Jumlah Lulus` | - | - | ? |
| **5** | `echo Total Skor` | - | - | ? |

### Soal 3 — Temukan Bug (30 poin)
Kode berikut memiliki **2 kesalahan**. Temukan bug tersebut dan perbaiki kodenya agar berjalan dengan lancar:
```php
<?php
$antrean = ["dr_andi", "dr_budi", "dr_citra"];

// 1. Ingin memeriksa apakah 'dr_budi' ada di dalam antrean
if (in_array($antrean, "dr_budi")) {
    echo "dr_budi ditemukan dalam antrean!\n";
}

// 2. Ingin menaikkan tarif konsultasi sebesar 10% untuk semua dokter
$tarifAwal = [100000, 150000, 200000];
$tarifBaru = array_map(function ($harga) {
    $tambahan = $harga * 0.10;
    // Apa yang kurang di baris ini agar nilainya kembali ke $tarifBaru?
}, $tarifAwal);

print_r($tarifBaru);
```

### Soal 4 — Coding Mini (35 poin)
Buat program PHP bernama `filter_transaksi.php` yang:
1. Memiliki data transaksi toko:
```php
$transaksi = [
    ["id" => "TRX01", "total" => 150000, "status" => "PAID"],
    ["id" => "TRX02", "total" => 50000,  "status" => "PENDING"],
    ["id" => "TRX03", "total" => 200000, "status" => "PAID"],
    ["id" => "TRX04", "total" => 75000,  "status" => "PAID"],
];
```
2. Menggunakan `array_filter` untuk menyaring hanya transaksi yang berstatus `"PAID"`.
3. Menggunakan `array_column` untuk memetik nominal `"total"` dari transaksi yang lolos saringan.
4. Menghitung total omzet masuk menggunakan `array_sum` dan jumlah transaksi sukses menggunakan `count`.
5. Cetak laporan ringkas ke terminal dengan format:
```text
=== Laporan Keuangan Toko ===
Jumlah Transaksi Sukses : 3 transaksi
Total Pemasukan (PAID)  : Rp 425000
```
