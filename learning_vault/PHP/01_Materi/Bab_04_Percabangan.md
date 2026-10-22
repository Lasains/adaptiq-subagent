---
icon: "📖"
sticker: "📖"
color: "#6366f1"
tags:
  - php
  - materi
  - fase-1
---

# 📚 Bab 04: Percabangan (`if`, `else`, `elseif`, `match`)

> **Level**: Pemula Murni (*Zero-Knowledge Beginner*)  
> **Prasyarat**: Bab 03 (Operator & Boolean)  
> **Estimasi Waktu**: 20–25 Menit  
> **Target Eksekusi**: PHP 8.3+ via CLI (`php nama_file.php`)  

---

## 💡 Konsep Utama (Dalam Bahasa Ringkas)

Secara default, komputer membaca kode dari baris atas ke baris bawah secara berurutan.  
**Percabangan** memberi komputer kemampuan untuk memilih jalur kode mana yang dijalankan berdasarkan suatu syarat (kondisi benar atau salah).  
Jika syarat terpenuhi (`true`), satu jalur kode dijalankan; jika tidak terpenuhi (`false`), jalur lain yang dipilih.  

---

## 🔧 Analogi Mekanis Dunia Nyata

| Situasi Nyata | Padanan di PHP | Penjelasan Mekanis |
| :--- | :--- | :--- |
| **Pintu Tiket Otomatis** | `if ($punyaTiket)` | Pintu terbuka hanya jika sensor mendeteksi tiket valid (`true`). |
| **Jalur Alternatif / Tolak** | `else` | Tindakan cadangan jika syarat di atas tidak terpenuhi (misal: alarm berbunyi). |
| **Banyak Pilihan Kategori** | `elseif ($kondisi)` | Mengecek pilihan kedua atau ketiga jika pilihan pertama gagal. |
| **Tombol Selektor Mesin Cuci** | `match ($opsi)` | Memilih tepat satu aksi cepat berdasarkan tombol yang ditekan (Fitur Modern PHP 8). |

---

## 📋 Peta Langkah-demi-Langkah (Dyslexia Friendly)

1. **Siapkan Syarat (Kondisi Boolean)**:
   - Buat perbandingan yang menghasilkan nilai `true` atau `false` (contoh: `$nilai >= 75`).
2. **Buka Cabang Utama (`if`)**:
   - Tulis `if (kondisi) { ... }`.
   - Kode di dalam kurung kurawal `{ }` **hanya jalan** jika kondisi bernilai `true`.
3. **Sediakan Cabang Alternatif (`elseif`)**:
   - Jika ada kondisi kedua yang ingin diuji saat kondisi pertama `false`.
4. **Pasang Jaring Terakhir (`else`)**:
   - Berfungsi sebagai penampung jika **semua** kondisi di atasnya bernilai `false`.
5. **Gunakan `match` untuk Pencocokan Nilai Tetap (PHP 8.0+)**:
   - Jauh lebih rapi dan aman dibanding deretan `if-else` panjang untuk memeriksa satu nilai pasti.

---

## 📊 Tabel Jejak Eksekusi Logika (Aphantasia Friendly)

Perhatikan program penentu kelulusan dan grade nilai berikut:

```php
<?php
$nilai = 80;

if ($nilai >= 85) {
    $grade = "A";
} elseif ($nilai >= 70) {
    $grade = "B";
} else {
    $grade = "C";
}

echo "Grade: " . $grade . "\n";
```

Berikut tabel jejak eksekusi mesin PHP baris demi baris:

