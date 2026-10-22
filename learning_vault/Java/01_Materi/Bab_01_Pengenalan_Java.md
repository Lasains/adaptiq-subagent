# 📚 Bab 1 — Pengenalan Java & Program Pertama

> **Level**: Pemula Murni (Zero-Knowledge) | **Fase**: 1 dari 4 | **Estimasi Waktu**: 45–60 menit

---

## 💡 Konsep Utama

Java adalah bahasa pemrograman yang memberikan **instruksi kepada komputer**. Setiap instruksi ditulis dengan aturan baku yang disebut **sintaksis**. Komputer tidak bisa menebak — setiap perintah harus ditulis tepat.

Java banyak dipakai untuk membuat aplikasi Android, server, dan sistem besar. Kita belajar Java murni dulu agar nanti bisa mengerti Android dengan benar.

---

## 🔧 Analogi Mekanis Dunia Nyata

Bayangkan kamu adalah **mandor pabrik**. Kamu punya cetak biru mesin (= `class`), tombol start mesin (= `main`), dan perintah kerja spesifik (= `System.out.println`).

Tapi karena kita belajar untuk **afantasia** dan **zero-knowledge**, kita gunakan tabel konkret, bukan imajinasi:

| Elemen Nyata | Padanan di Java | Peran |
|---|---|---|
| **Nama pabrik / gedung** | `class NamaPabrik` | Wadah semua kode |
| **Tombol ON / pintu masuk** | `public static void main(String[] args)` | Titik awal program berjalan |
| **Perintah cetak ke layar** | `System.out.println("...")` | Menampilkan teks di konsol |

---

## 📋 Peta Langkah-demi-Langkah

### Langkah 1 — Kenali Struktur Dasar Java

Setiap program Java **wajib** punya 3 bagian ini:

1. **`class`** → Nama file & wadah program (harus sama dengan nama file `.java`)
2. **`main`** → Pintu masuk — komputer mulai membaca kode dari sini
3. **`System.out.println`** → Perintah mencetak teks ke layar

### Langkah 2 — Aturan Penulisan Penting

- Nama `class` **harus huruf kapital di awal**: `HelloWorld` ✅ | `helloWorld` ❌
- Setiap perintah diakhiri **titik koma** `;`
- Tanda kurung kurawal `{` dan `}` harus selalu **berpasangan**
- Java **case-sensitive**: `System` ≠ `system`

### Langkah 3 — Cara Menjalankan Program Java

```
Tulis kode (.java) ──► Kompilasi (javac) ──► Jalankan (java)
```

Atau gunakan IDE seperti IntelliJ IDEA / VS Code yang mengerjakan langkah ini otomatis.

---

## 📊 Tabel Jejak Eksekusi — Program Hello World

Program di bawah dieksekusi baris per baris oleh JVM (Java Virtual Machine):

| Step | Baris Kode | Yang Terjadi | Output |
|:-----|:-----------|:-------------|:-------|
| 1 | `public class HelloWorld {` | JVM mengenali nama class = `HelloWorld` | *(tidak ada output)* |
| 2 | `public static void main(String[] args) {` | JVM menemukan pintu masuk → mulai eksekusi | *(tidak ada output)* |
| 3 | `System.out.println("Halo, Dunia!");` | JVM mencetak teks ke layar konsol | `Halo, Dunia!` |
| 4 | `}` (penutup main) | Blok `main` selesai | *(tidak ada output)* |
| 5 | `}` (penutup class) | Seluruh program selesai, JVM berhenti | *(tidak ada output)* |

---

## 💻 Kode Contoh Java — Siap Jalan di JDK 21

```java
// File: HelloWorld.java
// Nama file HARUS sama persis dengan nama class (termasuk huruf besar/kecil)

public class HelloWorld {

    // main adalah pintu masuk — program selalu mulai dari sini
    public static void main(String[] args) {

        // System.out.println = perintah cetak satu baris ke konsol
        System.out.println("Halo, Dunia!");

        // println (dengan ln) otomatis pindah baris setelah mencetak
        System.out.println("Selamat datang di Java!");

        // print (tanpa ln) TIDAK pindah baris
        System.out.print("Ini ");
        System.out.print("disambung.");

    } // akhir main

} // akhir class HelloWorld
```

