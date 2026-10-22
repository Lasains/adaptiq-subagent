# 📚 Bab 3 — Operator

> **Level**: Pemula Murni (Zero-Knowledge) | **Fase**: 1 dari 4 | **Prasyarat**: Bab 1 ✅ Bab 2 ✅ | **Estimasi Waktu**: 60–75 menit

---

## 💡 Konsep Utama

**Operator** adalah simbol yang memerintahkan Java untuk melakukan sesuatu terhadap nilai atau variabel. Seperti tombol di kalkulator — setiap tombol punya fungsi spesifik.

Ada **5 kelompok operator** yang wajib kamu kuasai di Fase 1 ini.

---

## 🔧 Analogi Mekanis Dunia Nyata

Bayangkan operator seperti **mesin produksi di pabrik**:

| Mesin Pabrik | Padanan Operator Java | Fungsi |
|---|---|---|
| Mesin penjumlah | `+` | Tambahkan dua nilai |
| Mesin pengurang | `-` | Kurangi dua nilai |
| Timbangan perbandingan | `==`, `>`, `<` | Cek apakah dua nilai sama / lebih besar / lebih kecil |
| Sakelar logika AND | `&&` | Hanya aktif jika **dua kondisi** sama-sama benar |
| Sakelar logika OR | `\|\|` | Aktif jika **salah satu kondisi** benar |

---

## 📋 Peta Langkah-demi-Langkah

### Langkah 1 — Operator Aritmatika (Hitung-Menghitung)

Digunakan untuk operasi matematika dasar:

| Operator | Nama | Contoh | Hasil |
|:---:|---|---|---|
| `+` | Tambah | `10 + 3` | `13` |
| `-` | Kurang | `10 - 3` | `7` |
| `*` | Kali | `10 * 3` | `30` |
| `/` | Bagi | `10 / 3` | `3` *(buang desimal jika keduanya `int`)* |
| `%` | Modulus (sisa bagi) | `10 % 3` | `1` |

> 💡 **Operator `%` (Modulus)** adalah yang paling sering bingung. Cara baca: "10 dibagi 3, **sisa berapa?**". Jawabannya `1` karena `3 × 3 = 9`, sisa `1`. Berguna untuk cek bilangan genap/ganjil!

---

### Langkah 2 — Operator Penugasan (Assignment)

Digunakan untuk memberi atau mengubah nilai variabel:

| Operator | Arti | Contoh Panjang | Contoh Singkat |
|:---:|---|---|---|
| `=` | Simpan nilai | `x = 5;` | — |
| `+=` | Tambah lalu simpan | `x = x + 3;` | `x += 3;` |
| `-=` | Kurang lalu simpan | `x = x - 3;` | `x -= 3;` |
| `*=` | Kali lalu simpan | `x = x * 3;` | `x *= 3;` |
| `/=` | Bagi lalu simpan | `x = x / 3;` | `x /= 3;` |
| `%=` | Modulus lalu simpan | `x = x % 3;` | `x %= 3;` |

---

### Langkah 3 — Operator Increment & Decrement

Cara cepat menambah atau mengurangi **1**:

| Operator | Arti | Sama Dengan |
|:---:|---|---|
| `x++` | Tambah 1 setelah dipakai | `x = x + 1;` |
| `++x` | Tambah 1 sebelum dipakai | `x = x + 1;` |
| `x--` | Kurang 1 setelah dipakai | `x = x - 1;` |
| `--x` | Kurang 1 sebelum dipakai | `x = x - 1;` |

> **Perbedaan `x++` vs `++x`** — ini sering jadi soal ujian!

```java
int a = 5;
System.out.println(a++); // cetak 5 DULU, baru tambah → a jadi 6
System.out.println(a);   // sekarang a sudah 6

int b = 5;
System.out.println(++b); // tambah DULU jadi 6, baru cetak → tampil 6
System.out.println(b);   // b tetap 6
```

---

