---
icon: "📖"
sticker: "📖"
color: "#6366f1"
tags:
  - php
  - materi
  - fase-1
---

# 📚 Bab 3 — Operator

> **Level**: Pemula Murni (*Zero-Knowledge*) | **Prasyarat**: Bab 1 ✅ Bab 2 ✅ | **Estimasi Waktu**: 50–60 menit
> **Jalur Spesialisasi**: Persiapan Framework Laravel (Fase 1: Fondasi PHP Murni via CLI)

---

## 💡 Konsep Utama (Dalam Bahasa Ringkas)

**Operator** adalah simbol yang memerintahkan komputer untuk melakukan aksi tertentu terhadap satu atau dua nilai. Ada operator untuk **menghitung angka**, **membandingkan dua nilai**, **menggabungkan kondisi logika**, dan **mengisi nilai default secara pintar**. Hasil dari sebuah operator selalu berupa sebuah nilai baru — bisa angka, bisa `true`/`false`.

---

## 🔧 Analogi Mekanis Dunia Nyata

| Konsep Nyata | Padanan di PHP | Contoh |
| :--- | :--- | :--- |
| **Kalkulator (+ − × ÷ %)** | Operator Aritmatika | `$total = 100 + 50;` → `150` |
| **Timbangan: lebih berat / sama?** | Operator Perbandingan (`>`, `<`, `==`, `===`) | `$usia > 17` → `true` atau `false` |
| **Saklar AND: dua kondisi harus ON** | Operator Logika `&&` | `$login && $bayar` → `true` hanya jika keduanya `true` |
| **Saklar OR: salah satu cukup ON** | Operator Logika `\|\|` | `$admin \|\| $moderator` → `true` jika salah satu `true` |
| **Tombol NOT: membalik ON jadi OFF** | Operator Logika `!` | `!true` → `false` |
| **Label cadangan jika kotak kosong** | Null Coalescing `??` | `$nama ?? "Tamu"` → pakai `"Tamu"` jika `$nama` null |

---

## 📋 Peta Langkah-demi-Langkah (Dyslexia Friendly)

### Kelompok 1 — Operator Aritmatika
1. **Penjumlahan** `+` : `$a + $b`
2. **Pengurangan** `-` : `$a - $b`
3. **Perkalian** `*` : `$a * $b`
4. **Pembagian** `/` : `$a / $b` → hasilnya bisa float jika tidak habis bagi
5. **Sisa bagi (modulo)** `%` : `$a % $b` → sisa pembagian, berguna cek angka genap/ganjil
6. **Pangkat** `**` : `$a ** $b` → `2 ** 3` = `8`

### Kelompok 2 — Operator Perbandingan
7. **Sama nilai** `==` : `"5" == 5` → `true` (PHP konversi tipe otomatis)
8. **Sama nilai & tipe** `===` : `"5" === 5` → `false` (tipe berbeda: string vs int)
9. **Tidak sama** `!=` : `$a != $b`
10. **Lebih besar** `>`, **lebih kecil** `<`, `>=`, `<=`

### Kelompok 3 — Operator Logika
11. **DAN** `&&` : kedua sisi harus `true`
12. **ATAU** `||` : minimal satu sisi `true`
13. **BUKAN** `!` : membalik nilai boolean

### Kelompok 4 — Operator Penugasan Singkat
14. **Tambah & simpan** `+=` : `$x += 5` sama dengan `$x = $x + 5`
15. **Kurang & simpan** `-=`, `*=`, `/=`, `%=` — pola yang sama
16. **Null Coalescing** `??` : `$nilai ?? "default"` → pakai kanan jika kiri `null`

---

## 📊 Tabel Jejak Eksekusi (Aphantasia Friendly)

Perhatikan program berikut:
```php
<?php
$harga  = 50000;
$diskon = 10000;
$qty    = 3;

$subtotal  = $harga - $diskon;
$total     = $subtotal * $qty;
$sisaBagi  = $total % 100000;
$cukup     = $total >= 100000;
$nama      = null;
$tampilkan = $nama ?? "Pembeli Umum";
```

