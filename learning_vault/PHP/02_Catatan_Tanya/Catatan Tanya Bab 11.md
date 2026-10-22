---
icon: "💬"
sticker: "💬"
color: "#06b6d4"
tags:
  - php
  - tanya
  - bab-11
  - error-handling
  - exception
---

# 💬 Catatan Tanya — Bab 11: Error & Exception Handling

> [!info] Metadata Catatan
> - **Topik Bab**: `try-catch-finally`, Exception, Error Handling PHP 8
> - **Status**: ✅ Terjawab & Tuntas

---

## ❓ Pertanyaan Siswa

> [!question] Pertanyaan Asli Siswa
> - [x] Apa itu `DivisionByZeroError`, `InvalidArgumentException`, `RuntimeException`, dan `UnexpectedValueException`? Masing-masing apa pembedanya dan kapan digunakan?
> - [x] Kapan sebaiknya kita `throw` Exception sendiri vs membiarkan PHP lempar error-nya sendiri?
> - [x] Bolehkah satu blok `try` punya lebih dari satu `catch`?
> - [x] Apakah `finally` tetap dijalankan jika di dalam `catch` ada `return` atau `exit`? Dan apa itu `exit`?
> - [x] Apa itu `file_exists()`?

---

## 💡 Jawaban & Pembahasan Tutor

### 1. Perbedaan 4 Jenis Exception — Kunci Satu Pertanyaan: *"Siapa yang menyebabkan masalah ini?"*

#### 📊 Tabel Paling Simpel

| Exception | Kondisi Pemicunya | Siapa yang Salah |
| :--- | :--- | :--- |
| `InvalidArgumentException` | Nilai/tipe argumen tidak masuk akal **dari awal** | Pemanggil fungsi |
| `RuntimeException` | Logika benar, tapi **kondisi sistem/lingkungan** gagal | Kondisi di luar kendali |
| `UnexpectedValueException` | Data masuk, tapi **formatnya/polanya salah** | Data yang diterima |
| `DivisionByZeroError` | Bagi dengan **nol** — dilempar otomatis oleh PHP | Mesin PHP |

#### 🔧 Analogi Mekanis

| Exception | Analogi Nyata |
| :--- | :--- |
| `InvalidArgumentException` | Mengisi kolom "tanggal lahir" dengan angka **-5** — sistem tolak sebelum proses |
| `RuntimeException` | Menekan tombol lift lantai 5 dengan benar, tapi **listrik mati** |
| `UnexpectedValueException` | Diminta mengisi nomor KTP (16 digit), Anda isi `"ABCD-EFGH"` |
| `DivisionByZeroError` | PHP lempar sendiri — Anda tinggal **tangkap** dengan `catch` |

#### 💻 Kode Perbandingan

```php
<?php
// InvalidArgumentException: nilai tidak masuk akal dari awal
if ($diskon < 0 || $diskon > 100) {
    throw new InvalidArgumentException("Diskon tidak valid: $diskon");
}

// RuntimeException: kondisi sistem yang gagal saat dijalankan
if (!file_exists($namaFile)) {
    throw new RuntimeException("File tidak ditemukan: $namaFile");
}

// UnexpectedValueException: data ada, tapi formatnya salah
if (!str_contains($email, "@")) {
    throw new UnexpectedValueException("Format email tidak valid: $email");
}

// DivisionByZeroError: tidak perlu throw — PHP otomatis lempar
try {
    $hasil = 10 / 0;
} catch (\DivisionByZeroError $e) {
    echo "Tidak bisa bagi nol!";
}
```

> [!tip] Cara Mudah Mengingatnya
> - **Invalid** → *"Nilainya gila dari awal!"*
> - **Runtime** → *"Semuanya benar, tapi kondisi saat ini tidak mendukung."*
> - **Unexpected** → *"Datanya ada, tapi bentuknya salah."*
> - **DivisionByZero** → *"PHP yang lempar sendiri, saya tinggal tangkap."*

---

### 2. Kapan `throw` Sendiri vs Biarkan PHP yang Lempar?

| Situasi | Strategi | Alasan |
| :--- | :--- | :--- |
| Validasi logika bisnis Anda sendiri | ✅ `throw` sendiri | PHP tidak tahu aturan bisnis Anda (misal: usia min 17 tahun) |
| Operasi matematis berbahaya (`/ 0`) | 🔄 Biarkan PHP + tangkap dengan `catch` | PHP sudah otomatis lempar `DivisionByZeroError` |
| Operasi file / jaringan yang bisa gagal | ✅ Cek hasilnya lalu `throw` sendiri | Fungsi seperti `file_get_contents()` hanya return `false`, tidak otomatis throw |
| Error sintaks / bug kode | ❌ Tidak perlu ditangkap | `catch` bukan alat menyembunyikan bug — ini untuk kondisi yang memang bisa gagal |

---

### 3. Bolehkah Satu Blok `try` Punya Lebih dari Satu `catch`?

**Boleh! Bahkan sangat dianjurkan** jika kode berpotensi melempar beberapa tipe Exception berbeda.