| Step | Baris Kode | Evaluasi Syarat | State `$grade` | Jalur Eksekusi |
| :---: | :--- | :--- | :--- | :--- |
| **1** | `$nilai = 80;` | - | Belum terdefinisi | Mesin menyimpan angka 80 ke `$nilai` |
| **2** | `if ($nilai >= 85)` | `80 >= 85` ➔ **FALSE** | Belum terdefinisi | Blok `{ $grade = "A"; }` **dilewati** |
| **3** | `elseif ($nilai >= 70)` | `80 >= 70` ➔ **TRUE** | Belum terdefinisi | Syarat cocok! Masuk ke blok ini |
| **4** | `$grade = "B";` | - | `"B"` (string) | Nilai `"B"` disimpan ke variabel `$grade` |
| **5** | `else { ... }` | - | `"B"` | Blok `else` **dilewati** karena `elseif` sudah terpenuhi |
| **6** | `echo "Grade: " . ...` | - | `"B"` | Terminal mencetak: `Grade: B` |

---

## 💻 Kode Contoh PHP (Siap Jalan di PHP 8.3+)

Simpan kode ini dengan nama `percabangan.php` lalu jalankan via CLI:

```php
<?php

// 1. Contoh if - else sederhana
$saldo = 50000;
$hargaBarang = 35000;

echo "=== Cek Saldo ===\n";
if ($saldo >= $hargaBarang) {
    $sisa = $saldo - $hargaBarang;
    echo "Pembayaran Berhasil! Sisa saldo: Rp " . $sisa . "\n";
} else {
    echo "Saldo tidak cukup untuk transaksi ini.\n";
}

echo "\n";

// 2. Contoh Ternary Operator (Shorthand if-else 1 baris)
// Format: (kondisi) ? nilai_jika_true : nilai_jika_false;
$statusMember = true;
$diskonTambahan = $statusMember ? "Dapat Diskon 5%" : "Tidak Ada Diskon";
echo "Status Diskon: " . $diskonTambahan . "\n";

echo "\n";

// 3. Contoh match expression modern (PHP 8.0+)
// Sangat umum digunakan di Laravel untuk mapping role pengguna atau status order
$peranUser = "editor";

$hakAkses = match ($peranUser) {
    "admin"     => "Akses Penuh Seluruh Sistem",
    "editor"    => "Akses Edit dan Publikasi Artikel",
    "penulis"   => "Akses Tulis Draft Baru",
    default     => "Akses Baca Saja",
};

echo "Peran User: " . $peranUser . "\n";
echo "Hak Akses : " . $hakAkses . "\n";
```

### Hasil Keluaran Terminal:
```text
=== Cek Saldo ===
Pembayaran Berhasil! Sisa saldo: Rp 15000

Status Diskon: Dapat Diskon 5%

Peran User: editor
Hak Akses : Akses Edit dan Publikasi Artikel
```

---

## ⚠️ Jebakan Umum

| Kesalahan | Contoh Salah ❌ | Contoh Benar ✅ | Penjelasan Teknis |
| :--- | :--- | :--- | :--- |
| **Tertukar `=` dengan `==`** | `if ($role = "admin")` | `if ($role === "admin")` | Satu tanda `=` adalah penugasan (*assignment*), bukan perbandingan! Kondisi ini akan selalu bernilai `true`. |
| **Titik koma setelah `if`** | `if ($x > 5); { echo "Besar"; }` | `if ($x > 5) { echo "Besar"; }` | Titik koma langsung mengakhiri instruksi `if`, sehingga blok `{ }` di bawahnya selalu jalan. |
| **Urutan `elseif` terbalik** | `if ($nilai >= 60) ... elseif ($nilai >= 90) ...` | `if ($nilai >= 90) ... elseif ($nilai >= 60) ...` | Nilai 95 akan terperangkap di `>= 60` lebih dulu, sehingga `>= 90` tidak pernah tersentuh. |
| **Lupa `default` di `match`** | `match ($opsi) { 1 => "A" };` | `match ($opsi) { 1 => "A", default => "B" };` | Jika `$opsi` bernilai selain 1, PHP akan melempar fatal error `UnhandledMatchError`. |

---

## 🧩 Kuis Mini Interaktif

Kerjakan kuis ini di berkas [Kuis_Bab_04.md](../03_Jawaban_Kuis/Kuis_Bab_04.md).

