---
icon: "📖"
sticker: "📖"
color: "#6366f1"
tags:
  - php
  - materi
  - fase-2
---

# 📚 Bab 10: Closure & Arrow Function (`fn() =>`)

> **Level**: Menengah (*Fase 2: Fungsi Fleksibel & Sintaks Ringkas Modern*)  
> **Prasyarat**: Bab 07 (Fungsi Dasar), Bab 08 (Array Lanjutan & Callback)  
> **Estimasi Waktu**: 25–30 Menit  
> **Target Eksekusi**: PHP 8.3+ via CLI (`php nama_file.php`)  
> **Relevansi Web / Laravel**: Sangat Tinggi (Dipakai di routing Laravel, query database Eloquent, dan event listener)  

---

## 💡 Konsep Utama (Dalam Bahasa Ringkas)

Selama ini, kita membuat fungsi yang memiliki nama tetap di pabrik utama (seperti `function hitungTotal()`).  
**Closure (Fungsi Anonim)** adalah fungsi tanpa nama yang bisa kita simpan ke dalam variabel atau kita selipkan langsung sebagai argumen sekali pakai.  
**Arrow Function (`fn() =>`)** adalah versi modern PHP 8 yang jauh lebih ringkas, otomatis membawa variabel dari luar, dan otomatis mengembalikan nilai (*return*) dalam satu baris ekspresi.

---

## 🔧 Analogi Mekanis Dunia Nyata

| Situasi Nyata | Padanan di PHP | Penjelasan Mekanis |
| :--- | :--- | :--- |
| **Gedung Pabrik Permanen** | Named Function (`function nama()`) | Mesin besar permanen yang terdaftar resmi di sistem. |
| **Peralatan Kerja Portabel di Dalam Koper** | Closure (`$alat = function()`) | Alat mini yang bisa dipindahkan, disimpan ke variabel, atau dipinjamkan ke fungsi lain. |
| **Satu Kartu Izin Akses dari Luar** | Kata Kunci `use ($variabelLuar)` | Izin khusus agar Closure bisa membaca variabel dari lingkungan luar. |
| **Kunci Pas Sekali Putar (Instan)** | Arrow Function (`fn($x) => $x * 2`) | Alat mini 1 baris yang otomatis bisa memakai barang di sekitarnya tanpa izin tambahan. |

---

## 📋 Peta Langkah-demi-Langkah (Dyslexia Friendly)

1. **Membuat Fungsi Tanpa Nama (Closure)**:
   - Format: `$fungsi = function ($parameter) { return ...; };`
   - **Wajib diakhiri titik koma `;`** karena dianggap sebagai penugasan variabel.
   - Cara memanggilnya: `$fungsi("nilai")`.
2. **Membawa Variabel Luar ke Dalam Closure (`use`)**:
   - Fungsi biasa tidak bisa membaca variabel luar secara otomatis.
   - Tambahkan `use ($variabelLuar)` sebelum kurung kurawal buka `{`.
3. **Menyingkat dengan Arrow Function Modern (`fn() =>`)**:
   - Format: `fn($param) => ekspresi;`
   - **Tanpa kata `return`**: Hasil ekspresi di kanan tanda `=>` otomatis dikembalikan.
   - **Tanpa kata `use`**: Variabel dari luar fungsi otomatis terbaca (*auto-capture by value*).

---

## 📊 Tabel Jejak Eksekusi Logika (Aphantasia Friendly)

Perhatikan perbandingan program penambahan diskon member berikut:

```php
<?php
$persenDiskon = 20;

// Menggunakan Arrow Function ringkas (PHP 8.3)
$hitungHargaAkhir = fn (int $harga) => $harga - ($harga * ($persenDiskon / 100));

$bayar = $hitungHargaAkhir(100000);
echo "Total Bayar: Rp " . $bayar . "\n";
```

Berikut alur mekanis mesin PHP membaca kode:

| Step | Baris Kode | Posisi Variabel Luar | Aksi Mesin PHP | Hasil yang Dihasilkan |
| :---: | :--- | :--- | :--- | :--- |
| **1** | `$persenDiskon = 20;` | `$persenDiskon = 20` | Menyimpan angka integer 20 ke memori | Siap digunakan |
| **2** | `$hitungHargaAkhir = fn...` | Terbaca otomatis oleh `fn` | Mesin merakit rumus ekspresi ringkas ke dalam variabel | `$hitungHargaAkhir` berisi fungsi callable |
| **3** | Pemanggilan `$hitungHargaAkhir(100000)` | `$persenDiskon` bernilai 20 | Mesin menghitung: `100000 - (100000 * 0.20) = 80000` | Nilai `80000` otomatis di-return tanpa kata `return` |
| **4** | `$bayar = ...` | - | Nilai `80000` ditampung ke variabel `$bayar` | `$bayar = 80000` |
| **5** | `echo ...` | - | Terminal mencetak keluaran | `Total Bayar: Rp 80000` |

---

## 💻 Kode Contoh PHP (Siap Jalan di PHP 8.3+)

Simpan kode ini dengan nama `closure_arrow.php` lalu jalankan via CLI:

