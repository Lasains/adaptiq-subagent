# 📚 Bab 4 — Percabangan (`if`, `else`, `switch`)

> **Level**: Pemula Murni (Zero-Knowledge) | **Fase**: 1 dari 4 | **Prasyarat**: Bab 1 ✅ Bab 2 ✅ Bab 3 ✅ | **Estimasi Waktu**: 60–75 menit

---

## 💡 Konsep Utama

**Percabangan** membuat program bisa **mengambil keputusan**. Tanpa percabangan, program selalu menjalankan semua baris dari atas ke bawah tanpa pengecualian.

Dengan percabangan, program bisa berkata: **"Jika kondisi ini benar, jalankan kode ini. Kalau tidak, jalankan kode yang lain."**

---

## 🔧 Analogi Mekanis Dunia Nyata

Bayangkan **palang pintu tol otomatis**:

| Situasi Nyata | Padanan di Java |
|---|---|
| Sensor baca plat nomor | Kondisi yang dicek (`if`) |
| Plat terdaftar → palang buka | Blok kode yang dijalankan jika `true` |
| Plat tidak terdaftar → palang tetap tutup | Blok `else` yang dijalankan jika `false` |
| Ada banyak kategori kendaraan (motor/mobil/truk) | `if - else if - else` atau `switch` |

---

## 📋 Peta Langkah-demi-Langkah

### Langkah 1 — `if` Sederhana

Blok `if` dijalankan **hanya jika kondisinya `true`**. Jika `false`, dilewati begitu saja.

```
if (kondisi) {
    // kode ini dijalankan HANYA jika kondisi = true
}
```

Contoh:
```java
int nilai = 80;

if (nilai >= 75) {
    System.out.println("Selamat, kamu lulus!");
}
// Jika nilai < 75, baris println di atas dilewati tanpa dijalankan
```

---

### Langkah 2 — `if - else`

Tambahkan `else` untuk menangani kondisi `false`:

```
if (kondisi) {
    // dijalankan jika kondisi = true
} else {
    // dijalankan jika kondisi = false
}
```

Contoh:
```java
int nilai = 60;

if (nilai >= 75) {
    System.out.println("Lulus");
} else {
    System.out.println("Tidak lulus");
}
```

> **Aturan penting**: Hanya **satu** blok yang dijalankan — `if` atau `else`, tidak pernah keduanya sekaligus.

---

### Langkah 3 — `if - else if - else` (Banyak Kondisi)

Untuk mengecek lebih dari dua kemungkinan:

```
if (kondisi1) {
    // dijalankan jika kondisi1 = true
} else if (kondisi2) {
    // dijalankan jika kondisi1 = false, kondisi2 = true
} else if (kondisi3) {
    // dijalankan jika kondisi1 dan 2 = false, kondisi3 = true
} else {
    // dijalankan jika SEMUA kondisi di atas = false
}
```

> **Penting**: Java mengecek kondisi **dari atas ke bawah**. Begitu satu kondisi `true`, bloknya dijalankan dan **sisanya dilewati semua**.

---

### Langkah 4 — `switch` (Untuk Nilai Spesifik)

`switch` cocok digunakan ketika kamu mengecek **satu variabel dengan banyak nilai yang mungkin**. Lebih rapi dibanding banyak `else if`.

```
switch (variabel) {
    case nilai1:
        // kode jika variabel == nilai1
        break;
    case nilai2:
        // kode jika variabel == nilai2
        break;
    default:
        // kode jika tidak ada case yang cocok
}
```

> ⚠️ **Jangan lupa `break`!** Tanpa `break`, Java terus mengeksekusi semua `case` di bawahnya (*fall-through*) — ini sering jadi sumber bug!

---

### Langkah 5 — `if` di Dalam `if` (Nested)

`if` bisa diletakkan di dalam `if` lain. Disebut **nested if**:

```java
if (sudahDaftar) {
    if (umur >= 17) {
        System.out.println("Boleh masuk");
    } else {
        System.out.println("Umur belum cukup");
    }
} else {
    System.out.println("Belum terdaftar");
}
```

> 💡 Gunakan nested `if` dengan hemat — terlalu banyak level membuat kode sulit dibaca. Jika bisa, gabungkan kondisi dengan `&&` atau `||`.

---

## 📊 Tabel Jejak Eksekusi — Program Nilai Rapor

```java
public class NilaiRapor {
    public static void main(String[] args) {
        int nilai = 82;

        if (nilai >= 90) {
            System.out.println("A");
        } else if (nilai >= 80) {
            System.out.println("B");
        } else if (nilai >= 70) {
            System.out.println("C");
        } else {
            System.out.println("D");
        }
    }
}
```

