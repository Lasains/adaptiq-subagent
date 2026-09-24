# Conversational Interview Guide for Vibe PRDs

Panduan ini mengatur ritme, etika, dan penanganan percakapan agar proses pengumpulan kebutuhan terasa menyenangkan, cepat, dan terbebas dari gesekan (*low-friction, high-vibe*).

---

## 1. Prinsip Utama Interaksi

1. **Conversational Pacing (1–2 Topik per Giliran)**: Jangan membombardir pengguna dengan 10 pertanyaan teknis sekaligus dalam satu pesan. Ajukan pertanyaan dalam blok logis bertahap.
2. **Berikan Opsi & Rekomendasi Siap Pakai (Mengurangi Decision Fatigue)**: Pengguna vibe coding ingin bergerak cepat. Selalu sertakan opsi terpopuler (misal: *"Mau pakai Next.js + Tailwind + shadcn/ui atau ada stack favoritmu sendiri?"*).
3. **Validasi & Apresiasi**: Ulangi inti gagasan pengguna secara ringkas sebelum melangkah ke pertanyaan berikutnya untuk memastikan keselarasan pemahaman.
4. **Respon Bilingual Alami**: Cocokkan bahasa respons dengan bahasa pengguna (Bahasa Indonesia atau English) dengan gaya santai rekan *pair-programming*.

---

## 2. Dynamic Conversation Recovery (Penanganan Non-Linear)

Dalam sesi nyata, pengguna sering kali memberikan jawaban yang tidak berurutan. Tangani dengan aturan berikut:

| Situasi Percakapan | Cara Penanganan Agen |
| :--- | :--- |
| **Pengguna Langsung Memberikan Detail Lengkap / PRD Draft** | Jangan tanyakan ulang apa yang sudah dijawab. Lakukan ekstraksi, identifikasi celah (*gap analysis*), dan langsung ajukan konfirmasi ke **Fase 4**. |
| **Pengguna Melompati Fase (e.g. menjawab ide langsung dengan daftar fitur)** | Catat fitur tersebut ke draft Fase 3, lalu mundur secara halus ke pertanyaan tech stack di Fase 2: *"Fitur-fitur itu mantap banget! Biar kita bisa rancang arsitekturnya, kamu mau bangun ini pakai stack apa?"* |
| **Jawaban Ambigu / Terlalu Singkat (e.g. "Terserah kamu aja")** | Jangan tanyakan berulang-ulang. Segera tawarkan Paket 1 (Modern SaaS Vibe) dari `vibe-stacks.md` sebagai rekomendasi default tercepat. |
| **Percakapan Terpotong / Pengguna Kembali Nanti** | Berikan rekap 1 kalimat status terakhir dan lanjutkan dari pertanyaan fase yang tertunda. |

---

## 3. Panduan 5 Fase Wawancara Terpadu

### Fase 1: Deteksi Konteks, Eksplorasi Ide & "The Vibe"
*Tujuan: Memahami apa produknya, siapa penggunanya, dan sensasi visual/estetika yang ingin dihadirkan.*

**Contoh Pertanyaan (ID):**
> "Halo! Keren banget, mari kita rancang PRD untuk proyek vibe coding kamu. Ceritakan sedikit:
> 1. Apa nama dan ide utama produk yang ingin kamu buat?
> 2. Siapa target penggunanya, dan masalah mendesak apa yang diselesaikan?
> 3. Seperti apa 'vibe' atau kesan visual yang kamu bayangkan? (Contoh: *sleek dark mode slate*, *clean minimalist*, *retro cyberpunk*, atau *colorful playful*?)"

**Sample Opening (EN):**
> "Hey there! Let's craft an AI-ready Vibe PRD for your app. Tell me a bit about it:
> 1. What's the project name and core concept?
> 2. Who is the target user and what core pain point are we solving?
> 3. What kind of 'vibe' or visual aesthetic are you envisioning? (e.g., sleek dark mode, clean minimalist, retro cyberpunk, or vibrant modern?)"

---

### Fase 2: Wawancara Tech Stack (Interaktif & 5 Golden Stacks)
*Tujuan: Menentukan lapisan teknologi secara presisi. Jika pengguna belum tahu, tawarkan paket dari `references/vibe-stacks.md`.*

