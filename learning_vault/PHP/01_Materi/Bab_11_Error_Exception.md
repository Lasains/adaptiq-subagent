---
icon: 📖
sticker: emoji//1f4d6
color: "#6366f1"
tags:
  - php
  - materi
  - fase-2
---

# 📚 Bab 11: Error & Exception Handling (`try-catch-finally`)

> **Level**: Menengah (*Fase 2: Fungsi Fleksibel & Penanganan Kesalahan*)
> **Prasyarat**: Bab 07 (Fungsi), Bab 10 (Closure & Arrow Function)
> **Estimasi Waktu**: 30–35 Menit
> **Target Eksekusi**: PHP 8.3+ via CLI (`php nama_file.php`)
> **Relevansi Web / Laravel**: Sangat Tinggi (Dipakai di setiap layer aplikasi: controller, service, dan query database)

---

## 💡 Konsep Utama (Dalam Bahasa Ringkas)

Saat program berjalan, ada kalanya terjadi kejadian tak terduga — seperti file yang tidak ditemukan, koneksi database yang gagal, atau input pengguna yang tidak valid.

**Error Handling** adalah sistem bawaan PHP untuk mendeteksi dan merespons kejadian tak terduga tersebut agar program tidak langsung berhenti dengan pesan error yang membingungkan.

**Exception** adalah "sinyal bahaya" berbentuk objek yang dilempar (*throw*) saat terjadi masalah dan harus ditangkap (*catch*) sebelum merusak program.

---

## 🔧 Analogi Mekanis Dunia Nyata

| Situasi Nyata | Padanan di PHP | Penjelasan Mekanis |
| :--- | :--- | :--- |
| **Pilot pesawat mencoba menyalakan mesin** | Blok `try { ... }` | Pilot mencoba menjalankan prosedur penerbangan — "Coba lakukan ini" |
| **Lampu peringatan menyala (mesin gagal)** | `throw new Exception(...)` | Mesin mengirim sinyal bahaya — "Ada yang salah, laporkan!" |
| **Ko-pilot mencatat masalah & ambil tindakan darurat** | `catch (Exception $e) { ... }` | Seseorang menangkap sinyal bahaya dan merespons — "Oke, tangani masalahnya" |
| **Checklist penutup penerbangan (selalu dikerjakan)** | `finally { ... }` | Prosedur wajib yang selalu dijalankan walau penerbangan gagal atau berhasil |

---

## 📋 Peta Langkah-demi-Langkah (Dyslexia Friendly)

1. **Blok `try`** — Tulis kode yang berpotensi gagal di dalam blok ini.
2. **Melempar Exception (`throw new Exception(pesan)`)** — Saat ada masalah terdeteksi, lempar sinyal bahaya.
3. **Blok `catch`** — Tangkap sinyal bahaya dan tulis respons yang ramah pengguna.
4. **Blok `finally`** — Opsional. Kode di sini **selalu dijalankan** apapun hasilnya (berhasil maupun gagal). Biasanya dipakai untuk menutup koneksi atau membersihkan sumber daya.

**Struktur Dasar:**
```php
try {
    // Kode yang mungkin bermasalah
} catch (TipeException $variabel) {
    // Respons jika ada masalah
} finally {
    // Selalu dijalankan (opsional)
}
```

---

## 📊 Tabel Jejak Eksekusi Logika (Aphantasia Friendly)

Perhatikan program validasi umur berikut:

```php
<?php
function periksaUmur(int $umur): string {
    if ($umur < 0) {
        throw new InvalidArgumentException("Umur tidak boleh negatif! Diterima: $umur");
    }
    return "Umur $umur tahun valid.";
}

try {
    echo periksaUmur(-5) . "\n";
    echo "Baris ini tidak akan dieksekusi.\n";
} catch (InvalidArgumentException $e) {
    echo "❌ Kesalahan: " . $e->getMessage() . "\n";
} finally {
    echo "✅ Pemeriksaan selesai.\n";
}
```