| Step | Baris yang Dievaluasi | Hasil Evaluasi | Yang Terjadi |
|:-----|:----------------------|:--------------:|:-------------|
| 1 | `int nilai = 82;` | — | `nilai` disimpan sebagai `82` |
| 2 | `if (nilai >= 90)` | `82 >= 90` = **`false`** | Blok `"A"` **dilewati** |
| 3 | `else if (nilai >= 80)` | `82 >= 80` = **`true`** | Blok `"B"` **dijalankan** → cetak `B` |
| 4 | `else if (nilai >= 70)` | **Tidak dicek** | Sudah ada yang `true` di atas → semua sisa dilewati |
| 5 | `else` | **Tidak dicek** | Dilewati |

**Output**: `B`

---

## 📊 Tabel Jejak Eksekusi — `switch`

```java
public class HariKerja {
    public static void main(String[] args) {
        int hari = 3;

        switch (hari) {
            case 1: System.out.println("Senin"); break;
            case 2: System.out.println("Selasa"); break;
            case 3: System.out.println("Rabu"); break;
            default: System.out.println("Hari lain");
        }
    }
}
```

| Step | Yang Dicek | Cocok? | Yang Terjadi |
|:-----|:-----------|:------:|:-------------|
| 1 | `hari = 3` | — | Nilai variabel adalah `3` |
| 2 | `case 1:` | `3 == 1` = **Tidak** | Dilewati |
| 3 | `case 2:` | `3 == 2` = **Tidak** | Dilewati |
| 4 | `case 3:` | `3 == 3` = **Ya** ✅ | Cetak `"Rabu"`, lalu `break` → keluar switch |
| 5 | `default:` | **Tidak dicek** | Sudah `break` sebelumnya |

**Output**: `Rabu`

---

## 💻 Kode Contoh Java — Siap Jalan di JDK 21

```java
// File: ContohPercabangan.java

public class ContohPercabangan {

    public static void main(String[] args) {

        // === CONTOH 1: if - else if - else ===
        System.out.println("=== NILAI RAPOR ===");
        int nilai = 78;

        if (nilai >= 90) {
            System.out.println("Grade A — Sangat Baik");
        } else if (nilai >= 80) {
            System.out.println("Grade B — Baik");
        } else if (nilai >= 70) {
            System.out.println("Grade C — Cukup");
        } else if (nilai >= 60) {
            System.out.println("Grade D — Kurang");
        } else {
            System.out.println("Grade E — Tidak Lulus");
        }

        // === CONTOH 2: if dengan operator logika ===
        System.out.println("\n=== CEK SYARAT BEASISWA ===");
        double ipk = 3.75;
        boolean aktifOrganisasi = true;

        if (ipk >= 3.5 && aktifOrganisasi) {
            System.out.println("Selamat! Kamu memenuhi syarat beasiswa.");
        } else if (ipk >= 3.5) {
            System.out.println("IPK cukup, tapi harus aktif di organisasi.");
        } else {
            System.out.println("IPK belum memenuhi syarat minimum 3.5");
        }

        // === CONTOH 3: switch ===
        System.out.println("\n=== JADWAL PELAJARAN ===");
        int hariKe = 2; // 1=Senin, 2=Selasa, dst.

        switch (hariKe) {
            case 1:
                System.out.println("Senin: Matematika & Fisika");
                break;
            case 2:
                System.out.println("Selasa: Bahasa Indonesia & Sejarah");
                break;
            case 3:
                System.out.println("Rabu: Kimia & Biologi");
                break;
            case 4:
                System.out.println("Kamis: Bahasa Inggris & Seni");
                break;
            case 5:
                System.out.println("Jumat: Olahraga & Prakarya");
                break;
            default:
                System.out.println("Akhir pekan — tidak ada pelajaran!");
        }

        // === CONTOH 4: Nested if ===
        System.out.println("\n=== CEK AKSES SISTEM ===");
        boolean sudahLogin = true;
        String role = "admin";

        if (sudahLogin) {
            if (role.equals("admin")) {
                System.out.println("Akses penuh ke semua menu.");
            } else if (role.equals("user")) {
                System.out.println("Akses terbatas — menu user saja.");
            } else {
                System.out.println("Role tidak dikenal.");
            }
        } else {
            System.out.println("Harap login terlebih dahulu.");
        }
    }
}
```

**Output yang diharapkan:**
```
=== NILAI RAPOR ===
Grade C — Cukup

=== CEK SYARAT BEASISWA ===
Selamat! Kamu memenuhi syarat beasiswa.

=== JADWAL PELAJARAN ===
Selasa: Bahasa Indonesia & Sejarah

=== CEK AKSES SISTEM ===
Akses penuh ke semua menu.
```

---

## 🔍 Perbedaan `if-else if` vs `switch` — Kapan Pakai Yang Mana?

