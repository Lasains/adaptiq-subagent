---
icon: "📝"
sticker: "📝"
color: "#f59e0b"
tags:
  - php
  - kuis
  - fase-2
---

# 📝 Lembar Jawaban Kuis — Bab 10: Closure & Arrow Function (`fn() =>`)

> **Petunjuk**: Tuliskan jawabanmu pada bagian yang telah disediakan di bawah ini. Setelah selesai, beri tahu tutormu di chat agar kuis ini dapat diperiksa dan dinilai!

---

## Soal 1 — Pilihan Ganda (10 poin)
*Perhatikan baris kode berikut:*
```php
<?php
$pengali = 3;
$rumus = fn($angka) => $angka * $pengali;
echo $rumus(4);
```
*Apa teks angka yang dicetak di terminal?*
- **A)** `12`
- **B)** `4`
- **C)** `3`
- **D)** Error: Undefined variable $pengali

**Pilihan Jawaban (A/B/C/D)**:
```text
A.
```

---

## Soal 2 — Jejak Eksekusi (25 poin)
*Lengkapi tabel jejak eksekusi untuk program filter angka berikut:*
```php
<?php
$angka = [5, 12, 8, 20];
$batas = 10;

// Menyaring angka yang lebih besar dari batas
$hasil = array_filter($angka, fn($x) => $x > $batas);
$total = array_sum($hasil);

echo "Total: " . $total . "\n";
```

| Step  | Baris / Bagian           | Nilai `$x` Saat Diuji | Evaluasi `$x > $batas` | Apakah Lolos Saringan? |
| :---: | :----------------------- | :-------------------- | :--------------------- | :--------------------- |
| **1** | Uji elemen 1             | 5                     | 5 > 10                 | Tidak                  |
| **2** | Uji elemen 2             | 12                    | 12 > 10                | Ya                     |
| **3** | Uji elemen 3             | 8                     | 8 > 10                 | Tidak                  |
| **4** | Uji elemen 4             | 20                    | 20 > 10                | Ya                     |
| **5** | Isi Array `$hasil` Akhir | -                     | -                      | 12, 20                 |
| **6** | Keluaran Terminal `echo` | -                     | -                      | Total: 32              |

---

## Soal 3 — Temukan Bug (30 poin)
*Kode berikut memiliki **2 kesalahan sintaks**. Temukan bug tersebut dan tulis kode perbaikannya agar program berjalan tanpa error:*
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

**Daftar Bug yang Ditemukan**:
1. `return $gajiPokok + $tambahanBonus;` $tambahanBonus belum di use
2. `$hitungPajak = fn (int $total) => return $total * 0.10;` arrow function tidak menggunakan return karena hasinya otomatis tersimpan ke variabel

**Kode Perbaikan (Executable)**:
```php
<?php
$tambahanBonus = 50000;

// 1. Ingin membuat fungsi biasa yang mengambil variabel luar
$hitungGaji = function (int $gajiPokok) use ($tambahanBonus) {
    return $gajiPokok + $tambahanBonus;
} // Apa yang kurang di ujung kurung kurawal ini?

// 2. Ingin menyingkat rumus persen dengan Arrow Function
$hitungPajak = fn (int $total) => $total * 0.10; // Mengapa baris ini syntax error?

echo "Gaji: " . $hitungGaji(2000000) . "\n";
echo "Pajak: " . $hitungPajak(100000) . "\n";
```

---

## Soal 4 — Coding Mini (35 poin)
*Buat program `format_produk_modern.php` sesuai spesifikasi di materi Bab 10.*

**Kode Program Kamu**:
```php
<?php
$hargaProduk = [250000, 50000, 100000];
$diskon = 5000;
$hargaDiskon = array_map(fn($harga) => $harga - $diskon, $hargaProduk);

echo "=== Harga Sebelum Diskon ===\n";
print_r($hargaProduk);

echo "=== Harga Setelah Diskon Rp 5000 ===\n";
print_r($hargaDiskon);
```

---

## 💬 Catatan / Pertanyaan Tambahan:
*(Jika ada bagian materi yang terasa membingungkan atau ingin ditanyakan ke tutor, tuliskan di sini!)*
