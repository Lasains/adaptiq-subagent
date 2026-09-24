# Product Requirements Document (PRD) - Example

> **Project Name**: PromptCraft Studio  
> **Author/Owner**: Developer Team  
> **Target Vibe**: Sleek Cyber-Minimalist Dark Mode AI Studio  
> **Date**: 2026-09-19  
> **Status**: Approved for Build  

---

## 1. Executive Summary & Vibe Statement

### 1.1 Problem Statement
Indie developers dan vibe coders sering kali menulis prompt LLM yang terlalu ambigu atau kurang terstruktur, mengakibatkan AI menghasilkan kode yang halusinasi atau merusak file yang sudah ada. Mengoptimalkan prompt secara manual memakan waktu.

### 1.2 Proposed Solution
PromptCraft Studio adalah web app minimalis yang menerima draft prompt kasar pengguna, menganalisis intensi coding-nya, dan secara instan merombaknya menjadi format prompt berstandar tinggi (dilengkapi role, constraints, context formatting, dan output specification) siap pakai.

### 1.3 The "Vibe" & Product Aesthetic
- **Visual Aesthetic**: Sleek Dark Mode (latar `#0B0F19`, slate card `#111827`, aksen emerald `#10B981` dan indigo `#6366F1`), font mono untuk cuplikan kode, border tipis semi-transparan (`border-white/10`).
- **Target Experience**: Zero lag, shortcut keyboard (`Cmd+Enter` untuk generate, `Cmd+C` untuk copy output), toast feedback instan, loading skeleton pulse halus.
- **Target User**: Solo developers, AI pair programmers, vibe coders.

---

## 2. Tech Stack Specification

| Layer | Technology | Justification & Details |
| :--- | :--- | :--- |
| **Frontend Framework** | Next.js 15+ (App Router, TypeScript) | React Server Components, zero config routing, static-first speed |
| **Styling & Design System** | Tailwind CSS v4 + shadcn/ui | Radix primitives, konsisten dan mudah di-generate AI |
| **Icons & Typography** | Lucide React + JetBrains Mono / Geist | Tampilan developer-centric yang tajam dan nyaman dibaca |
| **Backend / API** | Next.js Route Handlers (Edge / Node) | Server-side streaming API endpoints via SSE |
| **Database** | Supabase (PostgreSQL) | Menyimpan riwayat prompt dan template preset pengguna |
| **ORM** | Drizzle ORM | Type-safe, ultra-lightweight, zero bundle bloat |
| **Authentication** | Supabase Auth (GitHub OAuth) | One-click login untuk developer; fallback ke guest mode |
| **State Management** | Zustand | Manajemen state filter, riwayat lokal, dan draft editor |
| **AI API** | Google Gemini 2.0 Flash (`@google/genai`) | Eksekusi optimasi teks super cepat (<800ms latency) |
| **Deployment** | Vercel | Instant continuous deployment via Git push |

---

## 3. Core Features & Scope (MoSCoW)

### 3.1 P0 (Must Have for MVP Vibe)
- [ ] **Instant Prompt Optimizer**: Input textarea teks kasar -> klik Optimize / `Cmd+Enter` -> Output terstruktur dengan preview markdown dan tombol *Copy to Clipboard*.
- [ ] **Archetype Presets**: Pilihan preset prompt (e.g. *Feature Builder*, *Bug Fixer*, *Architecture Plan*, *Refactoring*).
- [ ] **History Log**: Simpan 10 riwayat prompt terakhir di database (atau local storage jika guest mode).

### 3.2 P1 (Nice to Have / Fast Follow)
- [ ] **One-click Export to Cursor Rules / Antigravity Skill**: Ekspor hasil optimasi langsung ke format `.cursorrules` atau `SKILL.md`.
- [ ] **Diff Highlighting**: Tampilan visual perbandingan sebelum vs sesudah optimasi.

