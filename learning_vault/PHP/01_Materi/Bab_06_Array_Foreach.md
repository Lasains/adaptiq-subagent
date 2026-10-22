---
icon: "📖"
sticker: "📖"
color: "#6366f1"
tags:
  - php
  - materi
  - fase-1
---

# 📚 Bab 06: Array & Perulangan `foreach`

> **Level**: Pemula Murni (*Zero-Knowledge Beginner*)  
> **Prasyarat**: Bab 05 (Perulangan)  
> **Estimasi Waktu**: 25–30 Menit  
> **Target Eksekusi**: PHP 8.3+ via CLI (`php nama_file.php`)  
> **Status Kurikulum**: Bab Terakhir di Fase 1 (Persiapan Menuju Ujian Fase 1)  

---

## 💡 Konsep Utama (Dalam Bahasa Ringkas)

Sampai saat ini, satu variabel hanya mampu menyimpan satu nilai saja (misalnya `$nama = "Budi"`).  
**Array** adalah variabel khusus berbentuk wadah bersekat yang mampu menyimpan banyak data sekaligus dalam satu nama variabel.  
**Perulangan `foreach`** adalah cara paling praktis dan alami di PHP untuk membuka sekat array satu demi satu dari awal sampai habis secara otomatis.

---

## 🔧 Analogi Mekanis Dunia Nyata

| Situasi Nyata | Padanan di PHP | Penjelasan Mekanis |
| :--- | :--- | :--- |
| **Rak Sepatu Bernomor Laci** | Array Terindeks (`['apel', 'jeruk']`) | Tiap kotak memiliki nomor urut otomatis mulai dari angka `0`. |
| **Loker Bernama Pemilik** | Array Asosiatif (`['nama' => 'Budi']`) | Tiap sekat diberi label kata kunci (*key*) buatan kita sendiri. |
| **Pemeriksa Tiket di Kereta** | `foreach ($penumpang as $orang)` | Kondektur mendatangi setiap kursi satu per satu sampai kursi terakhir. |
| **Pemisah Antara Kunci & Nilai** | `foreach ($data as $kunci => $nilai)` | Membaca nama pemilik loker sekaligus barang yang ada di dalamnya. |

---

## 📋 Peta Langkah-demi-Langkah (Dyslexia Friendly)

1. **Membuat Array Sederhana (Kurung Siku `[ ]`)**:
   - Tulis `$buah = ["Apel", "Jeruk", "Mangga"];`.
   - Laci pertama selalu bernomor indeks `0`: `$buah[0]` berisi `"Apel"`.
2. **Membuat Array Berlabel Kunci (*Associative Array*)**:
   - Gunakan tanda panah `=>` untuk memasangkan kunci dengan isinya.
   - Contoh: `$user = ["nama" => "Ali", "umur" => 20];`.
   - Mengambil datanya: `$user["nama"]` menghasilkan `"Ali"`.
3. **Membongkar Array dengan `foreach`**:
   - Format standar: `foreach ($daftarData as $item) { ... }`.
   - Variabel `$item` otomatis berganti isi di setiap putaran sesuai urutan sekat.
4. **Menghitung Total Isi Array**:
   - Gunakan fungsi bawaan `count($buah)` untuk mengetahui berapa jumlah data di dalam array.

---

## 📊 Tabel Jejak Eksekusi Logika (Aphantasia Friendly)

Perhatikan program perulangan array daftar harga belanjaan berikut:

```php
<?php
$hargaBarang = [10000, 25000, 15000];
$totalBelanja = 0;

foreach ($hargaBarang as $harga) {
    $totalBelanja += $harga;
}

echo "Total Bayar: Rp " . $totalBelanja . "\n";
```

Berikut alur mekanis mesin PHP membaca array baris demi baris:

| Step | Baris Kode | Posisi Indeks | State `$harga` | State `$totalBelanja` | Tampilan Terminal |
| :---: | :--- | :---: | :--- | :--- | :--- |
| **1** | `$hargaBarang = [...]` | - | *(belum ada)* | *(belum ada)* | *(kosong)* |
| **2** | `$totalBelanja = 0;` | - | *(belum ada)* | `0` | *(kosong)* |
| **3** | Putaran 1 `foreach` | Indeks `0` | `10000` | `0` | *(kosong)* |
| **4** | `$totalBelanja += $harga;` | Indeks `0` | `10000` | `10000` (0 + 10000) | *(kosong)* |
| **5** | Putaran 2 `foreach` | Indeks `1` | `25000` | `10000` | *(kosong)* |
| **6** | `$totalBelanja += $harga;` | Indeks `1` | `25000` | `35000` (10000 + 25000) | *(kosong)* |
| **7** | Putaran 3 `foreach` | Indeks `2` | `15000` | `35000` | *(kosong)* |
| **8** | `$totalBelanja += $harga;` | Indeks `2` | `15000` | `50000` (35000 + 15000) | *(kosong)* |
| **9** | Akhir array tercapai | - | - | `50000` | *(kosong)* |
| **10** | `echo "Total Bayar: ..."` | - | - | `50000` | `Total Bayar: Rp 50000` |

---

## 💻 Kode Contoh PHP (Siap Jalan di PHP 8.3+)

