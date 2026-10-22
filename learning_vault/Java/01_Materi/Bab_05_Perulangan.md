# 📚 Bab 5 — Perulangan (`for`, `while`, `do-while`)

> **Level**: Pemula Murni (Zero-Knowledge) | **Fase**: 1 dari 4 | **Prasyarat**: Bab 1–4 ✅ | **Estimasi Waktu**: 75–90 menit

---

## 💡 Konsep Utama

**Perulangan (loop)** membuat program menjalankan sekelompok kode **berkali-kali** secara otomatis. Tanpa loop, kamu harus menulis `System.out.println` sebanyak 100 kali jika ingin mencetak 100 baris — dengan loop, cukup 3 baris kode.

Ada **3 jenis loop** di Java, masing-masing punya kasus penggunaan yang tepat.

---

## 🔧 Analogi Mekanis Dunia Nyata

Bayangkan **mesin stempel pabrik**:

| Situasi Nyata | Padanan di Java |
|---|---|
| Stempel dokumen sebanyak 50 kali | `for` loop — jumlah pengulangan sudah diketahui |
| Stempel terus sampai tinta habis | `while` loop — ulangi selama kondisi masih `true` |
| Stempel setidaknya satu kali, lalu cek tintanya | `do-while` loop — jalankan dulu baru cek kondisi |

---

## 📋 Peta Langkah-demi-Langkah

### Langkah 1 — `for` Loop (Jumlah Sudah Diketahui)

Gunakan `for` saat kamu **tahu persis berapa kali** harus mengulang.

**Struktur:**
```
for (inisialisasi; kondisi; update) {
    // kode yang diulang
}
```

**3 bagian dalam kurung `for`:**

| Bagian | Posisi | Fungsi | Contoh |
|--------|--------|--------|--------|
| Inisialisasi | Pertama | Buat & set nilai awal variabel counter | `int i = 0` |
| Kondisi | Kedua | Cek apakah loop lanjut | `i < 5` |
| Update | Ketiga | Ubah counter setelah tiap iterasi | `i++` |

**Contoh — cetak angka 1 sampai 5:**
```java
for (int i = 1; i <= 5; i++) {
    System.out.println("Angka: " + i);
}
```

**Alur eksekusi `for`:**
```
1. int i = 1       → inisialisasi (hanya sekali)
2. i <= 5 ?        → cek kondisi
   - true  → jalankan isi loop, lalu i++, balik ke langkah 2
   - false → keluar loop
```

---

### Langkah 2 — `while` Loop (Kondisi Dulu, Baru Jalan)

Gunakan `while` saat **tidak tahu pasti berapa kali** mengulang — cukup tahu kapan harus berhenti.

**Struktur:**
```
while (kondisi) {
    // kode yang diulang
    // WAJIB ada sesuatu yang mengubah kondisi agar tidak infinite loop!
}
```

**Contoh — hitung mundur:**
```java
int hitungan = 5;

while (hitungan > 0) {
    System.out.println("Hitung mundur: " + hitungan);
    hitungan--; // tanpa ini → infinite loop!
}
System.out.println("Selesai!");
```

> ⚠️ **Bahaya Infinite Loop!** Jika kondisi `while` tidak pernah berubah menjadi `false`, program akan jalan selamanya dan hang. Pastikan ada perubahan variabel di dalam loop!

---

### Langkah 3 — `do-while` Loop (Jalan Dulu, Cek Belakangan)

Perbedaan utama dari `while`: **blok kode dijalankan minimal 1 kali**, baru kondisi dicek.

**Struktur:**
```
do {
    // kode yang diulang
} while (kondisi);  ← perhatikan titik koma di sini!
```

**Contoh — validasi input:**
```java
int angka = 0;

do {
    System.out.println("Masukkan angka positif...");
    angka = 7; // simulasi input user
} while (angka <= 0);

System.out.println("Angka valid: " + angka);
```

> Blok `do` selalu dijalankan setidaknya sekali, meskipun kondisi `while` langsung `false`.

---

### Langkah 4 — `break` dan `continue`

Dua kata kunci untuk mengontrol alur loop:

| Kata Kunci | Fungsi | Analogi |
|:---:|--------|---------|
| `break` | **Keluar** dari loop sepenuhnya | Tombol STOP darurat mesin |
| `continue` | **Lewati** iterasi saat ini, lanjut ke berikutnya | Skip satu giliran, mesin terus jalan |

