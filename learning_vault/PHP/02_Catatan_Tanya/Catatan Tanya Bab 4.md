---
icon: "💬"
sticker: "💬"
color: "#06b6d4"
tags:
  - php
  - tanya
  - bab-04
  - kontrol-alur
---

# 💬 Catatan Tanya — Bab 4: Kontrol Alur (Percabangan)

> [!info] Metadata Catatan
> - **Topik Bab**: Percabangan `if`, `else`, `switch`, dan `match` (PHP 8+)
> - **Status**: ✅ Terjawab & Tuntas

---

## ❓ Pertanyaan Siswa

> [!question] Pertanyaan Asli Siswa
> "Ada satu hal yang baru saya ketahui yaitu `match` dimana ini adalah konsep baru di perulangan dan juga saya mau tanya karna yang saya ketahui bahwa kita menggunakan `if` jika ingin membandingkan nilai yang tidak pasti, kita menggunakan `switch` ketika ingin membandingkan nilai yang sudah pasti.
> 
> Akan tetapi di `match` saya tidak tahu kapan kita akan menggunakannya? Dan kenapa kita harus menggunakan itu? Apakah di `if else` atau `switch` kita tidak bisa menggunakan untuk menyelesaikan masalah yang diselesaikan oleh `match` dan juga apakah saya menggunakan untuk sistem login?"

---

## 💡 Jawaban & Pembahasan Tutor

### 1. Koreksi Konsep Dasar: `match` adalah Percabangan, Bukan Perulangan
- `match` **bukan** perulangan (*loop*).
- `match` adalah **percabangan (*conditional expression*)** modern yang dirilis sejak **PHP 8.0**.
- Tujuannya adalah memilih satu nilai berdasarkan pencocokan nilai yang sudah pasti.

---

### 2. Kapan Harus Pakai `match` & Mengapa `match` Diciptakan?

Di PHP versi lama, kita sering menulis `switch` yang panjang dan rawan salah karena lupa menulis `break;`.

`match` hadir sebagai penyempurnaan modern dari `switch`:
1. **Mengembalikan Nilai Langsung (*Expression*)**: Hasil pencocokan bisa langsung dimasukkan ke dalam variabel.
2. **Pengecekan Ketat (*Strict Comparison `===`*)**: Tidak tertipu perbedaan tipe data (misal angka `0` tidak akan dianggap sama dengan teks `"0"`).
3. **Tanpa `break;`**: Tidak ada risiko bocor ke baris bawahnya (*no fallthrough bug*).

#### 📊 Tabel Perbandingan: `if-else` vs `switch` vs `match`

| Fitur | `if - else` | `switch` | `match` (PHP 8+) |
| :--- | :--- | :--- | :--- |
| **Karakter Perbandingan** | Kondisi fleksibel (`>`, `<`, `&&`, `!=`) | Nilai sama dengan (`==`) | Nilai identik (`===`) |
| **Kebutuhan `break;`** | Tidak perlu | **Wajib** (jika lupa, bocor) | **Tidak perlu sama sekali** |
| **Hasil Kembalian** | Blok perintah (*statement*) | Blok perintah (*statement*) | **Menghasilkan nilai (*expression*)** |
| **Kerapihan Sintaks** | Cukup panjang jika banyak opsi | Panjang dan bertele-tele | **Sangat ringkas dan rapi** |

---

### 3. Apakah `if-else` atau `switch` Bisa Menyelesaikan Masalah `match`?

**Bisa 100%!** Semua masalah yang diselesaikan oleh `match` bisa diselesaikan oleh `if-else` atau `switch`.

Namun, perhatikan perbandingan kebersihan kodenya:

#### ❌ Gaya Lama dengan `switch`:
```php
<?php
$role = "admin";
$hakAkses = "";

switch ($role) {
    case "admin":
        $hakAkses = "Akses Penuh";
        break; // Wajib ada break!
    case "editor":
        $hakAkses = "Akses Edit Artikel";
        break;
    default:
        $hakAkses = "Hanya Lihat";
        break;
}
```

#### ✅ Gaya Modern PHP 8 dengan `match`:
```php
<?php
$role = "admin";

// match langsung mengembalikan nilai ke variabel $hakAkses
$hakAkses = match ($role) {
    "admin"   => "Akses Penuh",
    "editor"  => "Akses Edit Artikel",
    default   => "Hanya Lihat",
};
```

---

### 4. Apakah `match` Bisa Digunakan untuk Sistem Login?

**Bisa untuk bagian tertentu, tetapi bukan untuk alur validasi password utamanya.**

- **Untuk Validasi Utama Login (Gunakan `if-else`)**:
  Pemeriksaan login biasanya bertingkat:
  1. Apakah email ada di database?
  2. Apakah password cocok dengan `password_verify()`?
  Kondisi ini membutuhkan eksekusi fungsi bersyarat, sehingga **`if-else`** adalah pilihan standar terbaik.

- **Untuk Penentuan Arah Halaman (*Routing/Role*) Pasca-Login (Gunakan `match`)**:
  Setelah login berhasil dan role pengguna diketahui, `match` sangat tepat digunakan:
  ```php
  <?php
  // Menentukan URL redirect berdasarkan peran user setelah login
  $halamanTujuan = match ($userRole) {
      "superadmin" => "/dashboard-utama.php",
      "guru"        => "/kelas-saya.php",
      "siswa"       => "/materi-belajar.php",
      default       => "/login.php?error=role_tidak_dikenal",
  };
  ```

---

## 📌 Poin Kunci yang Harus Diingat

> [!tip] Rangkuman Singkat
> 1. Gunakan **`if - else`** jika kondisinya berupa rentang logika kompleks (misal: `$nilai >= 80 && $kehadiran > 75`).
> 2. Gunakan **`match`** jika Anda ingin mencocokkan satu nilai pasti ke satu hasil tertentu dan langsung menyimpannya ke variabel.
> 3. Hindari penggunaan `switch` di proyek baru PHP 8+, gantikan dengan `match` yang lebih aman dan ringkas.