**Contoh Pertanyaan (ID):**
> "Sekarang kita tentukan tech stack yang mau digunakan. Apakah kamu sudah punya preferensi sendiri, atau mau saya rekomendasikan?
> 
> *Tips Cepat*:
> - **SaaS / Web App Lengkap**: Next.js + Tailwind + shadcn/ui + Supabase
> - **Prototype Ultra Cepat**: Vite + React + Tailwind + Supabase
> - **AI / Machine Learning**: Next.js + FastAPI (Python) + Gemini API
> - **Mobile iOS & Android**: React Native (Expo) + NativeWind
> - **Landing Page Cepat**: Astro + Tailwind
> 
> Tertarik pakai salah satu paket di atas, atau punya racikan stack sendiri?"

**Sample Tech Stack Question (EN):**
> "Let's lock in your tech stack. Do you already have a preferred stack, or would you like a curated recommendation?
> 
> *Quick Options*:
> - **Fullstack SaaS**: Next.js + Tailwind + shadcn/ui + Supabase
> - **Ultra-fast Prototype**: Vite + React + Tailwind + Supabase
> - **Python AI / RAG**: Next.js + FastAPI + Gemini API + pgvector
> - **Cross-platform Mobile**: React Native (Expo) + NativeWind
> - **High-speed Content/Landing**: Astro + Tailwind
> 
> Which direction fits your vision best?"

---

### Fase 3: Scope MVP & Anti-Goals ("Jangan Dulu")
*Tujuan: Menetapkan batasan tegas agar proyek selesai cepat dan terhindar dari scope creep.*

**Contoh Pertanyaan (ID):**
> "Biar proses vibe coding kita tetap tajam dan bisa langsung rilis versi demo:
> 1. **P0 (Must-Have)**: Apa 2–3 fitur krusial yang kalau ini jalan, produk sudah layak didemokan?
> 2. **P1 (Nice to Have)**: 1–2 fitur pelengkap yang bisa dikerjakan setelah P0 selesai?
> 3. **Anti-Goals**: Hal apa yang secara tegas **TIDAK PERLU** kita buat di versi awal ini? (Misal: jangan dulu bikin sistem langganan Stripe yang rumit, jangan dulu bikin dashboard multi-tenant, dll.)"

**Sample Scope Question (EN):**
> "To keep our vibe coding focused and hit MVP quickly:
> 1. **P0 (Must-Have)**: What are the 2–3 core features required to make the product functional and demo-ready?
> 2. **P1 (Nice-to-Have)**: 1–2 secondary features we can tackle once P0 is rock solid?
> 3. **Anti-Goals**: What are we strictly **NOT** building in V1? (e.g., no multi-tier billing, no enterprise auth, no native mobile app)."

---

### Fase 4: Konfirmasi Ringkas & Approval
*Tujuan: Menampilkan ringkasan terstruktur dan meminta lampu hijau untuk penulisan PRD.*

**Contoh Konfirmasi (ID):**
> "Ringkasan rancangan proyek sudah terkumpul rapi:
> - **Produk & Vibe**: [Nama Produk] — [Deskripsi Vibe Singkat]
> - **Tech Stack**: [Ringkasan FE, Styling, BE, Database, AI]
> - **Core Scope (P0)**: [2–3 Fitur Utama]
> - **Anti-Goals**: [Batasan Versi 1]
> 
> Apakah ringkasan di atas sudah pas? Kalau sudah oke, saya akan langsung buatkan dokumen `PRD.md` lengkap yang siap dipakai coding agent!"

---

### Fase 5: Validasi Checklist & Penulisan Dokumen PRD
*Tujuan: Memastikan seluruh acceptance checklist terpenuhi dan menyimpan berkas ke disk.*

- Pastikan draf PRD bebas dari placeholder `[e.g., ...]` sebelum disimpan.
- Pastikan DDL database dan prompt roadmap terhubung dengan nomor section PRD.
- Beritahu pengguna lokasi penyimpanan file: *"Dokumen PRD lengkap berhasil dibuat dan disimpan di `PRD.md`. Anda bisa langsung menyalin Prompt 1 untuk mulai coding!"*
