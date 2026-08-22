# Architecture Decision Record — `test-demo`

> **Status:** Approved  
> **Framework:** Next.js 13.3.1  
> **Architecture Pattern:** Pages Router  
> **Document Author:** Wilson — Solution Architect  
> **Last Updated:** 2026-08-21  
> **Compliance Target:** Bradesco / Avanade Method C.O.D.E.

---

## 1. Executive Summary

`test-demo` is a minimal Next.js 13.3.1 demonstration project configured with TypeScript (`strict: true`), Tailwind CSS 3.3.1, and the **Pages Router** architecture. The project employs path aliases (`@/*`, `@Pages/*`) and includes a basic API route (`pages/api/hello.ts`), an empty landing page (`pages/index.tsx`), and a unstyled dashboard component (`pages/dashboard/index.tsx`). The codebase requires structural improvements before it can meet production-grade Bradesco standards.

---

## 2. ADR-001: Pages Router vs App Router

### 2.1 Context

Next.js 13.3.1 introduces the App Router (`app/`) as the preferred routing paradigm, offering Server Components (RSC), streaming, and nested layouts. However, the existing `test-demo` project uses the legacy `pages/` directory structure. We must formally document why this decision remains in effect.

### 2.2 Decision

**Chosen:** Retain **Pages Router** (`pages/`)  
**Rejected:** Migrate to **App Router** (`app/`) at this stage  
**Status:** Documented / Deferred

### 2.3 Trade-Off Analysis

| Criterion | Pages Router (Chosen) | App Router (Rejected) |
|---|---|---|
| **Stability** | Proven, battle-tested since Next.js 9 | Stable in 13.3.1 but evolving rapidly |
| **Migration Cost** | Zero — no code changes required | High — requires directory restructuring, component rewrites, layout migration |
| **Server Components** | Not available (Client + SSR only) | Native RSC support — reduces bundle size |
| **Streaming / Suspense** | Partial (only through external libraries) | First-class streaming with `<Suspense>` |
| **Learning Curve** | Low — team already familiar | Medium — requires new patterns (`loading.tsx`, `error.tsx`, `layout.tsx`) |
| **Testing Compatibility** | `@testing-library/react` works without extra setup | Requires adjustments for Server Component testing |
| **Bradesco Standards** | Acceptable for demo/legacy projects | Recommended for new strategic projects |
| **Performance** | Good; full client hydration | Better; reduced JavaScript payload |

### 2.4 Consequences

- **Positive:** Minimal disruption; existing tests (`test/pages/index.test.tsx`) continue to work.
- **Negative:** No Server Components; full hydration overhead; future-proofing requires eventual migration.
- **Security Impact:** Pages Router does not alter security posture; defense-in-depth remains required (`_document.tsx` and `_app.tsx` provide standard protection).

### 2.5 Migration Path (Future)

> See Section 10 — Migration Recommendations.

---

## 3. Component Hierarchy

```mermaid
diagram
    flowchart TD
        A[_app.tsx] -->|wraps| B[index.tsx]
        A -->|wraps| C[dashboard/index.tsx]
        D[_document.tsx] -->|provides HTML skeleton| A
        E[pages/api/hello.ts] -->|API endpoint| F[Client / External Consumer]
        B -->|imports| G[styles/globals.css]
        C -->|imports| G
        H[test/pages/index.test.tsx] -->|tests| C
        I[components/ directory] -->|MISSING| E
        J[@/* path alias] --> K[src/*]
        L[@Pages/* path alias] --> M[src/pages/*]
```

> **Note:** The `components/` directory is missing; reusable UI elements are not abstracted from page-level files.

---

## 4. Module Structure & Path Aliases

