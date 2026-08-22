# Contributing Guide — test-demo

> **Project:** test-demo  
> **Version:** 0.1.0  
> **Framework:** Next.js 13.3.1 (Pages Router)  
> **Last Updated:** 2026-08-21  
> **Status:** Approved for team adoption

---

## Table of Contents

1. [Code of Conduct](#1-code-of-conduct)
2. [Development Setup](#2-development-setup)
3. [Branch Naming Convention](#3-branch-naming-convention)
4. [Commit Message Format](#4-commit-message-format)
5. [Pull Request Checklist](#5-pull-request-checklist)
6. [Coding Standards](#6-coding-standards)
7. [Testing Requirements](#7-testing-requirements)
8. [Architecture Guidelines](#8-architecture-guidelines)
9. [Security Requirements](#9-security-requirements)
10. [Documentation Updates](#10-documentation-updates)
11. [Issue Templates](#11-issue-templates)
12. [Release Process](#12-release-process)

---

## 1. Code of Conduct

### 1.1 Our Pledge

We are committed to fostering an open, inclusive, and respectful community. All contributors and maintainers pledge to make participation in this project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### 1.2 Expected Behavior

- **Be respectful** — Use welcoming and inclusive language
- **Be collaborative** — Accept constructive criticism gracefully
- **Be professional** — Focus on what is best for the project and community
- **Be responsible** — Take ownership of your contributions and their impact

### 1.3 Unacceptable Behavior

- Harassment, discrimination, or offensive comments
- Trolling, insulting, or derogatory remarks
- Public or private harassment
- Publishing others' private information without explicit permission
- Other conduct which could reasonably be considered inappropriate in a professional setting

### 1.4 Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported to the project maintainers. All complaints will be reviewed and investigated promptly and fairly. Maintainers are obligated to respect the privacy and security of the reporter.

---

## 2. Development Setup

### 2.1 Prerequisites

| Tool | Version | Notes |
|------|---------|-------|
| **Node.js** | >= 18.0.0 | LTS recommended (18.x or 20.x) |
| **npm** | >= 9.0.0 | Bundled with Node.js |
| **Git** | >= 2.30.0 | For version control |

> **Verify installation:**
> ```bash
> node --version   # v18.x.x or v20.x.x
> npm --version    # 9.x.x or higher
> ```

### 2.2 Initial Setup

```bash
# 1. Clone the repository
git clone <repository-url>
cd test-demo

# 2. Install dependencies
npm install

# 3. Verify installation
npm run lint       # Should pass with 0 errors
npm run build      # Should compile successfully
npm run test       # Should run tests in watch mode
```

### 2.3 Development Commands

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server at `http://localhost:3000` |
| `npm run build` | Production build (outputs to `.next/`) |
| `npm run start` | Start production server (requires `build` first) |
| `npm run lint` | Run ESLint with `eslint-config-next` |
| `npm run test` | Run Jest in watch mode |
| `npm run coverage` | Generate coverage report in `coverage/` |

### 2.4 Environment Variables

Create `.env.local` for local development (never commit):

```bash
# .env.local (example)
NEXT_PUBLIC_API_URL=http://localhost:3000/api
```

---

## 3. Branch Naming Convention

We follow **Conventional Branches** aligned with Conventional Commits:

### 3.1 Format

```
type>/<scope>-short-description>
```

### 3.2 Types

| Type | Purpose | Example |
|------|---------|---------|
| `feat` | New feature | `feat/dashboard-add-user-card` |
| `fix` | Bug fix | `fix/api-hello-null-response` |
| `chore` | Maintenance, tooling, deps | `chore/update-eslint-config` |
| `test` | Test additions or updates | `test/dashboard-add-coverage` |
| `docs` | Documentation only | `docs/update-readme-api` |
| `refactor` | Code restructuring (no behavior change) | `refactor/pages-extract-components` |
| `perf` | Performance improvement | `perf/optimize-tailwind-purge` |
| `security` | Security fix | `security/fix-xss-in-api` |
| `ci` | CI/CD pipeline changes | `ci/add-github-actions-workflow` |

### 3.3 Scope (Optional but Recommended)

| Scope | Area |
|-------|------|
| `pages` | Pages Router pages (`src/pages/`) |
| `api` | API routes (`src/pages/api/`) |
| `components` | Reusable components (`src/components/`) |
| `styles` | Global styles, Tailwind config |
| `config` | Tooling configs (ESLint, Jest, TS, Next) |
| `test` | Test files and configuration |
| `docs` | Documentation files |
| `deps` | Dependency updates |

### 3.4 Examples

```
feat/pages-add-dashboard-layout
fix/api-handle-empty-response
chore/deps-update-next-13.4
test/components-add-button-tests
docs/architecture-add-migration-path
refactor/pages-extract-header-component
perf/styles-remove-unused-tailwind
security/api-add-rate-limiting
ci/add-automated-security-scan
```

---

## 4. Commit Message Format

We enforce **Conventional Commits 1.0.0** specification.

### 4.1 Format

```
type>(scope>): <description>

[optional body]

[optional footer(s)]
```

### 4.2 Rules

- **Type** — Required: `feat`, `fix`, `chore`, `test`, `docs`, `refactor`, `perf`, `security`, `ci`
- **Scope** — Optional but encouraged (see [Branch Scopes](#33-scope-optional-but-recommended))
- **Description** — Required, imperative mood, lowercase, no trailing period, <= 72 chars
- **Body** — Optional, explains *what* and *why* (not *how*), wrapped at 72 chars
- **Footer** — Optional, for breaking changes (`BREAKING CHANGE:`) or issue references (`Closes #123`)

### 4.3 Examples

```bash
# Simple feat
feat(pages): add dashboard loading state

# Fix with body
fix(api): handle null response from hello endpoint

The hello API returned null when database was unavailable.
Added fallback to prevent 500 error on client.

Closes #42

# Breaking change
refactor(pages)!: migrate to App Router structure

BREAKING CHANGE: Directory structure changed from pages/ to app/.
All imports must be updated. See MIGRATION.md.

# Test addition
test(dashboard): add snapshot test for empty state

# Documentation
docs(readme): update installation steps for Node 20
```

### 4.4 Commit Message Validation

Commits are validated via `commitlint` (configured in `commitlint.config.js`). Invalid commits will be rejected by pre-commit hooks.

---

## 5. Pull Request Checklist

All PRs must satisfy **every** item before merge.

### 5.1 Required Checks

| Check | Command | Required |
|-------|---------|:--------:|
| **Tests Pass** | `npm run test -- --watchAll=false` | Yes |
| **Lint Pass** | `npm run lint` | Yes |
| **Build Pass** | `npm run build` | Yes |
| **Security Scan** | `npm audit --audit-level=high` | Yes |
| **Type Check** | `npx tsc --noEmit` | Yes |

### 5.2 Code Quality

- [ ] No `console.log`, `debugger`, or commented-out code
- [ ] No `any` types (use `unknown` or proper types)
- [ ] No `@ts-ignore` or `eslint-disable` without justification
- [ ] All new exports have JSDoc comments
- [ ] Components follow single responsibility principle

### 5.3 Testing

- [ ] New features include unit tests
- [ ] Bug fixes include regression tests
- [ ] Coverage does not decrease (target: >= 80%)
- [ ] Tests follow AAA pattern (Arrange, Act, Assert)
- [ ] Test names describe behavior, not implementation

### 5.4 Documentation

- [ ] `README.md` updated if user-facing changes
- [ ] `docs/ARCHITECTURE.md` updated if architecture changes
- [ ] `docs/TESTING.md` updated if test patterns change
- [ ] `docs/API.md` updated if API contracts change
- [ ] CHANGELOG entry added (see [Release Process](#12-release-process))

### 5.5 PR Metadata

- [ ] Clear, descriptive title (matches commit format)
- [ ] Description explains *what* and *why*
- [ ] Linked issue(s): `Closes #XXX` or `Refs #XXX`
- [ ] Screenshots for UI changes
- [ ] Labels: `type:`, `scope:`, `priority:`

---

## 6. Coding Standards

### 6.1 TypeScript

- **Strict mode:** Enabled (`"strict": true` in `tsconfig.json`)
- **No implicit any:** Disallowed (`"noImplicitAny": true`)
- **Strict null checks:** Enabled (`"strictNullChecks": true`)
- **Path aliases:** Use `@/*` and `@Pages/*` (configured in `tsconfig.json`)

```typescript
// Good
import { DashboardIndexPage } from '@Pages/dashboard';
import styles from '@/styles/globals.css';

// Avoid
import { DashboardIndexPage } from '../../../pages/dashboard';
```

### 6.2 ESLint

- **Config:** `eslint-config-next` (includes `core-web-vitals`)
- **React rules:** Enabled via Next.js config
- **TypeScript rules:** Enabled via `@typescript-eslint`
- **Run:** `npm run lint` (must pass with 0 errors, 0 warnings)

```json
// .eslintrc.json (extends)
{
  "extends": ["next/core-web-vitals"]
}
```

### 6.3 Prettier

- **Implied:** Format on save via editor integration
- **Config:** Uses Next.js defaults (single quotes, trailing commas, 2-space indent)
- **No separate config file** — relies on editor/IDE settings

### 6.4 React / Next.js Patterns

| Pattern | Requirement |
|---------|-------------|
| **Components** | Functional components with TypeScript interfaces |
| **Props** | Explicit `interface Props {}` — no inline types |
| **Hooks** | Custom hooks in `src/hooks/` (create if needed) |
| **State** | `useState`, `useReducer` — no class components |
| **Effects** | `useEffect` with proper cleanup |
| **Client/Server** | All components are client-side (Pages Router) |

### 6.5 File Naming

| Type | Convention | Example |
|------|------------|---------|
| **Pages** | `kebab-case.tsx` | `dashboard/index.tsx` |
| **Components** | `PascalCase.tsx` | `UserCard.tsx` |
| **Hooks** | `use-name>.ts` | `use-api.ts` |
| **Utilities** | `camelCase.ts` | `dateUtils.ts` |
| **Types** | `types.ts` or `<domain>.types.ts` | `api.types.ts` |
| **Tests** | `<source>.test.tsx` | `dashboard.index.test.tsx` |

---

## 7. Testing Requirements

### 7.1 Philosophy

> **Test-Driven Development (TDD) encouraged** — Write tests before or alongside implementation.

### 7.2 Coverage Target

| Metric | Target | Enforcement |
|--------|--------|-------------|
| **Statements** | >= 80% | CI gate |
| **Branches** | >= 80% | CI gate |
| **Functions** | >= 80% | CI gate |
| **Lines** | >= 80% | CI gate |

> Current baseline: ~15% (dashboard only). New code must raise overall coverage.

### 7.3 Test Structure

```
test/
├── pages/              # Page component tests
│   └── dashboard.index.test.tsx
├── components/         # Component tests (when created)
├── api/                # API route tests
├── hooks/              # Custom hook tests
├── utils/              # Utility function tests
└── setup.ts            # Global test setup (if needed)
```

### 7.4 Test Patterns

```tsx
// Good: Behavior-focused, descriptive name
describe('Dashboard Page', () => {
  it('renders welcome heading with correct text', () => {
    render(<DashboardIndexPage />);
    expect(screen.getByRole('heading')).toHaveTextContent('Hello World :D');
  });

  it('disables the action button by default', () => {
    render(<DashboardIndexPage />);
    expect(screen.getByRole('button')).toBeDisabled();
  });
});

// Avoid: Implementation-focused, vague names
it('renders component', () => { ... });
it('test button disabled', () => { ... });
```

### 7.5 Testing Library Queries (Priority Order)

1. **`getByRole`** — Accessible, user-facing
2. **`getByLabelText`** — Form inputs
3. **`getByPlaceholderText`** — Inputs without labels
4. **`getByText`** — Non-interactive text
5. **`getByTestId`** — Last resort (add `data-testid`)

### 7.6 Running Tests

```bash
# Watch mode (development)
npm run test

# CI mode (single run, coverage)
npm run coverage

# Specific file
npx jest test/pages/dashboard.index.test.tsx
```

---

## 8. Architecture Guidelines

### 8.1 Router: Pages Router Only

| Allowed | Forbidden |
|---------|-----------|
| `src/pages/` directory | `src/app/` directory (App Router) |
| `getServerSideProps`, `getStaticProps` | `Server Components` (RSC) |
| `pages/api/` routes | `route.ts` handlers |
| `_app.tsx`, `_document.tsx` | `layout.tsx`, `loading.tsx` |

> **Rationale:** Documented in `docs/ARCHITECTURE.md` (ADR-001). Migration deferred.

### 8.2 Path Aliases (Mandatory)

```typescript
// tsconfig.json
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

| Alias | Resolves To | Usage |
|-------|-------------|-------|
| `@/*` | `./src/*` | `import '@/styles/globals.css'` |
| `@Pages/*` | `./src/pages/*` | `import Page from '@Pages/dashboard'` |

### 8.3 Component Organization

```
src/
├── pages/
│   ├── _app.tsx           # Global wrapper, providers
│   ├── _document.tsx      # HTML shell, lang, fonts
│   ├── index.tsx          # Landing page (/)
│   ├── dashboard/
│   │   └── index.tsx      # Dashboard page (/dashboard)
│   └── api/
│       └── hello.ts       # API route (GET /api/hello)
├── components/            # REUSABLE components (create as needed)
│   ├── ui/                # Primitive components (Button, Input, Card)
│   ├── layout/            # Layout components (Header, Footer, Sidebar)
│   └── features/          # Feature-specific components
├── hooks/                 # Custom React hooks
├── lib/                   # Utilities, API clients, constants
├── styles/
│   └── globals.css        # Tailwind imports, CSS variables
└── types/                 # Shared TypeScript types
```

### 8.4 Component Creation Rules

1. **Extract to `components/`** when used in >= 2 pages
2. **Co-locate** component, types, and tests
3. **Default export** for components, **named exports** for utilities
4. **Props interface** named `<Component>Props`

```tsx
// src/components/ui/Button.tsx
export interface ButtonProps {
  variant: 'primary' | 'secondary';
  onClick: () => void;
  children: React.ReactNode;
}

export default function Button({ variant, onClick, children }: ButtonProps) {
  return (
    <button className={cn('btn', `btn-${variant}`)} onClick={onClick}>
      {children}
    </button>
  );
}
```

### 8.5 Styling

- **Tailwind CSS** — Utility-first, no custom CSS unless necessary
- **CSS Variables** — Defined in `globals.css` for theming
- **No inline styles** — Use Tailwind classes
- **Component variants** — Use `class-variance-authority` (CVA) or `cn()` helper

---

## 9. Security Requirements

### 9.1 Secrets Management

| Never Commit | Use Instead |
|--------------|-------------|
| API keys, tokens | Environment variables (`.env.local`) |
| Database passwords | Secret manager (Vercel, AWS, Azure) |
| JWT secrets | Runtime injection |
| Private keys | Secure key storage |

### 9.2 Pre-PR Security Checks

```bash
# 1. Audit dependencies (must pass)
npm audit --audit-level=high

# 2. Check for secrets (install git-secrets or trufflehog)
git secrets --scan
# or
trufflehog git file://. --since-commit HEAD~1

# 3. Verify no .env files staged
git diff --cached --name-only | grep -E '^\.env'
```

### 9.3 Dependency Security

- **Update regularly:** `npm outdated` -> `npm update`
- **Audit before PR:** `npm audit --audit-level=high` must show 0 high/critical
- **Lockfile:** Commit `package-lock.json` — ensures reproducible installs
- **Supply chain:** Prefer well-maintained packages, avoid abandoned deps

### 9.4 Application Security

- **XSS Prevention:** React auto-escapes — never use `dangerouslySetInnerHTML`
- **CSRF:** Next.js Pages Router API routes — implement CSRF tokens for mutations
- **Headers:** Configure in `next.config.js` (CSP, HSTS, X-Frame-Options)
- **Input Validation:** Zod schemas for API route validation

---

## 10. Documentation Updates

**Every change that affects behavior requires documentation updates.**

### 10.1 Required Files

| File | When to Update |
|------|----------------|
| `README.md` | User-facing changes: setup, scripts, features |
| `docs/ARCHITECTURE.md` | Architecture decisions, new patterns, migrations |
| `docs/TESTING.md` | New test utilities, patterns, coverage changes |
| `docs/API.md` | API route changes, new endpoints, breaking changes |
| `CHANGELOG.md` | Every merge (see [Release Process](#12-release-process)) |

### 10.2 Documentation Standards

- **CommonMark** compliant Markdown
- **Mermaid** diagrams for architecture/flows
- **Code blocks** with language hints (`typescript`, `bash`, `json`)
- **Cross-references** — Link to related docs (`[ARCHITECTURE.md](./ARCHITECTURE.md)`)
- **Version badges** — Update version in README after release

### 10.3 Review Process

Documentation changes follow same PR process as code. At least one reviewer must verify accuracy.

---

## 11. Issue Templates

### 11.1 Bug Report (`.github/ISSUE_TEMPLATE/bug_report.md`)

```markdown
---
name: Bug Report
about: Report a reproducible issue
title: "[BUG] <short description>"
labels: ["type:bug"]
---

## Description
Clear, concise description of the bug.

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. Scroll to '...'
4. See error

## Expected Behavior
What should happen.

## Actual Behavior
What actually happens (screenshots, logs, stack traces).

## Environment
- OS: [e.g., Windows 11, macOS 14, Ubuntu 22.04]
- Node: [e.g., 18.17.0]
- Browser: [e.g., Chrome 118, Firefox 119]
- Branch: [e.g., main, feat/new-feature]

## Additional Context
Any other information, configuration, or data.
```

### 11.2 Feature Request (`.github/ISSUE_TEMPLATE/feature_request.md`)

```markdown
---
name: Feature Request
about: Suggest a new feature or enhancement
title: "[FEAT] <short description>"
labels: ["type:feature"]
---

## Problem Statement
What problem does this solve? Why is it needed?

## Proposed Solution
Describe the desired behavior or API.

## Alternatives Considered
Other approaches you evaluated.

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Additional Context
Mockups, diagrams, references, or related issues.
```

### 11.3 Security Issue (`.github/ISSUE_TEMPLATE/security.md`)

```markdown
---
name: Security Vulnerability
about: Report a security issue (DO NOT use for non-security bugs)
title: "[SECURITY] <brief description - no exploit details>"
labels: ["type:security", "priority:critical"]
---

## ⚠️ SECURITY ISSUE - DO NOT DISCLOSE PUBLICLY

**Report privately to:** security@company.com

## Vulnerability Details
- **Component affected:** [e.g., API route, authentication, dependency]
- **Attack vector:** [e.g., XSS, SQLi, RCE, information disclosure]
- **Impact:** [Confidentiality / Integrity / Availability]
- **CVSS Score (if known):** [e.g., 7.5 High]

## Reproduction Steps
Minimal steps to verify (no exploit code).

## Suggested Fix
If you have a patch or mitigation.

## Affected Versions
[e.g., 0.1.0, main branch]
```

---

## 12. Release Process

### 12.1 Versioning

We follow **Semantic Versioning 2.0.0** (SemVer):

```
MAJOR.MINOR.PATCH
  │      │      │
  │      │      └─ Patch: Bug fixes (backward compatible)
  │      └──────── Minor: New features (backward compatible)
  └─────────────── Major: Breaking changes
```

| Release Type | Version Bump | Example |
|--------------|--------------|---------|
| Bug fix | PATCH | 0.1.0 -> 0.1.1 |
| New feature | MINOR | 0.1.0 -> 0.2.0 |
| Breaking change | MAJOR | 0.1.0 -> 1.0.0 |

### 12.2 Changelog

Maintain `CHANGELOG.md` (Keep a Changelog format):

```markdown
# Changelog

All notable changes documented per [Keep a Changelog](https://keepachangelog.com/).

## [0.2.0] - 2026-08-21

### Added
- Dashboard loading skeleton component
- User avatar in header

### Fixed
- API hello endpoint null response handling

### Changed
- Updated ESLint config to v8.40

### Security
- Patched CVE-2026-XXXX in lodash dependency
```

### 12.3 Release Workflow

```bash
# 1. Ensure main is clean and up to date
git checkout main
git pull origin main
npm run lint && npm run build && npm run test -- --watchAll=false

# 2. Create release branch
git checkout -b release/v0.2.0

# 3. Update version (npm version handles changelog if configured)
npm version minor  # or patch / major

# 4. Update CHANGELOG.md manually (review generated entries)
#    - Group by Added/Changed/Fixed/Removed/Security

# 5. Commit version bump
git add package.json package-lock.json CHANGELOG.md
git commit -m "chore(release): v0.2.0"

# 6. Open PR to main
#    - Title: "chore(release): v0.2.0"
#    - All checks must pass

# 7. After merge, tag and push
git tag -a v0.2.0 -m "Release v0.2.0"
git push origin v0.2.0

# 8. Deploy (Vercel auto-deploys on tag push)
# 9. Create GitHub Release from tag with changelog notes
```

### 12.4 Hotfix Process

For critical production fixes:

```bash
# 1. Branch from latest tag
git checkout -b hotfix/v0.1.1 v0.1.0

# 2. Apply fix, test, update version (patch)
npm version patch

# 3. Merge to main (and develop if using git-flow)
# 4. Tag and deploy
```

---

## Appendix: Quick Reference

### Commands Cheat Sheet

```bash
# Development
npm run dev          # Start dev server
npm run build        # Production build
npm run start        # Production server

# Quality
npm run lint         # ESLint
npm run test         # Jest watch
npm run coverage     # Coverage report
npx tsc --noEmit     # Type check

# Security
npm audit --audit-level=high
npm outdated         # Check updates

# Git
git status           # Check changes
git add -A           # Stage all
git commit -m "..."  # Commit (use conventional format)
git push origin <branch>
```

### Useful Links

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [Next.js Pages Router Docs](https://nextjs.org/docs/pages)
- [TypeScript Strict Mode](https://www.typescriptlang.org/tsconfig#strict)
- [ESLint Next Config](https://nextjs.org/docs/basic-features/eslint)
- [Testing Library Queries](https://testing-library.com/docs/queries/about/)

---

> **Maintainers:** Wilson (Architect), Paula (Product Owner), Tiago (Developer), Carla (QA)  
> **Questions?** Open a discussion or contact the maintainers directly.