### Langkah 4 — Operator Perbandingan (Comparison)

Hasilnya selalu **`true` atau `false`** (tipe `boolean`). Digunakan untuk membandingkan dua nilai:

| Operator | Arti | Contoh | Hasil |
|:---:|---|---|---|
| `==` | Sama dengan | `5 == 5` | `true` |
| `!=` | Tidak sama dengan | `5 != 3` | `true` |
| `>` | Lebih besar | `5 > 3` | `true` |
| `<` | Lebih kecil | `5 < 3` | `false` |
| `>=` | Lebih besar atau sama | `5 >= 5` | `true` |
| `<=` | Lebih kecil atau sama | `3 <= 5` | `true` |

> ⚠️ **Jangan tertukar!**
> - `=` → **menyimpan nilai** ke variabel (`x = 5`)
> - `==` → **membandingkan** apakah dua nilai sama (`x == 5`)

---

### Langkah 5 — Operator Logika (Logical)

Menggabungkan **dua kondisi** sekaligus. Hasilnya selalu `true` atau `false`:

| Operator | Nama | Arti | Contoh | Hasil |
|:---:|---|---|---|---|
| `&&` | AND | Benar jika **keduanya** benar | `(5 > 3) && (10 > 7)` | `true` |
| `\|\|` | OR | Benar jika **salah satu** benar | `(5 > 3) \|\| (2 > 10)` | `true` |
| `!` | NOT | Membalik nilai boolean | `!(5 > 3)` | `false` |

**Tabel kebenaran `&&` (AND):**

| Kondisi A | Kondisi B | A `&&` B |
|:---:|:---:|:---:|
| `true` | `true` | `true` ✅ |
| `true` | `false` | `false` ❌ |
| `false` | `true` | `false` ❌ |
| `false` | `false` | `false` ❌ |

**Tabel kebenaran `||` (OR):**

| Kondisi A | Kondisi B | A `\|\|` B |
|:---:|:---:|:---:|
| `true` | `true` | `true` ✅ |
| `true` | `false` | `true` ✅ |
| `false` | `true` | `true` ✅ |
| `false` | `false` | `false` ❌ |

---

### Langkah 6 — Urutan Prioritas Operator (Seperti Matematika)

Java menghitung operator dengan urutan prioritas ini (dari tinggi ke rendah):

| Prioritas | Operator | Nama |
|:---:|---|---|
| 1 (Tertinggi) | `++`, `--`, `!` | Unary / increment / NOT |
| 2 | `*`, `/`, `%` | Perkalian, pembagian, modulus |
| 3 | `+`, `-` | Penjumlahan, pengurangan |
| 4 | `>`, `<`, `>=`, `<=` | Perbandingan |
| 5 | `==`, `!=` | Kesamaan |
| 6 | `&&` | AND |
| 7 (Terendah) | `\|\|` | OR |

> **Sama seperti matematika**: `2 + 3 * 4` = `2 + 12` = `14`, bukan `20`. Gunakan `()` kalau mau ubah urutan.

---

## 📊 Tabel Jejak Eksekusi — Program Kalkulator Sederhana

```java
public class KalkulatorOperator {
    public static void main(String[] args) {
        int a = 10;
        int b = 3;
        int hasil;

        hasil = a + b;
        hasil = a % b;
        boolean cek = (a > b) && (b != 0);
    }
}
```

| Step | Baris Kode | Nilai Variabel Setelah Baris Ini | Keterangan |
|:-----|:-----------|:---------------------------------|:-----------|
| 1 | `int a = 10;` | `a=10` | Simpan 10 di rak `a` |
| 2 | `int b = 3;` | `a=10`, `b=3` | Simpan 3 di rak `b` |
| 3 | `int hasil;` | `a=10`, `b=3`, `hasil=?` | Rak `hasil` dibuat tapi kosong |
| 4 | `hasil = a + b;` | `a=10`, `b=3`, `hasil=13` | `10 + 3 = 13` disimpan ke `hasil` |
| 5 | `hasil = a % b;` | `a=10`, `b=3`, `hasil=1` | `10 % 3 = 1` (sisa bagi), **menimpa** nilai lama `13` |
| 6 | `boolean cek = (a > b) && (b != 0);` | `cek=true` | `(10>3)=true` AND `(3≠0)=true` → `true && true = true` |

