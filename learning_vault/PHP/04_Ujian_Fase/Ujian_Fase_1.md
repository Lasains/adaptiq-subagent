---
icon: 🎓
sticker: 🎓
color: "#ec4899"
tags:
  - php
  - ujian
  - fase-1
---

# 🎓 Ujian Akhir Fase 1: Fondasi PHP Murni & Logika Pemrograman

> **Cakupan Materi**: Bab 01 – Bab 06 (Pengenalan, Variabel, Operator, Percabangan, Perulangan, & Array)  
> **Passing Score**: **70%** (Wajib dicapai untuk membuka akses ke Fase 2)  
> **Target Eksekusi**: PHP 8.3+ via CLI (`php nama_file.php`)  
> **Format Pengerjaan**: Tuliskan kode solusi PHP yang executable pada tempat yang disediakan di bawah tiap soal.  

---

## 📋 Petunjuk Ujian
1. Ujian ini menguji kemampuan **menulis program mandiri** yang menggabungkan seluruh konsep dasar di Fase 1.
2. Setiap soal memiliki spesifikasi input data, aturan logika, dan contoh keluaran terminal yang diharapkan.
3. Pastikan kode kamu bebas dari kesalahan sintaks (*syntax error*) dan dapat dijalankan dengan perintah `php nama_file.php`.

---

## 📝 Soal 1 — Program Kasir Mini Diskon (Tingkat: Mudah | Bobot: 25 poin)

Buatlah program PHP untuk menghitung total pembayaran belanja:
1. Deklarasikan variabel:
   - `$namaPelanggan = "Rian";`
   - `$hargaBarang = 45000;`
   - `$jumlahBeli = 3;`
   - `$persenDiskon = 10;` (dalam persen)
2. Hitung:
   - Subtotal: `$hargaBarang * $jumlahBeli`
   - Nominal Diskon: Subtotal dikali `($persenDiskon / 100)`
   - Total Akhir: Subtotal dikurangi Nominal Diskon
3. Tampilkan hasil perhitungan ke terminal secara rapi menggunakan `echo`.

**Format Keluaran Terminal yang Diharapkan**:
```text
=== Struk Belanja Mini ===
Pelanggan    : Rian
Harga Satuan : Rp 45000
Jumlah Beli  : 3 pcs
Subtotal     : Rp 135000
Diskon 10%   : Rp 13500
Total Bayar  : Rp 121500
```

### 💻 Kode Jawaban Soal 1:
```php
<?php
$pelanggan = "Rian";
$hargaBarang = 45000;
$jumlahBeli = 3;
$persenDiskon = 10;
$subtotal = $hargaBarang * $jumlahBeli;
$nominalDiskon = $subtotal * ($persenDiskon / 100);
$totalBayar = $subtotal - $nominalDiskon;

echo "=== Struk Belanja Mini ===";
echo "Pelanggan : " . $pelanggan . "\n";
echo "Harga Satuan : " .  $hargaBarang . "\n";
echo "Jumlah Beli : " . $jumlahBeli . "\n";
echo "Subtotal : " . $subtotal . "\n";
echo "Diskon " . $persenDiskon . "% : " .$nominalDiskon . "\n";
echo "Total Bayar : " . $totalBayar . "\n"; 
```

---

## 📝 Soal 2 — Klasifikasi Tingkat Suhu & Rekomendasi (Tingkat: Sedang | Bobot: 35 poin)

Buatlah program PHP penentu status suhu ruangan menggunakan kombinasi `if - elseif - else` dan ekspresi modern `match`:
1. Deklarasikan variabel:
   - `$suhuCelcius = 32;`
2. Tentukan status kondisi suhu menggunakan `if - elseif - else`:
   - Jika suhu di atas `35` ➔ Status `"Panas Ekstrem"`
   - Jika suhu antara `28` sampai `35` (inklusif) ➔ Status `"Panas"`
   - Jika suhu antara `20` sampai `27` (inklusif) ➔ Status `"Sejuk"`
   - Jika suhu di bawah `20` ➔ Status `"Dingin"`
3. Gunakan ekspresi `match` untuk menentukan saran tindakan berdasarkan status di atas:
   - `"Panas Ekstrem"` ➔ `"Nyalakan AC kecepatan maksimal dan hindari keluar ruangan."`
   - `"Panas"` ➔ `"Nyalakan AC atau kipas angin."`
   - `"Sejuk"` ➔ `"Suhu nyaman, tidak perlu pendingin."`
   - `"Dingin"` ➔ `"Kenakan pakaian hangat atau matikan pendingin."`
   - `default` ➔ `"Kondisi suhu tidak diketahui."`
4. Cetak informasi suhu, status, dan saran tindakan ke terminal.

**Format Keluaran Terminal yang Diharapkan (untuk suhu 32)**:
```text
=== Pemantau Suhu Ruangan ===
Suhu Ruangan : 32°C
Kondisi      : Panas
Saran        : Nyalakan AC atau kipas angin.
```

