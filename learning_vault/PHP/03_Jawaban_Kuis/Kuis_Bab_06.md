---
icon: "📝"
sticker: "📝"
color: "#f59e0b"
tags:
  - php
  - kuis
  - fase-1
---

# 📝 Lembar Jawaban Kuis — Bab 6: Array & Perulangan `foreach`

> **Petunjuk**: Tuliskan jawabanmu pada bagian yang telah disediakan di bawah ini. Setelah selesai, beri tahu tutormu di chat agar kuis ini dapat diperiksa dan dinilai!

---

## Soal 1 — Pilihan Ganda (10 poin)
*Perhatikan kode berikut:*
```php
<?php
$hewan = ["Kucing", "Kelinci", "Burung"];
echo $hewan[1];
```
*Apa teks yang muncul di terminal?*
- **A)** `Kucing`
- **B)** `Kelinci`
- **C)** `Burung`
- **D)** `1`

**Pilihan Jawaban (A/B/C/D)**:
```text
B
```

---

## Soal 2 — Jejak Eksekusi (25 poin)
*Lengkapi tabel berikut berdasarkan kode di bawah:*
```php
<?php
$koleksi = [12, 45, 8];
$terbesar = 0;

foreach ($koleksi as $item) {
    if ($item > $terbesar) {
        $terbesar = $item;
    }
}
echo "Maksimal: " . $terbesar . "\n";
```

| Step  | Baris / Putaran        | State `$item` | Evaluasi `$item > $terbesar` | State `$terbesar` | Tampilan Terminal |
| :---: | :--------------------- | :------------ | :--------------------------- | :---------------- | :---------------- |
| **1** | `$terbesar = 0;`       | Belum ada     | -                            | 0                 | Kosong            |
| **2** | Putaran 1 (Data 12)    | 12            | 12 > 0 ➔ TRUE                | 12                | Kosong            |
| **3** | Putaran 2 (Data 45)    | 45            | 45 > 12 ➔ TRUE               | 45                | Kosong            |
| **4** | Putaran 3 (Data 8)     | 8             | 8 > 45 ➔ FALSE               | 45                | Kosong            |
| **5** | Selesai Loop           | -             | -                            | 45                | Kosong            |
| **6** | `echo "Maksimal: ..."` | -             | -                            | 45                | Maksimal: 45      |

---

## Soal 3 — Temukan Bug & Prediksi Output (30 poin)
*Kode kasir berikut memiliki **2 kesalahan**. Temukan bug tersebut dan perbaiki agar berjalan dengan benar tanpa error:*
```php
<?php
$keranjang = [
    "buku"    => 15000,
    "pensil"  => 3000,
];

// Ingin mencetak nama barang dan harganya
foreach ($keranjang as $barang) {
    echo "Barang: " . $barang . " seharga Rp " . $harga . "\n";
}

// Ingin mencetak seluruh array ke layar untuk debug
echo $keranjang;
```

**Daftar Bug yang Ditemukan**:
1. tidak ada variabel $harga yang dideklarasikan
2. foreach ($keranjang as $barang) harusnya ada => $harga disini

**Kode Perbaikan (Executable)**:
```php
<?php
$keranjang = [
    "buku"    => 15000,
    "pensil"  => 3000,
];

// Ingin mencetak nama barang dan harganya
foreach ($keranjang as $barang => $harga) {
    echo "Barang: " . $barang . " seharga Rp " . $harga . "\n";
}

// Ingin mencetak seluruh array ke layar untuk debug
echo $keranjang;
```

---

## Soal 4 — Coding Mini (35 poin)
*Buat program `rekap_nilai_siswa.php` sesuai spesifikasi di materi Bab 6.*

**Kode Program Kamu**:
```php
<?php
$daftarNilai = [
	"Matematika" => 80,
	"Bahasa" => 90,
	"IPA" => 70,
];

foreach ($daftarNilai => $total){
	$totalNilai = array_sum($total);
	$rataRata = $totalNilai / count($daftarNilai);
	
	echo "=== Rekap Nilai Siswa ===";
	echo $daftarNilai . ": " . $total;
	echo "-----------------------";
	echo "Nilai Rata-rata : " . $rataRata;
}


```

---

## 💬 Catatan / Pertanyaan Tambahan:
*(Jika ada bagian materi yang terasa membingungkan atau ingin ditanyakan ke tutor, tuliskan di sini!)*