| Step | Baris Kode | Nilai Baru | Tipe | Keterangan |
| :---: | :--- | :--- | :--- | :--- |
| 1 | `$harga = 50000;` | `$harga = 50000` | int | Nilai harga satuan |
| 2 | `$diskon = 10000;` | `$diskon = 10000` | int | Nilai potongan |
| 3 | `$qty = 3;` | `$qty = 3` | int | Jumlah barang |
| 4 | `$subtotal = $harga - $diskon;` | `$subtotal = 40000` | int | `50000 - 10000` |
| 5 | `$total = $subtotal * $qty;` | `$total = 120000` | int | `40000 * 3` |
| 6 | `$sisaBagi = $total % 100000;` | `$sisaBagi = 20000` | int | Sisa dari `120000 ÷ 100000` |
| 7 | `$cukup = $total >= 100000;` | `$cukup = true` | bool | `120000 >= 100000` → benar |
| 8 | `$nama = null;` | `$nama = null` | null | Kotak kosong |
| 9 | `$tampilkan = $nama ?? "Pembeli Umum";` | `$tampilkan = "Pembeli Umum"` | string | `$nama` null → pakai nilai kanan |

---

## 💻 Kode Contoh PHP (Siap Jalan di PHP 8.3+)

Ketik kode di bawah ini ke dalam berkas `operator.php`:

```php
<?php

// ── BAGIAN 1: Operator Aritmatika ───────────────────────────────────
$harga  = 50000;
$diskon = 10000;
$qty    = 3;

$subtotal = $harga - $diskon;        // 50000 - 10000 = 40000
$total    = $subtotal * $qty;        // 40000 * 3     = 120000
$ppn      = $total * 0.11;          // 11% dari total = 13200
$bayar    = $total + $ppn;          // total + ppn    = 133200

echo "=== Struk Belanja ===\n";
echo "Harga satuan : Rp " . $harga    . "\n";
echo "Diskon       : Rp " . $diskon   . "\n";
echo "Subtotal     : Rp " . $subtotal . "\n";
echo "Qty          : "    . $qty      . " pcs\n";
echo "Total        : Rp " . $total    . "\n";
echo "PPN 11%      : Rp " . $ppn      . "\n";
echo "Total Bayar  : Rp " . $bayar    . "\n";

// ── BAGIAN 2: Modulo — cek genap/ganjil ────────────────────────────
$angka = 17;
$sisa  = $angka % 2;    // sisa bagi 2: 0 = genap, 1 = ganjil
echo "\n" . $angka . " % 2 = " . $sisa . "\n";   // → 1 (ganjil)

// ── BAGIAN 3: Operator Perbandingan ─────────────────────────────────
echo "\n=== Perbandingan ===\n";
var_dump(5 == "5");    // true  → nilai sama (tipe diabaikan)
var_dump(5 === "5");   // false → tipe berbeda (int vs string)
var_dump(10 > 5);      // true
var_dump(3 <= 3);      // true

// ── BAGIAN 4: Operator Logika ────────────────────────────────────────
$sudahLogin = true;
$sudahBayar = false;

echo "\n=== Logika ===\n";
var_dump($sudahLogin && $sudahBayar);   // false (AND: keduanya harus true)
var_dump($sudahLogin || $sudahBayar);   // true  (OR: salah satu cukup true)
var_dump(!$sudahLogin);                 // false (NOT: membalik true → false)

// ── BAGIAN 5: Null Coalescing (??) ───────────────────────────────────
$namaPengguna = null;
$tampil = $namaPengguna ?? "Tamu";
echo "\nHalo, " . $tampil . "!\n";    // → Halo, Tamu!

// ── BAGIAN 6: Penugasan Singkat (+=, -=, *=) ─────────────────────────
$poin = 100;
$poin += 50;   // $poin = $poin + 50 → 150
$poin -= 30;   // $poin = $poin - 30 → 120
$poin *= 2;    // $poin = $poin * 2  → 240
echo "\nPoin akhir: " . $poin . "\n";
```

### Cara Menjalankan di Terminal:
```bash
php operator.php
```

### Hasil Keluaran Terminal:
```text
=== Struk Belanja ===
Harga satuan : Rp 50000
Diskon       : Rp 10000
Subtotal     : Rp 40000
Qty          : 3 pcs
Total        : Rp 120000
PPN 11%      : Rp 13200
Total Bayar  : Rp 133200

17 % 2 = 1

=== Perbandingan ===
bool(true)
bool(false)
bool(true)
bool(true)

=== Logika ===
bool(false)
bool(true)
bool(false)

Halo, Tamu!

Poin akhir: 240
```

