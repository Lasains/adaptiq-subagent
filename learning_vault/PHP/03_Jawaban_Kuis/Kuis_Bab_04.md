---
icon: "📝"
sticker: "📝"
color: "#f59e0b"
tags:
  - php
  - kuis
  - fase-1
---

# 📝 Lembar Jawaban Kuis — Bab 4: Percabangan (`if`, `else`, `match`)

> **Petunjuk**: Tuliskan jawabanmu pada bagian yang telah disediakan di bawah ini. Setelah selesai, beri tahu tutormu di chat agar kuis ini dapat diperiksa dan dinilai!

---

## Soal 1 — Pilihan Ganda (10 poin)
*Perhatikan kode berikut:*
```php
<?php
$umur = 15;
if ($umur = 20) {
    echo "Dewasa";
} else {
    echo "Remaja";
}
```
*Apa yang ditampilkan di terminal saat kode di atas dijalankan?*
- **A)** `Remaja`
- **B)** `Dewasa`
- **C)** Error sintaks
- **D)** Tidak menampilkan apa pun

**Pilihan Jawaban (A/B/C/D)**:
```text
A. Remaja
```

---

## Soal 2 — Jejak Eksekusi (25 poin)
*Lengkapi tabel berikut berdasarkan kode di bawah:*
```php
<?php
$durasiJam = 3;
$tarifPerJam = 4000;

if ($durasiJam <= 1) {
    $totalBayar = $tarifPerJam;
} else {
    $totalBayar = $durasiJam * $tarifPerJam;
}

$kategori = match (true) {
    $totalBayar > 20000 => "Parkir Lama",
    default             => "Parkir Standar",
};

echo "Total: " . $totalBayar . "\n";
echo "Kategori: " . $kategori . "\n";
```

| Step  | Baris Kode                                 | Evaluasi Kondisi | State `$totalBayar` | State `$kategori` | Tampilan Terminal       |
| :---: | :----------------------------------------- | :--------------- | :------------------ | :---------------- | :---------------------- |
| **1** | `$durasiJam = 3;`                          | -                | Belum ada           | Belum ada         | Kosong                  |
| **2** | `$tarifPerJam = 4000;`                     | -                | Belum ada           | Belum ada         | Kosong                  |
| **3** | `if ($durasiJam <= 1)`                     | false            | Belum ada           | Belum ada         | Kosong                  |
| **4** | `$totalBayar = $durasiJam * $tarifPerJam;` | -                | 12000               | Belum ada         | Kosong                  |
| **5** | `$kategori = match (true) ...`             | default          | 12000               | Parkir Standar    | Kosong                  |
| **6** | `echo "Total: " . ...`                     | -                | 12000               | (isi string teks) | Total: 12000            |
| **7** | `echo "Kategori: " . ...`                  | -                | (isi angka)         | Parkir Standar    | Kategori: Parkir Stadar |

---

## Soal 3 — Temukan Bug & Prediksi Output (30 poin)
*Periksa kode berikut. Temukan **minimal 2 bug** dan tulis kode perbaikannya agar bisa dieksekusi dengan benar:*
```php
<?php
$poin = 85;

// Syarat: jika poin >= 90 predikat A, jika poin >= 75 predikat B, sisanya C
if ($poin >= 75) {
    $predikat = "B";
} elseif ($poin >= 90) {
    $predikat = "A";
} else {
    $predikat = "C";
}

$status = match ($predikat) {
    "A" => "Sangat Memuaskan",
    "B" => "Memuaskan",
    // Apa yang kurang jika predikat bernilai "C"?
};

echo "Predikat: " . $predikat . "\n";
echo "Status: " . $status . "\n";
```

**Daftar Bug yang Ditemukan**:
1. bagian C di match tidak ada.
2. if ($poin >= 75) {
    $predikat = "B";
} elseif ($poin >= 90) {
    $predikat = "A";
} else {
    $predikat = "C";
} harusnya  angka yang paling tinggi dulu baru ke tengah.

**Kode Perbaikan (Executable)**:
```php
<?php
$poin = 85;

// Syarat: jika poin >= 90 predikat A, jika poin >= 75 predikat B, sisanya C
if ($poin >= 90) {
    $predikat = "A";
} elseif ($poin >= 75) {
    $predikat = "B";
} else {
    $predikat = "C";
}

$status = match ($predikat) {
    "A" => "Sangat Memuaskan",
    "B" => "Memuaskan",
    "C" => "Tidak Memuaskan"
};

echo "Predikat: " . $predikat . "\n";
echo "Status: " . $status . "\n";
```

---

## Soal 4 — Coding Mini (35 poin)
*Buat program `cek_kelayakan.php` sesuai spesifikasi di materi Bab 4.*

**Kode Program Kamu**:
```php
<?php
$penghasilan = 5000000;
$memilikiHutang = false;

if ($penghasilan >= 4000000 && $memilikiHutang = false){
	$statusPersetujuan = "Disetujui";
} else {
	$statusPersetujuan = "Ditolak";
}

$batasPlafon = match($statusPersetujuan){
	"Disetujui" => 20000000,
	default => 0,
}

echo "=== Hasil Analisis Pengajuan ==="
echo "Penghasilan: " . $penghasilan . "\n";
echo "Status: " . $statusPersetujuan . "\n";
echo "Plafon: " . $batasPlafon . "\n";
```

---

## 💬 Catatan / Pertanyaan Tambahan:
*(Jika ada bagian materi yang terasa membingungkan atau ingin ditanyakan ke tutor, tuliskan di sini!)*
