# 🎓 Ujian Akhir Fase 1 — Fondasi Java Murni

> **Cakupan**: Bab 1–7 (Pengenalan Java, Variabel, Operator, Percabangan, Perulangan, Array, Method)
> **Format**: Soal Coding — buat program Java yang berjalan sesuai spesifikasi
> **Jumlah Soal**: 5 soal
> **Passing Score**: **70%** = minimal **4 soal** harus benar dan bisa dijalankan
> **Jika Tidak Lulus**: Tutor akan tunjukkan bab mana yang perlu diulang

---

## 📋 Cara Mengerjakan

1. Buat satu file `.java` per soal (nama file sesuai instruksi tiap soal)
2. Pastikan kode **bisa dikompilasi dan dijalankan** tanpa error di JDK 21
3. Salin kode yang sudah jadi ke dalam file ini di bagian **"Jawabanku"** masing-masing soal
4. Kabari tutor — tutor akan menguji output program kamu dan memberikan nilai + feedback

---

## 🟢 Soal 1 — Mudah | Variabel & Output (Bab 1 & 2)

**Spesifikasi Program:**
Buat file `BioData.java`. Program harus mencetak biodata sederhana ke konsol dengan format tepat seperti ini:

```
Nama   : [nama kamu]
Umur   : [umur kamu] tahun
Kota   : [kota kamu]
Bahasa : Java
```

**Aturan:**
- Simpan nama, umur, dan kota di dalam **variabel** yang sesuai tipe datanya (`String` untuk teks, `int` untuk angka)
- Cetak biodata menggunakan variabel tersebut, bukan menulis teks langsung (*hardcoded*)
- Gunakan `System.out.println`

**File**: `BioData.java`

### Jawabanku — Soal 1:
```java
// Tulis kode Java kamu di sini
```

---

## 🟡 Soal 2 — Mudah-Sedang | Operator & Percabangan (Bab 3 & 4)

**Spesifikasi Program:**
Buat file `KalkulatorNilai.java`. Program menghitung nilai akhir siswa dan menentukan keterangannya.

**Logika yang harus diimplementasikan:**

| Kondisi | Keterangan |
|---------|------------|
| Nilai ≥ 90 | "Lulus dengan Pujian" |
| 75 ≤ Nilai < 90 | "Lulus" |
| 60 ≤ Nilai < 75 | "Lulus Bersyarat" |
| Nilai < 60 | "Tidak Lulus" |

**Aturan:**
- Simpan nilai di variabel `int nilaiAkhir = 82;` (atau angka lain pilihanmu)
- Gunakan `if-else if-else` untuk menentukan keterangan
- Output contoh (untuk nilai 82):
```
Nilai Akhir : 82
Keterangan  : Lulus
```

**File**: `KalkulatorNilai.java`

### Jawabanku — Soal 2:
```java
// Tulis kode Java kamu di sini
```

---

## 🟡 Soal 3 — Sedang | Perulangan & Array (Bab 5 & 6)

**Spesifikasi Program:**
Buat file `StatistikNilai.java`. Program menyimpan 5 nilai ujian dalam sebuah array, lalu menghitung dan mencetak:
- Semua nilai satu per satu (gunakan loop `for`)
- Total semua nilai
- Rata-rata nilai

**Output yang diharapkan** (nilai bisa berbeda, format harus sama):
```
Daftar Nilai:
1. 85
2. 72
3. 90
4. 68
5. 77

Total Nilai : 392
Rata-rata   : 78.4
```

**Aturan:**
- Gunakan `int[] daftarNilai = {85, 72, 90, 68, 77};`
- Gunakan `for` loop untuk iterasi array
- Rata-rata dicetak sebagai `double`

**File**: `StatistikNilai.java`

### Jawabanku — Soal 3:
```java
// Tulis kode Java kamu di sini
```

---

## 🟠 Soal 4 — Sedang-Menantang | Method & Percabangan (Bab 4 & 7)

**Spesifikasi Program:**
Buat file `KonversiSuhu.java`. Program menyediakan **2 method** konversi suhu:
1. `celsiusKefahrenheit(double celsius)` — mengembalikan suhu dalam Fahrenheit
2. `fahrenheitKeCelsius(double fahrenheit)` — mengembalikan suhu dalam Celsius

**Rumus:**
- Celsius → Fahrenheit: `(celsius × 9/5) + 32`
- Fahrenheit → Celsius: `(fahrenheit - 32) × 5/9`

**Di `main`, panggil kedua method dan cetak hasilnya:**
```
100°C = 212.0°F
98.6°F = 37.0°C
```

**Aturan:**
- Kedua method harus `static` dan mengembalikan `double`
- Gunakan `System.out.printf` atau string concatenation untuk format output

**File**: `KonversiSuhu.java`

### Jawabanku — Soal 4:
```java
// Tulis kode Java kamu di sini
```

---

## 🔴 Soal 5 — Menantang | Integrasi Semua Konsep (Bab 1–7)

**Spesifikasi Program:**
Buat file `AnalisaAngka.java`. Program menganalisa sebuah array angka dan mencetak laporan lengkap.

**Array yang digunakan:**
```java
int[] angka = {15, 3, 42, 7, 28, 55, 12, 33, 8, 21};
```

**Program harus mencetak:**
```
=== LAPORAN ANALISA ANGKA ===
Jumlah data  : 10
Nilai minimum: 3
Nilai maksimum: 55
Total        : 224
Rata-rata    : 22.4

Angka Genap  : 42 28 12 8
Angka Ganjil : 15 3 7 55 33 21
```

**Aturan:**
- Buat **method terpisah** untuk setiap perhitungan:
  - `cariMin(int[] data)` → return `int`
  - `cariMaks(int[] data)` → return `int`
  - `hitungTotal(int[] data)` → return `int`
- Gunakan loop `for` dan kondisi `if` untuk memisahkan genap/ganjil
- Semua method harus `static`

**File**: `AnalisaAngka.java`

### Jawabanku — Soal 5:
```java
// Tulis kode Java kamu di sini
```

---

## 📊 Rekap Nilai Ujian (Diisi oleh Tutor)

| Soal | Topik | Nilai (0/1) | Catatan Tutor |
|------|-------|:-----------:|---------------|
| 1 | Variabel & Output | — | — |
| 2 | Operator & Percabangan | — | — |
| 3 | Perulangan & Array | — | — |
| 4 | Method & Return Value | — | — |
| 5 | Integrasi Semua Konsep | — | — |
| | **Total** | **— / 5** | |
| | **Persentase** | **—%** | |
| | **Status** | **—** | |

---

> Setelah mengisi semua jawaban di atas, kabari tutormu! 🚀
> Jika lulus (≥ 70%), kamu siap lanjut ke **Fase 2 — OOP** 🎉
