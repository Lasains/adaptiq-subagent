---
icon: "📝"
sticker: "📝"
color: "#f59e0b"
tags:
  - php
  - kuis
  - fase-1
---

# 📝 Lembar Jawaban Kuis — Bab 3: Operator

> **Petunjuk**: Tuliskan jawabanmu pada bagian yang telah disediakan di bawah ini. Setelah selesai, beri tahu tutormu di chat agar kuis ini dapat diperiksa dan dinilai!

---

## Soal 1 — Pilihan Ganda (10 poin)
*Perhatikan kode berikut:*
```php
<?php
var_dump(0 == false);
```
*Apa yang ditampilkan di terminal?*
- **A)** `bool(false)`
- **B)** `bool(true)`
- **C)** `int(0)`
- **D)** Error

**Pilihan Jawaban (A/B/C/D)**:
```text
B. bool(true)
```

---

## Soal 2 — Jejak Eksekusi (25 poin)
*Lengkapi tabel berikut:*
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

| Step  | Baris Kode                      | State `$saldo` | State Variabel Lain | Tampilan Terminal |
| :---: | :------------------------------ | :------------- | :------------------ | :---------------- |
| **1** | `$saldo = 200000;`              | 200000         | $cukup = true       | kosong            |
| **2** | `$saldo -= 75000;`              | 125000         | $cukup = true       | kosong            |
| **3** | `$saldo += 50000;`              | 175000         | $cukup = true       | kosong            |
| **4** | `$cukup = $saldo >= 100000;`    | 175000         | $cukup = true       | kosong            |
| **5** | `$pemilik = null;`              |                | $pemilik = Anonim   | Anonim            |
| **6** | `$nama = $pemilik ?? "Anonim";` |                | $nama =             |                   |
| **7** | `echo $saldo . "\n";`           |                |                     |                   |
| **8** | `echo $nama . "\n";`            |                |                     |                   |

---

## Soal 3 — Temukan Bug & Perbaikan (30 poin)
*Kode berikut ada kesalahan. Temukan minimal 2 bug dan tulis kode perbaikannya!*
```php
<?php
$nilai = 85;
$lulus = $nilai => 75;
$bonus = null;
$hadiah = $bonus || "Tidak ada";
echo "Lulus: " + $lulus . "\n";
echo "Hadiah: " . $hadiah . "\n";
```

**Daftar Bug yang Ditemukan**:
1. $hadiah = $bonus || "Tidak ada"; harusnya menggunana ??
2. echo "Lulus: " + $lulus . "\n"; harusnya menggunakan .
3. (tulis bug ketiga jika ada)

**Kode Perbaikan (Executable)**:
```php
<?php
$nilai = 85;
$lulus = $nilai => 75;
$bonus = null;
$hadiah = $bonus ?? "Tidak ada";
echo "Lulus: " . $lulus . "\n";
echo "Hadiah: " . $hadiah . "\n";
```

---

## Soal 4 — Coding Mini (35 poin)
*Buat program `kalkulator_diskon.php` sesuai spesifikasi di materi.*

**Kode Program Kamu**:
```php
<?php
$harga = 10000;
$diskon = 0.1;
$total = $harga / $diskon;

echo "Harga: " . $harga . "\n";
echo "Diskon: " . $diskon . "\n";
echo "Total: " . $total . "\n";
```

---

## 💬 Catatan / Pertanyaan Tambahan:
*(Jika ada bagian materi yang terasa membingungkan atau ingin ditanyakan ke tutor, tuliskan di sini!)*
