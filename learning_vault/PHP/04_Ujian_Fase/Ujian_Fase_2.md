---
icon: "🎓"
sticker: "🎓"
color: "#8b5cf6"
tags:
  - php
  - ujian
  - fase-2
---

# 🎓 Ujian Akhir Fase 2 — Fungsi, Struktur Data & Penanganan Error

> [!important] Informasi Ujian
> - **Cakupan Materi**: Bab 7 (Fungsi) · Bab 8 (Array Lanjutan) · Bab 9 (String) · Bab 10 (Closure & Arrow) · Bab 11 (Error Handling)
> - **Format**: Soal coding murni — buat program yang berjalan sesuai spesifikasi
> - **Passing Score**: **75%** (75 poin dari 100)
> - **Jumlah Soal**: 3 soal, tingkat kesulitan bertingkat
> - **Target Eksekusi**: PHP 8.3+ via CLI (`php nama_file.php`)

---

> [!tip] Petunjuk Pengerjaan
> 1. Buat masing-masing program di file terpisah sesuai nama yang ditentukan.
> 2. Tulis jawaban (kode program) di bagian yang sudah disediakan di bawah ini.
> 3. Setelah selesai semua, beri tahu tutor di chat untuk diperiksa dan dinilai.
> 4. Anda boleh menggunakan semua fungsi bawaan PHP yang pernah dipelajari.

---

## Soal 1 — Validator Kupon Diskon (Mudah · 30 poin)

Buat program PHP bernama `validator_kupon.php` yang:

1. Memiliki fungsi `validasiKupon(string $kupon): array` yang menerima satu kode kupon mentah dan mengembalikan array dengan dua kunci:
   - `"status"` → `"valid"` atau `"invalid"`
   - `"pesan"` → pesan penjelasan hasil validasi

2. Aturan validasi (gunakan fungsi string yang sudah dipelajari):
   - Hapus spasi di awal dan akhir kode kupon (`trim`).
   - Kupon dianggap **valid** jika memenuhi **semua** syarat berikut:
     - Diawali dengan teks `"DISC-"` (gunakan `str_starts_with`).
     - Panjang total kupon (setelah di-trim) tepat **10 karakter** (gunakan `strlen`).
     - Seluruhnya huruf kapital dan angka (tidak ada huruf kecil).
   - Jika tidak memenuhi salah satu syarat, status `"invalid"` dengan pesan yang menjelaskan syarat mana yang gagal.

3. Uji fungsi dengan array kupon berikut menggunakan `foreach`:
   ```php
   $daftarKupon = ["DISC-AB12", "  DISC-XY99  ", "disc-ab12", "PROMO-001", "DISC-TOOLONG99"];
   ```

4. Cetak hasil setiap kupon ke terminal dalam format:
   ```
   Kupon "DISC-AB12"   → ❌ INVALID | Panjang harus 10 karakter, diterima: 9
   Kupon "DISC-XY99"   → ✅ VALID   | Kupon dapat digunakan
   ```

---

**Kode Program Kamu** (`validator_kupon.php`):
```php
<?php
function validasiKupon(string $kupon): array {
        $k = trim($kupon);
        if (!str_starts_with($k, "DISC-")) {
            return ["status" => "invalid", "pesan" => "Harus diawali 'DISC-'"];
        }
        if (strlen($k) !== 10) {
            return ["status" => "invalid", "pesan" => "Panjang harus 10 karakter, diterima: " . strlen($k)];
        }
        if ($k !== strtoupper($k)) {
            return ["status" => "invalid", "pesan" => "Harus huruf kapital semua"];
        }
        return ["status" => "valid", "pesan" => "Kupon dapat digunakan"];
    }
    $daftarKupon = ["DISC-AB12", "  DISC-XY99  ", "disc-ab12", "PROMO-001", "DISC-TOOLONG99"];

    foreach ($daftarKupon as $item) {
        $res = validasiKupon($item);
        $clean = trim($item);
        $tag = $res["status"] === "valid" ? "✅ VALID  " : "❌ INVALID";
        echo "Kupon \"$clean\"   → $tag | {$res['pesan']}\n";
    }
```

---

## Soal 2 — Pengolah Data Transaksi (Sedang · 35 poin)

Buat program PHP bernama `rekap_transaksi.php` yang:

1. Memiliki data transaksi dalam array asosiatif 2 dimensi:
   ```php
   $transaksi = [
       ["id" => "TRX-001", "nama" => "Budi Santoso",  "kategori" => "elektronik", "total" => 1500000],
       ["id" => "TRX-002", "nama" => "Siti Rahma",    "kategori" => "fashion",    "total" => 250000],
       ["id" => "TRX-003", "nama" => "Andi Wijaya",   "kategori" => "elektronik", "total" => 3200000],
       ["id" => "TRX-004", "nama" => "Dewi Lestari",  "kategori" => "makanan",    "total" => 85000],
       ["id" => "TRX-005", "nama" => "Rudi Hermawan", "kategori" => "fashion",    "total" => 420000],
       ["id" => "TRX-006", "nama" => "Maya Putri",    "kategori" => "makanan",    "total" => 135000],
   ];
   ```

2. Buat fungsi `rekapPerKategori(array $transaksi): array` yang menggunakan **Arrow Function** (`fn() =>`) untuk:
   - Mengelompokkan total transaksi per kategori.
   - Menghitung jumlah transaksi per kategori.
   - Mengembalikan array asosiatif dengan kunci nama kategori.

3. Buat fungsi `formatRupiah(int $angka): string` yang mengubah angka menjadi format Rupiah (gunakan `number_format`).

4. Cetak rekap ke terminal dalam format:
   ```
   ========== REKAP TRANSAKSI PER KATEGORI ==========
   
   📦 elektronik
      Jumlah Transaksi : 2
      Total Omzet      : Rp 4.700.000
   
   👗 fashion
      Jumlah Transaksi : 2
      Total Omzet      : Rp 670.000
   
   🍽️ makanan
      Jumlah Transaksi : 2
      Total Omzet      : Rp 220.000
   
   ─────────────────────────────────────
   GRAND TOTAL: Rp 5.590.000
   ═══════════════════════════════════════
   ```

---

**Kode Program Kamu** (`rekap_transaksi.php`):
```php
<?php
(Tulis program lengkapmu di sini)
```

---

## Soal 3 — Parser & Validator Data Siswa (Menantang · 35 poin)

Buat program PHP bernama `parser_siswa.php` yang:

1. Memiliki data mentah siswa dalam format string CSV satu baris per siswa:
   ```php
   $dataMentah = [
       "Budi Santoso,17,85,92,78",
       "Siti Rahma,16,90,88,95",
       "INVALID DATA HERE",
       "Andi Wijaya,18,70,65,80",
       "Dewi,,20,100,99",
   ];
   ```

2. Buat fungsi `parseDataSiswa(string $baris): array` yang:
   - Memisahkan data menggunakan `explode`.
   - Melempar `InvalidArgumentException` jika:
     - Jumlah kolom bukan tepat 5.
     - Kolom nama kosong.
     - Kolom usia bukan angka atau di luar rentang 15–25 tahun.
   - Jika valid, mengembalikan array asosiatif:
     ```php
     ["nama" => "...", "usia" => 17, "nilai" => [85, 92, 78], "rata_rata" => 85.0]
     ```
   - Hitung `rata_rata` dari 3 nilai menggunakan `array_sum`.

3. Proses seluruh `$dataMentah` menggunakan `foreach` dengan `try-catch`:
   - Data valid → cetak informasi siswa.
   - Data invalid → cetak pesan error yang informatif.

4. Cetak hasil ke terminal dalam format:
   ```
   ✅ Budi Santoso (17 thn) | Nilai: 85, 92, 78 | Rata-rata: 85.0
   ✅ Siti Rahma (16 thn)   | Nilai: 90, 88, 95 | Rata-rata: 91.0
   ❌ Baris 3 gagal: Jumlah kolom tidak valid (diterima 1, harusnya 5)
   ✅ Andi Wijaya (18 thn)  | Nilai: 70, 65, 80 | Rata-rata: 71.7
   ❌ Baris 5 gagal: Kolom nama tidak boleh kosong
   ```

---

**Kode Program Kamu** (`parser_siswa.php`):
```php
<?php
(Tulis program lengkapmu di sini)
```

---

## 💬 Catatan / Pertanyaan Tambahan:
*(Jika ada bagian soal yang kurang jelas atau ingin ditanyakan, tuliskan di sini!)*