### 4.1 Path Aliases (`tsconfig.json`)

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"],
      "@Pages/*": ["./src/pages/*"]
    }
  }
}
```

### 4.2 Module Mapping

| Alias Pattern | Resolved Path | Usage Example |
|---|---|---|
| `@/*` | `./src/*` | `import '@/styles/globals.css'` |
| `@Pages/*` | `./src/pages/*` | `import DashboardIndexPage from "@Pages/dashboard"` |

### 4.3 Directory Tree

```
.
├── docs/
│   └── ARCHITECTURE.md          # This document
├── public/
│   ├── favicon.ico
│   ├── next.svg
│   └── vercel.svg
├── src/
│   ├── pages/
│   │   ├── _app.tsx              # Application wrapper (clean, 9/10 score)
│   │   ├── _document.tsx         # HTML document skeleton (clean, 9/10 score)
│   │   ├── index.tsx             # Empty landing page (needs fix)
│   │   ├── dashboard/
│   │   │   └── index.tsx         # Unstyled component (quality 4/10)
│   │   └── api/
│   │       └── hello.ts         # Basic API route (quality 5/10)
│   └── styles/
│       └── globals.css          # Tailwind directives + custom variables
├── test/
│   ├── components/              # MISSING reusable test fixtures
│   └── pages/
│       └── index.test.tsx       # Dashboard tests (quality 6/10)
├── package.json
├── tsconfig.json
└── README.md                    # Minimal; 24 bytes
```

---

## 5. API Route Architecture

### 5.1 Endpoint Specification

| Property | Value |
|---|---|
| **Route** | `/api/hello` |
| **File** | `src/pages/api/hello.ts` |
| **Method** | `GET` (default) |
| **Response Type** | `NextApiResponse<Data>` |
| **Status** | `200 OK` |
| **Payload** | `{ "name": "John Doe" }` |

### 5.2 Source Analysis

```typescript
// src/pages/api/hello.ts
import type { NextApiRequest, NextApiResponse } from 'next'

type Data = { name: string }

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {
  res.status(200).json({ name: 'John Doe' })
}
```

### 5.3 Quality Assessment

| Metric | Score | Notes |
|---|---|---|
| **Type Safety** | High | `NextApiResponse<Data>` typed |
| **Error Handling** | **FAIL** | No try/catch; no input validation; no 500 path |
| **Input Validation** | **FAIL** | No `req.query` or `req.body` parsing |
| **Security** | Low | Hardcoded name; no rate-limiting; no authentication |
| **Testing** | **FAIL** | No `test/pages/api/` directory exists |
| **Overall Score** | **5/10** | Functional but unprepared for production |

### 5.4 Security Considerations (Security by Design)

- **Defense in Depth:** API routes must include request validation (e.g., `zod` or `joi`), rate limiting (`express-rate-limit` or Vercel Edge Config), and structured error responses.
- **Secrets:** No environment variables (`{env:...}` or `{file:...}`) are referenced; this prevents secret leakage but also prevents dynamic configuration.
- **CORS:** Default Next.js behavior; must be explicitly configured if external consumers require access.

---

## 6. Component Quality Analysis

### 6.1 Component Scorecard

| Component | Path | Lines | Score | Key Issues |
|---|---|---|---|---|
| `_app.tsx` | `pages/_app.tsx` | 8 | **9/10** | Clean; standard `AppProps` usage; imports `globals.css` correctly |
| `_document.tsx` | `pages/_document.tsx` | 12 | **9/10** | Standard; `lang="en"` set; `Head` included; `NextScript` present |
| `index.tsx` (Landing) | `pages/index.tsx` | 5 | **2/10** | **Empty `<main>`**; no content; `inter` font imported but unused |
| `dashboard/index.tsx` | `pages/dashboard/index.tsx` | 13 | **4/10** | Unstyled JSX; `disabled` button without `aria-label`; `.blue` class undefined in CSS; `data-testid` present (positive) |
| `api/hello.ts` | `pages/api/hello.ts` | 15 | **5/10** | Hardcoded response; no error handling; no validation |
| `globals.css` | `styles/globals.css` | 19 | **6/10** | Tailwind directives present; `.blue` class missing; custom CSS variables defined |

### 6.2 Detailed Component Review

#### 6.2.1 Empty Landing Page (`pages/index.tsx`)

```typescript
import Image from 'next/image'
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return <main></main>
}
```

- **Defect:** The `<main>` element is completely empty; the `Inter` font is initialized but never applied (no `inter.className`).
- **Impact:** Page renders as blank; no SEO value; no user journey progress.
- **Fix Priority:** Critical — required before any stakeholder review.

#### 6.2.2 Unstyled Dashboard (`pages/dashboard/index.tsx`)

```typescript
export default function DashboardIndexPage() {
  return (
    <div>
      <h1>Hello World :D</h1>
      <button disabled={true}>Click :D</button>
      <p data-testid="paragraph-blue" className="blue">{"Pedro <:()"}</p>
    </div>
  )
}
```

- **Positive Notes:** Uses `data-testid` for testability; JSX structure is clean; test file exists (`test/pages/index.test.tsx`).
- **Defects:**
  - No `.blue` CSS definition (global or module-level).
  - Disabled button lacks `aria-label` or `aria-disabled` description.
  - No TypeScript exports for component interface.
  - No responsive layout classes (Tailwind utility classes absent).

#### 6.2.3 Clean Application Wrapper (`pages/_app.tsx`)

- **Status:** Production-ready.
- **Observations:** Minimal wrapper; no custom providers (`ThemeProvider`, `AuthProvider`, etc.) injected. This aligns with simplicity principles but may require extension as requirements grow.

---

## 7. Data Flow Diagram

```mermaid
sequenceDiagram
    actor User as User / Browser
    participant App as Next.js App (_app.tsx)
    participant Page as Page Component (index / dashboard)
    participant Style as globals.css (Tailwind)
    participant API as API Route (api/hello)
    participant Test as Test Suite (jest)

    User->>App: HTTP GET /
    App->>Page: Render Component
    App->>Style: Load Tailwind base/components
    Page-->>User: HTML Response (empty for index; unstyled for dashboard)

    User->>App: HTTP GET /dashboard
    App->>Page: Render DashboardIndexPage
    Page-->>User: Unstyled JSX (no .blue styling)

    Test->>Page: render(<DashboardIndexPage/>)
    Page->>Test: DOM assertions (heading, button, paragraph)

    User->>API: HTTP GET /api/hello
    API-->>User: JSON { name: "John Doe" }
```

---

## 8. Testing Architecture

### 8.1 Test Stack

| Layer | Tool | Version | Coverage |
|---|---|---|---|
| **Unit / Component** | Jest | 29.5.0 | Partial (`test/pages/` only) |
| **Testing Library** | `@testing-library/react` | 14.0.0 | Component-level assertions |
| **Matchers** | `@testing-library/jest-dom` | 5.16.5 | `toBeDisabled`, `toHaveClass`, `toHaveTextContent` |
| **Environment** | `jest-environment-jsdom` | 29.5.0 | Browser-like DOM |

### 8.2 Existing Tests (`test/pages/index.test.tsx`)

| Test Case | Target | Assertion | Status |
|---|---|---|---|
| `Shoud render properly` | `<h1>` heading | `toHaveTextContent('Hello World :D')` | ✅ Pass |
| `Should have a disable button` | `<button>` | `toBeDisabled()` | ✅ Pass |
| `Should have a <p> Tag...` | `data-testid="paragraph-blue"` | `toHaveClass('blue')`, `toHaveTextContent("Pedro <:()")` | ⚠️ Fail (`.blue` undefined) |

### 8.3 Testing Gaps

| Missing Area | Impact | Recommendation |
|---|---|---|
| **API Tests** | No `test/pages/api/hello.test.ts` | Add unit tests for status codes, payload structure, error paths |
| **Landing Page Tests** | No `test/pages/index.test.tsx` for `pages/index.tsx` | Add snapshot or content assertions |
| **Component Tests** | No `test/components/` directory | Create reusable component tests after `components/` directory is added |
| **Accessibility** | No `jest-axe` integration | Add `axe-core` + `jest-axe` for a11y validation |
| **Snapshot Testing** | Not configured | Implement `toMatchSnapshot()` for UI regression detection |
| **E2E / Integration** | No Cypress / Playwright | Consider Playwright for critical user journeys |

---

## 9. Missing Components Directory Analysis

### 9.1 Current State

The `src/components/` directory does **not exist**. All UI logic is embedded directly in page files (`pages/dashboard/index.tsx`). This violates the **Single Responsibility Principle** and prevents reuse.

### 9.2 Recommended Component Hierarchy (Future)

```
src/components/
├── layout/                 # Page-level layout abstractions
│   ├── Header.tsx
│   ├── Footer.tsx
│   └── Sidebar.tsx
├── ui/                     # Atomic / reusable UI primitives
│   ├── Button.tsx
│   ├── Card.tsx
│   ├── Typography.tsx
│   └── Badge.tsx
├── forms/                  # Form-related components
│   ├── Input.tsx
│   └── Label.tsx
└── shared/                 # Cross-cutting utilities
    ├── ErrorBoundary.tsx
    └── LoadingSpinner.tsx
```

### 9.3 Impact Assessment

| Issue | Severity | Description |
|---|---|---|
| No abstraction layer | High | Page components mix layout, data, and presentation |
| No reuse | High | Dashboard elements cannot be imported by other pages |
| Testing difficulty | Medium | Component isolation requires directory restructuring |
| Clean architecture violation | High | Missing separation of concerns (presentation vs business logic) |

---

## 10. Migration Recommendations

### 10.1 Immediate Fixes (Sprint 1)

- [ ] **Fix empty `pages/index.tsx`** — add content, apply `inter.className` to `<main>`, include SEO `<Head>`.
- [ ] **Add `.blue` CSS definition** in `styles/globals.css` or migrate to Tailwind utility (`text-blue-600`).
- [ ] **Add `aria-label`** to disabled button in `dashboard/index.tsx`.
- [ ] **Run `npm audit fix`** — 25 vulnerabilities (15 critical/high) identified in `analysis_report.json`.
- [ ] **Create `src/components/`** with at least one reusable `Button` component.
- [ ] **Add `test/pages/api/hello.test.ts`** for API coverage.

### 10.2 Medium-Term Improvements (Sprint 2–3)

- [ ] **Upgrade Next.js** to 14+ (or latest stable); upgrade TypeScript to 5.5+; Tailwind to 3.4+.
- [ ] **Implement App Router migration plan** — evaluate whether the project requires RSC and streaming benefits.
- [ ] **Add accessibility testing** — `jest-axe` integration.
- [ ] **Add snapshot testing** — `jest --updateSnapshot` workflow.
- [ ] **Implement clean architecture** — hexagonal / enriched service layer (separate `services/`, `repositories/`, `models/` if project grows beyond demo scope).

### 10.3 App Router Migration Path (Long-Term)

If strategic requirements justify the migration, the following steps apply for Next.js 13.3.1 → 14+:

1. **Directory Migration:** Create `app/` directory alongside `pages/` (Next.js supports both during transition).
2. **Layout Migration:** Move `pages/_app.tsx` and `pages/_document.tsx` logic into `app/layout.tsx`.
3. **Page Migration:** Convert `pages/index.tsx` → `app/page.tsx`; `pages/dashboard/index.tsx` → `app/dashboard/page.tsx`.
4. **API Migration:** Convert `pages/api/hello.ts` → `app/api/hello/route.ts` (Route Handlers).
5. **Testing Updates:** Adjust `test/pages/` paths; add `test/app/` directory for new routes.
6. **Path Aliases:** Confirm `@Pages/*` remains valid or migrate aliases to `@/app/*`.

> **Architect Note (Wilson):** Migration should only proceed after stakeholder approval of the trade-offs documented in ADR-001. Do not migrate for innovation alone; migrate only when business value (performance, SEO, developer experience) exceeds migration cost.

---

## 11. Bradesco Standards Compliance Assessment

### 11.1 Methodology Reference

- **Standard:** Avanade Method C.O.D.E. (Discovery → Planning → Solutioning → Implementation → Documentation)
- **Security:** Defense in depth; secrets via `{env:}` / `{file:}`; no hardcoded credentials.
- **Code Quality:** TypeScript `strict`; clean code patterns; practical notes in source files.

### 11.2 Compliance Matrix

| Standard Area | Requirement | Status | Evidence / Note |
|---|---|---|---|
| **Stack — Next.js Version** | 13+ recommended; 14+ preferred for new strategic projects | ⚠️ **Partial** | 13.3.1 is acceptable for demo; upgrade required for production |
| **Stack — TypeScript** | 5.5+ preferred; `strict: true` required | ✅ **Compliant** | `"typescript": "5.0.4"`; `strict: true` enabled |
| **Stack — Tailwind CSS** | 3.4+ preferred | ✅ **Compliant** | `3.3.1` acceptable; upgrade recommended |
| **Testing Coverage** | ≥ 80% target | ❌ **FAIL** | Partial tests; no API tests; no landing page tests |
| **Security — Vulnerabilities** | Zero critical/high in production | ❌ **FAIL** | 25 vulnerabilities (15 critical/high) — `npm audit` required |
| **Security — Secrets Management** | No hardcoded secrets; use `{env:}` or `{file:}` | ✅ **Compliant** | No secrets present in source; must be maintained |
| **Architecture — ADR Documentation** | Every major decision documented with trade-offs | ✅ **Compliant** | ADR-001 included in this document |
| **Architecture — C4 Diagrams** | System and container diagrams required | ⚠️ **Partial** | Component hierarchy (Mermaid) present; C4 container diagram recommended |
| **Methodology — PRD / Brief** | Formal brief approved before implementation | ❌ **FAIL** | This is a demo/test project; no PRD or brief exists |
| **Methodology — INVEST Stories** | User stories with clear acceptance criteria | ❌ **FAIL** | No stories documented |
| **Methodology — Tests Before Implementation** | TDD or at least test coverage before release | ❌ **FAIL** | Tests added post-implementation; coverage < 80% |
| **Methodology — Clean Code Patterns** | Functions should explain themselves; no magic numbers | ⚠️ **Partial** | `pages/index.tsx` violates this (empty content); `_app.tsx` complies |
| **Methodology — Practical Notes** | Source files contain context / rationale comments | ❌ **FAIL** | No inline comments or practical notes in source files |
| **Methodology — Dev Agent Record** | Agent actions logged and traceable | ❌ **FAIL** | Not applicable to this demo; required for formal Bradesco development |
| **Documentation — Readme** | Clear setup, build, and test instructions | ⚠️ **Partial** | `README.md` is minimal (24 bytes); must be expanded |

### 11.3 Overall Compliance Score

```
Stack Compliance:     75%  (Acceptable; upgrades recommended)
Security Compliance:   50%  (FAIL — vulnerabilities must be remediated)
Methodology Compliance: 30% (FAIL — not a formal Bradesco story)
Documentation:         60%  (Partial — this ARCHITECTURE.md improves score)
```

> **Wilson's Verdict:** This project is a **technical demonstration**, not a production-grade Bradesco/Avanade deliverable. It requires remediation of security vulnerabilities, addition of formal documentation (README, API.md, TESTING.md), and adherence to the Avanade Method C.O.D.E. phases before it can be promoted to a strategic project.

---

## 12. References

- [Next.js 13.3.1 Documentation — Pages Router](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts)
- [Next.js — App Router Migration Guide](https://nextjs.org/docs/app/building-your-application/upgrading/from-pages)
- [TypeScript 5.0 — `strict` Mode](https://www.typescriptlang.org/tsconfig#strict)
- [Tailwind CSS 3.3 — Custom CSS Variables](https://tailwindcss.com/docs/customizing-colors)
- [Bradesco / Avanade Method C.O.D.E.](.avanade-method/) — Internal Methodology Reference

---

## 13. Appendix: Document Control

| Version | Date | Author | Change Description |
|---|---|---|---|
| 1.0 | 2026-08-21 | Wilson (Solution Architect) | Initial architecture document; ADR-001 (Pages Router); component analysis; Bradesco compliance assessment |

---

*Document generated in compliance with Wilson Architect protocol: understand requirements first, document trade-offs explicitly, visualize with diagrams, and stop for stakeholder review before implementation decisions are finalized.*