---

## 💻 Kode Contoh Java — Siap Jalan di JDK 21

```java
// File: ContohOperator.java

public class ContohOperator {

    public static void main(String[] args) {

        // === OPERATOR ARITMATIKA ===
        int a = 17;
        int b = 5;

        System.out.println("=== ARITMATIKA ===");
        System.out.println("a + b = " + (a + b));   // 22
        System.out.println("a - b = " + (a - b));   // 12
        System.out.println("a * b = " + (a * b));   // 85
        System.out.println("a / b = " + (a / b));   // 3 (bukan 3.4!)
        System.out.println("a % b = " + (a % b));   // 2 (sisa bagi)

        // === OPERATOR PENUGASAN ===
        System.out.println("\n=== PENUGASAN ===");
        int skor = 100;
        System.out.println("Skor awal : " + skor);  // 100
        skor -= 20;     // skor = skor - 20
        System.out.println("Setelah -= 20 : " + skor); // 80
        skor *= 2;      // skor = skor * 2
        System.out.println("Setelah *= 2  : " + skor); // 160

        // === INCREMENT & DECREMENT ===
        System.out.println("\n=== INCREMENT ===");
        int nyawa = 3;
        System.out.println("Nyawa awal : " + nyawa);    // 3
        nyawa++;
        System.out.println("Setelah ++ : " + nyawa);    // 4
        nyawa--;
        System.out.println("Setelah -- : " + nyawa);    // 3

        // === OPERATOR PERBANDINGAN ===
        System.out.println("\n=== PERBANDINGAN ===");
        int nilai = 75;
        System.out.println("nilai == 75 : " + (nilai == 75));  // true
        System.out.println("nilai > 80  : " + (nilai > 80));   // false
        System.out.println("nilai >= 75 : " + (nilai >= 75));  // true
        System.out.println("nilai != 60 : " + (nilai != 60));  // true

        // === OPERATOR LOGIKA ===
        System.out.println("\n=== LOGIKA ===");
        boolean sudahMakan = true;
        boolean sudahMinum = false;
        System.out.println("Makan && Minum : " + (sudahMakan && sudahMinum)); // false
        System.out.println("Makan || Minum : " + (sudahMakan || sudahMinum)); // true
        System.out.println("!sudahMakan    : " + (!sudahMakan));               // false

        // === CONTOH NYATA: CEK BILANGAN GENAP ===
        System.out.println("\n=== CEK GENAP/GANJIL ===");
        int angka = 28;
        boolean isGenap = (angka % 2 == 0); // sisa bagi 2 = 0 → genap
        System.out.println(angka + " adalah genap: " + isGenap); // true
    }
}
```

**Output yang diharapkan:**
```
=== ARITMATIKA ===
a + b = 22
a - b = 12
a * b = 85
a / b = 3
a % b = 2

=== PENUGASAN ===
Skor awal : 100
Setelah -= 20 : 80
Setelah *= 2  : 160

=== INCREMENT ===
Nyawa awal : 3
Setelah ++ : 4
Setelah -- : 3

=== PERBANDINGAN ===
nilai == 75 : true
nilai > 80  : false
nilai >= 75 : true
nilai != 60 : true

=== LOGIKA ===
Makan && Minum : false
Makan || Minum : true
!sudahMakan    : false

=== CEK GENAP/GANJIL ===
28 adalah genap: true
```

---

## ⚠️ Jebakan Paling Umum di Bab 3

