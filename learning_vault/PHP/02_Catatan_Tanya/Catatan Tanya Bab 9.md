---
icon: "💬"
sticker: "💬"
color: "#06b6d4"
tags:
  - php
  - tanya
  - bab-09
  - manipulasi-string
---

# 💬 Catatan Tanya — Bab 9: Manipulasi String & Fungsi Bawaan

> [!info] Metadata Catatan
> - **Topik Bab**: Fungsi String PHP 8 (`str_*`, `explode`, `implode`, `trim`, `strlen`)
> - **Status**: ✅ Terjawab & Tuntas

---

## ❓ Pertanyaan Siswa

> [!question] Kumpulan Pertanyaan Siswa di Bab 9
> 1. Apakah `str_contains` digunakan jika yang dicari bertipe string dan `str_starts_with` jika yang dicari bertipe int?
> 2. Minta dijelaskan ulang mengenai perbedaan `explode()` dengan `implode()`?
> 3. Kenapa data harus dipisah (`explode`) kalau ujung-ujungnya disatukan kembali (`implode`)?
> 4. Bagaimana cara menghitung jumlah karakter pada sebuah kalimat?
> 5. Bagaimana caranya agar kalimat `"  Tutorial Belajar PHP 8 Lengkap  "` tetap utuh spasi depannya saat ditampilkan di layar?

---

## 💡 Jawaban & Pembahasan Tutor

### 1. `str_contains` vs `str_starts_with` (Keduanya untuk String!)

Kedua fungsi ini sama-sama menerima **teks (*string*)**, bukan angka int. Perbedaannya murni pada **posisi pencarian**:

| Fungsi | Posisi yang Diperiksa | Contoh Kasus Nyata |
| :--- | :--- | :--- |
| `str_starts_with($teks, "INV-")` | **Wajib di awal kalimat** | Memeriksa format nomor invoice atau awalan `https://` |
| `str_contains($teks, "@")` | **Bebas di posisi mana saja** | Memeriksa apakah ada tanda `@` dalam email |
| `str_ends_with($teks, ".pdf")` | **Wajib di ujung akhir kalimat** | Memeriksa ekstensi file upload |

```php
<?php
$kode = "INV-2024-001";

// Cek awalan:
if (str_starts_with($kode, "INV-")) {
    echo "Ini adalah dokumen invoice.";
}
```

---

### 2. Analogi Mekanis: `explode()` vs `implode()`

Bayangkan rantai kalung manik-manik:

- **`explode(pemisah, teks)`**: **Gunting kalung menjadi butiran manik-manik** (String ➔ Array).
- **`implode(penghubung, array)`**: **Merangkai butiran manik-manik menjadi kalung kembali** (Array ➔ String).

```php
<?php
// 1. String ke Array (explode)
$hobiTeks = "Membaca, Koding, Gaming";
$hobiArray = explode(", ", $hobiTeks);
// Hasil: ["Membaca", "Koding", "Gaming"]

// 2. Array kembali ke String (implode)
$kalimatBaru = implode(" - ", $hobiArray);
// Hasil: "Membaca - Koding - Gaming"
```

---

### 3. Kenapa Harus Dipisah Kalau Ujung-Ujungnya Disatukan Kembali?

> [!tip] Inti Jawabannya: **Proses Pengolahan / Modifikasi di Tengah Jalan!**

Komputer tidak bisa memodifikasi kata-kata tertentu di dalam satu gumpalan string panjang secara leluasa. Kita memisahkannya ke dalam elemen array agar **mudah diolah satu per satu**, baru kemudian disatukan kembali.

#### Contoh Nyata Alur Kerja:
1. **Dapat Input Mentah**: `"anjing, kucing, monyet"`
2. **Pisah (`explode`)** jadi array: `["anjing", "kucing", "monyet"]`
3. **Proses di Tengah (Sensor Kata Kasar)**:
   - Ganti `"anjing"` jadi `"***"`
   - Ganti `"monyet"` jadi `"***"`
4. **Satukan Kembali (`implode`)**: `"***, kucing, ***"`

Tanpa `explode`, kita akan sangat kesulitan memfilter, mengurutkan abjad (*sort*), atau memvalidasi tiap kata secara individual.

---

### 4. Cara Menghitung Jumlah Karakter Kalimat

Gunakan fungsi bawaan **`strlen()`** (atau **`mb_strlen()`** untuk teks multibyte/emoji):

```php
<?php
$kalimat = "Belajar PHP 8";

// Menghitung panjang karakter
$jumlahKarakter = strlen($kalimat);

echo "Total karakter: " . $jumlahKarakter; 
// Output: Total karakter: 13 (spasi ikut dihitung)
```

---

### 5. Menampilkan Kalimat Berspasi Utuh Tanpa Terpangkas

Jika kalimat `"  Tutorial Belajar PHP 8 Lengkap  "` ditampilkan langsung di HTML browser, browser secara default akan meringkas spasi ganda menjadi 1 spasi.

Ada 2 cara agar spasi awal dan akhir tetap utuh:

#### Cara 1: Menggunakan Tag HTML `<pre>` (Paling Praktis)
Tag `<pre>` memerintahkan browser mempertahankan semua whitespace dan spasi apa adanya:
```php
<?php
$judul = "  Tutorial Belajar PHP 8 Lengkap  ";
echo "<pre>" . $judul . "</pre>";
```

#### Cara 2: Di Terminal CLI (Secara Bawaan Sudah Utuh)
Jika dijalankan lewat CLI terminal (bukan browser HTML), spasi tidak akan dipangkas kecuali Anda sengaja memanggil fungsi `trim()`.

---

## 📌 Poin Kunci yang Harus Diingat

> [!important] Rangkuman
> - `str_starts_with()`, `str_ends_with()`, `str_contains()` mengembalikan nilai boolean (`true` / `false`).
> - `explode()` menghasilkan **Array**, sedangkan `implode()` menghasilkan **String**.
> - Alasan *explode ➔ proses ➔ implode*: untuk membedah dan membersihkan data per item secara aman sebelum disimpan kembali.