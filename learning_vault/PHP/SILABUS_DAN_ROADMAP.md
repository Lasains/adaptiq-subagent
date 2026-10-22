---
icon: "🗺️"
sticker: "🗺️"
color: "#3b82f6"
tags:
  - php
  - roadmap
  - silabus
---

# 🗺️ Silabus & Roadmap Belajar PHP

> **Target Akhir**: 🌐 Web MVC (Persiapan Framework Laravel 11+)
> **Level Awal**: Pemula Murni (*Zero-Knowledge Beginner*)
> **Bahasa & Runtime**: PHP 8.3+ (CLI untuk fondasi, Web & Laravel untuk spesialisasi)
> **Lokasi Vault**: `learning_vault/PHP/`

---

## 🎯 Tujuan Belajar (Dinamis — Diisi Bersama Tutor)

> Tujuan ini diselaraskan oleh tutor berdasarkan tujuan yang kamu sebutkan di awal sesi.

| Bidang                         | Contoh Target                                     | Status          |
| :----------------------------- | :------------------------------------------------ | :-------------- |
| 🌐 Web MVC                     | Laravel 11+, Blade Template, Eloquent ORM         | 🎯 Target Aktif |
| 🔌 RESTful API & Microservices | API Resource, Sanctum Auth, JSON responses        | ⬜ Opsi Lanjutan |
| 🔧 CMS & Plugin                | WordPress/Bedrock, plugin custom, hooks & filters | ⬜ Opsi Lanjutan |
| ⚡ CLI & Otomasi                | Script otomasi, file processor, scraper CLI       | ⬜ Opsi Lanjutan |
| 🏗️ Clean Architecture         | Hexagonal, Repository Pattern, DI Container       | ⬜ Opsi Lanjutan |

**Tujuan Aktif Saat Ini**: 🌐 **Web MVC (Persiapan Framework Laravel 11+)**

---

## 📍 Peta Kemajuan Belajar

```
Fase 1: ✅ Selesai (95%) ──► Fase 2: Fungsi & Struktur Data [Kamu di sini: Ujian Fase 2] ★ ──► Fase 3: OOP Modern ──► Fase 4: Web & Database ──► Fase 5: Web MVC Laravel
```

---

## 🏗️ FASE 1 — Fondasi PHP Murni & Logika Pemrograman (Bab 01–06)
> Sebelum menyentuh browser atau web server, kita bangun cara berpikir logis dulu via CLI.
> Ini seperti belajar mengasah pisau sebelum memasak di dapur restoran.

| Bab | Topik                                                                                                 |  Status   | File Materi                                                         |
| :-: | :---------------------------------------------------------------------------------------------------- | :-------: | :------------------------------------------------------------------ |
| 01  | **Pengenalan PHP & Program Pertama** — Apa itu PHP, cara kerja CLI, `<?php`, `echo`, & Hello World    | ✅ Selesai | [Bab_01_Pengenalan_PHP.md](01_Materi/Bab_01_Pengenalan_PHP.md)      |
| 02  | **Variabel & Tipe Data** — `$nama`, `int`, `string`, `float`, `bool`, cara PHP menyimpan nilai        | ✅ Selesai | [Bab_02_Variabel_Tipe_Data](01_Materi/Bab_02_Variabel_Tipe_Data.md) |
| 03  | **Operator** — Aritmatika, perbandingan, logika, & null coalescing (`??`)                             | ✅ Selesai | [Bab_03_Operator](01_Materi/Bab_03_Operator.md)                     |
| 04  | **Percabangan (`if`, `else`, `match`)** — Program mengambil keputusan berdasarkan kondisi             | ✅ Selesai | [Bab_04_Percabangan.md](01_Materi/Bab_04_Percabangan.md)            |
| 05  | **Perulangan (`for`, `while`, `do-while`)** — Program yang berjalan berulang sampai kondisi terpenuhi | ✅ Selesai | [Bab_05_Perulangan.md](01_Materi/Bab_05_Perulangan.md)              |
| 06  | **Array & Perulangan `foreach`** — Menyimpan banyak data sekaligus & iterasi koleksi                  | ✅ Selesai | [Bab_06_Array_Foreach.md](01_Materi/Bab_06_Array_Foreach.md)        |

### 🎓 Ujian Akhir Fase 1
| Properti | Detail |
| :--- | :--- |
| **Format** | Proyek Mini CLI: Buat program filter & agregasi data dari array |
| **Passing Score** | **70%** |
| **File Soal** | [Ujian_Fase_1.md](04_Ujian_Fase/Ujian_Fase_1.md) |
| **Status** | ✅ **LULUS (95%)** |