| Step | Baris Kode | Nilai / Kondisi | Aksi Mesin PHP | Output Terminal |
| :---: | :--- | :--- | :--- | :--- |
| **1** | `periksaUmur(-5)` dipanggil | `$umur = -5` | Masuk fungsi, evaluasi kondisi `if (-5 < 0)` → `true` | — |
| **2** | `throw new InvalidArgumentException(...)` | Pesan: *"Umur tidak boleh negatif! Diterima: -5"* | Mesin melempar Exception, eksekusi fungsi berhenti | — |
| **3** | Blok `catch` aktif | `$e` berisi objek Exception | Mesin menangkap, menjalankan baris echo di dalam catch | `❌ Kesalahan: Umur tidak boleh negatif! Diterima: -5` |
| **4** | `echo "Baris ini..."` | — | **DILEWATI** — Exception sudah dilempar sebelum baris ini | — |
| **5** | Blok `finally` | — | Selalu dijalankan apapun hasilnya | `✅ Pemeriksaan selesai.` |

---

## 💻 Kode Contoh PHP (Siap Jalan di PHP 8.3+)

Simpan dengan nama `error_handling.php` lalu jalankan via CLI:

```php
<?php

// ========================================
// CONTOH 1: try-catch Dasar
// ========================================
echo "=== Contoh 1: Pembagian Aman ===\n";

function bagikan(int $pembilang, int $penyebut): float {
    if ($penyebut === 0) {
        throw new DivisionByZeroError("Tidak bisa dibagi dengan nol!");
    }
    return $pembilang / $penyebut;
}

try {
    echo bagikan(10, 2) . "\n"; // Berhasil: Output: 5
    echo bagikan(10, 0) . "\n"; // Ini akan melempar error
} catch (DivisionByZeroError $e) {
    echo "❌ Error: " . $e->getMessage() . "\n";
}


// ========================================
// CONTOH 2: try-catch-finally
// ========================================
echo "\n=== Contoh 2: Simulasi Baca File ===\n";

function bacaFile(string $namaFile): string {
    if (!file_exists($namaFile)) {
        throw new RuntimeException("File '$namaFile' tidak ditemukan!");
    }
    return file_get_contents($namaFile);
}

try {
    $isi = bacaFile("data_penting.txt");
    echo "Isi file: " . $isi . "\n";
} catch (RuntimeException $e) {
    echo "❌ Gagal membaca: " . $e->getMessage() . "\n";
} finally {
    // Blok ini SELALU dijalankan — cocok untuk menutup koneksi, log aktivitas, dll.
    echo "📋 Log: Proses pembacaan file telah selesai dieksekusi.\n";
}


// ========================================
// CONTOH 3: Menangkap Beberapa Tipe Exception
// ========================================
echo "\n=== Contoh 3: Validasi Input Formulir ===\n";

function validasiEmail(string $email): void {
    if (empty($email)) {
        throw new InvalidArgumentException("Email tidak boleh kosong!");
    }
    if (!str_contains($email, "@")) {
        throw new UnexpectedValueException("Format email tidak valid: $email");
    }
}

$daftarEmail = ["budi@gmail.com", "", "emailtanpasimbol"];

foreach ($daftarEmail as $email) {
    try {
        validasiEmail($email);
        echo "✅ Email valid: $email\n";
    } catch (InvalidArgumentException $e) {
        echo "❌ Input kosong: " . $e->getMessage() . "\n";
    } catch (UnexpectedValueException $e) {
        echo "⚠️ Format salah: " . $e->getMessage() . "\n";
    }
}
```

### Hasil Keluaran Terminal:
```text
=== Contoh 1: Pembagian Aman ===
5
❌ Error: Tidak bisa dibagi dengan nol!

=== Contoh 2: Simulasi Baca File ===
❌ Gagal membaca: File 'data_penting.txt' tidak ditemukan!
📋 Log: Proses pembacaan file telah selesai dieksekusi.

=== Contoh 3: Validasi Input Formulir ===
✅ Email valid: budi@gmail.com
❌ Input kosong: Email tidak boleh kosong!
⚠️ Format salah: Format email tidak valid: emailtanpasimbol
```

