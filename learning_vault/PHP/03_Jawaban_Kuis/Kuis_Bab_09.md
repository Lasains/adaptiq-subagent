---
icon: "📝"
sticker: "📝"
color: "#f59e0b"
tags:
  - php
  - kuis
  - fase-2
---

# 📝 Lembar Jawaban Kuis — Bab 9: String & Manipulasi Teks

> **Petunjuk**: Tuliskan jawabanmu pada bagian yang telah disediakan di bawah ini. Setelah selesai, beri tahu tutormu di chat agar kuis ini dapat diperiksa dan dinilai!

---

## Soal 1 — Pilihan Ganda (10 poin)
*Perhatikan baris kode berikut:*
```php
<?php
$hobi = "makan,tidur,koding";
$hasil = explode(",", $hobi);
echo $hasil[2];
```
*Apa teks yang dicetak di terminal?*
- **A)** `makan`
- **B)** `tidur`
- **C)** `koding`
- **D)** `makan,tidur,koding`

**Pilihan Jawaban (A/B/C/D)**:
```text
C
```

---

## Soal 2 — Jejak Eksekusi (25 poin)
*Lengkapi tabel jejak eksekusi untuk program sanitasi kode kupon diskon berikut:*
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

| Step  | Baris Kode                  | State `$step1`    | State `$step2`    | State `$step3`    | Tampilan Terminal          |
| :---: | :-------------------------- | :---------------- | :---------------- | :---------------- | :------------------------- |
| **1** | `$step1 = trim(...)`        | diskon-merdeka-50 | Belum ada         | Belum ada         | Kosong                     |
| **2** | `$step2 = strtoupper(...)`  | diskon-merdeka-50 | DISKON-MERDEKA-50 | Belum ada         | Kosong                     |
| **3** | `$step3 = str_replace(...)` | diskon-merdeka-50 | DISKON-MERDEKA-50 | DISKON_MERDEKA_50 | Kosong                     |
| **4** | `echo Kupon`                | -                 | -                 | -                 | Kupon :  DISKON_MERDEKA_50 |
| **5** | `echo Valid`                | -                 | -                 | -                 | Valid : YA                 |

---

## Soal 3 — Temukan Bug (30 poin)
*Kode validator email dan username berikut memiliki **2 kesalahan**. Temukan bug tersebut dan perbaiki kodenya agar berjalan dengan benar:*
```php
<?php
$username = "  john_doe_99  ";

// 1. Ingin memotong spasi liar dari username dan mengecek panjang karakter
trim($username); // Mengapa $username di bawah tetap memiliki spasi?
$panjang = count($username); // Mengapa baris ini melempar TypeError fatal error?

echo "Username : " . $username . "\n";
echo "Panjang  : " . $panjang . " karakter\n";
```

**Daftar Bug yang Ditemukan**:
1. `trim($username);` tidak disimpan ke variabel
2. `$panjang = count($username);` count itu untuk menghitung jumlah data yang tersimpan di variabel

**Kode Perbaikan (Executable)**:
```php
<?php
$username = "  john_doe_99  ";

// 1. Ingin memotong spasi liar dari username dan mengecek panjang karakter
$username = trim($username); 
$panjang = strlen($username);

echo "Username : " . $username . "\n";
echo "Panjang  : " . $panjang . " karakter\n";
```

---

## Soal 4 — Coding Mini (35 poin)
*Buat program `pembuat_slug.php` sesuai spesifikasi di materi Bab 9.*

**Kode Program Kamu**:
```php
<?php
$judul= "  Tutorial Belajar PHP 8 Lengkap  ";
function generateFlug(string $judul): string{
	$step1 = trim($judul);
	$step2 = strtolower($step1);
	$step3 = str_replace(" ", "-", $step2);
	return $step3;
}

echo "Judul : " . $judul . "\n";
echo "Slug URL : " . generateFlug($judul) . "\n";
```

---

## 💬 Catatan / Pertanyaan Tambahan:
*(Jika ada bagian materi yang terasa membingungkan atau ingin ditanyakan ke tutor, tuliskan di sini!)*

