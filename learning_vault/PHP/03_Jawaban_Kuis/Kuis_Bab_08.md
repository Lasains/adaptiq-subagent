---
icon: "📝"
sticker: "📝"
color: "#f59e0b"
tags:
  - php
  - kuis
  - fase-2
---

# 📝 Lembar Jawaban Kuis — Bab 8: Array Lanjutan & Fungsi Pengolah Data

> **Petunjuk**: Tuliskan jawabanmu pada bagian yang telah disediakan di bawah ini. Setelah selesai, beri tahu tutormu di chat agar kuis ini dapat diperiksa dan dinilai!

---

## Soal 1 — Pilihan Ganda (10 poin)
*Perhatikan baris kode berikut:*
```php
<?php
$data = [
    ["id" => 1, "kota" => "Bandung"],
    ["id" => 2, "kota" => "Surabaya"],
];

$hasil = array_column($data, "kota");
echo $hasil[1];
```
*Apa teks yang dicetak di terminal?*
- **A)** `Bandung`
- **B)** `Surabaya`
- **C)** `2`
- **D)** Error

**Pilihan Jawaban (A/B/C/D)**:
```text
B
```

---

## Soal 2 — Jejak Eksekusi (25 poin)
*Lengkapi tabel jejak eksekusi untuk program pengolahan nilai berikut:*
```php
<?php
$siswa = [
    ["nama" => "Ali",  "skor" => 80],
    ["nama" => "Budi", "skor" => 60],
    ["nama" => "Cici", "skor" => 90],
];

$daftarSkor = array_column($siswa, "skor");
$lulus = array_filter($daftarSkor, function ($skor) {
    return $skor >= 75;
});

$totalSkorLulus = array_sum($lulus);
$jumlahLulus = count($lulus);
echo "Jumlah Lulus: " . $jumlahLulus . "\n";
echo "Total Skor  : " . $totalSkorLulus . "\n";
```

| Step  | Baris Kode                     | State `$daftarSkor` | State `$lulus` | Nilai Dicetak Terminal |
| :---: | :----------------------------- | :------------------ | :------------- | :--------------------- |
| **1** | `$siswa = [...]`               | Belum ada           | Belum ada      | Kosong                 |
| **2** | `array_column($siswa, "skor")` | 80, 60, 90          | Belum ada      | Kosong                 |
| **3** | `array_filter(...)`            | 80, 60, 90          | 80, 90         | Kosong                 |
| **4** | `echo Jumlah Lulus`            | -                   | -              | Jumlah Lulus: 2        |
| **5** | `echo Total Skor`              | -                   | -              | Total Skor: 170        |

---

## Soal 3 — Temukan Bug (30 poin)
*Kode berikut memiliki **2 kesalahan**. Temukan bug tersebut dan perbaiki kodenya agar berjalan dengan lancar:*
```php
<?php
$antrean = ["dr_andi", "dr_budi", "dr_citra"];

// 1. Ingin memeriksa apakah 'dr_budi' ada di dalam antrean
if (in_array($antrean, "dr_budi")) {
    echo "dr_budi ditemukan dalam antrean!\n";
}

// 2. Ingin menaikkan tarif konsultasi sebesar 10% untuk semua dokter
$tarifAwal = [100000, 150000, 200000];
$tarifBaru = array_map(function ($harga) {
    $tambahan = $harga * 0.10;
    // Apa yang kurang di baris ini agar nilainya kembali ke $tarifBaru?
}, $tarifAwal);

print_r($tarifBaru);
```

**Daftar Bug yang Ditemukan**:
1. function tidak di return
2. di in array juga kebalik harusnya dr_budi dulu baru $antrean

**Kode Perbaikan (Executable)**:
```php
<?php
$antrean = ["dr_andi", "dr_budi", "dr_citra"];

// 1. Ingin memeriksa apakah 'dr_budi' ada di dalam antrean
if (in_array("dr_budi", $antrean)) {
    echo "dr_budi ditemukan dalam antrean!\n";
}

// 2. Ingin menaikkan tarif konsultasi sebesar 10% untuk semua dokter
$tarifAwal = [100000, 150000, 200000];
$tarifBaru = array_map($tarifAwal, function ($harga) {
    $tambahan = $harga * 0.10;
    return $tambahan;
});

print_r($tarifBaru);
```

---

## Soal 4 — Coding Mini (35 poin)
*Buat program `filter_transaksi.php` sesuai spesifikasi di materi Bab 8.*

**Kode Program Kamu**:
```php
<?php
$transaksi = [
    ["id" => "TRX01", "total" => 150000, "status" => "PAID"],
    ["id" => "TRX02", "total" => 50000,  "status" => "PENDING"],
    ["id" => "TRX03", "total" => 200000, "status" => "PAID"],
    ["id" => "TRX04", "total" => 75000,  "status" => "PAID"],
];

$paid = array_filter($transaksi, function($transaksiBaru){
	return $transaksiBaru["status"] === "PAID";
})

$total = array_column($paid, "total");
$jumlahTransaksi = count($paid);
$totalPemasukan = array_sum($total);

echo "=== Laporan Keuangan Toko ===\n";
echo "Jumlah Transaksi Sukses : " . $jumlahTransaksi . " transaksi\n";
echo "Total Pemasukan (PAID)  : Rp " . $totalPemasukan . "\n";
```

---

## 💬 Catatan / Pertanyaan Tambahan:
*(Jika ada bagian materi yang terasa membingungkan atau ingin ditanyakan ke tutor, tuliskan di sini!)*
