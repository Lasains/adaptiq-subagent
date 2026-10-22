---
icon: "📖"
sticker: "📖"
color: "#6366f1"
tags:
  - php
  - materi
  - fase-2
---

# 📚 Bab 07: Fungsi (`function`, Parameter, & Return Value)

> **Level**: Menengah Awal (*Fase 2: Struktur Modular*)  
> **Prasyarat**: Lulus Ujian Akhir Fase 1 (Fondasi PHP Murni)  
> **Estimasi Waktu**: 25–30 Menit  
> **Target Eksekusi**: PHP 8.3+ via CLI (`php nama_file.php`)  

---

## 💡 Konsep Utama (Dalam Bahasa Ringkas)

Sampai saat ini, jika kita butuh rumus hitung diskon di 5 tempat berbeda, kita terpaksa menyalin baris kode yang sama sebanyak 5 kali.  
**Fungsi (*function*)** adalah pabrik mini buatan kita sendiri yang membungkus sekumpulan perintah menjadi satu nama alat yang bisa dipanggil berulang kali kapan saja.  
Fungsi menerima bahan mentah masukan (**parameter**), memprosesnya di dalam, lalu mengeluarkan hasil olahannya (**return value**).

---

## 🔧 Analogi Mekanis Dunia Nyata

| Situasi Nyata | Padanan di PHP | Penjelasan Mekanis |
| :--- | :--- | :--- |
| **Mesin Pembuat Jus (Blender)** | `function buatJus(...)` | Wadah pemroses yang sudah dirakit sekali dan siap dipakai berkali-kali. |
| **Buah yang Dimasukkan ke Corong** | Parameter `$buah` | Bahan mentah yang dioper ke dalam fungsi saat dipanggil. |
| **Gelas Jus yang Keluar di Bawah** | `return $hasil;` | Produk akhir yang dikembalikan ke pemanggil untuk diminum atau disimpan. |
| **Resep Standar (Gula Default)** | `string $manis = "Normal"` | Nilai cadangan jika pemanggil tidak menyebutkan pilihannya (*default argument*). |

---

## 📋 Peta Langkah-demi-Langkah (Dyslexia Friendly)

1. **Membuat Wadah Fungsi (`function`)**:
   - Tulis kata kunci `function namaFungsi(parameter) { ... }`.
   - Gunakan nama yang berupa kata kerja (contoh: `hitungTotal`, `formatRupiah`).
2. **Menentukan Bahan Masukan (Parameter & Tipe Data)**:
   - PHP 8.3 mendukung *Type Hinting*: `function sapa(string $nama, int $umur)`.
   - Menghindari salah tipe data sejak awal.
3. **Mengembalikan Nilai Akhir (`return`)**:
   - Kata kunci `return` **menghentikan fungsi seketika** dan menyerahkan hasilnya ke luar.
   - Tanpa `return`, fungsi hanya melakukan tindakan tanpa mengembalikan data apa pun (`null`).
4. **Memanggil Fungsi**:
   - Panggil namanya dan isi bahannya di dalam kurung: `$hasil = hitungTotal(50000, 2);`.

---

## 📊 Tabel Jejak Eksekusi Logika (Aphantasia Friendly)

Perhatikan program penghitung diskon menggunakan fungsi berikut:

```php
<?php
function hitungDiskon(int $harga, int $persen = 10): int {
    $potongan = $harga * ($persen / 100);
    return $harga - $potongan;
}

$bayar1 = hitungDiskon(100000);
$bayar2 = hitungDiskon(200000, 25);

echo "Bayar 1: Rp " . $bayar1 . "\n";
echo "Bayar 2: Rp " . $bayar2 . "\n";
```

Berikut alur mekanis mesin PHP saat melompati dan memanggil fungsi:

| Step | Baris Kode | Posisi Eksekusi | State Variabel Lokal Fungsi | Efek / Nilai yang Dihasilkan |
| :---: | :--- | :--- | :--- | :--- |
| **1** | `function hitungDiskon(...)` | Deklarasi Pabrik | - | Mesin mendaftarkan fungsi ke memori (belum dijalankan) |
| **2** | `$bayar1 = hitungDiskon(100000);` | Pemanggilan 1 | `$harga = 100000`, `$persen = 10` *(default)* | Mesin melompat masuk ke dalam fungsi |
| **3** | `$potongan = ...` | Di dalam fungsi | `$potongan = 10000` | Menghitung potongan 10% |
| **4** | `return $harga - $potongan;` | Keluar fungsi | - | Mengembalikan angka `90000`. Nilai disimpan ke `$bayar1` |
| **5** | `$bayar2 = hitungDiskon(200000, 25);` | Pemanggilan 2 | `$harga = 200000`, `$persen = 25` | Mesin melompat masuk ke fungsi lagi |
| **6** | `return $harga - $potongan;` | Keluar fungsi | `$potongan = 50000` | Mengembalikan angka `150000`. Nilai disimpan ke `$bayar2` |
| **7** | `echo ...` | Program Utama | `$bayar1 = 90000`, `$bayar2 = 150000` | Layar terminal mencetak kedua baris struk |

---

## 💻 Kode Contoh PHP (Siap Jalan di PHP 8.3+)

Simpan kode ini dengan nama `fungsi_dasar.php` lalu jalankan via CLI:

```php
<?php

// 1. Fungsi dengan Type Hinting Modern & Return Type (PHP 8.3)
function formatRupiah(int $angka): string {
    return "Rp " . number_format($angka, 0, ',', '.');
}

// 2. Fungsi dengan Default Parameter
function buatPesanSambutan(string $nama, string $peran = "Member"): string {
    return "Selamat datang, " . $nama . "! Status akun: [" . $peran . "]";
}

// 3. Menggabungkan fungsi-fungsi mini
function hitungSubtotal(int $hargaSatuan, int $qty): int {
    return $hargaSatuan * $qty;
}

// --- PROGRAM UTAMA ---
$hargaBuku = 45000;
$jumlah = 3;

$subtotal = hitungSubtotal($hargaBuku, $jumlah);

echo buatPesanSambutan("Budi Santoso", "VIP") . "\n";
echo "Harga Satuan : " . formatRupiah($hargaBuku) . "\n";
echo "Jumlah Beli  : " . $jumlah . " pcs\n";
echo "Total Bayar  : " . formatRupiah($subtotal) . "\n";
```

### Hasil Keluaran Terminal:
```text
Selamat datang, Budi Santoso! Status akun: [VIP]
Harga Satuan : Rp 45.000
Jumlah Beli  : 3 pcs
Total Bayar  : Rp 135.000
```

---

## ⚠️ Jebakan Umum

| Kesalahan | Contoh Salah ❌ | Contoh Benar ✅ | Penjelasan Teknis |
| :--- | :--- | :--- | :--- |
| **Lupa kata `return`** | `function tambah($a, $b) { $a + $b; }` | `function tambah($a, $b) { return $a + $b; }` | Tanpa `return`, fungsi menghasilkan nilai `null` saat ditampung ke variabel. |
| **Scope Variabel (Variabel Lokal)** | `$x = 10; function tes() { echo $x; }` | Berikan lewat parameter: `function tes($x) { echo $x; }` | Variabel di luar fungsi **tidak bisa dibaca langsung** dari dalam fungsi (terisolasi secara aman). |
| **Posisi Default Parameter** | `function data($a = 1, $b)` | `function data($b, $a = 1)` | Parameter yang memiliki nilai bawaan (*default*) **wajib diletakkan di posisi paling kanan**. |
| **Kode Setelah `return` Mati** | `return $x; echo "Selesai";` | Letakkan echo sebelum `return` | Perintah apa pun setelah baris `return` tidak akan pernah dieksekusi (*unreachable code*). |

---

## 🧩 Kuis Mini Interaktif

Kerjakan kuis ini di berkas [Kuis_Bab_07.md](../03_Jawaban_Kuis/Kuis_Bab_07.md).

### Soal 1 — Pilihan Ganda (10 poin)
Perhatikan baris kode berikut:
```php
<?php
function kalikanDua(int $angka) {
    $hasil = $angka * 2;
}

$nilai = kalikanDua(5);
var_dump($nilai);
```
Apa output yang dicetak di terminal?
- **A)** `int(10)`
- **B)** `NULL`
- **C)** `int(5)`
- **D)** Fatal error

### Soal 2 — Jejak Eksekusi (25 poin)
Lengkapi tabel jejak eksekusi untuk program penentu biaya kirim berikut:
```php
<?php
function hitungOngkir(int $beratKg, string $layanan = "Reguler"): int {
    $tarifPerKg = match ($layanan) {
        "Kilat" => 20000,
        default => 10000,
    };
    return $beratKg * $tarifPerKg;
}

$ongkir1 = hitungOngkir(3);
$ongkir2 = hitungOngkir(2, "Kilat");
echo "Ongkir 1: " . $ongkir1 . "\n";
echo "Ongkir 2: " . $ongkir2 . "\n";
```

| Step | Pemanggilan | State Parameter Lokal | State `$tarifPerKg` | Nilai yang di-Return | Tampilan Terminal |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | Deklarasi fungsi | - | - | - | Kosong |
| **2** | `hitungOngkir(3)` | `$beratKg = 3`, `$layanan = ?` | ? | ? | Kosong |
| **3** | `hitungOngkir(2, "Kilat")` | `$beratKg = 2`, `$layanan = ?` | ? | ? | Kosong |
| **4** | `echo Ongkir 1` | - | - | - | ? |
| **5** | `echo Ongkir 2` | - | - | - | ? |

### Soal 3 — Temukan Bug (30 poin)
Kode berikut memiliki **2 kesalahan**. Temukan bug tersebut dan perbaiki agar berjalan dengan benar:
```php
<?php
$pajakPersen = 11;

// Ingin menghitung nilai pajak dari suatu nominal
function hitungPajak(int $total = 0, int $persen): int {
    $nominalPajak = $total * ($pajakPersen / 100);
    return $nominalPajak;
    echo "Pajak selesai dihitung!\n";
}

$pajak = hitungPajak(100000, 11);
echo "Pajak: " . $pajak . "\n";
```

### Soal 4 — Coding Mini (35 poin)
Buat program PHP bernama `kalkulator_bmi.php` yang memiliki:
1. Fungsi bernama `hitungBMI(float $beratKg, float $tinggiMeter): float`
   - Rumus: `$beratKg / ($tinggiMeter * $tinggiMeter)`
   - Kembalikan nilai hasil BMI (*return*).
2. Fungsi bernama `statusBMI(float $bmi): string`
   - Menggunakan `if - elseif - else` atau `match (true)`:
     - Jika `$bmi < 18.5` ➔ `"Kurus"`
     - Jika `$bmi <= 24.9` ➔ `"Normal"`
     - Sisanya ➔ `"Kelebihan Berat Badan"`
   - Kembalikan teks status (*return*).
3. Panggil kedua fungsi tersebut untuk orang dengan:
   - Berat: `65` kg, Tinggi: `1.70` meter.
4. Tampilkan hasilnya ke terminal dengan format:
```text
=== Analisis Indeks Massa Tubuh (BMI) ===
Nilai BMI : 22.49
Kategori  : Normal
```
*(Gunakan `round($bmi, 2)` jika ingin membulatkan 2 angka di belakang koma).*