| Jebakan | Contoh Salah | Benar | Penjelasan |
|---------|-------------|-------|-----------|
| Pakai `=` untuk perbandingan | `if (x = 5)` | `if (x == 5)` | `=` adalah assignment, `==` adalah perbandingan |
| Lupa `int/int` buang desimal | `int x = 7/2;` → `3` | `double x = 7.0/2;` → `3.5` | Salah satu harus `double` |
| `&&` vs `\|\|` tertukar | — | Hapal: AND = **keduanya** harus benar | OR = **cukup satu** yang benar |
| Urutan tanpa kurung | `"Hasil: " + 2 + 3` → `"Hasil: 23"` | `"Hasil: " + (2 + 3)` → `"Hasil: 5"` | Selalu kurung operasi aritmatika dalam `println` |

---

## 🧩 Kuis Mini Interaktif — Bab 3

Jawab di [`03_Jawaban_Kuis/Kuis_Bab_03.md`](../03_Jawaban_Kuis/Kuis_Bab_03.md)!

---

### Soal 1 — Pilihan Ganda

Apa hasil dari ekspresi berikut?
```java
int x = 10;
int y = 3;
System.out.println(x % y);
```

- A) `3`
- B) `3.33`
- C) `1`
- D) `0`

---

### Soal 2 — Jejak Eksekusi

Lengkapi tabel untuk program berikut:

```java
public class TraceOperator {
    public static void main(String[] args) {
        int skor = 50;
        skor += 30;
        skor *= 2;
        skor -= 20;
        skor++;
        System.out.println(skor);
    }
}
```

| Step | Operasi | Nilai `skor` Setelahnya |
|:-----|:--------|:-----------------------|
| 1 | `int skor = 50;` | ??? |
| 2 | `skor += 30;` | ??? |
| 3 | `skor *= 2;` | ??? |
| 4 | `skor -= 20;` | ??? |
| 5 | `skor++;` | ??? |
| 6 | `println` mencetak | ??? |

---

### Soal 3 — Prediksi Output Logika

Tentukan hasil **`true` atau `false`** untuk setiap ekspresi:

```java
int a = 8;
int b = 3;
int c = 8;
```

| Ekspresi | Prediksi (`true` / `false`) |
|:---------|:---------------------------|
| `a == c` | ??? |
| `a != b` | ??? |
| `a > b && b > 0` | ??? |
| `a < b \|\| c == 8` | ??? |
| `!(a == b)` | ??? |
| `a >= c && b <= 2` | ??? |

---

### Soal 4 — Coding Mini

Buat program `CekKelayakan.java` yang:
1. Menyimpan variabel `int umur = 17` dan `boolean punyaKTP = false`
2. Menggunakan **operator logika** untuk mengecek apakah seseorang **layak memilih** (syarat: umur ≥ 17 **DAN** punya KTP)
3. Mencetak hasilnya:

```
Umur      : 17
Punya KTP : false
Layak Memilih : false
```

> **Petunjuk**: Simpan hasil pengecekan di variabel `boolean layakMemilih = ...`

---

## 📌 Ringkasan Bab 3

- ✅ **Aritmatika**: `+` `-` `*` `/` `%` — `%` untuk sisa bagi
- ✅ **Penugasan**: `+=` `-=` `*=` dll. — cara singkat ubah nilai variabel
- ✅ **Increment/Decrement**: `x++` / `x--` — tambah atau kurang 1
- ✅ **Perbandingan**: hasilnya selalu `true`/`false` — jangan tukar `=` dan `==`
- ✅ **Logika**: `&&` (keduanya benar), `||` (salah satu benar), `!` (balik nilai)
- ✅ **Prioritas**: `*` `/` `%` lebih dulu dari `+` `-` — gunakan `()` untuk kejelasan

---

> **Langkah selanjutnya**: Setelah kuis selesai, kita masuk ke **[Bab 4 — Percabangan](Bab_04_Percabangan.md)** — di sinilah program mulai bisa "berpikir" dan ambil keputusan! 🚀