```java
// Contoh break — berhenti saat ketemu angka 4
for (int i = 1; i <= 10; i++) {
    if (i == 4) break;           // keluar loop jika i = 4
    System.out.println(i);       // cetak 1, 2, 3 (lalu break)
}

// Contoh continue — lewati angka genap
for (int i = 1; i <= 6; i++) {
    if (i % 2 == 0) continue;   // skip jika genap
    System.out.println(i);       // cetak 1, 3, 5
}
```

---

### Langkah 5 — Nested Loop (Loop di Dalam Loop)

Loop bisa diletakkan di dalam loop lain. Loop dalam selesai **penuh** setiap kali loop luar berjalan satu iterasi.

```java
for (int baris = 1; baris <= 3; baris++) {
    for (int kolom = 1; kolom <= 3; kolom++) {
        System.out.print(baris + "x" + kolom + "=" + (baris*kolom) + "  ");
    }
    System.out.println(); // pindah baris setelah tiap baris selesai
}
```

Output:
```
1x1=1  1x2=2  1x3=3
2x1=2  2x2=4  2x3=6
3x1=3  3x2=6  3x3=9
```

---

## 📊 Tabel Jejak Eksekusi — `for` Loop

```java
for (int i = 1; i <= 4; i++) {
    System.out.println("Iterasi ke-" + i);
}
```

| Iterasi | Nilai `i` | Cek `i <= 4` | Yang Terjadi | Output |
|:-------:|:---------:|:------------:|:-------------|:-------|
| — | `i = 1` | `1 <= 4` = **true** | Jalankan isi loop | `Iterasi ke-1` |
| — | `i = 2` (setelah `i++`) | `2 <= 4` = **true** | Jalankan isi loop | `Iterasi ke-2` |
| — | `i = 3` | `3 <= 4` = **true** | Jalankan isi loop | `Iterasi ke-3` |
| — | `i = 4` | `4 <= 4` = **true** | Jalankan isi loop | `Iterasi ke-4` |
| — | `i = 5` | `5 <= 4` = **false** | **Loop selesai, keluar** | *(tidak ada)* |

---

## 📊 Tabel Jejak Eksekusi — `while` Loop dengan `break`

```java
int n = 1;
while (n <= 10) {
    if (n == 4) break;
    System.out.println(n);
    n++;
}
```

| Step | Nilai `n` | Cek `n <= 10` | Cek `n == 4` | Output |
|:-----|:---------:|:-------------:|:------------:|:-------|
| 1 | `1` | true | false | Cetak `1`, n++ → n=2 |
| 2 | `2` | true | false | Cetak `2`, n++ → n=3 |
| 3 | `3` | true | false | Cetak `3`, n++ → n=4 |
| 4 | `4` | true | **true** | `break` — **keluar loop** |

**Output total**: `1` `2` `3` *(berhenti sebelum 4)*

---

## 💻 Kode Contoh Java — Siap Jalan di JDK 21

```java
// File: ContohPerulangan.java

public class ContohPerulangan {

    public static void main(String[] args) {

        // === FOR LOOP: Cetak tabel perkalian 3 ===
        System.out.println("=== TABEL PERKALIAN 3 ===");
        for (int i = 1; i <= 10; i++) {
            System.out.println("3 x " + i + " = " + (3 * i));
        }

        // === FOR LOOP: Hitung total & rata-rata ===
        System.out.println("\n=== TOTAL NILAI ===");
        int[] nilaiSiswa = {80, 90, 75, 85, 70};
        int total = 0;

        for (int i = 0; i < nilaiSiswa.length; i++) {
            total += nilaiSiswa[i];
        }
        double rata = (double) total / nilaiSiswa.length;
        System.out.println("Total : " + total);
        System.out.println("Rata  : " + rata);

        // === WHILE LOOP: Hitung mundur ===
        System.out.println("\n=== HITUNG MUNDUR ===");
        int hitungan = 5;
        while (hitungan > 0) {
            System.out.println(hitungan + "...");
            hitungan--;
        }
        System.out.println("Liftoff! 🚀");

        // === DO-WHILE LOOP ===
        System.out.println("\n=== DO-WHILE ===");
        int x = 10;
        do {
            System.out.println("Nilai x: " + x);
            x++;
        } while (x < 10); // kondisi langsung false, tapi tetap jalan 1x
        System.out.println("Setelah loop, x = " + x);

        // === BREAK & CONTINUE ===
        System.out.println("\n=== HANYA ANGKA GANJIL 1-10 ===");
        for (int i = 1; i <= 10; i++) {
            if (i % 2 == 0) continue; // lewati angka genap
            System.out.print(i + " ");
        }
        System.out.println();

        // === NESTED LOOP: Pola bintang ===
        System.out.println("\n=== POLA BINTANG ===");
        for (int baris = 1; baris <= 4; baris++) {
            for (int bintang = 1; bintang <= baris; bintang++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
```