> [!important] Aturan Urutan Wajib
> Tulis `catch` yang **paling spesifik** di atas, yang **paling umum** (`Exception`) di paling bawah. PHP mencocokkan dari atas ke bawah.

```php
<?php
try {
    prosesData("ERROR");

} catch (InvalidArgumentException $e) {
    // Tangkap dulu yang paling spesifik
    echo "❌ Argumen salah: " . $e->getMessage() . "\n";

} catch (RuntimeException $e) {
    echo "⚠️ Error runtime: " . $e->getMessage() . "\n";

} catch (Exception $e) {
    // Tangkap SEMUA sisa — taruh paling bawah!
    echo "🔴 Error tidak terduga: " . $e->getMessage() . "\n";
}
```

#### 📊 Hierarki Exception di PHP

```
Throwable
├── Error                      ← Kesalahan level mesin PHP
│   ├── DivisionByZeroError
│   ├── TypeError
│   └── ParseError
└── Exception                  ← Kondisi yang bisa ditangani
    ├── RuntimeException
    │   └── UnexpectedValueException
    ├── InvalidArgumentException
    └── LogicException
```

---

### 4. Apakah `finally` Tetap Jalan jika Ada `return` atau `exit`?

| Kondisi di dalam `catch` | `finally` Dijalankan? |
| :--- | :---: |
| Ada `return` | ✅ **Ya** — `finally` jalan dulu sebelum return selesai |
| Ada `exit()` / `die()` | ❌ **Tidak** — program dihentikan paksa total |

```php
<?php
function tesReturn(): string {
    try {
        throw new Exception("masalah");
    } catch (Exception $e) {
        echo "Catch dijalankan.\n";
        return "Nilai dari catch";
    } finally {
        // TETAP jalan meski ada return di catch
        echo "Finally TETAP jalan!\n";
    }
}

$hasil = tesReturn();
echo "Hasil: $hasil\n";
```

**Output:**
```
Catch dijalankan.
Finally TETAP jalan!
Hasil: Nilai dari catch
```

#### Apa itu `exit()`?

`exit()` (alias `die()`) adalah perintah untuk **menghentikan seluruh program PHP secara paksa dan permanen** pada saat itu juga.

```php
echo "Baris ini dicetak.\n";
exit(); // ← Program BERHENTI TOTAL di sini
echo "Baris ini TIDAK pernah dicetak.\n"; // ← Tidak akan dieksekusi
```

> [!warning] Kapan Boleh Pakai `exit()`?
> Hanya setelah `header("Location: ...")` untuk redirect di web, atau kondisi kritis yang benar-benar tidak bisa dilanjutkan. **Hindari `exit()` jika masalah masih bisa ditangani dengan `try-catch`.**

---

### 5. Apa itu `file_exists()`?

`file_exists()` adalah fungsi bawaan PHP untuk **memeriksa apakah sebuah file atau folder benar-benar ada** di sistem sebelum kita mencoba membacanya.

- Mengembalikan `true` jika ada, `false` jika tidak ada.

```php
<?php
$namaFile = "laporan.txt";

// ❌ Berbahaya: langsung baca tanpa cek — Error jika file tidak ada!
// $isi = file_get_contents($namaFile);

// ✅ Aman: cek dulu, baru baca
if (file_exists($namaFile)) {
    $isi = file_get_contents($namaFile);
    echo "Isi file: " . $isi;
} else {
    echo "File '$namaFile' tidak ditemukan.";
}
```

#### Pola Terbaik: Gabung dengan `try-catch`

```php
<?php
function bacaFileDenganAman(string $path): string {
    if (!file_exists($path)) {
        throw new RuntimeException("File tidak ditemukan: $path");
    }
    return file_get_contents($path);
}

try {
    echo bacaFileDenganAman("config.php");
} catch (RuntimeException $e) {
    echo "❌ Gagal: " . $e->getMessage();
}
```

#### Fungsi-Fungsi Sejenis

| Fungsi | Kegunaan |
|:---|:---|
| `file_exists($path)` | Cek apakah file atau folder **ada** |
| `is_file($path)` | Cek apakah itu **file** (bukan folder) |
| `is_dir($path)` | Cek apakah itu **folder** (bukan file) |
| `is_readable($path)` | Cek apakah file ada **DAN** bisa dibaca |

---

## 📌 Poin Kunci yang Harus Diingat

> [!tip] Rangkuman Bab 11
> 1. Pilih jenis Exception berdasarkan **siapa yang salah** — argumen salah (`Invalid`), sistem gagal (`Runtime`), format data salah (`Unexpected`).
> 2. `throw` sendiri untuk **aturan bisnis Anda**. Biarkan PHP lempar sendiri untuk error level mesin.
> 3. Satu blok `try` boleh punya **banyak `catch`** — urut dari paling spesifik ke paling umum.
> 4. **`finally` selalu jalan** meski ada `return`, tapi **berhenti jika ada `exit()`**.
> 5. Selalu gunakan `file_exists()` sebelum membaca file untuk mencegah crash.
