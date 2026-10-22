# 📚 Bab 2 — Variabel & Tipe Data

> **Level**: Pemula Murni (Zero-Knowledge) | **Fase**: 1 dari 4 | **Prasyarat**: Bab 1 ✅ | **Estimasi Waktu**: 60–75 menit

---

## 💡 Konsep Utama

**Variabel** adalah tempat penyimpanan data di dalam memori komputer. Setiap variabel punya **nama**, **tipe data**, dan **nilai**.

Di Java, kamu **wajib** menyebutkan tipe data sebelum memberi nama variabel. Ini berbeda dengan beberapa bahasa lain yang tidak perlu menyebutkan tipe.

---

## 🔧 Analogi Mekanis Dunia Nyata

Gunakan analogi **rak gudang berlabel**:

| Konsep Nyata | Padanan di Java | Contoh |
|---|---|---|
| **Jenis rak** (ukuran & tipe barang) | Tipe data (`int`, `double`, dll.) | Rak khusus buku |
| **Label nama rak** | Nama variabel | Label: `jumlahBuku` |
| **Barang di dalam rak** | Nilai variabel | Isi: `42` |
| **Mengisi rak** | Assignment `=` | `jumlahBuku = 42;` |

Contoh konkret dalam kode:
```
int jumlahBuku = 42;
│    │           │
│    │           └── Nilai yang disimpan
│    └────────────── Nama variabel (label rak)
└─────────────────── Tipe data (jenis rak)
```

---

## 📋 Peta Langkah-demi-Langkah

### Langkah 1 — Kenali 5 Tipe Data Primitif Utama

| Tipe | Untuk Menyimpan | Contoh Nilai | Ukuran Memori |
|------|-----------------|--------------|---------------|
| `int` | Bilangan bulat | `10`, `-5`, `0` | 32-bit |
| `double` | Bilangan desimal | `3.14`, `-0.5` | 64-bit |
| `boolean` | Benar/Salah | `true`, `false` | 1-bit |
| `char` | Satu karakter | `'A'`, `'z'`, `'3'` | 16-bit |
| `String` | Teks (kata/kalimat) | `"Halo"`, `"Java"` | Dinamis |

> **Catatan penting**: `String` ditulis dengan huruf kapital `S` karena ia bukan tipe primitif — ia adalah sebuah *class* bawaan Java. Empat lainnya ditulis huruf kecil semua.

---

### Langkah 2 — Cara Mendeklarasikan Variabel

**Pola umum:**
```
TipeData namaVariabel = nilai;
```

Ada **2 cara** membuat variabel:

**Cara A — Deklarasi + Isi sekaligus:**
```java
int umur = 20;
```

**Cara B — Deklarasi dulu, isi belakangan:**
```java
int umur;       // deklarasi: rak sudah ada tapi kosong
umur = 20;      // assignment: mengisi rak
```

---

### Langkah 3 — Aturan Penamaan Variabel

**✅ BOLEH:**
- Huruf, angka, underscore `_`, dollar `$`
- Mulai dengan huruf kecil: `namaLengkap`, `nilaiUjian`
- Gunakan camelCase untuk nama panjang: `jumlahMahasiswaBaru`

**❌ TIDAK BOLEH:**
- Mulai dengan angka: `1nama` ❌
- Mengandung spasi: `nama lengkap` ❌
- Menggunakan kata kunci Java: `int`, `class`, `public` ❌

---

### Langkah 4 — Perbedaan `int` vs `double`

```java
int    nilaiA = 10 / 3;    // hasil: 3  (desimal dibuang!)
double nilaiB = 10.0 / 3;  // hasil: 3.3333...
```

> Saat dua `int` dibagi, Java **membuang sisa desimalnya**. Untuk hasil presisi, gunakan `double`.

---

### Langkah 5 — Cara Menulis Nilai per Tipe Data

| Tipe | Cara Menulis | Salah |
|------|-------------|-------|
| `int` | `42` | `42.0` ❌ |
| `double` | `3.14` atau `3.0` | `3,14` ❌ (jangan pakai koma) |
| `boolean` | `true` atau `false` | `"true"` ❌ (jangan pakai kutip) |
| `char` | `'A'` (kutip tunggal) | `"A"` ❌ (itu String) |
| `String` | `"Halo"` (kutip ganda) | `'Halo'` ❌ |