> **Catatan**: `var_dump()` menampilkan tipe + nilai sekaligus — sangat berguna untuk debug. Berbeda dengan `echo` yang hanya cetak nilai.

---

## ⚠️ Jebakan Umum

| Kesalahan | Contoh Salah ❌ | Contoh Benar ✅ | Penjelasan |
| :--- | :--- | :--- | :--- |
| **`==` vs `===`** | `if ("0" == false)` → `true` | `if ("0" === false)` → `false` | `==` hanya bandingkan nilai (bisa konversi tipe), `===` bandingkan nilai **dan** tipe. Di Laravel pakai `===` lebih aman. |
| **Pembagian integer** | `$x = 7 / 2;` dikira `3` | `$x = 7 / 2;` → `3.5` (float) | PHP otomatis hasilkan float jika tidak habis bagi. Jika mau bulat, pakai `intdiv(7, 2)` → `3`. |
| **Salah pakai `+` untuk teks** | `echo "Total: " + $total;` | `echo "Total: " . $total;` | `+` di PHP untuk angka, `.` untuk sambung teks. Hasil `+` dengan string bisa tak terduga. |
| **Lupa `!` untuk membalik** | `$tidakAktif = $aktif;` | `$tidakAktif = !$aktif;` | Tanpa `!`, nilainya hanya disalin, tidak dibalik. |
| **`??` vs `?:`** | `$x = $val ?: "default";` | `$x = $val ?? "default";` | `??` cek apakah **null**. `?:` cek apakah **falsy** (0, "", false, null). Pilih sesuai kebutuhan. |

---

## 🧩 Kuis Mini Interaktif

Kerjakan kuis ini di berkas [Kuis_Bab_03.md](../03_Jawaban_Kuis/Kuis_Bab_03.md).

### Soal 1 — Pilihan Ganda (10 poin)
Perhatikan kode berikut:
```php
<?php
var_dump(0 == false);
```
Apa yang ditampilkan di terminal?
- **A)** `bool(false)`
- **B)** `bool(true)`
- **C)** `int(0)`
- **D)** Error

### Soal 2 — Jejak Eksekusi (25 poin)
Lengkapi tabel jejak eksekusi untuk program berikut:
```php
<?php
$saldo = 200000;
$saldo -= 75000;
$saldo += 50000;
$cukup = $saldo >= 100000;
$pemilik = null;
$nama = $pemilik ?? "Anonim";
echo $saldo . "\n";
echo $nama . "\n";
```

| Step | Baris Kode | State `$saldo` | State Variabel Lain | Tampilan Terminal |
| :---: | :--- | :--- | :--- | :--- |
| 1 | `$saldo = 200000;` | | | |
| 2 | `$saldo -= 75000;` | | | |
| 3 | `$saldo += 50000;` | | | |
| 4 | `$cukup = $saldo >= 100000;` | | `$cukup = ?` | |
| 5 | `$pemilik = null;` | | `$pemilik = ?` | |
| 6 | `$nama = $pemilik ?? "Anonim";` | | `$nama = ?` | |
| 7 | `echo $saldo . "\n";` | | | |
| 8 | `echo $nama . "\n";` | | | |

### Soal 3 — Temukan Bug (30 poin)
Kode berikut ada kesalahan. Temukan **minimal 2 bug** dan tulis kode perbaikannya!
```php
<?php
$nilai = 85;
$lulus = $nilai => 75;
$bonus = null;
$hadiah = $bonus || "Tidak ada";
echo "Lulus: " + $lulus . "\n";
echo "Hadiah: " . $hadiah . "\n";
```

### Soal 4 — Coding Mini (35 poin)
Buat program PHP bernama `kalkulator_diskon.php` yang:
1. Mendeklarasikan variabel `$hargaAsli = 250000` dan `$persen_diskon = 20`
2. Menghitung nilai diskon: `$diskon = $hargaAsli * ($persen_diskon / 100)`
3. Menghitung harga akhir: `$hargaAkhir = $hargaAsli - $diskon`
4. Mengecek apakah harga akhir di bawah 200000 menggunakan operator perbandingan, simpan ke `$murah` (boolean)
5. Menampilkan semua variabel di atas dengan format rapi menggunakan `echo`

Output yang diharapkan:
```text
=== Kalkulator Diskon ===
Harga Asli    : Rp 250000
Diskon 20%    : Rp 50000
Harga Akhir   : Rp 200000
Harga Murah?  : (true atau false)
```