**Output yang diharapkan:**
```
Halo, Dunia!
Selamat datang di Java!
Ini disambung.
```

---

## 🔍 Bedah Sintaksis — Baris per Baris

| Kode | Arti Sederhana |
|------|----------------|
| `public` | "Bisa diakses dari mana saja" |
| `class HelloWorld` | "Buat wadah bernama HelloWorld" |
| `static` | "Bisa dijalankan langsung tanpa membuat objek dulu" |
| `void` | "Method ini tidak mengembalikan nilai apapun" |
| `main` | "Nama khusus — pintu masuk program" |
| `String[] args` | "Bisa menerima teks dari luar saat program dijalankan" |
| `System.out.println(...)` | `System` = sistem komputer, `out` = keluaran, `println` = cetak baris |

---

## ⚠️ Kesalahan Paling Umum Pemula

| Kesalahan | Contoh Salah | Contoh Benar |
|-----------|-------------|--------------|
| Lupa titik koma `;` | `System.out.println("Hi")` | `System.out.println("Hi");` |
| Nama class ≠ nama file | File: `helloworld.java`, Class: `HelloWorld` | File: `HelloWorld.java`, Class: `HelloWorld` |
| Salah kapitalisasi | `system.out.Println(...)` | `System.out.println(...)` |
| Tanda kutip tidak ditutup | `System.out.println("Halo)` | `System.out.println("Halo")` |

---

## 🧩 Kuis Mini Interaktif — Bab 1

Jawab dulu sebelum lanjut ke Bab 2! Tulis jawabanmu di `03_Jawaban_Kuis/Kuis_Bab_01.md`.

---

### Soal 1 — Pilihan Ganda
Manakah struktur program Java yang **benar**?

- A) `class HelloWorld { main { System.out.println("Hi"); } }`
- B) `public class HelloWorld { public static void main(String[] args) { System.out.println("Hi"); } }`
- C) `Public Class HelloWorld { Public Static Void Main() { system.out.println("Hi"); } }`
- D) `class helloWorld { void main() { System.out.println("Hi") } }`

---

### Soal 2 — Jejak Eksekusi (Trace)

Perhatikan kode berikut:

```java
public class Latihan {
    public static void main(String[] args) {
        System.out.println("Satu");
        System.out.print("Dua ");
        System.out.print("Tiga");
        System.out.println("!");
        System.out.println("Selesai");
    }
}
```

Lengkapi tabel jejak eksekusi ini:

| Step | Baris yang Dieksekusi | Output di Konsol |
|:-----|:----------------------|:-----------------|
| 1 | `System.out.println("Satu");` | ??? |
| 2 | `System.out.print("Dua ");` | ??? |
| 3 | `System.out.print("Tiga");` | ??? |
| 4 | `System.out.println("!");` | ??? |
| 5 | `System.out.println("Selesai");` | ??? |

**Pertanyaan bonus**: Berapa total baris teks yang muncul di konsol?

---

### Soal 3 — Temukan Bug

Kode berikut memiliki **2 kesalahan**. Temukan dan perbaiki!

```java
public class buggy {
    public static void main(String[] args) {
        System.out.println("Program mulai")
        System.out.println("Program selesai");
    }
}
```

---

## 📌 Ringkasan Bab 1

- ✅ Program Java dimulai dari `class`, lalu `main`, lalu perintah-perintah di dalamnya
- ✅ `System.out.println` = cetak + pindah baris | `System.out.print` = cetak tanpa pindah baris
- ✅ Setiap perintah diakhiri `;`
- ✅ Java case-sensitive — huruf besar/kecil sangat penting
- ✅ Nama file `.java` harus sama persis dengan nama `class`

---

> **Langkah selanjutnya**: Setelah kamu mengerjakan kuis di atas dan menyimpan jawabannya di `03_Jawaban_Kuis/Kuis_Bab_01.md`, kabari tutormu! Kita akan lanjut ke **[Bab 2 — Variabel & Tipe Data](Bab_02_Variabel_dan_Tipe_Data.md)** 🚀