---

## 📊 Tabel Jejak Eksekusi — Cara Java Menyimpan Variabel di Memori

Program berikut dieksekusi langkah per langkah. Perhatikan kolom **Stack Memory** yang berisi nilai variabel saat itu:

```java
public class ContohVariabel {
    public static void main(String[] args) {
        int usia = 17;
        double tinggi = 165.5;
        boolean lulus = true;
        String nama = "Andi";
        usia = 18;
    }
}
```

| Step | Baris Kode               | Stack Memory (isi variabel aktif)                              | Keterangan                                  |
| :--- | :----------------------- | :------------------------------------------------------------- | :------------------------------------------ |
| 1    | `int usia = 17;`         | `usia = 17`                                                    | Rak `int` bernama `usia` dibuat, diisi `17` |
| 2    | `double tinggi = 165.5;` | `usia = 17`, `tinggi = 165.5`                                  | Rak `double` baru ditambahkan               |
| 3    | `boolean lulus = true;`  | `usia = 17`, `tinggi = 165.5`, `lulus = true`                  | Rak `boolean` ditambahkan                   |
| 4    | `String nama = "Andi";`  | `usia = 17`, `tinggi = 165.5`, `lulus = true`, `nama = "Andi"` | Rak `String` ditambahkan                    |
| 5    | `usia = 18;`             | `usia = 18`, `tinggi = 165.5`, `lulus = true`, `nama = "Andi"` | Nilai `usia` **ditimpa** dari `17` → `18`   |

---

## 💻 Kode Contoh Java — Siap Jalan di JDK 21

```java
// File: ContohVariabel.java

public class ContohVariabel {

    public static void main(String[] args) {

        // === DEKLARASI & INISIALISASI VARIABEL ===

        String  nama    = "Budi Santoso";   // teks (String pakai kutip ganda)
        int     umur    = 20;               // bilangan bulat
        double  tinggi  = 172.5;            // bilangan desimal
        boolean aktif   = true;             // benar/salah
        char    inisial = 'B';              // satu karakter (pakai kutip tunggal)

        // === MENCETAK SEMUA VARIABEL ===

        System.out.println("=== DATA MAHASISWA ===");
        System.out.println("Nama    : " + nama);
        System.out.println("Umur    : " + umur + " tahun");
        System.out.println("Tinggi  : " + tinggi + " cm");
        System.out.println("Aktif   : " + aktif);
        System.out.println("Inisial : " + inisial);

        // === MENGUBAH NILAI VARIABEL ===

        umur = 21;          // ulang tahun — nilai lama (20) diganti
        tinggi = 173.0;     // pengukuran baru

        System.out.println("\n=== DATA SETELAH UPDATE ===");
        System.out.println("Umur baru   : " + umur);
        System.out.println("Tinggi baru : " + tinggi);

        // === OPERASI DASAR ANTAR VARIABEL ===

        int tahunLahir    = 2024 - umur;    // menghitung dari variabel lain
        double tinggimM   = tinggi / 100;   // konversi cm ke meter

        System.out.println("\nTahun lahir perkiraan : " + tahunLahir);
        System.out.println("Tinggi dalam meter    : " + tinggimM);

    }
}
```

**Output yang diharapkan:**
```
=== DATA MAHASISWA ===
Nama    : Budi Santoso
Umur    : 20 tahun
Tinggi  : 172.5 cm
Aktif   : true
Inisial : B

=== DATA SETELAH UPDATE ===
Umur baru   : 21
Tinggi baru : 173.0

Tahun lahir perkiraan : 2003
Tinggi dalam meter    : 1.73
```

---

## 🔍 Topik Bonus — Menggabungkan Teks dengan Variabel (Concatenation)

Tanda `+` di Java punya **2 fungsi berbeda** tergantung konteks:

| Konteks       | Fungsi `+`            | Contoh          | Hasil        |
| ------------- | --------------------- | --------------- | ------------ |
| Dua angka     | **Penjumlahan**       | `10 + 5`        | `15`         |
| Teks + apapun | **Penggabungan teks** | `"Umur: " + 20` | `"Umur: 20"` |

**Hati-hati dengan urutan:**
```java
System.out.println("Hasil: " + 10 + 5);    // → "Hasil: 105"  ⚠️ bukan 15!
System.out.println("Hasil: " + (10 + 5));  // → "Hasil: 15"   ✅ pakai kurung
```

> Begitu ada `String` di sebelah kiri `+`, semua yang di kanan dianggap teks dan **digabungkan**, bukan dijumlahkan.

---

## ⚠️ Kesalahan Paling Umum di Bab 2

| Kesalahan | Contoh Salah | Contoh Benar |
|-----------|-------------|--------------|
| Lupa tipe data | `nama = "Andi";` | `String nama = "Andi";` |
| Salah kutip untuk `char` | `char c = "A";` | `char c = 'A';` |
| Gunakan koma untuk desimal | `double x = 3,14;` | `double x = 3.14;` |
| `boolean` pakai kutip | `boolean b = "true";` | `boolean b = true;` |
| Nama variabel dimulai angka | `int 1nilai = 90;` | `int nilai1 = 90;` |

---

## 🧩 Kuis Mini Interaktif — Bab 2

Jawab di [`03_Jawaban_Kuis/Kuis_Bab_02.md`](../03_Jawaban_Kuis/Kuis_Bab_02.md)!

---

### Soal 1 — Pilihan Ganda

Manakah deklarasi variabel yang **sepenuhnya benar** di Java?

- A) `Int umur = 20;`
- B) `double harga = 15,000;`
- C) `String nama = 'Budi';`
- D) `boolean lulus = false;`

---

### Soal 2 — Temukan Bug

Kode berikut memiliki **3 kesalahan**. Temukan semuanya!

```java
public class DataSiswa {
    public static void main(String[] args) {
        String  nama  = "Citra"
        int     nilai = 85.5;
        char    kelas = "A";
        System.out.println(nama + " kelas " + kelas + " nilai " + nilai);
    }
}
```

---

### Soal 3 — Prediksi Output

Tanpa menjalankan kode, prediksi output dari program berikut **baris per baris**:

```java
public class Prediksi {
    public static void main(String[] args) {
        int a = 10;
        int b = 3;
        double c = 10.0;

        System.out.println(a + b);
        System.out.println(a - b);
        System.out.println(a / b);
        System.out.println(c / b);
        System.out.println("Nilai: " + a + b);
        System.out.println("Nilai: " + (a + b));
    }
}
```

Isi tabel ini:

| Baris `println` | Prediksi Output |
|:----------------|:----------------|
| `a + b` | ??? |
| `a - b` | ??? |
| `a / b` | ??? |
| `c / b` | ??? |
| `"Nilai: " + a + b` | ??? |
| `"Nilai: " + (a + b)` | ??? |

---

### Soal 4 — Coding Mini

Buat sebuah **program singkat** (tidak perlu file baru, cukup tulis kodenya di file jawaban) yang:
1. Menyimpan panjang sebuah persegi panjang (`int panjang = 12`) dan lebar (`int lebar = 7`)
2. Menghitung luas (`panjang × lebar`) dan keliling (`2 × (panjang + lebar)`)
3. Mencetak hasilnya dengan format:

```
Panjang  : 12
Lebar    : 7
Luas     : 84
Keliling : 38
```

---

## 📌 Ringkasan Bab 2

- ✅ Variabel = nama + tipe data + nilai
- ✅ 5 tipe utama: `int`, `double`, `boolean`, `char`, `String`
- ✅ `char` pakai kutip tunggal `'A'`, `String` pakai kutip ganda `"Halo"`
- ✅ `int / int` membuang desimal — gunakan `double` untuk hasil presisi
- ✅ `+` dengan `String` = penggabungkan teks, bukan menjumlahkan

---

> **Langkah selanjutnya**: Setelah mengerjakan kuis di atas, kabari tutormu!
> Lanjut ke **[Bab 3 — Operator](Bab_03_Operator.md)** 🚀