### 3.3 Anti-Goals (Strictly NOT in MVP)
- ❌ Tidak ada sistem langganan berbayar / Stripe di V1 (Gunakan personal API key atau kuota gratis).
- ❌ Tidak ada integrasi IDE plugin langsung (fokus web app terlebih dahulu).
- ❌ Tidak ada fitur kolaborasi tim / multi-user workspace.

---

## 4. Directory & File Architecture Blueprint

```text
promptcraft/
├── src/
│   ├── app/
│   │   ├── layout.tsx              # Root layout + Providers (Theme, Auth)
│   │   ├── page.tsx                # Studio main screen
│   │   └── api/
│   │       └── optimize/
│   │           └── route.ts        # Gemini API streaming endpoint
│   ├── components/
│   │   ├── ui/                     # shadcn primitives (button, badge, textarea, dialog)
│   │   ├── studio/
│   │   │   ├── prompt-input.tsx    # Raw text input with preset badges
│   │   │   ├── prompt-output.tsx   # Formatted markdown output + copy actions
│   │   │   ├── diff-viewer.tsx     # P1: Side-by-side comparison view
│   │   │   └── history-drawer.tsx  # Sidebar list of previous generations
│   │   └── layout/
│   │       └── navbar.tsx
│   ├── lib/
│   │   ├── gemini.ts               # Gemini client initialization (@google/genai)
│   │   ├── db.ts                   # Supabase / Drizzle connection
│   │   └── utils.ts                # cn helper & formatters
│   └── types/
│       └── index.ts                # TypeScript interfaces
├── public/
├── .env.example
├── package.json
└── tailwind.config.ts
```

---

## 5. Data Schema & Core Models

### 5.1 Supabase SQL DDL
```sql
CREATE TABLE prompts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  raw_input TEXT NOT NULL,
  optimized_output TEXT NOT NULL,
  preset TEXT DEFAULT 'general' NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL
);

-- Index for fast user query
CREATE INDEX idx_prompts_user ON prompts(user_id, created_at DESC);
```

### 5.2 TypeScript Interfaces
```typescript
export interface PromptRecord {
  id: string;
  userId?: string;
  rawInput: string;
  optimizedOutput: string;
  preset: 'feature' | 'bugfix' | 'refactor' | 'general';
  createdAt: string;
}

export interface OptimizeRequest {
  rawInput: string;
  preset: 'feature' | 'bugfix' | 'refactor' | 'general';
  apiKey?: string;
}
```

---

## 6. Key User Flows & Edge Cases

### 6.1 Happy Path Flow
1. Pengguna membuka web -> fokus kursor langsung aktif di textarea input (`prompt-input.tsx`).
2. Memilih preset badge (misal: `Feature Builder`) dan mengetik ide prompt kasar.
3. Menekan `Cmd + Enter` -> Loading spinner dengan skeleton pulse di panel output.
4. Gemini streaming hasil optimasi -> pengguna klik *Copy* -> muncul toast "Copied to clipboard!".
5. Riwayat tersimpan otomatis di sidebar `history-drawer.tsx`.

### 6.2 Edge Cases & Fallbacks
- **Gemini Rate Limit / Quota Exceeded**: Tampilkan banner ramah "Quota reached. Masukkan personal Google Gemini API Key di menu pengaturan".
- **Empty or Short Prompt**: Tombol *Optimize* disabled bila teks input < 5 karakter.
- **Offline / Network Drops**: Tampilkan toast peringatan, simpan draft input pengguna di `localStorage` agar tidak hilang.
- **Guest Mode (Tanpa Login)**: Riwayat prompt disimpan di `localStorage` per peramban hingga 10 riwayat.

---

## 7. Step-by-Step AI Vibe Coding Prompt Roadmap

> **How to use this section**: Copy and execute each prompt sequentially in your AI coding assistant (Antigravity, Cursor, Claude Code). Do not skip ahead until the current step is verified.