---

## 🗃️ FASE 2 — Fungsi, Struktur Data & Penanganan Error (Bab 07–11)

> [!IMPORTANT]
> **Prasyarat**: Lulus Ujian Akhir Fase 1 dengan nilai ≥ 70%. *(Status: Terpenuhi ✅)*

| Bab | Topik                                                                                             |      Status       | File Materi                                                              |
| :-: | :------------------------------------------------------------------------------------------------ | :---------------: | :----------------------------------------------------------------------- |
| 07  | **Fungsi** — Membuat blok kode yang bisa dipanggil ulang, parameter & return value                |     ✅ Selesai     | [Bab_07_Fungsi.md](01_Materi/Bab_07_Fungsi.md)                           |
| 08  | **Array Lanjutan** — Array asosiatif, multidimensi, & fungsi bawaan (`array_map`, `array_filter`) |     ✅ Selesai     | [Bab_08_Array_Lanjutan.md](01_Materi/Bab_08_Array_Lanjutan.md)           |
| 09  | **String & Manipulasi Teks** — Fungsi string penting untuk pengolahan data                        |     ✅ Selesai     | [Bab_09_String_Manipulation.md](01_Materi/Bab_09_String_Manipulation.md) |
| 10  | **Closure & Arrow Function** — Fungsi anonim dan ekspresi `fn() =>` modern                        |    ✅ Selesai     | [Bab_10_Closure_Arrow.md](01_Materi/Bab_10_Closure_Arrow.md)             |
| 11  | **Error & Exception Handling** — `try-catch-finally`, custom exception, & error graceful          |    ✅ Selesai     | [Bab_11_Error_Exception.md](01_Materi/Bab_11_Error_Exception.md)         |

### 🎓 Ujian Akhir Fase 2
| Properti | Detail |
| :--- | :--- |
| **Format** | Buat parser & validator data CSV/JSON sederhana via CLI |
| **Passing Score** | **75%** |
| **File Soal** | [Ujian_Fase_2.md](04_Ujian_Fase/Ujian_Fase_2.md) |
| **Status** | 🔄 **Sedang Dikerjakan** |

---

## 🏛️ FASE 3 — Pemrograman Berorientasi Objek (OOP) Modern (Bab 12–17)

> [!IMPORTANT]
> **Prasyarat**: Lulus Ujian Akhir Fase 2 dengan nilai ≥ 75%.

| Bab | Topik | Status | File Materi |
| :---: | :--- | :---: | :--- |
| 12 | **Class & Object Dasar** — `class`, `new`, `public`/`private`/`protected`, encapsulation | ⬜ Belum | `01_Materi/Bab_12_Class_Object.md` |
| 13 | **Constructor & Property Modern** — Constructor Property Promotion, `readonly` | ⬜ Belum | `01_Materi/Bab_13_Constructor_Readonly.md` |
| 14 | **Inheritance & Komposisi** — Kapan `extends` vs *Composition over Inheritance* | ⬜ Belum | `01_Materi/Bab_14_Inheritance_Komposisi.md` |
| 15 | **Interface & Abstract Class** — Kontrak perilaku & polimorfisme | ⬜ Belum | `01_Materi/Bab_15_Interface_Abstract.md` |
| 16 | **Trait & Enum** — Reusabilitas kode & tipe data enumerasi PHP 8.1+ | ⬜ Belum | `01_Materi/Bab_16_Trait_Enum.md` |
| 17 | **Prinsip SOLID** — 5 prinsip desain kode yang bersih & mudah dikembangkan | ⬜ Belum | `01_Materi/Bab_17_Prinsip_SOLID.md` |

### 🎓 Ujian Akhir Fase 3
| Properti | Detail |
| :--- | :--- |
| **Format** | Rancang sistem OOP mini (contoh: sistem kasir atau manajemen buku) berbasis SOLID |
| **Passing Score** | **75%** |
| **File Soal** | `04_Ujian_Fase/Ujian_Fase_3.md` |
| **Status** | ⬜ Belum dikerjakan |

---

## 🌐 FASE 4 — Web Fundamentals & Database (Bab 18–23)

> [!IMPORTANT]
> **Prasyarat**: Lulus Ujian Akhir Fase 3 dengan nilai ≥ 75%.
> Di fase ini kita baru masuk ke browser! PHP Built-in Server (`php -S localhost:8000`) digunakan — tanpa perlu XAMPP.