### Soal 1 — Pilihan Ganda (10 poin)
Perhatikan baris kode berikut:
```php
<?php
$umur = 15;
if ($umur = 20) {
    echo "Dewasa";
} else {
    echo "Remaja";
}
```
Apa yang ditampilkan di terminal saat kode di atas dijalankan?
- **A)** `Remaja`
- **B)** `Dewasa`
- **C)** Error sintaks
- **D)** Tidak menampilkan apa pun

### Soal 2 — Jejak Eksekusi (25 poin)
Lengkapi tabel jejak eksekusi untuk program penentu tarif parkir berikut:
```php
<?php
$durasiJam = 3;
$tarifPerJam = 4000;

if ($durasiJam <= 1) {
    $totalBayar = $tarifPerJam;
} else {
    $totalBayar = $durasiJam * $tarifPerJam;
}

$kategori = match (true) {
    $totalBayar > 20000 => "Parkir Lama",
    default             => "Parkir Standar",
};

echo "Total: " . $totalBayar . "\n";
echo "Kategori: " . $kategori . "\n";
```

| Step | Baris Kode | Evaluasi Kondisi | State `$totalBayar` | State `$kategori` | Tampilan Terminal |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | `$durasiJam = 3;` | - | Belum ada | Belum ada | Kosong |
| **2** | `$tarifPerJam = 4000;` | - | Belum ada | Belum ada | Kosong |
| **3** | `if ($durasiJam <= 1)` | ? | ? | Belum ada | Kosong |
| **4** | `$totalBayar = $durasiJam * $tarifPerJam;` | - | ? | Belum ada | Kosong |
| **5** | `$kategori = match (true) ...` | ? | ? | ? | Kosong |
| **6** | `echo "Total: " . ...` | - | ? | ? | ? |
| **7** | `echo "Kategori: " . ...` | - | ? | ? | ? |

### Soal 3 — Temukan Bug & Prediksi Output (30 poin)
Periksa kode berikut. Temukan **minimal 2 bug** dan tulis kode perbaikannya agar bisa dieksekusi dengan benar:
```php
<?php
$poin = 85;

// Syarat: jika poin >= 90 predikat A, jika poin >= 75 predikat B, sisanya C
if ($poin >= 75) {
    $predikat = "B";
} elseif ($poin >= 90) {
    $predikat = "A";
} else {
    $predikat = "C";
}

$status = match ($predikat) {
    "A" => "Sangat Memuaskan",
    "B" => "Memuaskan",
    // Apa yang kurang jika predikat bernilai "C"?
};

echo "Predikat: " . $predikat . "\n";
echo "Status: " . $status . "\n";
```

### Soal 4 — Coding Mini (35 poin)
Buat program PHP bernama `cek_kelayakan.php` yang mensimulasikan sistem persetujuan pinjaman sederhana:
1. Deklarasikan variabel:
   - `$penghasilan = 5000000`
   - `$memilikiHutang = false`
2. Gunakan `if - else` dengan operator logika:
   - Syarat disetujui: `$penghasilan >= 4000000` **DAN** `!$memilikiHutang` (tidak punya hutang).
   - Jika memenuhi syarat, isi variabel `$statusPersetujuan = "DISETUJUI"`.
   - Jika tidak memenuhi syarat, isi `$statusPersetujuan = "DITOLAK"`.
3. Tentukan batas plafon pinjaman menggunakan `match`:
   - Jika status `"DISETUJUI"` ➔ Plafon Rp 20.000.000
   - Jika status `"DITOLAK"` ➔ Plafon Rp 0
   - Sediakan nilai cadangan `default` ➔ Rp 0
4. Cetak output ke terminal dengan format:
```text
=== Hasil Analisis Pengajuan ===
Penghasilan : Rp 5000000
Status      : DISETUJUI
Plafon      : Rp 20000000
```