### 🚀 Prompt 1: Project Setup & Tailwind Layout
```markdown
Initialize the Next.js 15 App Router project per PRD Section 2 (Tech Stack) and Section 1.3 (The Vibe):
1. Create Next.js project with TypeScript, Tailwind CSS v4, and App Router.
2. Configure dark theme in `src/app/layout.tsx` using background #0B0F19, emerald accent #10B981, and slate card #111827 (ref: Section 1.3).
3. Install dependencies: `lucide-react`, `clsx`, `tailwind-merge`, and `@google/genai`.
4. Set up the directory structure specified in PRD Section 4.
Verify by checking that `npm run dev` starts cleanly on port 3000.
```

### 🗄️ Prompt 2: Database Schema & Environment Variables
```markdown
Configure data access according to PRD Section 5 (Data Schema) and Section 8 (Environment Variables):
1. Create `src/types/index.ts` containing the `PromptRecord` and `OptimizeRequest` interfaces from Section 5.2.
2. Create `.env.example` documenting all variables from Section 8 (`GEMINI_API_KEY`, `DATABASE_URL`, `NEXT_PUBLIC_SUPABASE_URL`, etc.).
3. Set up the Supabase/Drizzle client connection in `src/lib/db.ts` and initialize `@google/genai` client in `src/lib/gemini.ts`.
```

### 🧩 Prompt 3: Studio UI Shell & Components
```markdown
Build the core application layout in `src/app/page.tsx` per PRD Section 4 and Section 1.3:
1. Create a two-column responsive studio layout:
   - Left Column: `prompt-input.tsx` with textarea, character counter, preset badges (Feature, Bugfix, Refactor), and keyboard shortcut trigger (Cmd+Enter).
   - Right Column: `prompt-output.tsx` with markdown preview container and copy button.
2. Include empty state placeholder illustrations and loading skeleton animations matching Section 1.3 & Section 6.2.
```

### ⚡ Prompt 4: AI API Route & Streaming Optimization Logic
```markdown
Implement the AI optimization backend and client integration per PRD Section 2, Section 3.1, and Section 6.1:
1. Build `src/app/api/optimize/route.ts` using Google Gemini 2.0 Flash via `@google/genai`.
2. Craft a system prompt that structures user input into Role, Context, Constraints, and Output Specification.
3. Wire the frontend `prompt-input.tsx` to call `/api/optimize` via SSE streaming and render chunks into `prompt-output.tsx`.
4. Save each successful optimization into `prompts` table / local storage history per Section 5.1.
```

### 💎 Prompt 5: Polish, P1 Features, Edge Cases & Readiness
```markdown
Finalize the application for launch according to PRD Section 3.2 (P1 Features), Section 6.2 (Edge Cases), and Section 1.3:
1. Implement P1 Features:
   - Add `diff-viewer.tsx` to toggle side-by-side comparison between raw input and optimized output.
   - Add an "Export to Skill/Rule" button formatting the output as `.cursorrules` or `SKILL.md`.
2. Wire up edge case fallbacks from Section 6.2:
   - Custom API Key modal fallback if Gemini rate-limit occurs.
   - Offline draft caching in `localStorage`.
3. Add keyboard shortcuts (`Cmd+Enter` to generate, `Cmd+C` to copy output) and success toast feedback.
4. Verify with zero type errors (`tsc --noEmit`) and clean console output.
```

---

## 8. Environment Variables Reference

| Variable | Required | Description | Example / Fallback Value |
| :--- | :--- | :--- | :--- |
| `GEMINI_API_KEY` | ✅ Yes | Google Gemini API Key for model inference | `AIzaSyD-sample-key-12345` |
| `NEXT_PUBLIC_SUPABASE_URL` | ⚠️ Optional | Supabase project URL (if using database history) | `https://promptcraft.supabase.co` |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | ⚠️ Optional | Supabase public anonymous client key | `eyJhbGciOiJIUzI1NiIsIn...` |
| `SUPABASE_SERVICE_ROLE_KEY` | ⚠️ Optional | Supabase service role key for backend mutations | `eyJhbGciOiJIUzI1NiIsIn...` |
| `NEXT_PUBLIC_APP_URL` | ✅ Yes | Base public domain URL | `http://localhost:3000` |
