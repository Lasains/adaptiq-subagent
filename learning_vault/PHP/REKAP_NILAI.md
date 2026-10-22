---
icon: 📊
sticker: 📊
color: "#10b981"
tags:
  - php
  - nilai
  - rekap
banner:
---

# 📊 Sistem Penilaian Kuis — PHP AdaptiKog

> Dokumen ini menjelaskan bobot setiap jenis soal dan rekap nilai kuis per bab untuk pembelajaran PHP.

---

## ⚖️ Bobot Soal per Tipe

Setiap kuis memiliki total **100 poin**. Bobot berbeda karena tingkat kesulitan dan usaha yang dibutuhkan berbeda:

| Tipe Soal | Bobot | Alasan |
|-----------|:-----:|--------|
| **Soal Pilihan Ganda / Konsep** | 10 poin | Mengecek pemahaman konsep dasar — satu jawaban benar/salah |
| **Soal Jejak Eksekusi (Trace)** | 25 poin | Membutuhkan penelusuran baris per baris kode |
| **Soal Temukan Bug / Prediksi Output** | 30 poin | Membutuhkan analisis kode & kemampuan debugging |
| **Soal Coding Mini** | 35 poin | Membutuhkan kemampuan menulis kode executable sendiri dari nol |
| **Total** | **100 poin** | |

### Aturan Penskoran Detail

- **Soal Konsep / Pilihan Ganda (10 poin)**: Benar penuh = 10, ada esensi tepat = 7-9, salah = 0.
- **Soal Jejak Eksekusi (25 poin)**: Dihitung proporsional per langkah/state variabel yang tepat.
- **Soal Temukan Bug / Prediksi Output (30 poin)**: Dihitung proporsional per bug yang ditemukan atau baris prediksi tepat.
- **Soal Coding Mini (35 poin)**: Logika benar (20), Output sesuai (10), Kode bersih & bebas bug (5). Bug minor (-5~10), bug mayor (-15~20).

---

## 🏆 Rekap Nilai Semua Kuis

### 📘 Bab 1 — Pengenalan PHP & Program Pertama (4 Soal, Total 100 poin)

| Soal | Tipe | Bobot | Nilai Kamu | Catatan |
|------|------|:-----:|:----------:|---------|
| Soal 1 | Pilihan Ganda (Tag `<?php`) | 10 | **0** | ❌ Jawaban A (salah) — jawaban benar: B |
| Soal 2 | Jejak Eksekusi | 25 | **25** | ✅ Semua 3 step benar |
| Soal 3 | Temukan Bug | 30 | **30** | ✅ 2 bug ditemukan + kode perbaikan benar |
| Soal 4 | Coding Mini (`perkenalan.php`) | 35 | **25** | ⚠️ Lupa `\n` & baris ke-3 masih placeholder (-10) |
| | **Total** | **100** | **80** | ✅ **LULUS** |

### 📗 Bab 2 — Variabel & Tipe Data (4 Soal, Total 100 poin)

| Soal | Tipe | Bobot | Nilai Kamu | Catatan |
|------|------|:-----:|:----------:|---------|
| Soal 1 | Pilihan Ganda (`gettype`) | 10 | **10** | ✅ Benar: B (string) |
| Soal 2 | Jejak Eksekusi | 25 | **25** | ✅ Semua 8 sel benar sempurna |
| Soal 3 | Temukan Bug | 30 | **25** | ⚠️ Bug `produk` tanpa `$` di baris echo terlewat (-5) |
| Soal 4 | Coding Mini (`biodata.php`) | 35 | **20** | ⚠️ Deklarasi benar tapi tidak ada `echo` sama sekali (-15) |
| | **Total** | **100** | **80** | ✅ **LULUS** |

### 📙 Bab 3 — Operator (4 Soal, Total 100 poin)