---

## ⚠️ Jebakan Umum

| Kesalahan | Contoh Salah ❌ | Contoh Benar ✅ | Penjelasan Teknis |
| :--- | :--- | :--- | :--- |
| **Tidak menangkap Exception** | `throw new Exception("gagal");` tanpa `try-catch` | Selalu bungkus dengan `try-catch` saat exception bisa dilempar | Exception yang tidak ditangkap akan crash dan hentikan seluruh program |
| **`catch` terlalu umum di bagian atas** | `catch (Exception $e)` di baris pertama (menutupi catch spesifik di bawah) | Tulis `catch` yang spesifik dulu, baru `catch (Exception $e)` di paling akhir | PHP mencocokkan `catch` dari atas ke bawah — yang spesifik harus lebih dulu |
| **Menelan Exception tanpa respons** | `catch (Exception $e) { }` *(blok kosong)* | Selalu tampilkan atau catat pesan error di dalam catch | Exception yang ditelan tanpa aksi menyembunyikan bug dan sangat berbahaya |
| **Logika penting di luar `finally`** | Tutup koneksi DB di dalam blok `try` (tidak jalan jika exception terjadi) | Pindahkan tutup koneksi ke blok `finally` | `finally` adalah satu-satunya blok yang **SELALU** dijalankan, berhasil atau tidak |

---

## 🧩 Kuis Mini Interaktif

Kerjakan kuis ini di berkas [Kuis_Bab_11.md](../03_Jawaban_Kuis/Kuis_Bab_11.md).

### Soal 1 — Pilihan Ganda (10 poin)
Perhatikan kode berikut:
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
Apa yang dicetak di terminal?
- **A)** `A` kemudian `C`
- **B)** `B` kemudian `C`
- **C)** `A` kemudian `B` kemudian `C`
- **D)** Hanya `C`

### Soal 2 — Jejak Eksekusi (25 poin)
Lengkapi tabel jejak eksekusi untuk program berikut:
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

| Step | Baris / Bagian | Nilai Parameter | Kondisi Dievaluasi | Output Terminal |
| :---: | :--- | :--- | :--- | :--- |
| **1** | `cekStok(10)` dipanggil | `$stok = 10` | `10 < 0` → ? | ? |
| **2** | `cekStok(-3)` dipanggil | `$stok = -3` | `-3 < 0` → ? | ? |
| **3** | Blok `catch` aktif | `$e` berisi pesan: ? | — | ? |
| **4** | `cekStok(5)` dipanggil | ? | — | ? |
| **5** | Blok `finally` | — | — | ? |

### Soal 3 — Temukan Bug (30 poin)
Kode berikut memiliki **2 kesalahan**. Temukan dan tulis kode perbaikannya:
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

### Soal 4 — Coding Mini (35 poin)
Buat program PHP bernama `validasi_usia_anggota.php` yang:
1. Memiliki fungsi `daftarAnggota(string $nama, int $usia)`.
2. Fungsi melempar `InvalidArgumentException` jika:
   - `$usia < 17` → dengan pesan: `"$nama belum cukup umur (min. 17 tahun)."`
   - `$usia > 60` → dengan pesan: `"$nama melebihi batas usia anggota (maks. 60 tahun)."`
3. Jika valid, cetak: `"✅ $nama berhasil didaftarkan (usia: $usia tahun)."`
4. Uji dengan 3 data berbeda menggunakan `try-catch` dan cetak pesan error yang informatif.

Output yang diharapkan di terminal:
```text
✅ Budi berhasil didaftarkan (usia: 25 tahun).
❌ Pendaftaran gagal: Andi belum cukup umur (min. 17 tahun).
❌ Pendaftaran gagal: Pak Soekarno melebihi batas usia anggota (maks. 60 tahun).
```
