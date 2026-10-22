---
icon: "📝"
sticker: "📝"
color: "#f59e0b"
tags:
  - php
  - kuis
  - fase-1
---

# 📝 Lembar Jawaban Kuis — Bab 2: Variabel & Tipe Data

> **Petunjuk**: Tuliskan jawabanmu pada bagian yang telah disediakan di bawah ini. Setelah selesai, beri tahu tutormu di chat agar kuis ini dapat diperiksa dan dinilai!

---

## Soal 1 — Pilihan Ganda (10 poin)
*Perhatikan kode berikut:*
```php
<?php
$nilai = "100";
echo gettype($nilai);
```
*Apa yang ditampilkan di terminal?*
- **A)** `integer`
- **B)** `string`
- **C)** `double`
- **D)** `boolean`

**Pilihan Jawaban (A/B/C/D)**:
```text
B. string
```

---

## Soal 2 — Jejak Eksekusi (25 poin)
*Lengkapi tabel jejak eksekusi untuk program di bawah ini:*
```php
<?php
$stok = 50;
echo "Stok awal: " . $stok . "\n";
$stok = $stok - 10;
echo "Stok setelah terjual: " . $stok . "\n";
```

| Step  | Baris Kode                                      | State `$stok` | Tampilan Terminal        |
| :---: | :---------------------------------------------- | :------------ | :----------------------- |
| **1** | `$stok = 50;`                                   | 50            | kosong                   |
| **2** | `echo "Stok awal: " . $stok . "\n";`            | 50            | Stok awal: 50            |
| **3** | `$stok = $stok - 10;`                           | 40            | kosong                   |
| **4** | `echo "Stok setelah terjual: " . $stok . "\n";` | 40            | Stok setelah terjual: 40 |

---

## Soal 3 — Temukan Bug & Perbaikan (30 poin)
*Kode berikut mengalami error. Temukan minimal 2 kesalahan dan tulis kode perbaikannya!*
```php
<?php
$produk = Laptop
$harga  = "15000000"
$ready  = ya;
echo "Produk : " . produk . "\n";
echo "Harga  : " . $harga . "\n";
```

**Daftar Bug yang Ditemukan**:
1. $produk = Laptop kutip dan itik koma
2. $harga  = "15000000" titik koma
3. $ready  = ya; harusnya True atau kalau bukan kutip

**Kode Perbaikan (Executable)**:
```php
<?php
$produk = "Laptop";
$harga  = "15000000";
$ready  = true;
echo "Produk : " . produk . "\n";
echo "Harga  : " . $harga . "\n";
```

---

## Soal 4 — Coding Mini (35 poin)
*Buat program PHP bernama `biodata.php` dengan 5 variabel bertipe berbeda dan tampilkan semuanya.*

**Kode Program Kamu**:
```php
<?php
$nama = "Angga";
$jenisKelamin = 'L';
$umur = 19;
$beratBadan = 120.3;
$punyaPacar = false;
```

---

## 💬 Catatan / Pertanyaan Tambahan:
*(Jika ada bagian materi yang terasa membingungkan atau ingin ditanyakan ke tutor, tuliskan di sini!)*
