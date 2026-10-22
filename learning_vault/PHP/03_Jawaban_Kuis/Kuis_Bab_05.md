---
icon: "📝"
sticker: "📝"
color: "#f59e0b"
tags:
  - php
  - kuis
  - fase-1
---

# 📝 Lembar Jawaban Kuis — Bab 5: Perulangan (`for`, `while`, `do-while`)

> **Petunjuk**: Tuliskan jawabanmu pada bagian yang telah disediakan di bawah ini. Setelah selesai, beri tahu tutormu di chat agar kuis ini dapat diperiksa dan dinilai!

---

## Soal 1 — Pilihan Ganda (10 poin)
*Perhatikan kode berikut:*
```php
<?php
for ($i = 1; $i < 4; $i++) {
    echo $i . " ";
}
```
*Apa output yang dicetak di terminal?*
- **A)** `1 2 3 4 `
- **B)** `1 2 3 `
- **C)** `0 1 2 3 `
- **D)** `1 2 `

**Pilihan Jawaban (A/B/C/D)**:
```text
B
```

---

## Soal 2 — Jejak Eksekusi (25 poin)
*Lengkapi tabel berikut berdasarkan kode di bawah:*
```php
<?php
$total = 0;
for ($x = 1; $x <= 3; $x++) {
    $total += $x * 10;
}
echo "Total: " . $total . "\n";
```

| Step  | Baris Kode             | Evaluasi `$x <= 3` | State `$x` | State `$total` | Tampilan Terminal |
| :---: | :--------------------- | :----------------- | :--------- | :------------- | :---------------- |
| **1** | `$total = 0;`          | -                  | Belum ada  | 0              | Kosong            |
| **2** | Putaran 1: `$x = 1`    | TRUE               | 1          | 10             | Kosong            |
| **3** | Putaran 2: `$x = 2`    | TRUE               | 2          | 30             | Kosong            |
| **4** | Putaran 3: `$x = 3`    | TRUE               | 3          | 30             | Kosong            |
| **5** | Selesai: `$x = 4`      | FALSE              | 4          | 30             | Kosong            |
| **6** | `echo "Total: " . ...` | -                  | 4          | 30             | Total: 30         |

---

## Soal 3 — Temukan Bug & Prediksi Output (30 poin)
*Kode berikut memiliki **2 kesalahan besar**. Temukan bug tersebut dan tulis kode perbaikannya agar program mencetak angka genap dari 2 sampai 8:*
```php
<?php
$hitung = 2;

// Program ingin mencetak angka genap 2, 4, 6, 8
while ($hitung <= 8); {
    echo $hitung . "\n";
    // Apa yang kurang di sini agar perulangan tidak macet selamanya?
}
```

**Daftar Bug yang Ditemukan**:
1. while ($hitung <= 8); {
    echo $hitung . "\n";
    // Apa yang kurang di sini agar perulangan tidak macet selamanya?
} terjadinya infinite loop
2. tidak ada $hitung += 2

**Kode Perbaikan (Executable)**:
```php
<?php
$hitung = 2;
while ($hitung <= 8); {
    echo $hitung . "\n";
    $hitung += 2;
}
```

---

## Soal 4 — Coding Mini (35 poin)
*Buat program `tabel_perkalian.php` sesuai spesifikasi di materi Bab 5.*

**Kode Program Kamu**:
```php
<?php
$pengali = 7;
for($i = 1; $i <= 5; i++){
	$hasil = $pengali * $i;
	echo $pengali . " x " . $i . " = " . $hasil;
}

echo "Selesai!";
```

---

## 💬 Catatan / Pertanyaan Tambahan:
*(Jika ada bagian materi yang terasa membingungkan atau ingin ditanyakan ke tutor, tuliskan di sini!)*
