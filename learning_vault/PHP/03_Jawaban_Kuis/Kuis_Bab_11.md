---
icon: "📝"
sticker: "📝"
color: "#f59e0b"
tags:
  - php
  - kuis
  - fase-2
---

# 📝 Lembar Jawaban Kuis — Bab 11: Error & Exception Handling

> **Petunjuk**: Tuliskan jawabanmu pada bagian yang telah disediakan di bawah ini. Setelah selesai, beri tahu tutormu di chat agar kuis ini dapat diperiksa dan dinilai!

---

## Soal 1 — Pilihan Ganda (10 poin)
*Perhatikan baris kode berikut:*
```php
<?php
try {
    throw new Exception("Terjadi masalah!");
    echo "A\n";
} catch (Exception $e) {
    echo "B\n";
} finally {
    echo "C\n";
}
```
*Apa yang dicetak di terminal?*
- **A)** `A` kemudian `C`
- **B)** `B` kemudian `C`
- **C)** `A` kemudian `B` kemudian `C`
- **D)** Hanya `C`

**Pilihan Jawaban (A/B/C/D)**:
```text
B
```

---

## Soal 2 — Jejak Eksekusi (25 poin)
*Lengkapi tabel jejak eksekusi untuk program cek stok berikut:*
```php
<?php
function cekStok(int $stok): void {
    if ($stok < 0) {
        throw new InvalidArgumentException("Stok tidak boleh negatif: $stok");
    }
    echo "Stok tersedia: $stok unit\n";
}

try {
    cekStok(10);
    cekStok(-3);
    cekStok(5);
} catch (InvalidArgumentException $e) {
    echo "❌ " . $e->getMessage() . "\n";
} finally {
    echo "Pengecekan stok selesai.\n";
}
```

| Step  | Baris / Bagian          | Nilai Parameter                                 | Kondisi Dievaluasi | Output Terminal                |
| :---: | :---------------------- | :---------------------------------------------- | :----------------- | :----------------------------- |
| **1** | `cekStok(10)` dipanggil | `$stok = 10`                                    | `10 < 0` → Tidak   | Stok tersedia: 10 unit         |
| **2** | `cekStok(-3)` dipanggil | `$stok = -3`                                    | `-3 < 0` → Ya      | ❌ Stok tidak boleh negatif: -3 |
| **3** | Blok `catch` aktif      | `$e` berisi pesan: Stok tidak boleh negatif: -3 | —                  | ❌ Stok tidak boleh negatif: -3 |
| **4** | `cekStok(5)` dipanggil  | `$stok = 5`                                     | —                  | Stok tersedia: 5 unit          |
| **5** | Blok `finally`          | —                                               | —                  | Pengecekan stok selesai.       |

---

## Soal 3 — Temukan Bug (30 poin)
*Kode berikut memiliki **2 kesalahan**. Temukan bug tersebut dan tulis kode perbaikannya agar program berjalan tanpa error:*
```php
<?php
function periksaNilai(int $nilai): string {
    if ($nilai < 0 || $nilai > 100) {
        throw "Nilai harus antara 0-100, diterima: $nilai"; // Bug 1
    }
    return "Nilai $nilai valid.";
}

try {
    echo periksaNilai(150) . "\n";
catch (Exception $e) {                // Bug 2
    echo "Error: " . $e->getMessage();
}
```

**Daftar Bug yang Ditemukan**:
1. tidak ata kata new dan InvalidAgumentException
2. Exception nya tidak jelas dan tidak lengkap harusnya InvalidArgumentException

**Kode Perbaikan (Executable)**:
```php
<?php
function periksaNilai(int $nilai): string {
    if ($nilai < 0 || $nilai > 100) {
        throw new InvalidArgumentException("Nilai harus antara 0-100, diterima: $nilai"); // Bug 1
    }
    return "Nilai $nilai valid.";
}

try {
    echo periksaNilai(150) . "\n";
catch (InvalidArgumentException $e) {                // Bug 2
    echo "Error: " . $e->getMessage();
}
```

---

## Soal 4 — Coding Mini (35 poin)
*Buat program `validasi_usia_anggota.php` sesuai spesifikasi di materi Bab 11.*

**Kode Program Kamu**:
```php
<?php
function daftarAnggota(string $nama, int $usia): string{
	if($usia < 17){
		throw new InvalidArgumentException($nama . " belum cukup umur (min. 17 tahun)");
	} else if($usia > 60){
		throw new InvalidArgumentException($nama . " melebihi batas usia anggota (max. 60 tahun)");
	}
		return "✅ " . $nama . " berhasil didaftarkan (usia: " . $usia . " tahun).";
}

try{
	echo daftarAnggota("Budi", 25) . "\n";
	echo daftarAnggota("Andi", 17) . "\n";
	echo daftarAnggota("Pak Soekarno", 61) . "\n";
}catch (InvalidArgumentException $e){
	echo "Error: " . $e->getMessage();
}
```

---

## 💬 Catatan / Pertanyaan Tambahan:
*(Jika ada bagian materi yang terasa membingungkan atau ingin ditanyakan ke tutor, tuliskan di sini!)*