### 💻 Kode Jawaban Soal 2:
```php
<?php
$suhuCelcius = 32;

if ($suhuCelcius >= 35 ){
	$status = "Panas Ekstream";
} else if ($suhuCelcius >= 28 || $suhuCelcius <= 35){
	$status = "Panas";
} else if ($suhuCelcius >= 20 || $suhuCelcius <= 27){
	$status = "Sejuk";
} else {
	$status = "Dingin";
}

$tindakan = match($status){
	"Panas Ekstream" => "Nyalakan AC kecepatan maksimal dan hindari keluar ruangan",
	"Panas" => "Nyalakan AC atau kipas angin",
	"Sejuk" => "Suhu nyaman, tidak perlu pendingin",
	"Dingin" => "Kenakan pakaian hangat atau matikan pendingin",
	default => "Kondisi suhu tidak diketahui",
};

echo "=== Pemantau Suhu Ruangan === \n";
echo "Suhu Ruangan :" . $suhuCelcius . "°C\n";
echo "Kondisi      :" . $status ."\n";
echo "Saran        :" . $tindakan . "\n";
```

---

## 📝 Soal 3 — Filter & Agregasi Katalog Toko (Tingkat: Menantang | Bobot: 40 poin)

Buatlah program PHP untuk menganalisis data inventaris toko yang tersimpan dalam **Array 2 Dimensi**:
1. Gunakan data katalog berikut:
```php
$katalog = [
    ["nama" => "Keyboard Mekanik", "kategori" => "Elektronik", "harga" => 350000, "tersedia" => true],
    ["nama" => "Mouse Wireless",   "kategori" => "Elektronik", "harga" => 150000, "tersedia" => false],
    ["nama" => "Buku Catatan",     "kategori" => "Alat Tulis", "harga" => 25000,  "tersedia" => true],
    ["nama" => "Headset Gaming",   "kategori" => "Elektronik", "harga" => 200000, "tersedia" => true],
    ["nama" => "Pulpen Gel",       "kategori" => "Alat Tulis", "harga" => 10000,  "tersedia" => true],
];
```
2. Tugas Program:
   - Gunakan perulangan `foreach` untuk memeriksa seluruh item.
   - **Tampilkan hanya barang yang berstatus `tersedia === true`** dengan format nomor urut berurutan.
   - Hitung **total harga** dan **banyaknya barang** yang tersedia tersebut.
   - Hitung **rata-rata harga** dari barang-barang yang tersedia (`$totalHarga / $jumlahTersedia`).
3. Tampilkan rangkuman data di akhir program.

**Format Keluaran Terminal yang Diharapkan**:
```text
=== Daftar Produk Tersedia ===
1. Keyboard Mekanik (Elektronik) - Rp 350000
2. Buku Catatan (Alat Tulis) - Rp 25000
3. Headset Gaming (Elektronik) - Rp 200000
4. Pulpen Gel (Alat Tulis) - Rp 10000
--------------------------------------------------
Total Produk Siap Jual : 4 barang
Total Nilai Stok       : Rp 585000
Rata-rata Harga Stok   : Rp 146250
```

### 💻 Kode Jawaban Soal 3:
```php
<?php
$katalog = [
    ["nama" => "Keyboard Mekanik", "kategori" => "Elektronik", "harga" => 350000, "tersedia" => true],
    ["nama" => "Mouse Wireless",   "kategori" => "Elektronik", "harga" => 150000, "tersedia" => false],
    ["nama" => "Buku Catatan",     "kategori" => "Alat Tulis", "harga" => 25000,  "tersedia" => true],
    ["nama" => "Headset Gaming",   "kategori" => "Elektronik", "harga" => 200000, "tersedia" => true],
    ["nama" => "Pulpen Gel",       "kategori" => "Alat Tulis", "harga" => 10000,  "tersedia" => true],
];
$nomor = 1;
$totalHarga = 0;
$jumlahTersedia = 0;
echo "=== Daftar Produk Tersedia ===\n";
foreach ($katalog as $barang) {
	if ($barang["tersedia"] === true){
		echo $nomor . ". " . $barang["nama"] . " (" . $barang["kategori"] . ") - Rp " . $barang["harga"] . "\n";
		$nomor++;
		$totalHarga += $barang["harga"];
		$jumlahTersedia++;
	}
}
$rataRataHarga = $totalHarga / $jumlahTersedia;
echo "--------------------------------------------------\n";
echo "Total Produk Siap Jual : " . $jumlahTersedia . " barang \n";
echo "Total Nilai Stok       : Rp " . $totalHarga . "\n" ;
echo "Rata-rata Harga Stok   : Rp " . $rataRataHarga . "\n";

```

---

## 💬 Catatan Tambahan Siswa
*(Tulis catatan atau kendala jika ada bagian soal yang terasa membingungkan)*
