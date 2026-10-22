---
icon: "📝"
sticker: "📝"
color: "#f59e0b"
tags:
  - php
  - kuis
  - fase-1
---

# 📝 Lembar Jawaban Kuis — Bab 1: Pengenalan PHP & Program Pertama

> **Petunjuk**: Tuliskan jawabanmu pada bagian yang telah disediakan di bawah ini. Setelah selesai, beri tahu tutormu di chat agar kuis ini dapat diperiksa dan dinilai!

---

## Soal 1 — Pilihan Ganda (10 poin)
*Apa yang terjadi jika kamu lupa menuliskan tag `<?php` pada baris pertama berkas PHP?*
- **A)** Program langsung menampilkan error merah di terminal.
- **B)** Teks kode akan dicetak mentah begitu saja ke terminal tanpa dieksekusi sebagai program.
- **C)** Komputer otomatis memperbaikinya dan program tetap berjalan normal.
- **D)** Komputer mati mendadak.

**Pilihan Jawaban (A/B/C/D)**:
```text
A. Program langsung menampilkan error merah di terminal
```

---

## Soal 2 — Jejak Eksekusi (25 poin)
*Perhatikan potongan kode berikut:*
```php
<?php
echo "Langkah Satu\n";
echo "Langkah " . "Dua\n";
```

*Lengkapi tabel jejak eksekusi berikut sesuai yang terjadi pada terminal:*

| Step  | Baris Kode                   | Efek / Tampilan Output di Terminal                                                |
| :---: | :--------------------------- | :-------------------------------------------------------------------------------- |
| **1** | `<?php`                      | tidak ada output cuman hanya untuk menandakan bahwa filenya meruppppakan file php |
| **2** | `echo "Langkah Satu\n";`     | Langkah Satu                                                                      |
| **3** | `echo "Langkah " . "Dua\n";` | Langkah Dua                                                                       |

---

## Soal 3 — Temukan Bug & Perbaikan (30 poin)
*Perhatikan kode berikut yang mengalami error:*
```php
<?php
echo "Saya siap belajar PHP"
echo Laravel . " Mantap!\n";
```

**Daftar Bug yang Ditemukan**:
1. echo "Saya siap belajar PHP" ada titik coma
2. echo Laravel . " Mantap!\n"; laravelnya tidak menggunakan kutip

**Kode Perbaikan (Executable)**:
```php
<?php
echo "Saya siap belajar PHP";
echo "Laravel" . " Mantap!\n";
```

---

## Soal 4 — Coding Mini (35 poin)
*Buat program PHP mandiri bernama `perkenalan.php` yang ketika dijalankan di terminal menampilkan:*
1. *Nama panggilanmu.*
2. *Targetmu: Belajar PHP dari nol untuk persiapan framework Laravel.*
3. *Ide aplikasi web yang ingin kamu buat setelah menguasai Laravel.*

**Kode Program Kamu**:
```php
<?php
echo "Angga";
echo "Target : Belajar PHP dari nol untuk persiapan framework Laravel";
echo "Ide aplikasi web yang ingin kamu buat setelah menguasai Laravel";
```

---

## 💬 Catatan / Pertanyaan Tambahan:
*(Jika ada bagian materi yang terasa membingungkan atau ingin ditanyakan ke tutor, tuliskan di sini!)*
