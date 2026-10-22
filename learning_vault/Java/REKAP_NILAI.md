# 📊 Sistem Penilaian Kuis — Java AdaptiKog

> Dokumen ini menjelaskan bobot setiap jenis soal dan rekap nilai kuis per bab.

---

## ⚖️ Bobot Soal per Tipe

Setiap kuis memiliki total **100 poin**. Bobot berbeda karena tingkat kesulitan dan usaha yang dibutuhkan berbeda:

| Tipe Soal | Bobot | Alasan |
|-----------|:-----:|--------|
| **Soal Pilihan Ganda** | 10 poin | Mengecek pemahaman konsep dasar — satu jawaban benar/salah |
| **Soal Jejak Eksekusi (Trace)** | 25 poin | Membutuhkan penelusuran baris per baris — lebih kompleks dari PG |
| **Soal Temukan Bug / Prediksi Output** | 30 poin | Membutuhkan analisis kode — mendekati skill debugging nyata |
| **Soal Coding Mini** | 35 poin | Membutuhkan kemampuan menulis kode sendiri dari nol |
| **Total** | **100 poin** | |

### Aturan Penskoran Detail

**Soal Pilihan Ganda (10 poin):**
- Benar → 10 poin
- Salah → 0 poin

**Soal Jejak Eksekusi (25 poin):**
- Dihitung per langkah/baris yang benar
- Misal 6 langkah → tiap langkah = 25/6 ≈ 4 poin
- Sebagian benar → poin proporsional

**Soal Temukan Bug / Prediksi Output (30 poin):**
- Dihitung per bug ditemukan atau per baris prediksi benar
- Misal 3 bug → tiap bug = 10 poin
- Misal 6 prediksi → tiap prediksi = 5 poin

**Soal Coding Mini (35 poin):**
- Logika inti benar → 20 poin
- Output sesuai spesifikasi → 10 poin
- Kode rapi & bebas bug → 5 poin
- Bug minor (typo, operator kecil) → pengurangan 5–10 poin
- Bug mayor (logika salah total) → pengurangan 15–20 poin

---

## 🏆 Rekap Nilai Semua Kuis

### 📘 Bab 1 — Pengenalan Java (3 Soal, Total 100 poin)

> *Bab 1 memiliki 3 soal, bobot disesuaikan: PG=15, Trace=35, Bug=50*

| Soal | Tipe | Bobot | Nilai Kamu | Catatan |
|------|------|:-----:|:----------:|---------|
| Soal 1 | Pilihan Ganda | 15 | **15** | ✅ Benar + alasan tepat |
| Soal 2 | Jejak Eksekusi (5 langkah) | 35 | **22** | ⚠️ 3/5 step benar, bonus salah |
| Soal 3 | Temukan Bug (2 bug) | 50 | **50** | ✅ Sempurna, kode perbaikan benar |
| | **Total** | **100** | **87** | ✅ **LULUS** |

---

### 📘 Bab 2 — Variabel & Tipe Data (4 Soal, Total 100 poin)

| Soal | Tipe | Bobot | Nilai Kamu | Catatan |
|------|------|:-----:|:----------:|---------|
| Soal 1 | Pilihan Ganda | 10 | **10** | ✅ Benar + alasan detail |
| Soal 2 | Temukan Bug (3 bug) | 25 | **25** | ✅ Semua 3 bug ditemukan |
| Soal 3 | Prediksi Output (6 baris) | 30 | **20** | ⚠️ 4/6 benar — `double` presisi terlewat |
| Soal 4 | Coding Mini | 35 | **35** | ✅ Logika & output sempurna, pakai `()` dengan benar |
| | **Total** | **100** | **90** | ✅ **LULUS** |

---

### 📘 Bab 3 — Operator (4 Soal, Total 100 poin)

| Soal | Tipe | Bobot | Nilai Kamu | Catatan |
|------|------|:-----:|:----------:|---------|
| Soal 1 | Pilihan Ganda | 10 | **0** | ❌ Keliru `%` dengan `/` |
| Soal 2 | Jejak Eksekusi (5 langkah) | 25 | **25** | ✅ Sempurna |
| Soal 3 | Prediksi Logika (6 ekspresi) | 30 | **25** | ⚠️ 5/6 benar — `&&` dengan satu `false` terlewat |
| Soal 4 | Coding Mini | 35 | **35** | ✅ Logika & kode benar, `punyaKtp == true` (minor, tidak dikurangi) |
| | **Total** | **100** | **85** | ✅ **LULUS** |

---

### 📘 Bab 4 — Percabangan (4 Soal, Total 100 poin)

| Soal | Tipe | Bobot | Nilai Kamu | Catatan |
|------|------|:-----:|:----------:|---------|
| Soal 1 | Pilihan Ganda | 10 | **10** | ✅ Benar + alasan lengkap |
| Soal 2 | Jejak Eksekusi Switch | 25 | **20** | ⚠️ Tabel 3/3 benar, output akhir tidak diisi |
| Soal 3 | Temukan Bug (2 bug) | 30 | **30** | ✅ Sempurna, urutan diperbaiki dengan benar |
| Soal 4 | Coding Mini | 35 | **20** | ⚠️ Logika `if-else` benar (+20), typo `prinln` (-5), `\|\|` harusnya `&&` (-10) |
| | **Total** | **100** | **80** | ✅ **LULUS** |

---

### 📘 Bab 5 — Perulangan (4 Soal, Total 100 poin)

| Soal | Tipe | Bobot | Nilai Kamu | Catatan |
|------|------|:-----:|:----------:|---------|
| Soal 1 | Pilihan Ganda | 10 | **0** | ❌ `i++` di `for` adalah update-nya — bukan infinite loop |
| Soal 2 | Jejak Eksekusi `while` | 25 | **25** | ✅ Sempurna |
| Soal 3 | Prediksi `break` & `continue` | 30 | **30** | ✅ Sempurna + penjelasan jelas |
| Soal 4 | Coding Mini | 35 | **25** | ⚠️ Logika loop benar (+25), `println` harusnya `print` di inner loop (-10) |
| | **Total** | **100** | **80** | ✅ **LULUS** |

---

## 📈 Grafik Progres Nilai

```
Bab 1  ████████████████████░░  87/100
Bab 2  ██████████████████████  90/100  ← Tertinggi!
Bab 3  █████████████████████░  85/100
Bab 4  ████████████████████░░  80/100
Bab 5  ████████████████████░░  80/100
```

---

## 📌 Pola Kesalahan & Area Fokus

| Topik | Frekuensi Salah | Rekomendasi |
|-------|:---------------:|-------------|
| `%` (modulus) vs `/` (bagi) | 1x (Bab 3) | Ingat: `%` = **sisa** bagi |
| `&&` vs `\|\|` untuk rentang | 1x (Bab 4) | Rentang nilai → selalu `&&` |
| `print` vs `println` | 2x (Bab 1, 5) | `print` = sambung baris, `println` = pindah baris |
| Struktur `for` (init;kondisi;**update**) | 1x (Bab 5) | `i++` di bagian ketiga `for` adalah update otomatis |
| Presisi `double` | 1x (Bab 2) | `double` tidak membulatkan otomatis |
| Output tidak diisi lengkap | 1x (Bab 4) | Pastikan semua kolom terisi |

---

> **Catatan Tutor**: Nilai stabil di 80–90 setiap bab. Rata-rata **84.4/100** — jauh di atas passing score! 💪
> Soal Coding Mini adalah area paling konsisten mengalami bug kecil — fokus di sini saat Bab 6 & 7.