| Soal | Tipe | Bobot | Nilai Kamu | Catatan |
|------|------|:-----:|:----------:|---------|
| Soal 1 | Pilihan Ganda (`0 == false`) | 10 | **10** | ✅ Benar: B (`bool(true)`) |
| Soal 2 | Jejak Eksekusi | 25 | **12** | ⚠️ Langkah 1-4 benar nilai saldo, langkah 5-8 state dan terminal masih kosong/belum tepat (-13) |
| Soal 3 | Temukan Bug | 30 | **20** | ⚠️ Berhasil temukan 2 bug (`||` dan `+`), terlewat bug operator `=>` yang harusnya `>=` (-10) |
| Soal 4 | Coding Mini (`kalkulator_diskon.php`) | 35 | **16** | ⚠️ Logika hitung diskon pembagian (bukan perkalian diskon & pengurangan), belum ada operator perbandingan `$murah` (-19) |
| | **Total** | **100** | **58** | ⚠️ **Selesai (Perlu Review)** |

### 📕 Bab 4 — Percabangan (`if`, `else`, `match`) (4 Soal, Total 100 poin)

| Soal | Tipe | Bobot | Nilai Kamu | Catatan |
|------|------|:-----:|:----------:|---------|
| Soal 1 | Pilihan Ganda (`if ($umur = 20)`) | 10 | **0** | ❌ Jawaban A (salah) — terjebak single `=` (assignment), jawaban benar: B (`Dewasa`) |
| Soal 2 | Jejak Eksekusi | 25 | **23** | ✅ Luar biasa! Alur dan state variabel 100% tepat, hanya pengurangan minor 2 sel placeholder (-2) |
| Soal 3 | Temukan Bug & Prediksi | 30 | **30** | ✅ Sempurna! Menemukan bug urutan if-elseif dan cabang 'C' di match + kode perbaikan valid |
| Soal 4 | Coding Mini (`cek_kelayakan.php`) | 35 | **20** | ⚠️ Alur logika bagus, tapi single `=` di `$memilikiHutang = false` dan kurang titik koma di match & echo (-15) |
| | **Total** | **100** | **73** | ✅ **LULUS** |

### 📓 Bab 5 — Perulangan (`for`, `while`, `do-while`) (4 Soal, Total 100 poin)

| Soal | Tipe | Bobot | Nilai Kamu | Catatan |
|------|------|:-----:|:----------:|---------|
| Soal 1 | Pilihan Ganda (Loop `for`) | 10 | **10** | ✅ Benar: B (`1 2 3 `) |
| Soal 2 | Jejak Eksekusi | 25 | **20** | ⚠️ Langkah 1-3 tepat, di langkah 4 lupa menjumlahkan akumulatif 30 + 30 = 60 (-5) |
| Soal 3 | Temukan Bug | 30 | **18** | ⚠️ Berhasil temukan infinite loop & butuh `$hitung += 2`, tapi terlewat titik koma `;` setelah `while` (-12) |
| Soal 4 | Coding Mini (`tabel_perkalian.php`) | 35 | **25** | ⚠️ Logika perkalian & loop tepat, ada typo `i++` tanpa `$` dan kurang format judul/newline (-10) |
| | **Total** | **100** | **73** | ✅ **LULUS** |

### 📚 Bab 6 — Array & Perulangan `foreach` (4 Soal, Total 100 poin)

| Soal | Tipe | Bobot | Nilai Kamu | Catatan |
|------|------|:-----:|:----------:|---------|
| Soal 1 | Pilihan Ganda (Indeks Array) | 10 | **10** | ✅ Benar: B (`Kelinci`) |
| Soal 2 | Jejak Eksekusi (Maksimal Array) | 25 | **25** | ✅ Sempurna 100%! Semua 6 baris dan kolom tabel terisi akurat |
| Soal 3 | Temukan Bug | 30 | **20** | ⚠️ Berhasil temukan `as $barang => $harga`, tapi terlewat bug `echo $keranjang` (-10) |
| Soal 4 | Coding Mini (`rekap_nilai_siswa.php`) | 35 | **15** | ⚠️ Ide logika bagus, tapi sintaks `foreach` kurang kata `as`, `array_sum($total)` tipe salah, & output di dalam loop (-20) |
| | **Total** | **100** | **70** | ✅ **LULUS** |