Simpan berkas ini dengan nama `array_belanja.php` lalu jalankan via CLI:

```php
<?php

// 1. Array Terindeks (Indexed Array)
$daftarSiswa = ["Andi", "Budi", "Citra"];

echo "=== Daftar Nama Siswa ===\n";
foreach ($daftarSiswa as $nomor => $nama) {
    $nomorUrut = $nomor + 1; // Indeks 0 kita jadikan nomor 1
    echo $nomorUrut . ". " . $nama . "\n";
}

echo "\n";

// 2. Array Berlabel / Asosiatif (Sangat Sering Dipakai di Database / Laravel)
$profilPengguna = [
    "username" => "dev_junior",
    "email"    => "junior@belajarphp.com",
    "level"    => "Admin",
    "aktif"    => true,
];

echo "=== Data Profil Pengguna ===\n";
foreach ($profilPengguna as $kunci => $nilai) {
    // Jika nilai berupa boolean, ubah jadi teks agar tidak kosong di terminal
    if (is_bool($nilai)) {
        $nilai = $nilai ? "Aktif" : "Non-Aktif";
    }
    echo ucfirst($kunci) . " : " . $nilai . "\n";
}

echo "\nJumlah data tersimpan: " . count($profilPengguna) . " item.\n";
```

### Hasil Keluaran Terminal:
```text
=== Daftar Nama Siswa ===
1. Andi
2. Budi
3. Citra

=== Data Profil Pengguna ===
Username : dev_junior
Email : junior@belajarphp.com
Level : Admin
Aktif : Aktif

Jumlah data tersimpan: 4 item.
```

---

## ⚠️ Jebakan Umum

| Kesalahan | Contoh Salah ❌ | Contoh Benar ✅ | Penjelasan Teknis |
| :--- | :--- | :--- | :--- |
| **Indeks Array Mulai dari 0** | `$buah = ["A", "B"]; echo $buah[1];` (dikira cetak "A") | `echo $buah[0];` | Laci pertama selalu bernomor `0`, laci kedua bernomor `1`. |
| **Echo Langsung Seluruh Array** | `echo $buah;` | `print_r($buah);` atau `var_dump($buah);` | Perintah `echo` hanya bisa mencetak teks, bukan array. Hasilnya akan muncul peringatan `Array to string conversion`. |
| **Mengakses Kunci yang Tidak Ada** | `$user = ["nama" => "Ali"]; echo $user["umur"];` | `echo $user["umur"] ?? "Belum diisi";` | Memanggil kunci yang belum dibuat akan melempar peringatan `Undefined array key`. Amankan pakai operator `??`. |
| **Menambah Elemen Baru** | `$buah = "Jeruk";` (menimpa array jadi string) | `$buah[] = "Jeruk";` | Gunakan kurung siku kosong `[]` untuk menyisipkan data baru ke bagian akhir array. |

---

## 🧩 Kuis Mini Interaktif

Kerjakan kuis ini di berkas [Kuis_Bab_06.md](../03_Jawaban_Kuis/Kuis_Bab_06.md).

### Soal 1 — Pilihan Ganda (10 poin)
Perhatikan kode berikut:
```php
<?php
$hewan = ["Kucing", "Kelinci", "Burung"];
echo $hewan[1];
```
Apa teks yang muncul di terminal?
- **A)** `Kucing`
- **B)** `Kelinci`
- **C)** `Burung`
- **D)** `1`

### Soal 2 — Jejak Eksekusi (25 poin)
Lengkapi tabel jejak eksekusi untuk program pencarian angka terbesar (*max*) berikut:
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

| Step | Baris / Putaran | State `$item` | Evaluasi `$item > $terbesar` | State `$terbesar` | Tampilan Terminal |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | `$terbesar = 0;` | Belum ada | - | 0 | Kosong |
| **2** | Putaran 1 (Data 12) | 12 | 12 > 0 ➔ TRUE | ? | Kosong |
| **3** | Putaran 2 (Data 45) | 45 | 45 > 12 ➔ TRUE | ? | Kosong |
| **4** | Putaran 3 (Data 8) | 8 | 8 > 45 ➔ ? | ? | Kosong |
| **5** | Selesai Loop | - | - | ? | Kosong |
| **6** | `echo "Maksimal: ..."` | - | - | ? | ? |

### Soal 3 — Temukan Bug & Prediksi Output (30 poin)
Kode kasir berikut memiliki **2 kesalahan**. Temukan bug tersebut dan perbaiki agar berjalan dengan benar tanpa error:
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

### Soal 4 — Coding Mini (35 poin)
Buat program PHP bernama `rekap_nilai_siswa.php` yang:
1. Menyimpan data array asosiatif daftar mata pelajaran dan nilainya:
   - Matematika: 80
   - Bahasa: 90
   - IPA: 70
2. Menghitung total seluruh nilai menggunakan perulangan `foreach`.
3. Menghitung nilai rata-rata: `$rataRata = $totalNilai / count($daftarNilai);`.
4. Menampilkan daftar nilai per mata pelajaran dan nilai rata-rata akhirnya ke terminal.

Output yang diharapkan di terminal:
```text
=== Rekap Nilai Siswa ===
- Matematika : 80
- Bahasa : 90
- IPA : 70
-----------------------
Nilai Rata-rata : 80
```
