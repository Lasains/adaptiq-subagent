---
icon: "💬"
sticker: "💬"
color: "#06b6d4"
tags:
  - php
  - tanya
  - bab-06
  - array
---

# 💬 Catatan Tanya — Bab 6: Struktur Data Array

> [!info] Metadata Catatan
> - **Topik Bab**: Array 1 Dimensi, 2 Dimensi, dan Multidimensi di PHP
> - **Status**: ✅ Terjawab & Tuntas

---

## ❓ Pertanyaan Siswa

> [!question] Pertanyaan Asli Siswa
> "Dulu saya pernah dengar soal array dan katanya array itu ada 1 dimensi, 2 dimensi dan multi dimensi?"

---

## 💡 Jawaban & Pembahasan Tutor

### 1. Benar Sekali! Apa Itu Dimensi pada Array?

Dimensi pada array menunjukkan **tingkat kedalaman sarang (*nesting level*)** tempat data disimpan.
Semakin banyak dimensinya, semakin banyak lapisan tanda kurung siku `[]` yang dibutuhkan untuk mengambil datanya.

---

### 2. Analogi Dunia Nyata (Mekanis & Konkret)

| Dimensi Array | Analogi Nyata | Cara Bayangkan di Memori |
| :--- | :--- | :--- |
| **1 Dimensi** | **Satu Rak Sepatu Lurus** | Deret satu garis horizontal: `[0, 1, 2, ...]` |
| **2 Dimensi** | **Lemari Laci / Tabel Excel** | Kotak petak yang punya **Baris** dan **Kolom** |
| **Multidimensi** | **Gedung Bertingkat** | Lantai ➔ Ruangan ➔ Meja ➔ Laci berkas |

---

### 3. Bedah Per Dimensi & Contoh Kode PHP

#### A. Array 1 Dimensi (Satu Garis Datar)
Hanya memiliki satu indeks untuk memanggil isinya.

```php
<?php
// Satu deret lurus daftar nama buah
$buah = ["Apel", "Jeruk", "Mangga"];

// Akses data (butuh 1 pasang kurung siku):
echo $buah[0]; // Output: Apel
```

---

#### B. Array 2 Dimensi (Tabel Baris & Kolom)
Array di dalam array (satu tingkat sarang). Sering digunakan untuk daftar data pengguna dari database.

```php
<?php
// Baris = Tiap Siswa, Kolom = Info Siswa
$daftarSiswa = [
    ["Budi", 85, "Lulus"],  // Baris index 0
    ["Siti", 92, "Lulus"],  // Baris index 1
    ["Andi", 50, "Remidi"], // Baris index 2
];

// Akses data: [Indeks Baris][Indeks Kolom]
echo $daftarSiswa[1][0]; // Baris 1, Kolom 0 -> Output: Siti
echo $daftarSiswa[2][2]; // Baris 2, Kolom 2 -> Output: Remidi
```

---

#### C. Array Multidimensi (Lebih dari 2 Tingkat)
Array bersarang dengan kedalaman 3 tingkat atau lebih.

```php
<?php
// Contoh struktur data cabang toko dan stok produk
$gudang = [
    "Cabang_Jakarta" => [
        "Elektronik" => [
            "Laptop" => 15,
            "Mouse"  => 50
        ],
        "Pakaian" => [
            "Kaos" => 120
        ]
    ]
];

// Akses butuh 3 kunci:
echo $gudang["Cabang_Jakarta"]["Elektronik"]["Laptop"]; // Output: 15
```

---

### 4. 📊 Tabel Jejak Akses Memori

| Kode Pemanggilan | Lapisan 1 | Lapisan 2 | Nilai yang Didapat |
| :--- | :--- | :--- | :--- |
| `$buah[0]` | Index 0 | — | `"Apel"` |
| `$daftarSiswa[0][0]` | Baris index 0 | Kolom index 0 | `"Budi"` |
| `$daftarSiswa[1][1]` | Baris index 1 | Kolom index 1 | `92` |

---

## 📌 Poin Kunci yang Harus Diingat

> [!tip] Rumus Praktis
> - Butuh `1` pasang `[]` = **Array 1 Dimensi**.
> - Butuh `2` pasang `[][]` = **Array 2 Dimensi** (paling sering dipakai untuk data tabel).
> - Butuh `3+` pasang `[][][]` = **Array Multidimensi**.
> - Di dunia kerja nyata (web development), 90% waktu Anda akan berkutat dengan Array 1 Dimensi (list) dan Array 2 Dimensi (tabel data database).