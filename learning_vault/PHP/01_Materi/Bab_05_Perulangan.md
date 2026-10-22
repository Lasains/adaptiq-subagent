---
icon: "📖"
sticker: "📖"
color: "#6366f1"
tags:
  - php
  - materi
  - fase-1
---

# 📚 Bab 05: Perulangan (`for`, `while`, `do-while`)

> **Level**: Pemula Murni (*Zero-Knowledge Beginner*)  
> **Prasyarat**: Bab 04 (Percabangan & Kondisional)  
> **Estimasi Waktu**: 20–25 Menit  
> **Target Eksekusi**: PHP 8.3+ via CLI (`php nama_file.php`)  

---

## 💡 Konsep Utama (Dalam Bahasa Ringkas)

Tanpa perulangan, untuk mencetak angka 1 sampai 100 kita harus menulis perintah `echo` sebanyak 100 kali.  
**Perulangan (*loop*)** memungkinkan kita menulis satu blok instruksi saja, lalu memerintahkan komputer mengulanginya berkali-kali secara otomatis.  
Perulangan akan terus berputar selama syarat kondisi bernilai `true`, dan baru berhenti saat syarat bernilai `false` atau diputus secara paksa.

---

## 🔧 Analogi Mekanis Dunia Nyata

| Situasi Nyata | Padanan di PHP | Kapan Digunakan |
| :--- | :--- | :--- |
| **Putaran Jarum Jam (12 Detik)** | `for ($i = 1; $i <= 12; $i++)` | Saat **jumlah putaran sudah pasti diketahui** sejak awal. |
| **Menyetir Selama Lampu Hijau** | `while ($lampuHijau)` | Saat **tidak tahu berapa lama berputar**, periksa syarat dulu sebelum jalan. |
| **Cicipi Sup Dulu Sekali** | `do { ... } while ($kurangGaram)` | Kode **pasti dijalankan minimal 1 kali**, baru cek kondisi di akhir. |
| **Rem Darurat Kereta** | `break;` | Menghentikan putaran seketika dan langsung keluar dari loop. |
| **Lompati Antrean Nomor 13** | `continue;` | Lewati putaran saat ini, langsung lompat ke putaran berikutnya. |

---

## 📋 Peta Langkah-demi-Langkah (Dyslexia Friendly)

1. **Struktur Loop `for` (Tiga Bagian Utama)**:
   - `for (titik_mulai; syarat_berputar; perubahan_langkah) { ... }`
   - Bagian 1: `$i = 1` (Penghitung mulai dari angka 1).
   - Bagian 2: `$i <= 5` (Berputar selama `$i` kurang dari atau sama dengan 5).
   - Bagian 3: `$i++` (Setiap kali selesai 1 putaran, tambahkan `$i` dengan 1).
2. **Struktur Loop `while` (Jalan Selama Kondisi Benar)**:
   - Periksa kondisi di pintu gerbang. Jika salah sejak awal, isi loop tidak pernah disentuh.
3. **Struktur Loop `do-while` (Jalan Dulu Baru Cek)**:
   - Jalankan kode minimal satu kali, baru periksa kondisi di bagian bawah.
4. **Alat Kendali Ekstra**:
   - `break;` ➔ Keluar dari perulangan sekarang juga.
   - `continue;` ➔ Lewati sisa kode di putaran ini, lanjutkan ke putaran berikutnya.

---

## 📊 Tabel Jejak Eksekusi Logika (Aphantasia Friendly)

Perhatikan program hitung mundur sederhana berikut:

```php
<?php
$angka = 3;

while ($angka > 0) {
    echo $angka . "\n";
    $angka--;
}

echo "Mulai!\n";
```

Berikut alur mekanis mesin PHP membaca perulangan baris demi baris:

| Step | Baris Kode | Evaluasi Kondisi | State `$angka` | Tampilan Terminal | Keterangan |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | `$angka = 3;` | - | `3` | *(kosong)* | Inisialisasi awal |
| **2** | `while ($angka > 0)` | `3 > 0` ➔ **TRUE** | `3` | *(kosong)* | Kondisi terpenuhi, masuk ke loop |
| **3** | `echo $angka . "\n";`| - | `3` | `3` | Angka 3 dicetak ke terminal |
| **4** | `$angka--;` | - | `2` | `3` | `$angka` berkurang jadi 2 |
| **5** | `while ($angka > 0)` | `2 > 0` ➔ **TRUE** | `2` | `3` | Masuk ke putaran ke-2 |
| **6** | `echo $angka . "\n";`| - | `2` | `2` | Angka 2 dicetak ke terminal |
| **7** | `$angka--;` | - | `1` | `2` | `$angka` berkurang jadi 1 |
| **8** | `while ($angka > 0)` | `1 > 0` ➔ **TRUE** | `1` | `2` | Masuk ke putaran ke-3 |
| **9** | `echo $angka . "\n";`| - | `1` | `1` | Angka 1 dicetak ke terminal |
| **10** | `$angka--;` | - | `0` | `1` | `$angka` berkurang jadi 0 |
| **11** | `while ($angka > 0)` | `0 > 0` ➔ **FALSE** | `0` | `1` | **Syarat GAGAL!** Loop berhenti & keluar |
| **12** | `echo "Mulai!\n";` | - | `0` | `Mulai!` | Baris setelah loop dijalankan |

---

## 💻 Kode Contoh PHP (Siap Jalan di PHP 8.3+)

Simpan kode ini dengan nama `perulangan.php` lalu jalankan via CLI:

```php
<?php

// 1. Loop FOR: Mengulang dengan jumlah pasti (1 sampai 5)
echo "=== Perulangan FOR ===\n";
for ($i = 1; $i <= 5; $i++) {
    echo "Antrean ke-" . $i . "\n";
}

echo "\n";

// 2. Loop WHILE: Berulang selama kondisi terpenuhi
echo "=== Perulangan WHILE ===\n";
$baterai = 30;
while ($baterai < 100) {
    $baterai += 35; // Tambah daya 35%
    if ($baterai > 100) {
        $baterai = 100; // Maksimal 100%
    }
    echo "Daya saat ini: " . $baterai . "%\n";
}

echo "\n";

// 3. Penggunaan BREAK dan CONTINUE
echo "=== BREAK & CONTINUE ===\n";
for ($nomor = 1; $nomor <= 6; $nomor++) {
    // Lewati nomor 3
    if ($nomor === 3) {
        echo "Nomor 3 dilewati!\n";
        continue;
    }

    // Berhenti total di nomor 5
    if ($nomor === 5) {
        echo "Operasi dihentikan di nomor 5!\n";
        break;
    }

    echo "Memproses nomor: " . $nomor . "\n";
}
```

### Hasil Keluaran Terminal:
```text
=== Perulangan FOR ===
Antrean ke-1
Antrean ke-2
Antrean ke-3
Antrean ke-4
Antrean ke-5

=== Perulangan WHILE ===
Daya saat ini: 65%
Daya saat ini: 100%

=== BREAK & CONTINUE ===
Memproses nomor: 1
Memproses nomor: 2
Nomor 3 dilewati!
Memproses nomor: 4
Operasi dihentikan di nomor 5!
```

---

## ⚠️ Jebakan Umum

| Kesalahan | Contoh Salah ❌ | Contoh Benar ✅ | Penjelasan Teknis |
| :--- | :--- | :--- | :--- |
| **Infinite Loop (Loop Abadi)** | `$i = 1; while ($i <= 5) { echo $i; }` | `$i = 1; while ($i <= 5) { echo $i; $i++; }` | Tanpa penambahan `$i++`, nilai `$i` akan selalu 1, sehingga kondisi `1 <= 5` selalu `true` dan program macet selamanya. |
| **Off-by-One Error** | `for ($i = 0; $i < 5; $i++)` (dikira 1-5) | `for ($i = 1; $i <= 5; $i++)` | Mulai dari 0 dengan `< 5` hanya berputar untuk angka 0, 1, 2, 3, 4. Sesuaikan tanda `<` atau `<=` dengan kebutuhan. |
| **Titik koma setelah `for()`** | `for ($i=1; $i<=3; $i++); { echo $i; }` | `for ($i=1; $i<=3; $i++) { echo $i; }` | Titik koma langsung mengakhiri loop sebelum blok `{ }` dijalankan, sehingga `{ }` hanya jalan sekali di akhir. |
| **Tertukar `break` dan `continue`** | Mau lompat 1 kali tapi pakai `break;` | Gunakan `continue;` | `break` menghentikan loop sepenuhnya, sedangkan `continue` hanya melewati 1 putaran aktif. |

---

## 🧩 Kuis Mini Interaktif

Kerjakan kuis ini di berkas [Kuis_Bab_05.md](../03_Jawaban_Kuis/Kuis_Bab_05.md).

### Soal 1 — Pilihan Ganda (10 poin)
Perhatikan kode berikut:
```php
<?php
for ($i = 1; $i < 4; $i++) {
    echo $i . " ";
}
```
Apa output yang dicetak di terminal?
- **A)** `1 2 3 4 `
- **B)** `1 2 3 `
- **C)** `0 1 2 3 `
- **D)** `1 2 `

### Soal 2 — Jejak Eksekusi (25 poin)
Lengkapi tabel jejak eksekusi untuk program penjumlahan akumulatif berikut:
```php
<?php
$total = 0;
for ($x = 1; $x <= 3; $x++) {
    $total += $x * 10;
}
echo "Total: " . $total . "\n";
```

| Step | Baris Kode | Evaluasi `$x <= 3` | State `$x` | State `$total` | Tampilan Terminal |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | `$total = 0;` | - | Belum ada | 0 | Kosong |
| **2** | Putaran 1: `$x = 1` | TRUE | 1 | ? | Kosong |
| **3** | Putaran 2: `$x = 2` | TRUE | 2 | ? | Kosong |
| **4** | Putaran 3: `$x = 3` | TRUE | 3 | ? | Kosong |
| **5** | Selesai: `$x = 4` | ? | 4 | ? | Kosong |
| **6** | `echo "Total: " . ...` | - | 4 | ? | ? |

### Soal 3 — Temukan Bug & Prediksi Output (30 poin)
Kode berikut memiliki **2 kesalahan besar**. Temukan bug tersebut dan tulis kode perbaikannya agar program mencetak angka genap dari 2 sampai 8:
```php
<?php
$hitung = 2;

// Program ingin mencetak angka genap 2, 4, 6, 8
while ($hitung <= 8); {
    echo $hitung . "\n";
    // Apa yang kurang di sini agar perulangan tidak macet selamanya?
}
```

### Soal 4 — Coding Mini (35 poin)
Buat program PHP bernama `tabel_perkalian.php` yang:
1. Menentukan variabel angka pengali: `$pengali = 7;`
2. Menggunakan perulangan `for` dari angka `1` sampai `5`.
3. Di dalam perulangan:
   - Hitung hasil kali: `$hasil = $i * $pengali;`
   - Cetak baris perkalian dengan format rapi.
4. Di luar perulangan, cetak teks penutup `"Selesai!"`.

Output yang diharapkan di terminal:
```text
=== Tabel Perkalian 7 ===
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
Selesai!
```