**Output yang diharapkan:**
```
=== TABEL PERKALIAN 3 ===
3 x 1 = 3
3 x 2 = 6
...
3 x 10 = 30

=== TOTAL NILAI ===
Total : 400
Rata  : 80.0

=== HITUNG MUNDUR ===
5...
4...
3...
2...
1...
Liftoff! 🚀

=== DO-WHILE ===
Nilai x: 10
Setelah loop, x = 11

=== HANYA ANGKA GANJIL 1-10 ===
1 3 5 7 9

=== POLA BINTANG ===
*
* *
* * *
* * * *
```

---

## 🔍 Kapan Pakai Loop yang Mana?

| Situasi | Loop yang Tepat | Contoh |
|---------|:---------------:|--------|
| Jumlah iterasi **sudah pasti** | `for` | Cetak 1–100, tabel perkalian |
| Jumlah iterasi **tidak pasti**, kondisi dicek dulu | `while` | Baca sampai data habis |
| Harus **jalan minimal 1x** sebelum cek kondisi | `do-while` | Validasi input user |

---

## ⚠️ Jebakan Paling Umum di Bab 5

| Jebakan                    | Contoh                                  | Penjelasan                                  |
| -------------------------- | --------------------------------------- | ------------------------------------------- |
| **Infinite loop**          | `while (true) { }` tanpa `break`        | Kondisi tidak pernah `false` → program hang |
| **Off-by-one error**       | `for (i=1; i<5; i++)` → hanya 4 iterasi | Pakai `<=` jika mau iterasi ke-5 ikut       |
| **Lupa update di `while`** | `while (x > 0) { println(x); }`         | `x` tidak pernah berubah → infinite loop    |
| **`i` di luar scope**      | Pakai `i` setelah `for` selesai         | Variabel `i` hanya ada di dalam blok `for`  |

---

## 🧩 Kuis Mini Interaktif — Bab 5

Jawab di [`03_Jawaban_Kuis/Kuis_Bab_05.md`](../03_Jawaban_Kuis/Kuis_Bab_05.md)!

---

### Soal 1 — Pilihan Ganda (10 poin)

Berapa kali kode berikut mencetak sesuatu?

```java
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}
```

- A) 4 kali
- B) 5 kali
- C) 6 kali
- D) Infinite loop

---

### Soal 2 — Jejak Eksekusi `while` (25 poin)

Lengkapi tabel untuk program berikut:

```java
int skor = 1;
while (skor <= 5) {
    System.out.println("Skor: " + skor);
    skor += 2;
}
```

| Iterasi | Nilai `skor` | Cek `skor <= 5` | Output | `skor` setelah `+= 2` |
|:-------:|:------------:|:---------------:|:------:|:---------------------:|
| 1 | 1 | ??? | ??? | ??? |
| 2 | ??? | ??? | ??? | ??? |
| 3 | ??? | ??? | ??? | ??? |
| 4 | ??? | ??? | Loop berhenti | — |

---

### Soal 3 — Prediksi Output `break` & `continue` (30 poin)

Tanpa menjalankan kode, tuliskan **semua output** dari program ini:

```java
for (int i = 1; i <= 8; i++) {
    if (i == 3) continue;
    if (i == 6) break;
    System.out.println(i);
}
```

---

### Soal 4 — Coding Mini (35 poin)

Buat program `PolaBintang.java` yang mencetak pola berikut menggunakan **nested loop**:

```
* * * * *
* * * *
* * *
* *
*
```

**Ketentuan:**
- Baris pertama punya 5 bintang, baris terakhir 1 bintang
- Gunakan nested `for` loop
- **Petunjuk**: loop luar untuk baris (1–5), loop dalam untuk bintang (berkurang tiap baris)

---

## 📌 Ringkasan Bab 5

- ✅ `for` — jumlah iterasi diketahui, counter jelas
- ✅ `while` — iterasi selama kondisi `true`, cek kondisi di awal
- ✅ `do-while` — minimal jalan 1x, cek kondisi di akhir
- ✅ `break` — keluar loop sepenuhnya
- ✅ `continue` — lewati iterasi saat ini, lanjut ke berikutnya
- ✅ Nested loop — loop di dalam loop, loop dalam selesai penuh per iterasi luar

---

> **Langkah selanjutnya**: Setelah kuis selesai, kita masuk ke **[Bab 6 — Array](Bab_06_Array.md)** — cara menyimpan banyak data dalam satu variabel! 🚀