---

## 🗃️ FASE 2 — Fungsi, Struktur Data & Penanganan Error

### 🛠️ Bab 7 — Fungsi (`function`, Parameter, & Return Value) (4 Soal, Total 100 poin)

| Soal | Tipe | Bobot | Nilai Kamu | Catatan |
|------|------|:-----:|:----------:|---------|
| Soal 1 | Pilihan Ganda (Fungsi tanpa `return`) | 10 | **0** | ❌ Jawaban A (salah) — fungsi tanpa `return` menghasilkan `NULL` (B) |
| Soal 2 | Jejak Eksekusi | 25 | **25** | ✅ Sempurna 100%! Seluruh 5 step penelusuran fungsi dan default parameter akurat |
| Soal 3 | Temukan Bug | 30 | **30** | ✅ Sempurna 100%! Berhasil temukan kode unreachable setelah `return` & perbaiki variable scope `$pajakPersen` |
| Soal 4 | Coding Mini (`kalkulator_bmi.php`) | 35 | **29** | ✅ Struktur fungsi, type hinting & return 100% rapi! Minor pada `match($bmi)` yang seharusnya `match(true)` (-6) |
| | **Total** | **100** | **84** | ✅ **LULUS** |

### 🗂️ Bab 8 — Array Lanjutan & Fungsi Pengolah Data (4 Soal, Total 100 poin)

| Soal | Tipe | Bobot | Nilai Kamu | Catatan |
|------|------|:-----:|:----------:|---------|
| Soal 1 | Pilihan Ganda (`array_column`) | 10 | **10** | ✅ Benar: B (`Surabaya`) |
| Soal 2 | Jejak Eksekusi | 25 | **25** | ✅ Sempurna 100%! Seluruh 5 step alur transformasi array terisi tepat |
| Soal 3 | Temukan Bug | 30 | **25** | ✅ Berhasil temukan urutan `in_array` & missing `return`, minor tertukar parameter `array_map` (-5) |
| Soal 4 | Coding Mini (`filter_transaksi.php`) | 35 | **32** | ✅ Alur `array_filter`, `array_column`, `count`, & `array_sum` 100% sempurna! Typo titik koma di penutup filter (-3) |
| | **Total** | **100** | **92** | 🏆 **LULUS (Sangat Memuaskan)** |

### 🔤 Bab 9 — String & Manipulasi Teks (4 Soal, Total 100 poin)

| Soal | Tipe | Bobot | Nilai Kamu | Catatan |
|------|------|:-----:|:----------:|---------|
| Soal 1 | Pilihan Ganda (`explode`) | 10 | **10** | ✅ Benar: C (`koding`) |
| Soal 2 | Jejak Eksekusi (Sanitasi Kupon) | 25 | **25** | ✅ Sempurna 100%! Seluruh 5 step penelusuran string akurat |
| Soal 3 | Temukan Bug | 30 | **30** | ✅ Sempurna 100%! Menemukan hasil `trim` yang tidak ditampung & mengganti `count` dengan `strlen` |
| Soal 4 | Coding Mini (`pembuat_slug.php`) | 35 | **34** | ✅ Fungsi slug bekerja sempurna, return string valid, judul asli utuh (-1 header judul terlewat) |
| | **Total** | **100** | **99** | 🏆 **LULUS (Hampir Sempurna)** |

### ⚡ Bab 10 — Closure & Arrow Function (`fn() =>`) (4 Soal, Total 100 poin)

| Soal | Tipe | Bobot | Nilai Kamu | Catatan |
|------|------|:-----:|:----------:|---------|
| Soal 1 | Pilihan Ganda (Arrow Function & auto-capture) | 10 | **10** | ✅ Benar: A (`12`) — paham `fn()` otomatis tangkap variabel luar |
| Soal 2 | Jejak Eksekusi (`array_filter`) | 25 | **25** | ✅ Sempurna 100%! Semua 6 baris tabel terisi akurat, `12+20=32` tepat |
| Soal 3 | Temukan Bug | 30 | **28** | ✅ Dua bug ditemukan & diperbaiki. Penjelasan bug `return` di Arrow Function kurang presisi (-2) |
| Soal 4 | Coding Mini (`format_produk_modern.php`) | 35 | **32** | ✅ Logika Arrow Function & sintaks sempurna! Nilai array harga pertama beda dari spesifikasi soal (-3) |
| | **Total** | **100** | **95** | 🏆 **LULUS (Hampir Sempurna)** |