```php
<?php

// 1. Closure Biasa dengan kata kunci 'use'
$pajakPPN = 11; // Variabel luar

$hitungPajak = function (int $subtotal) use ($pajakPPN): int {
    return $subtotal * ($pajakPPN / 100);
};

echo "Pajak dari 100.000: Rp " . $hitungPajak(100000) . "\n\n";

// 2. Perbandingan: Mengubah Data Array dengan array_map
$hargaBarang = [10000, 20000, 50000];

// GAYA LAMA (Closure panjang):
$hargaPlusOngkirLama = array_map(function ($h) {
    return $h + 5000;
}, $hargaBarang);

// GAYA MODERN PHP 8 (Arrow Function 1 baris yang sangat elegan!):
$ongkir = 5000;
$hargaPlusOngkirModern = array_map(fn($h) => $h + $ongkir, $hargaBarang);

echo "=== Hasil Tambah Ongkir (Arrow Function) ===\n";
print_r($hargaPlusOngkirModern);

// 3. Penerapan di Laravel Route Preview
// Di framework Laravel nanti, kamu akan sering menulis seperti ini:
$routeHandler = fn(string $nama) => "Halo dari route, " . ucfirst($nama) . "!";
echo "\n" . $routeHandler("budi") . "\n";
```

### Hasil Keluaran Terminal:
```text
Pajak dari 100.000: Rp 11000

=== Hasil Tambah Ongkir (Arrow Function) ===
Array
(
    [0] => 15000
    [1] => 25000
    [2] => 55000
)

Halo dari route, Budi!
```

---

## ⚠️ Jebakan Umum

| Kesalahan | Contoh Salah ❌ | Contoh Benar ✅ | Penjelasan Teknis |
| :--- | :--- | :--- | :--- |
| **Lupa `;` di Penutup Closure** | `$f = function() { ... }` | `$f = function() { ... };` | Karena fungsi disimpan ke variabel, kurung penutupnya wajib diakhiri titik koma `;`. |
| **Lupa `use` pada Closure Biasa** | `$f = function() { echo $luar; };` | `$f = function() use ($luar) { ... };` | Closure biasa **tidak bisa** membaca variabel luar tanpa izin kata kunci `use`. |
| **Memakai `return` di Arrow Function** | `fn($x) => return $x * 2;` | `fn($x) => $x * 2;` | Arrow function **otomatis mengembalikan** nilai ekspresi. Menulis kata `return` di sana adalah *syntax error*. |
| **Menulis Banyak Baris di Arrow Function** | `fn($x) => { $a = 1; return $a; };` | Gunakan Closure biasa jika butuh multi-baris | Arrow Function hanya boleh memiliki **tepat 1 baris ekspresi** di sebelah kanan tanda `=>`. |

---

## 🧩 Kuis Mini Interaktif

Kerjakan kuis ini di berkas [Kuis_Bab_10.md](../03_Jawaban_Kuis/Kuis_Bab_10.md).

### Soal 1 — Pilihan Ganda (10 poin)
Perhatikan baris kode berikut:
```php
<?php
$pengali = 3;
$rumus = fn($angka) => $angka * $pengali;
echo $rumus(4);
```
Apa teks angka yang dicetak di terminal?
- **A)** `12`
- **B)** `4`
- **C)** `3`
- **D)** Error: Undefined variable $pengali

### Soal 2 — Jejak Eksekusi (25 poin)
Lengkapi tabel jejak eksekusi untuk program filter angka berikut:
```php
<?php
$angka = [5, 12, 8, 20];
$batas = 10;

// Menyaring angka yang lebih besar dari batas
$hasil = array_filter($angka, fn($x) => $x > $batas);
$total = array_sum($hasil);

echo "Total: " . $total . "\n";
```

| Step | Baris / Bagian | Nilai `$x` Saat Diuji | Evaluasi `$x > $batas` | Apakah Lolos Saringan? |
| :---: | :--- | :--- | :--- | :--- |
| **1** | Uji elemen 1 | 5 | 5 > 10 | (Tulis YA / TIDAK) |
| **2** | Uji elemen 2 | 12 | 12 > 10 | (Tulis YA / TIDAK) |
| **3** | Uji elemen 3 | 8 | 8 > 10 | (Tulis YA / TIDAK) |
| **4** | Uji elemen 4 | 20 | 20 > 10 | (Tulis YA / TIDAK) |
| **5** | Isi Array `$hasil` Akhir | - | - | (Tulis isi array lolos) |
| **6** | Keluaran Terminal `echo` | - | - | (Tulis teks terminal) |

### Soal 3 — Temukan Bug (30 poin)
Kode berikut memiliki **2 kesalahan sintaks**. Temukan bug tersebut dan tulis kode perbaikannya agar program berjalan tanpa error:
```php
<?php
$tambahanBonus = 50000;

// 1. Ingin membuat fungsi biasa yang mengambil variabel luar
$hitungGaji = function (int $gajiPokok) {
    return $gajiPokok + $tambahanBonus;
} // Apa yang kurang di ujung kurung kurawal ini?

// 2. Ingin menyingkat rumus persen dengan Arrow Function
$hitungPajak = fn (int $total) => return $total * 0.10; // Mengapa baris ini syntax error?

echo "Gaji: " . $hitungGaji(2000000) . "\n";
echo "Pajak: " . $hitungPajak(100000) . "\n";
```

### Soal 4 — Coding Mini (35 poin)
Buat program PHP bernama `format_produk_modern.php` yang:
1. Memiliki data array harga barang:
   `$hargaProduk = [25000, 50000, 100000];`
2. Memiliki variabel penentu diskon:
   `$potongan = 5000;`
3. Gunakan fungsi `array_map` dengan **Arrow Function modern (`fn() =>`)** untuk memotong setiap harga produk dengan nominal `$potongan`.
4. Cetak hasil perbandingan array harga awal dan array harga setelah diskon menggunakan `print_r`.

Output yang diharapkan di terminal:
```text
=== Harga Sebelum Diskon ===
Array
(
    [0] => 25000
    [1] => 50000
    [2] => 100000
)

=== Harga Setelah Diskon Rp 5000 ===
Array
(
    [0] => 20000
    [1] => 45000
    [2] => 95000
)
```