| Bab | Topik | Status | File Materi |
| :---: | :--- | :---: | :--- |
| 18 | **Siklus Request HTTP & Superglobals** — Cara browser bicara ke PHP, `$_GET`, `$_POST`, `$_SERVER` | ⬜ Belum | `01_Materi/Bab_18_HTTP_Superglobals.md` |
| 19 | **Form Handling & Validasi** — Menerima input form, sanitasi, & validasi data masuk | ⬜ Belum | `01_Materi/Bab_19_Form_Validasi.md` |
| 20 | **Session & Cookie** — Menyimpan state pengguna antar halaman | ⬜ Belum | `01_Materi/Bab_20_Session_Cookie.md` |
| 21 | **Database dengan PDO** — Koneksi MySQL, query aman dengan Prepared Statements | ⬜ Belum | `01_Materi/Bab_21_Database_PDO.md` |
| 22 | **Keamanan Web Dasar** — SQL Injection, XSS, password hashing `password_hash()` | ⬜ Belum | `01_Materi/Bab_22_Keamanan_Web.md` |
| 23 | **Composer & Autoloading PSR-4** — Manajemen dependensi & struktur proyek modern | ⬜ Belum | `01_Materi/Bab_23_Composer_Autoloading.md` |

### 🎓 Ujian Akhir Fase 4
| Properti | Detail |
| :--- | :--- |
| **Format** | Bangun aplikasi CRUD sederhana (To-Do App / Buku Tamu) dengan PDO & form handling |
| **Passing Score** | **75%** |
| **File Soal** | `04_Ujian_Fase/Ujian_Fase_4.md` |
| **Status** | ⬜ Belum dikerjakan |

---

## 🚀 FASE 5 — Spesialisasi Tujuan Belajar (Bab 24+)

> [!IMPORTANT]
> **Prasyarat**: Lulus Ujian Akhir Fase 4 dengan nilai ≥ 80%.
> Fase ini menyesuaikan dengan **tujuan belajar dinamis** yang kamu pilih di awal.

Konten fase ini akan disesuaikan oleh tutor berdasarkan tujuan belajarmu:

| Jalur | Topik yang Akan Dipelajari |
| :--- | :--- |
| 🌐 **Web MVC (Laravel)** | Routing, Controller, Eloquent ORM, Blade, Middleware, Auth |
| 🔌 **RESTful API** | API Resource, Sanctum, JSON formatting, versioning, rate limiting |
| 🔧 **CMS & Plugin (WordPress)** | Plugin architecture, hooks & filters, Custom Post Types, WP REST API |
| ⚡ **CLI & Otomasi** | Symfony Console, file automation, cron jobs, shell scripting via PHP |
| 🏗️ **Clean Architecture** | Hexagonal, Repository Pattern, DI Container (PSR-11), testing (Pest) |

**Jalur Aktif**: 🌐 **Web MVC (Laravel)**

---

## 📁 Struktur Folder Vault

```
learning_vault/PHP/
├── SILABUS_DAN_ROADMAP.md   ← File ini (peta jalan belajar)
├── REKAP_NILAI.md            ← Catatan skor kuis & ujian
├── 01_Materi/                ← Modul materi tiap bab
├── 02_Catatan_Tanya/         ← Pertanyaanmu tentang materi
├── 03_Jawaban_Kuis/          ← Jawabanmu atas kuis tiap bab
└── 04_Ujian_Fase/            ← Soal ujian akhir tiap fase
```

---

## 🔗 Dokumentasi Resmi & Referensi Belajar (Link Embed)

```embed
title: "PHP: Preface - Manual"
image: "https://www.php.net/images/meta-image.png"
description: "PHP Manual"
url: "https://www.php.net/manual/en/"
favicon: ""
aspectRatio: "62.5"
```

```embed
title: "Installation | Laravel 11.x - The clean stack for Artisans and agents"
image: "https://laravel.com/images/og/laravel-home.png"
description: "Laravel is a framework for building modern web apps and AI agents. Expressive syntax, built-in tools, and everything you need to ship fast."
url: "https://laravel.com/docs/11.x"
favicon: ""
aspectRatio: "52.5"
```

```embed
title: "GitHub - Lasains/adaptiq-subagent"
image: "https://opengraph.githubassets.com/f29c6a453c61ac3f8d6a76b76572c4db2b023064e06f12940d162d5c89d6533f/Lasains/adaptiq-subagent"
description: "Contribute to Lasains/adaptiq-subagent development by creating an account on GitHub."
url: "https://github.com/lasains/adaptiq-subagent"
favicon: ""
aspectRatio: "50"
```
