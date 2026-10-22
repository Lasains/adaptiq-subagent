---
icon: "💬"
sticker: "💬"
color: "#06b6d4"
tags:
  - php
  - tanya
  - bab-10
  - anonymous-function
  - arrow-function
---

# 💬 Catatan Tanya — Bab 10: Anonymous Function & Arrow Function

> [!info] Metadata Catatan
> - **Topik Bab**: Fungsi Tanpa Nama (*Closure*) & *Arrow Function* (`fn() =>`)
> - **Status**: ✅ Terjawab & Tuntas

---

## ❓ Pertanyaan Siswa

> [!question] Pertanyaan Asli Siswa
> - [x] Coba jelaskan mengapa kita harus menggunakan closure/arrow dan kapan dibutuhkan?
> - [x] Apakah ada permasalahan yang diselesaikan oleh closure/arrow tapi tidak bisa diselesaikan oleh function biasa?
> - [x] Coba jelasin lagi apa itu `use` dan arrow function?
> - [x] Kalau variabel yang mau di `use` lebih dari 1 gimana?

---

## 💡 Jawaban & Pembahasan Tutor

### 1. Mengapa Harus Pakai Closure/Arrow Function & Kapan Dibutuhkan?

#### 🔧 Analogi Mekanis

| Tipe Fungsi | Analogi Nyata | Sifat |
| :--- | :--- | :--- |
| **Fungsi Biasa** | Mesin Bor Permanen di lemari perkakas | Punya nama, dipakai berkali-kali |
| **Closure / Arrow** | Catatan Tempel (*Sticky Note*) | Sekali pakai, tidak mengotori "lemari" |

#### ⏱️ Kapan Menggunakannya?
1. **Memproses Array cepat** dengan `array_map()`, `array_filter()`, `usort()`.
2. **Logika sangat pendek** (hanya 1 baris): rumus kali dua, tambah pajak, dll.
3. **Di Framework Modern** (Laravel): mendefinisikan rute halaman secara singkat.

```php
<?php
// Contoh di Laravel:
Route::get('/halo', fn() => "Selamat Datang!");

// Contoh sehari-hari dengan array_map:
$hasil = array_map(fn($angka) => $angka * 2, [1, 2, 3]);
// Hasil: [2, 4, 6]
```

---

### 2. Apakah Ada Masalah yang Hanya Bisa Diselesaikan Closure, Tapi Tidak Function Biasa?

> [!NOTE] Jawaban Jujur & Tegas
> Secara logika komputer, **TIDAK ADA**. Semua yang bisa dikerjakan Closure/Arrow bisa dikerjakan function biasa.

Namun, Closure dan Arrow Function menyelesaikan **3 masalah nyata dalam penulisan kode**:

#### A. Mencegah Polusi Nama Fungsi
- Jika ada 50 pemrosesan array kecil, Anda terpaksa mengarang 50 nama fungsi unik yang hanya dipakai satu kali seumur hidup.
- **Solusi Closure**: Tidak perlu nama. Buat fungsinya langsung di tempat.

#### B. Mengambil Variabel Luar Secara Aman
- Fungsi biasa **tidak memiliki akses** ke variabel lokal di luarnya (kecuali dipaksa `global $x;` yang berbahaya dan rawan bug).
- **Closure**: Bisa mengambil variabel luar secara aman lewat `use`.
- **Arrow Function**: Bahkan lebih aman, variabel luar ditangkap otomatis.

#### C. Memangkas Kode Menjadi 1 Baris Rapi

```php
<?php
// ❌ Gaya Lama (Function Biasa): 6 baris + nama tercatat di memori global
function kalikanDua($angka) {
    return $angka * 2;
}
$hasil = array_map('kalikanDua', [1, 2, 3]);

// ✅ Gaya Modern (Arrow Function): cukup 1 baris
$hasil = array_map(fn($angka) => $angka * 2, [1, 2, 3]);
```

---

### 3. Penjelasan: Apa Itu `use` dan Apa Itu Arrow Function?

#### 🧱 Tembok Ruang Lingkup (*Scope Wall*) di PHP
Di PHP, variabel di luar fungsi **tidak bisa masuk** ke dalam fungsi secara otomatis:

```php
<?php
$pajak = 1000;

// ❌ ERROR: $pajak tidak dikenal di dalam fungsi!
$hitung = function ($harga) {
    return $harga + $pajak;
};
```

#### 🔑 Kata Kunci `use` — Izin Resmi Membawa Variabel Masuk

```php
<?php
$pajak = 1000;

// ✅ BERHASIL: $pajak dibawa masuk lewat "use"
$hitung = function ($harga) use ($pajak) {
    return $harga + $pajak;
};

echo $hitung(5000); // Output: 6000
```

#### 🏹 Arrow Function `fn() =>` — PHP 8 Modern

Arrow Function punya **2 keajaiban otomatis**:
1. **Otomatis menangkap variabel luar** — tidak perlu `use`.
2. **Otomatis mengembalikan nilai** — tidak perlu `return` dan `{}`.

```php
<?php
$pajak = 1000;

// Tidak ada "use", tidak ada "return", tidak ada kurung kurawal:
$hitung = fn($harga) => $harga + $pajak;

echo $hitung(5000); // Output: 6000
```

---

### 4. Jika Variabel yang Digunakan Lebih dari Satu?

#### Pada Closure Klasik → Pisahkan dengan Koma `,`

```php
<?php
$pajak  = 1000;
$diskon = 500;
$ongkir = 2000;

$hitungTotal = function ($hargaBarang) use ($pajak, $diskon, $ongkir) {
    return $hargaBarang + $pajak - $diskon + $ongkir;
};

echo $hitungTotal(10000); // Output: 12500
```

#### Pada Arrow Function → Langsung Pakai, Tanpa Daftar!

```php
<?php
$pajak  = 1000;
$diskon = 500;
$ongkir = 2000;

// PHP otomatis mendeteksi & mengambil semua variabel luar yang digunakan:
$hitungTotal = fn($hargaBarang) => $hargaBarang + $pajak - $diskon + $ongkir;

echo $hitungTotal(10000); // Output: 12500
```

#### 📊 Tabel Jejak Variabel di Memori (Saat `$hitungTotal(10000)` Dijalankan)

| Nama Variabel   | Asal             | Nilai       | Keterangan                    |
| :-------------- | :--------------- | :---------- | :---------------------------- |
| `$hargaBarang`  | Argumen input    | `10000`     | Dikirim saat fungsi dipanggil |
| `$pajak`        | Luar (via `use`) | `1000`      | Ditangkap dari luar fungsi    |
| `$diskon`       | Luar (via `use`) | `500`       | Ditangkap dari luar fungsi    |
| `$ongkir`       | Luar (via `use`) | `2000`      | Ditangkap dari luar fungsi    |
| **Hasil Akhir** | `return`         | **`12500`** | `10000 + 1000 - 500 + 2000`   |

---

## 📌 Poin Kunci yang Harus Diingat

> [!tip] Rangkuman Bab 10
> 1. **Closure Klasik**: Gunakan `use ($var1, $var2)` untuk membawa variabel dari luar — pisahkan dengan koma jika lebih dari satu.
> 2. **Arrow Function `fn() =>`**: Tidak perlu `use`, tidak perlu `return`. PHP otomatis menangkap semua variabel yang dipakai.
> 3. **Kapan pakai Arrow Function?** → Jika logikanya pendek dan muat di 1 baris ekspresi.
> 4. **Kapan pakai Closure Klasik?** → Jika logikanya kompleks, butuh beberapa baris, atau butuh kondisi `if` di dalamnya.
