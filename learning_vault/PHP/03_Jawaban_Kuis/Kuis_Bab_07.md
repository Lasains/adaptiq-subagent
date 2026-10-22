---
icon: "📝"
sticker: "📝"
color: "#f59e0b"
tags:
  - php
  - kuis
  - fase-2
---

# 📝 Lembar Jawaban Kuis — Bab 7: Fungsi (`function`, Parameter, & Return Value)

> **Petunjuk**: Tuliskan jawabanmu pada bagian yang telah disediakan di bawah ini. Setelah selesai, beri tahu tutormu di chat agar kuis ini dapat diperiksa dan dinilai!

---

## Soal 1 — Pilihan Ganda (10 poin)
*Perhatikan baris kode berikut:*
```php
<?php
function kalikanDua(int $angka) {
    $hasil = $angka * 2;
}

$nilai = kalikanDua(5);
var_dump($nilai);
```
*Apa output yang dicetak di terminal?*
- **A)** `int(10)`
- **B)** `NULL`
- **C)** `int(5)`
- **D)** Fatal error

**Pilihan Jawaban (A/B/C/D)**:
```text
A
```

---

## Soal 2 — Jejak Eksekusi (25 poin)
*Lengkapi tabel jejak eksekusi untuk program penentu biaya kirim berikut:*
```php
<?php
function hitungOngkir(int $beratKg, string $layanan = "Reguler"): int {
    $tarifPerKg = match ($layanan) {
        "Kilat" => 20000,
        default => 10000,
    };
    return $beratKg * $tarifPerKg;
}

$ongkir1 = hitungOngkir(3);
$ongkir2 = hitungOngkir(2, "Kilat");
echo "Ongkir 1: " . $ongkir1 . "\n";
echo "Ongkir 2: " . $ongkir2 . "\n";
```

| Step  | Pemanggilan                | State Parameter Lokal                | State `$tarifPerKg` | Nilai yang di-Return | Tampilan Terminal |
| :---: | :------------------------- | :----------------------------------- | :------------------ | :------------------- | :---------------- |
| **1** | Deklarasi fungsi           | -                                    | -                   | -                    | Kosong            |
| **2** | `hitungOngkir(3)`          | `$beratKg = 3`, `$layanan = Reguler` | 10000               | 30000                | Kosong            |
| **3** | `hitungOngkir(2, "Kilat")` | `$beratKg = 2`, `$layanan = kilat`   | 20000               | 40000                | Kosong            |
| **4** | `echo Ongkir 1`            | -                                    | -                   | -                    | Ongkir 1: 30000   |
| **5** | `echo Ongkir 2`            | -                                    | -                   | -                    | Ongkir 2: 40000   |

---

## Soal 3 — Temukan Bug (30 poin)
*Kode berikut memiliki **2 kesalahan**. Temukan bug tersebut dan perbaiki agar berjalan dengan benar:*
```php
<?php
$pajakPersen = 11;

// Ingin menghitung nilai pajak dari suatu nominal
function hitungPajak(int $total = 0, int $persen): int {
    $nominalPajak = $total * ($pajakPersen / 100);
    return $nominalPajak;
    echo "Pajak selesai dihitung!\n";
}

$pajak = hitungPajak(100000, 11);
echo "Pajak: " . $pajak . "\n";
```

**Daftar Bug yang Ditemukan**:
1. echo "Pajak selesai dihitung!\n"; harusnya ditaru h sebelum return
2. `$nominalPajak = $total * ($pajakPersen / 100); `

**Kode Perbaikan (Executable)**:
```php
<?php
$pajakPersen = 11;

// Ingin menghitung nilai pajak dari suatu nominal
function hitungPajak(int $total = 0, int $persen): int {
    $nominalPajak = $total * ($persen / 100);
	echo "Pajak selesai dihitung!\n";    
    return $nominalPajak;
}

$pajak = hitungPajak(100000, 11);
echo "Pajak: " . $pajak . "\n";
```

---

## Soal 4 — Coding Mini (35 poin)
*Buat program `kalkulator_bmi.php` sesuai spesifikasi di materi Bab 7.*

**Kode Program Kamu**:
```php
<?php
function hitungBMI(float $beratKg, float $tinggiMeter):float{
	$hasil = $beratKg / ($tinggiMeter * $tinggiMeter);
	return $hasil;
}

function statusBMI(float $bmi): string{
	$status = match($bmi){
		$bmi < 18.5 => "Kurus",
		$bmi <= 24.5 => "Normal",
		default => "Kelebihan Berat Badan",
	};
	return $status;
}

$nilaiBMI = hitungBMI(65, 1.70);
$kategori = statusBMI($nilaiBMI);

echo "=== Analisis Indeks Massa Tubuh (BMI) ===\n";
echo "Nilai BMI : " . round($nilaiBMI, 2) . "\n";
echo "Kategori  : " . $kategori . "\n";
```

---

## 💬 Catatan / Pertanyaan Tambahan:
*(Jika ada bagian materi yang terasa membingungkan atau ingin ditanyakan ke tutor, tuliskan di sini!)*