### 🛡️ Bab 11 — Error & Exception Handling (4 Soal, Total 100 poin)

| Soal | Tipe | Bobot | Nilai Kamu | Catatan |
|------|------|:-----:|:----------:|---------|
| Soal 1 | Pilihan Ganda (`try-catch-finally` flow) | 10 | **10** | ✅ Benar: B (`B` kemudian `C`) — paham exception menghentikan `try` |
| Soal 2 | Jejak Eksekusi (`cekStok` dengan exception) | 25 | **20** | ⚠️ Step 4 salah — `cekStok(5)` tidak dieksekusi setelah exception dilempar di Step 2 (-5) |
| Soal 3 | Temukan Bug | 30 | **27** | ✅ Bug #1 sempurna. Bug #2 kurang presisi — bug utamanya `}` penutup `try` yang hilang, bukan tipe Exception (-3) |
| Soal 4 | Coding Mini (`validasi_usia_anggota.php`) | 35 | **31** | ✅ Logika & sintaks bagus! Data uji Andi (usia 17) tidak memicu penolakan, format pesan `catch` beda spesifikasi (-4) |
| | **Total** | **100** | **88** | ✅ **LULUS** |

---

## 🎓 Rekap Ujian Akhir Fase

### 🏛️ Ujian Akhir Fase 1 — Fondasi PHP Murni & Logika Pemrograman (Total 100 poin)

> **Passing Score**: **70%**

| Soal | Topik Ujian | Bobot | Nilai Kamu | Catatan Evaluasi |
|------|------------|:-----:|:----------:|------------------|
| **Soal 1** | Kasir Mini Diskon (Mudah) | 25 | **24** | ✅ Rumus & logika 100% tepat, kode executable, format rapi (-1 newline header) |
| **Soal 2** | Klasifikasi Suhu & Match (Sedang) | 35 | **31** | ✅ Match & percabangan rapi, tertukar `\|\|` dengan `&&` untuk rentang angka (-4) |
| **Soal 3** | Filter & Agregasi Katalog (Menantang) | 40 | **40** | ✅ **Sempurna 100%!** Array 2D, filter `if`, counter manual, dan agregasi total/rata-rata tepat sesuai spesifikasi |
| | **Total Nilai Ujian** | **100** | **95** | 🏆 **LULUS (Sangat Memuaskan)** |

---

## 📈 Grafik Progres Nilai

```
[FASE 1]
Bab 1   ████████████████░░░░  80/100 ✅ LULUS
Bab 2   ████████████████░░░░  80/100 ✅ LULUS
Bab 3   ███████████░░░░░░░░░  58/100 ⚠️ SELESAI (Perlu Review)
Bab 4   ██████████████░░░░░░  73/100 ✅ LULUS
Bab 5   ██████████████░░░░░░  73/100 ✅ LULUS
Bab 6   ██████████████░░░░░░  70/100 ✅ LULUS
─────────────────────────────────────────────────────────────
Ujian 1 ███████████████████░  95/100 🏆 LULUS SANGAT MEMUASKAN

[FASE 2]
Bab 7   █████████████████░░░  84/100 ✅ LULUS
Bab 8   ██████████████████░░  92/100 🏆 LULUS SANGAT MEMUASKAN
Bab 9   ███████████████████▉  99/100 🏆 LULUS HAMPIR SEMPURNA
Bab 10  ███████████████████░  95/100 🏆 LULUS HAMPIR SEMPURNA
Bab 11  █████████████████░░░  88/100 ✅ LULUS
```

---

> **Passing score ujian fase**: **70%** (Fase 1) / **75%** (Fase 2 & 3).