| Situasi | Gunakan |
|---------|---------|
| Kondisi melibatkan **rentang nilai** (`>= 80`, `< 60`) | `if - else if` |
| Kondisi melibatkan **operator logika** (`&&`, `\|\|`) | `if - else if` |
| Mengecek **satu variabel** dengan **nilai-nilai spesifik** (`1`, `2`, `"admin"`) | `switch` |
| Banyak kemungkinan nilai dan ingin kode lebih rapi | `switch` |

---

## ⚠️ Jebakan Paling Umum di Bab 4

| Jebakan                            | Contoh Salah                          | Penjelasan                                                      |
| ---------------------------------- | ------------------------------------- | --------------------------------------------------------------- |
| Lupa `break` di `switch`           | `case 1: println("A");` tanpa `break` | Program terus ke `case 2`, `3`, dst. sampai ada `break`         |
| Pakai `=` bukan `==`               | `if (nilai = 90)`                     | `=` adalah penugasan, bukan perbandingan — gunakan `==`         |
| Urutan `else if` terbalik          | Cek `>= 60` sebelum `>= 80`           | Kondisi pertama yang `true` selalu menang — urutan penting!     |
| Membandingkan `String` dengan `==` | `if (nama == "Budi")`                 | Untuk `String`, gunakan `.equals()`: `if (nama.equals("Budi"))` |

---

## 🧩 Kuis Mini Interaktif — Bab 4

Jawab di [`03_Jawaban_Kuis/Kuis_Bab_04.md`](../03_Jawaban_Kuis/Kuis_Bab_04.md)!

---

### Soal 1 — Pilihan Ganda

Perhatikan kode berikut:

```java
int x = 75;

if (x >= 80) {
    System.out.println("Baik");
} else if (x >= 70) {
    System.out.println("Cukup");
} else if (x >= 60) {
    System.out.println("Kurang");
} else {
    System.out.println("Gagal");
}
```

Apa yang dicetak?

- A) `Baik`
- B) `Cukup`
- C) `Kurang`
- D) `Gagal`

---

### Soal 2 — Jejak Eksekusi `switch`

Lengkapi tabel untuk program berikut (ingat nilai: `pilihan = 2`):

```java
int pilihan = 2;

switch (pilihan) {
    case 1: System.out.println("Nasi Goreng"); break;
    case 2: System.out.println("Mie Ayam"); break;
    case 3: System.out.println("Soto"); break;
    default: System.out.println("Menu habis");
}
```

| Step | Yang Dicek | Cocok? | Yang Terjadi |
|:-----|:-----------|:------:|:-------------|
| 1 | `case 1:` | ??? | ??? |
| 2 | `case 2:` | ??? | ??? |
| 3 | `case 3:` | ??? | ??? |

**Output akhir program**: ???

---

### Soal 3 — Temukan Bug

Kode berikut ada **2 kesalahan logika/sintaksis**. Temukan dan perbaiki!

```java
public class CekUmur {
    public static void main(String[] args) {
        int umur = 20;

        if (umur >= 13) {
            System.out.println("Remaja atau dewasa");
        } else if (umur >= 18) {
            System.out.println("Dewasa");
        } else {
            System.out.println("Anak-anak");
        }
    }
}
```

---

### Soal 4 — Coding Mini

Buat program `KategoriIMT.java` yang menentukan kategori Indeks Massa Tubuh (IMT):

| Nilai IMT | Kategori |
|-----------|----------|
| IMT < 18.5 | `"Kurus"` |
| 18.5 ≤ IMT < 25.0 | `"Normal"` |
| 25.0 ≤ IMT < 30.0 | `"Gemuk"` |
| IMT ≥ 30.0 | `"Obesitas"` |

**Ketentuan program:**
- Gunakan variabel `double imt = 22.5;` (atau nilai lain pilihanmu)
- Gunakan `if - else if - else`
- Output contoh (untuk imt = 22.5):

```
IMT kamu   : 22.5
Kategori   : Normal
```

---

## 📌 Ringkasan Bab 4

- ✅ `if` — jalankan kode jika kondisi `true`
- ✅ `else` — alternatif jika kondisi `false`
- ✅ `else if` — cek kondisi tambahan secara berurutan dari atas ke bawah
- ✅ `switch` — untuk mengecek satu variabel dengan banyak nilai spesifik, wajib ada `break`
- ✅ Nested `if` — `if` di dalam `if`, gunakan dengan hemat
- ✅ Bandingkan `String` dengan `.equals()`, bukan `==`

---

> **Langkah selanjutnya**: Setelah kuis selesai, kita masuk ke **[Bab 5 — Perulangan](Bab_05_Perulangan.md)** — program yang bisa mengulang pekerjaan ratusan kali hanya dengan beberapa baris kode! 🚀
