# Curated "Golden" Tech Stacks for Vibe Coding

Ketika pengguna ragu atau meminta rekomendasi teknologi, tawarkan salah satu dari paket "Golden Vibe Stacks" berikut yang terbukti paling cepat, minim friksi, dan didukung sangat baik oleh AI coding assistant (Antigravity, Cursor, Claude Code).

---

## 1. The Modern Fullstack SaaS Vibe (Most Popular & Recommended)
> **Cocok untuk**: Web apps, SaaS, dashboards, micro-tools, AI wrappers, marketplace MVP.

- **Frontend Framework**: Next.js 14/15 (App Router, TypeScript)
- **Styling**: Tailwind CSS v4 + `shadcn/ui` (Radix Primitives)
- **Icons**: Lucide React (`lucide-react`)
- **Backend / API**: Next.js Server Actions & Route Handlers
- **Database**: PostgreSQL (via Supabase atau Neon Serverless)
- **ORM / Query**: Drizzle ORM atau Prisma
- **Auth**: Supabase Auth atau Clerk
- **State Management**: Zustand (untuk client UI) + Server Components
- **Deployment**: Vercel
- **Alasan Keunggulan**: Ekosistem komponen UI (`shadcn/ui`) sangat mudah digenerate oleh AI, tipe data end-to-end terintegrasi dari database hingga UI, dan deployment 1-klik di Vercel.

---

## 2. The Ultra-Fast Lightweight Prototype Vibe
> **Cocok untuk**: Proof-of-concept (PoC), internal tool, ide hackathon 24 jam, single-page app interaktif.

- **Frontend Framework**: Vite + React (TypeScript)
- **Styling**: Tailwind CSS + Lucide Icons
- **UI Components**: Radix UI atau Tailwind UI / daisyUI
- **Backend / Database**: Supabase (BaaS) atau PocketBase
- **Auth**: Supabase Auth (Magic Link / OAuth)
- **State Management**: TanStack Query + Zustand
- **Deployment**: Cloudflare Pages / Vercel
- **Alasan Keunggulan**: Hot-reload instan (HMR super cepat dengan Vite), tidak ada kerumitan server-side rendering, sangat ringan dijalankan di laptop spek minim.

---

## 3. The Python AI & Machine Learning Vibe
> **Cocok untuk**: Aplikasi deep learning, data processing, LangChain/LlamaIndex agents, RAG pipeline, computer vision.

- **Frontend**: Next.js (TypeScript) atau Streamlit (untuk internal data apps)
- **Styling**: Tailwind CSS + shadcn/ui
- **Backend API**: FastAPI (Python 3.11+) + Pydantic v2
- **AI Libraries**: Google Generative AI (`google-genai`), OpenAI SDK, LiteLLM
- **Database**: PostgreSQL dengan pgvector (Supabase / Neon)
- **Task Queue / Background**: Celery / Redis atau Inngest
- **Deployment**: Frontend di Vercel, Backend di Railway atau Render
- **Alasan Keunggulan**: Memberikan fleksibilitas penuh Python untuk manipulasi data & ekosistem LLM terkini, sembari mempertahankan UI frontend yang modern dan interaktif.

---

## 4. The Mobile Cross-Platform Vibe
> **Cocok untuk**: Aplikasi iOS & Android cepat, companion app, mobile-first utility.

- **Mobile Framework**: React Native dengan Expo (SDK 51+, Expo Router)
- **Styling**: NativeWind (Tailwind CSS untuk React Native)
- **UI Components**: React Native Paper atau custom Tailwind components
- **Backend / DB**: Supabase (Auth + Database + Storage)
- **Deployment**: Expo EAS (Expo Application Services) untuk build APK / TestFlight
- **Alasan Keunggulan**: Menulis satu codebase untuk iOS dan Android dengan syntax Tailwind yang sudah familiar bagi web developer.

---

## 5. The Content & High-Speed Landing Vibe
> **Cocok untuk**: Blog, dokumentasi produk, portfolio, agency site, company profile berkecepatan tinggi.

- **Framework**: Astro (v4+)
- **Styling**: Tailwind CSS
- **Content Engine**: Astro Content Collections (Markdown / MDX)
- **Interactive Islands**: React (bila dibutuhkan komponen interaktif tertentu)
- **Deployment**: Cloudflare Pages / GitHub Pages / Vercel
- **Alasan Keunggulan**: Zero JavaScript by default, skor Google Lighthouse 100/100, SEO optimal sejak hari pertama.

---

## Matriks Pilihan Cepat untuk User

| Kategori Proyek | Rekomendasi Pilihan |
| :--- | :--- |
| "Saya mau bikin SaaS / Web App lengkap" | **Paket 1** (Next.js + shadcn + Supabase) |
| "Saya mau bikin tool cepat tanpa ribet server" | **Paket 2** (Vite + React + Supabase) |
| "Saya butuh backend Python buat AI & Data" | **Paket 3** (Next.js + FastAPI + Gemini) |
| "Saya mau rilis di Play Store / App Store" | **Paket 4** (Expo + NativeWind + Supabase) |
| "Saya mau bikin landing page / blog super cepat" | **Paket 5** (Astro + Tailwind) |
