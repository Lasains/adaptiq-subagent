# Product Requirements Document (PRD)

> **Project Name**: [Project Name]  
> **Author/Owner**: [Name / GitHub Handle]  
> **Target Vibe**: [e.g., Sleek Dark Mode AI SaaS, Minimal Fast Prototype, Retro Cyberpunk Utility]  
> **Date**: [YYYY-MM-DD]  
> **Status**: [Draft / In Review / Approved / In Build]

---

## 1. Executive Summary & Vibe Statement

### 1.1 Problem Statement
[Describe in 2-3 sentences the exact user pain point being solved.]

### 1.2 Proposed Solution
[Describe what this product is and how it solves the pain point cleanly and quickly.]

### 1.3 The "Vibe" & Product Aesthetic
- **Visual Aesthetic**: [e.g., Minimalist dark mode with deep slate tones (#0F172A), crisp emerald accents (#10B981), subtle glassmorphism, micro-animations]
- **Target Experience**: [e.g., Instant response (<200ms interactions), zero clutter, high keyboard accessibility, intuitive flow]
- **Target User**: [e.g., Solo developers, indie hackers, content creators, productivity enthusiasts]

---

## 2. Tech Stack Specification

| Layer | Technology | Justification & Details |
| :--- | :--- | :--- |
| **Frontend Framework** | `[e.g., Next.js 15+ (App Router) / Vite + React / Expo]` | `[e.g., React Server Components, fast routing]` |
| **Styling & Design System** | `[e.g., Tailwind CSS v4 + shadcn/ui]` | `[e.g., Radix primitives, consistent accessible tokens]` |
| **Icons & Typography** | `[e.g., Lucide React + Geist / Inter / JetBrains Mono]` | `[e.g., Lightweight crisp SVG icons, clean developer font]` |
| **Backend / API** | `[e.g., Next.js Route Handlers + Server Actions / FastAPI]`| `[e.g., Type-safe mutations, serverless streaming]` |
| **Database** | `[e.g., PostgreSQL via Supabase / SQLite via Turso]` | `[e.g., Relational, serverless, fast read/write]` |
| **ORM / Query Builder** | `[e.g., Drizzle ORM / Prisma]` | `[e.g., End-to-end type safety, zero runtime bloat]` |
| **Authentication** | `[e.g., Supabase Auth / Clerk / None for MVP]` | `[e.g., OAuth GitHub/Google + email magic link]` |
| **State Management** | `[e.g., Zustand / TanStack Query]` | `[e.g., Minimal client state boilerplate, cache management]` |
| **AI / External APIs** | `[e.g., Google Gemini 2.0 Flash (@google/genai), Stripe]` | `[e.g., Low-latency generative AI completions]` |
| **Deployment & Hosting**| `[e.g., Vercel / Cloudflare Pages / Railway]` | `[e.g., Instant continuous deployment via Git push]` |

---

## 3. Core Features & Scope (MoSCoW)

### 3.1 P0 (Must Have for MVP Vibe)
*Features required to make the core loop functional and demonstratable.*
- [ ] **Feature 1**: [Description & Acceptance Criteria]
- [ ] **Feature 2**: [Description & Acceptance Criteria]
- [ ] **Feature 3**: [Description & Acceptance Criteria]

### 3.2 P1 (Nice to Have / Fast Follow)
- [ ] **Feature 4**: [Description & Acceptance Criteria]
- [ ] **Feature 5**: [Description & Acceptance Criteria]

### 3.3 Anti-Goals (Strictly NOT in MVP)
*Explicit boundaries to avoid vibe coding rabbit holes and scope creep.*
- ❌ [e.g., No multi-tenant enterprise billing or complex team roles in V1]
- ❌ [e.g., No custom drag-and-drop workflow canvas until core export works]
- ❌ [e.g., No native mobile apps — web-first responsive design only]

---

## 4. Directory & File Architecture Blueprint

```text
[project-root]/
├── src/
│   ├── app/                    # App Router pages & layout
│   │   ├── layout.tsx          # Root layout with providers & fonts
│   │   ├── page.tsx            # Landing / Studio main page
│   │   ├── api/                # API route handlers
│   │   └── ...
│   ├── components/             # Reusable UI components
│   │   ├── ui/                 # shadcn/ui primitives (button, dialog, etc.)
│   │   └── features/           # Feature-specific components
│   ├── lib/                    # Shared utilities, DB client, API helpers
│   │   ├── db.ts               # Database connection instance
│   │   ├── utils.ts            # cn() helper, formatters
│   │   └── api-client.ts       # External API wrappers
│   ├── types/                  # TypeScript interfaces & types
│   │   └── index.ts
│   └── hooks/                  # Custom React hooks
├── public/                     # Static assets (favicons, logos)
├── .env.example                # Documented environment variables
├── package.json
├── tailwind.config.ts
└── tsconfig.json
```

---

## 5. Data Schema & Core Models

### 5.1 Database Tables (DDL / Prisma / Drizzle)

```sql
-- Schema for Core Domain Entities
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT UNIQUE NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL
);

CREATE TABLE [entities] (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  title TEXT NOT NULL,
  content JSONB,
  status TEXT DEFAULT 'active' NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL,
  updated_at TIMESTAMPTZ DEFAULT NOW() NOT NULL
);
```

### 5.2 TypeScript Interfaces

```typescript
export interface User {
  id: string;
  email: string;
  createdAt: string;
}

export interface [Entity] {
  id: string;
  userId: string;
  title: string;
  content: Record<string, any>;
  status: 'active' | 'archived';
  createdAt: string;
  updatedAt: string;
}
```

---

## 6. Key User Flows & Edge Cases

### 6.1 Happy Path Flow
1. User lands on page -> [Initial View / Onboarding]
2. User triggers action -> [State Update / API Call]
3. Result displays with instant feedback -> [Optimistic UI / Success Toast]

### 6.2 Edge Cases & Error Boundaries
- **Network / API Timeout**: Show graceful fallback banner with retry button.
- **Empty State**: Render clean, inspiring illustration + quick start CTA.
- **Rate Limit / Quota Exceeded**: Display clear, actionable banner allowing users to input their own API key or retry later.

---

## 7. Step-by-Step AI Vibe Coding Prompt Roadmap

> **How to use this section**: Copy and execute each prompt sequentially in your AI coding assistant (Antigravity, Cursor, Claude Code). Do not skip ahead until the current step is verified.

### 🚀 Prompt 1: Scaffolding, Styling & Base Layout
```markdown
Set up the base project according to PRD Section 2 (Tech Stack) and Section 1.3 (The Vibe):
1. Initialize the project with [Framework from Section 2] and TypeScript.
2. Configure Tailwind CSS with the color palette, fonts, and dark mode theme from Section 1.3.
3. Install base UI dependencies: [list packages from Section 2].
4. Set up the root layout in `src/app/layout.tsx` matching the architecture in Section 4.
Verify by checking that the development server starts cleanly without warnings.
```

### 🗄️ Prompt 2: Database Schema, Environment & Client Config
```markdown
Configure data access according to PRD Section 5 (Data Schema) and Section 8 (Environment Variables):
1. Set up the schema models for [Entity] using [ORM/DDL from Section 5.1].
2. Create `.env.example` containing all variables documented in Section 8.
3. Initialize the database client connection in `src/lib/db.ts`.
4. Export TypeScript models from `src/types/index.ts` matching Section 5.2.
```

### 🧩 Prompt 3: Core UI Shell & Navigation
```markdown
Build the core UI layout and component primitives per PRD Section 4 (Architecture) and Section 1.3 (The Vibe):
1. Create the primary container and navigation layout in `src/app/page.tsx`.
2. Implement required UI primitives in `src/components/ui/` (buttons, inputs, dialogs).
3. Build feature skeleton components with empty states and loading spinners matching Section 6.2.
```

### ⚡ Prompt 4: Core Feature Logic & API Integration
```markdown
Implement the core P0 feature loop defined in PRD Section 3.1:
1. Build the API route handler / server action in `src/app/api/...` per Section 2 & 4.
2. Connect frontend triggers to the API endpoint with optimistic UI feedback.
3. Implement toast notifications and error handling for the Happy Path in Section 6.1.
```

### 💎 Prompt 5: Polish, Edge Cases & Launch Readiness
```markdown
Refine the build for demo readiness per PRD Section 3.2 (P1), Section 6.2 (Edge Cases), and Section 1.3:
1. Implement P1 features: [Feature 4 & 5].
2. Wire up graceful fallbacks for all edge cases documented in Section 6.2 (timeouts, rate limits, empty states).
3. Add micro-animations, keyboard shortcuts, and hover states to elevate "the vibe".
4. Run full linter and type-checker to ensure zero console errors.
```

---

## 8. Environment Variables Reference

| Variable | Required | Description | Example / Fallback Value |
| :--- | :--- | :--- | :--- |
| `DATABASE_URL` | ✅ Yes | Database connection string | `postgresql://postgres:password@localhost:5432/db` |
| `NEXT_PUBLIC_SUPABASE_URL` | ⚠️ Optional | Supabase Project URL (if using Supabase) | `https://xyzproject.supabase.co` |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | ⚠️ Optional | Supabase Anonymous Client Key | `eyJhbGciOiJIUzI1NiIsIn...` |
| `GEMINI_API_KEY` | ⚠️ Optional | Google Gemini Generative AI Key | `AIzaSyD...` |
| `NEXTAUTH_SECRET` | ⚠️ Optional | Session encryption secret key | `super-secret-random-32-chars` |
| `NEXT_PUBLIC_APP_URL` | ✅ Yes | Base public domain URL | `http://localhost:3000` |
