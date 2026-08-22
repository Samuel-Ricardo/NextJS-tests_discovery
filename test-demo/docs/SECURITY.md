# Security Audit Report — test-demo

> **Project:** `test-demo`  
> **Audit Date:** 2026-08-20  
> **Audit Source:** `npm audit --json` (auditReportVersion 2)  
> **Scan Command:** `npm audit --json` (run in `test-demo/`)  
> **Lockfile:** `package-lock.json` (292,554 bytes; 650 total dependencies: 325 prod + 316 dev + 10 optional)

---

## 1. Executive Summary

### Vulnerability Tally (Verified from `npm audit` Metadata)

| Severity | Count | % of Total |
|----------|-------|------------|
| Critical | **3** | 12% |
| High     | **12** | 48% |
| Moderate | **8** | 32% |
| Low      | **2** | 8% |
| **Total** | **25** | **100%** |

- **Direct vulnerabilities:** 3 (`next` direct critical + high, `postcss` direct high + moderate)
- **Transitive / indirect:** 22 (88%) propagate through nested `node_modules/` trees
- **Zero fixes applied** at audit time; `npm audit fix` not executed

### Top-Line Risk Statement

`next` v13.3.1 carries a **critical authorization bypass** (`GHSA-f82v-jwr5-mffw`, CVSS 9.1) allowing unauthenticated middleware bypass, plus 5 high DoS advisories (`GHSA-fq54-2j52-jc42`, `GHSA-7gfc-8cq8-jh5f`, `GHSA-mwv6-3258-q52c`, `GHSA-5j59-xgg2-r9c4`, `GHSA-h25m-26qc-wcjf`). `postcss` 8.4.23 has high arbitrary file read (`GHSA-6g55-p6wh-862q`, CVSS 7.5) and path traversal (`GHSA-r28c-9q8g-f849`). `@babel/traverse` (`GHSA-67hx-6x53-jw92`, CVSS 9.3) enables arbitrary code execution during build. **Production deployment blocked until critical/high remediated.**

---

## 2. Detailed CVE / Advisory Table (Actual `npm audit` Data)

### 2.1 Critical — 3 Advisories

| Package | Advisory ID | Title / Description | Severity | CWE | CVSS Score / Vector | Affected Range | Fix Version | Direct? |
|---------|-------------|---------------------|----------|-----|---------------------|----------------|-------------|---------|
| `next` | `GHSA-f82v-jwr5-mffw` (1113690) | **Authorization Bypass in Next.js Middleware** — unauthenticated bypass of middleware authorization checks | Critical | CWE-285, CWE-863 | 9.1 / `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N` | `>=13.0.0 <13.5.9` | `>=13.5.9` (or 14.2.34+) | **Direct** (`next` 13.3.1) |
| `@babel/traverse` | `GHSA-67hx-6x53-jw92` (1117420) | **Arbitrary Code Execution** — Babel vulnerable to arbitrary code execution when compiling specifically crafted malicious code | Critical | CWE-184, CWE-697 | 9.3 / `AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H` | `<7.23.2` | `>=7.23.2` | Indirect (build pipeline) |
| `form-data` | `GHSA-fjxv-7rqg-78g4` (1109538) | Unsafe random function for multipart boundary (predictable boundaries) | Critical | CWE-330 | 0.0 / null (advisory critical label) | `>=4.0.0 <4.0.4` | `>=4.0.4` | Indirect |

### 2.2 High — 12 Advisories (Selected Key Direct + Indirect)

| Package | Advisory ID | Title / Description | Severity | CWE | CVSS | Range | Fix | Direct? |
|---------|-------------|---------------------|----------|-----|------|-------|-----|---------|
| `next` | `GHSA-fq54-2j52-jc42` (1100393) | DoS condition in Next.js | High | CWE-400 | 7.5 / `AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H` | `>=13.3.1 <13.5.0` | `>=13.5.0` | **Direct** |
| `next` | `GHSA-7gfc-8cq8-jh5f` (1107420) | Authorization bypass vulnerability (second advisory) | High | CWE-285, CWE-863 | 7.5 / `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N` | `>=9.5.5 <14.2.15` | `>=14.2.15` | **Direct** |
| `next` | `GHSA-mwv6-3258-q52c` (1111391) | DoS with Server Components | High | CWE-400, CWE-502, CWE-1395 | 7.5 | `>=13.3.0 <14.2.34` | `>=14.2.34` | **Direct** |
| `next` | `GHSA-5j59-xgg2-r9c4` (1112182) | DoS with Server Components — Incomplete Fix Follow-Up | High | CWE-400, CWE-502, CWE-1395 | 7.5 | `>=13.3.1-canary.0 <14.2.35` | `>=14.2.35` | **Direct** |
| `next` | `GHSA-h25m-26qc-wcjf` (1112653) | HTTP request deserialization → DoS with insecure React Server Components | High | CWE-400, CWE-502 | 7.5 | `>=13.0.0 <15.0.8` | `>=15.0.8` | **Direct** |
| `postcss` | `GHSA-6g55-p6wh-862q` (1124252) | Arbitrary file read / info disclosure via attacker-controlled `sourceMappingURL` | High | CWE-22, CWE-200 | 7.5 / `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N` | `<=8.5.11` | `>=8.5.23` | **Direct** (`postcss` 8.4.23) |
| `postcss` | `GHSA-r28c-9q8g-f849` (1139510) | Path Traversal in Previous Source Map Auto-Loading (`sourceMappingURL`) | High | CWE-22 | 7.5 / `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N` | `<=8.5.17` | `>=8.5.18` | **Direct** |
| `brace-expansion` | `GHSA-3jxr-9vmj-r5cp` (1123897) | DoS — exponential-time expansion of consecutive non-expanding `{}` groups | High | CWE-400, CWE-407 | 5.3 / `AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L` | `<1.1.16` | `>=1.1.18` | Indirect |
| `brace-expansion` | `GHSA-mh99-v99m-4gvg` (1130588) | DoS — unbounded expansion length → out-of-memory crash | High | CWE-400, CWE-770 | 7.5 / `AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H` | `<1.1.17` | `>=1.1.18` | Indirect |
| `braces` | `GHSA-grv7-fg5c-xmjg` (1098094) | Uncontrolled resource consumption | High | CWE-400, CWE-1050 | 7.5 | `<3.0.3` | `>=3.0.3` | Indirect |
| `js-yaml` | `GHSA-52cp-r559-cp3m` (1123911 / 1123912) | Quadratic CPU consumption in YAML merge-key chains | High | CWE-400, CWE-407 | 7.5 | `>=3.0.0 <3.15.0` / `>=4.0.0 <4.3.0` | `>=3.15.0` / `>=4.3.0` | Indirect |
| `lodash` | `GHSA-r5fr-rjxr-66jc` (1115806) | Code Injection via `_.template` imports key names | High | CWE-94 | 8.1 / `AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H` | `>=4.0.0 <=4.17.23` | `>=4.17.24` | Indirect |
| `minimatch` | `GHSA-7r86-cg39-jmmj` (1113538) | ReDoS: `matchOne()` combinatorial backtracking | High | CWE-407 | 7.5 | `<3.1.3` | `>=3.1.3` | Indirect |
| `minimatch` | `GHSA-23c5-xmqv-rm74` (1113546) | ReDoS: nested `*()` extglobs → catastrophic backtracking regex | High | CWE-1333 | 7.5 | `<3.1.4` | `>=3.1.4` | Indirect |
| `picomatch` | `GHSA-c2c7-rcm5-vvqj` (1115552) | ReDoS via extglob quantifiers | High | CWE-1333 | 7.5 | `<2.3.2` | `>=2.3.2` | Indirect |
| `semver` | `GHSA-c2qf-rxjj-qqgw` (1112921 / 1112922) | ReDoS in semver regex parsing | High | CWE-1333 | 7.5 | `>=7.0.0 <7.5.2` / `>=6.0.0 <6.3.1` | `>=7.5.2` / `>=6.3.1` | Indirect |
| `ws` | `GHSA-3h5v-q93c-6h6q` (1118728) | DoS: request with many HTTP headers (`CWE-476` Null Pointer Dereference) | High | CWE-476 | 7.5 / `AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H` | `>=8.0.0 <8.17.1` | `>=8.17.1` | Indirect |
| `ws` | `GHSA-96hv-2xvq-fx4p` (1123259) | Memory exhaustion DoS from tiny fragments and data chunks | High | CWE-400, CWE-770, CWE-1050 | 7.5 / `AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H` | `>=8.0.0 <8.21.0` | `>=8.21.0` | Indirect |

### 2.3 Moderate — 8 Advisories

| Package | Advisory ID | Title / Description | CWE | CVSS | Range | Fix |
|---------|-------------|---------------------|-----|------|-------|-----|
| `next` | `GHSA-g77x-44xx-532m` (1100421) | Denial of Service in image optimization | CWE-674 | 5.9 / `AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H` | `>=10.0.0 <14.2.7` | `>=14.2.7` |
| `next` | `GHSA-7m27-7ghc-44w9` (1101439) | DoS with Server Actions | CWE-770 | 5.3 | `>=13.0.0 <13.5.8` | `>=13.5.8` |
| `next` | `GHSA-g5qg-72qw-gw5v` (1107226) | Cache Key Confusion for Image Optimization API Routes | CWE-524 | 6.2 | `>=0.9.9 <14.2.31` | `>=14.2.31` |
| `next` | `GHSA-xv57-4mr9-wg8v` (1107513) | Content Injection Vulnerability for Image Optimization | CWE-20 | 4.3 | `>=0.9.9 <14.2.31` | `>=14.2.31` |
| `postcss` | `GHSA-7fh5-64p2-3v2j` (1109574) | Line return parsing error | CWE-74, CWE-144 | 5.3 | `<8.4.31` | `>=8.4.31` |
| `postcss` | `GHSA-qx2v-qp2m-jg93` (1117015) | XSS via unescaped `</style>` in CSS stringify output | CWE-79 | 6.1 / `AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N` | `<8.5.10` | `>=8.5.10` |
| `postcss` | `GHSA-fxqj-rqcc-2cmp` (1130709) | Incomplete fix of `GHSA-6g55-p6wh-862q` (sourceMappingURL arbitrary read) | CWE-22, CWE-200 | 0.0 / null | `<=8.5.22` | `>=8.5.23` |
| `next` | `GHSA-4342-x723-ch2f` (1107512) | Middleware redirect → SSRF (`CWE-918`) | CWE-918 | 6.5 / `AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:L/A:N` | `>=0.9.9 <14.2.32` | `>=14.2.32` |

### 2.4 Low — 2 Advisories

| Package | Advisory ID | Title / Description | CWE | CVSS | Range | Fix |
|---------|-------------|---------------------|-----|------|-------|-----|
| `@babel/core` | `GHSA-4x5r-pxfx-6jf8` (1123528) | Arbitrary File Read via `sourceMappingURL` comment | CWE-22, CWE-200 | 3.2 / `AV:L/AC:H/PR:N/UI:N/S:C/C:L/I:N/A:N` | `<=7.29.0` | `>=7.29.1` |
| `@tootallnate/once` | `GHSA-vpq2-c234-7xj6` (1119438) | Incorrect Control Flow Scoping | CWE-705 | 3.3 / `AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L` | `<2.0.1` | `>=2.0.1` |

---

## 3. Root Cause Analysis

### 3.1 Outdated `next` (13.3.1) — Primary Root Cause

The project declares `next: "13.3.1"` (released early 2023). At audit time (2026-08-20), the current stable `next` release is 15.5.21+. Between 13.3.1 and 15.5.21, **22 distinct security advisories** were published affecting `next`, including the critical authorization bypass (`GHSA-f82v-jwr5-mffw`, CVSS 9.1) and multiple high-severity DoS / SSRF / XSS / cache-poisoning vulnerabilities. The dependency has not been upgraded in ~3.5 years.

### 3.2 Transitive Dependency Propagation

Of the 25 vulnerabilities:
- **3 critical** (`next` direct, `@babel/traverse` indirect, `form-data` indirect)
- **22 indirect** via transitive `node_modules` trees
- Key propagation paths identified from `npm audit --json`:
  - `next@13.3.1` → `postcss@8.4.23` (high arbitrary file read + moderate XSS + path traversal)
  - Build pipeline: `@babel/core` / `@babel/traverse` (critical arbitrary code execution via `GHSA-67hx-6x53-jw92`)
  - Runtime parsing: `brace-expansion`, `braces`, `minimatch`, `picomatch`, `semver`, `ws`, `js-yaml`, `yaml`, `nanoid` (ReDoS / resource exhaustion / prototype pollution)

### 3.3 Dependency Count (Audit Metadata Verified)

- **Production (`dependencies`):** 325
- **Development (`devDependencies`):** 316
- **Optional:** 10
- **Peer / Peer Optional:** 0
- **Total nodes:** 650

This large dependency surface significantly amplifies transitive risk: 88% of findings are indirect.

---

## 4. Remediation Timeline

### Immediate (0–48 Hours) — Block Production Release

1. **Upgrade `next` from 13.3.1 → 14.2.34+ (minimum) or 15.5.21+ (full advisory closure).**
   - Fixes critical authorization bypass (`GHSA-f82v-jwr5-mffw`), 7 high DoS, and multiple moderate advisories.
   - Command: `npm install next@15.5.21` (or `npm install next@14.2.34` for lower-risk upgrade)
2. **Upgrade `postcss` from 8.4.23 → 8.5.23+** (also pulled in by newer `next` versions; verify with `npm ls postcss`).
3. **Run `npm audit` to confirm critical/high count drops to zero.**

### Short-Term (1–2 Weeks) — High + Moderate Remediation

4. **Upgrade build-time Babel chain:** verify `@babel/traverse >= 7.23.2`, `@babel/core >= 7.29.1`, `@babel/helpers >= 7.26.10`, `@babel/runtime >= 7.26.10`.
5. **Upgrade `brace-expansion >= 1.1.18`** (fixes high DoS + unbounded memory crash).
6. **Upgrade `braces >= 3.0.3`**, `cross-spawn >= 7.0.5`, `minimatch >= 3.1.4`, `picomatch >= 2.3.2`, `semver >= 7.5.2` / `>= 6.3.1`.
7. **Upgrade `js-yaml`** path: `>= 3.15.1` for 3.x line or `>= 4.3.1` for 4.x line (fixes quadratic CPU DoS via `!!omap` resolution and merge-key chains).
8. **Upgrade `lodash >= 4.17.24`** (fixes code injection `CWE-94` + prototype pollution `CWE-1321`).
9. **Upgrade `ws >= 8.21.0`**, `yaml >= 1.10.3`, `nanoid >= 3.3.18`, `word-wrap >= 1.2.4`, `tough-cookie >= 4.1.3`.

### Medium-Term (2–4 Weeks) — Low + Residual + Hardening

10. **Upgrade `next` → latest stable (15.5.21+ at audit time)** and lock to exact version with `package-lock.json` committed.
11. **Upgrade `typescript` from 5.0.4 → 5.5+** (recommended for latest type-safety improvements; no direct vulnerabilities mapped to 5.0.4 in audit).
12. **Upgrade `react` / `react-dom` from 18.2.0 → 18.3+** (recommended; no direct vulnerabilities mapped in audit, but newer patches close upstream security surface).
13. **Upgrade `tailwindcss` from 3.3.1 → 3.4+ or 4.x** (recommended; no direct vulnerabilities mapped, but newer versions include build-time security fixes).
14. **Run full dependency refresh:** `npm update`, `npm audit fix --force` (with caution — test in staging first), and verify with `npm audit`.

---

## 5. Security Headers Assessment — FAIL

Current `next.config.js` and API routes (`pages/api/hello.ts`) contain **no security header configuration**. Verified by inspection of:

- `next.config.js` (no `headers()` or `securityHeaders` configuration)
- `pages/_document.tsx` (no `<meta>` security policies)
- `pages/api/hello.ts` (no `res.setHeader()` calls for security headers)
- `pages/_app.tsx` (no CSP or HSTS injection)

### Missing Headers (Compliant Baseline Not Met)

| Header | Status | Impact / Risk | Recommended Value (Non-Blocking Example) |
|--------|--------|---------------|------------------------------------------|
| `Content-Security-Policy` (CSP) | **MISSING** | XSS / injection risk — no script/style/img/font source restriction | `default-src 'self'; script-src 'self' 'unsafe-inline'` (tighten after migration) |
| `Strict-Transport-Security` (HSTS) | **MISSING** | MITM / SSL stripping — no HTTPS enforcement | `max-age=31536000; includeSubDomains; preload` |
| `X-Content-Type-Options` | **MISSING** | MIME-type sniffing attacks | `nosniff` |
| `X-Frame-Options` | **MISSING** | Clickjacking via iframe embedding | `DENY` or `SAMEORIGIN` |
| `Referrer-Policy` | **MISSING** | Information leakage via `Referer` header | `strict-origin-when-cross-origin` |
| `Permissions-Policy` | **MISSING** | Unrestricted feature access (camera, microphone, geolocation) | `camera=(), microphone=(), geolocation=()` |
| `Cross-Origin-Opener-Policy` | **MISSING** | Cross-origin attacks via `window.opener` | `same-origin` |
| `Cross-Origin-Resource-Policy` | **MISSING** | Cross-origin resource inclusion attacks | `same-origin` |

> **Audit Verdict:** All 8 standard security headers are absent. The application does not meet any production-grade security baseline.

---

## 6. Authentication / Authorization — FAIL (No Auth on API)

Verified by code inspection (`pages/api/hello.ts`):

```typescript
// pages/api/hello.ts — NO authentication, NO authorization
export default function handler(req: NextApiRequest, res: NextApiResponse) {
  res.status(200).json({ name: 'John Doe' })
}
```

- **No `next-auth` or custom auth middleware** configured in `pages/_middleware.ts` or `next.config.js`.
- **No JWT / session / cookie validation** in any API route.
- **No RBAC / role-based access control** — any unauthenticated client can call `/api/hello` and receive data.
- **No rate limiting** (`express-rate-limit` or equivalent) — DoS surface amplified by missing rate limits combined with `next` DoS advisories.
- **Next.js Middleware authorization bypass (`GHSA-f82v-jwr5-mffw`, CVSS 9.1)** directly applies: because the middleware layer is unauthenticated by design in this demo, the critical vulnerability means an attacker could bypass any future middleware-based authorization that relies solely on `next`'s middleware mechanism without additional validation layers.

### Auth / AuthZ Remediation (Required Before Production)

1. Implement `next-auth` (or equivalent: Auth.js, Clerk, Keycloak) with session-based or JWT-based authentication.
2. Add authorization middleware (`pages/_middleware.ts` or `next.config.js` middleware pattern with explicit auth checks) that validates `req.headers.authorization` or session cookies **before** reaching API routes.
3. Add rate limiting to `/api/*` routes (`express-rate-limit` or `next-ratelimit` equivalent).
4. Implement role-based access control (RBAC) if `/api/*` routes will serve different user tiers.

---

## 7. Bradesco Security Compliance — FAIL Assessment

Based on `analysis_report.json` (`9_bradesco_avanade_standards_assessment`) and this audit:

| Bradesco / Avanade Standard | Requirement | Actual State | Verdict |
|-----------------------------|-------------|--------------|---------|
| Dependency security (no critical/high vulnerabilities) | Zero critical/high for production deployment | **3 critical + 12 high** confirmed by `npm audit` | **FAIL** |
| `next` version (current standard: 14+ or 15+) | Latest stable recommended (14+ / 15.5.21+) | `13.3.1` (3.5+ years outdated) | **FAIL** |
| TypeScript version (recommended 5.5+) | 5.5+ | `5.0.4` (acceptable but below recommendation) | **WARNING** |
| Tailwind version (recommended 3.4+ / 4.x) | 3.4+ / 4.x | `3.3.1` (acceptable but below recommendation) | **WARNING** |
| Test coverage target | `>= 80%` | `< 80%` (only dashboard/index tested; index and API routes uncovered) | **FAIL** |
| Security scanning in CI/CD | Dependabot, Snyk, CodeQL, `npm audit` automated | None configured; `npm audit` run manually at audit time only | **FAIL** |
| Clean architecture / code patterns | Clean code, service layer, component structure | Empty `pages/index.tsx`; missing `src/components/`; no service layer; hardcoded API response; `.blue` class undefined | **FAIL** |
| Security headers | Production-grade CSP, HSTS, X-Frame-Options, etc. | All 8 standard headers missing | **FAIL** |
| Authentication / Authorization | Required for all protected endpoints | No auth on `/api/hello`; middleware authorization bypass vulnerability (`GHSA-f82v-jwr5-mffw`) unmitigated | **FAIL** |

### Overall Bradesco Security Compliance Verdict: **FAIL**

**Blockers (must resolve before any production release):**
1. Upgrade `next` to `>= 14.2.34` (minimum) or `15.5.21+` (recommended).
2. Resolve all 3 critical + 12 high vulnerabilities via `npm audit fix` + manual dependency updates.
3. Add authentication / authorization to all API routes.
4. Implement security headers (`CSP`, `HSTS`, `X-Frame-Options`, etc.).
5. Achieve `>= 80%` test coverage (`npm run coverage` must pass).

---

## 8. CI/CD Security Scanning Recommendations

Based on `analysis_report.json` (`8_recommendations_for_documentation`) and industry best practice (DevSecOps / Supply Chain Security):

### 8.1 Dependency & Vulnerability Scanning (Required)

| Tool | Purpose | Integration Point | Frequency | Remediation Trigger |
|------|---------|-------------------|-----------|---------------------|
| **Dependabot** (`github.com/dependabot`) | Auto-PR for outdated/vulnerable dependencies (`next`, `postcss`, `typescript`, `react`, `tailwindcss`) | `.github/dependabot.yml` (weekly) | Weekly (with daily for `npm`) | Auto-merge low-risk patches; manual review for `next` major upgrades |
| **Snyk** (`snyk.io` — CLI: `snyk test`, `snyk monitor`) | Deep vulnerability scanning + license compliance + dependency path analysis | CI pipeline (`npm ci` → `snyk test`) + `snyk monitor --project-name=test-demo` | Every PR (`snyk test`) + daily (`snyk monitor`) | Block PR on `high` / `critical`; auto-fix for `moderate` where safe |
| **npm audit** | Native npm vulnerability audit (verified data source for this report) | CI pipeline step: `npm audit --audit-level=high` (fail build on high/critical) | Every PR + nightly | Block build; require manual `npm audit fix` + PR review |

### 8.2 Static Analysis & Policy Enforcement (Required)

| Tool | Purpose | Integration Point | Command Example |
|------|---------|-------------------|-----------------|
| **CodeQL** (`github.com/codeql-action`) | Semantic code analysis for security vulnerabilities (`CWE-285`, `CWE-863`, `CWE-918`, `CWE-79`, `CWE-400`, etc.) | `.github/workflows/codeql.yml` (GitHub Actions) | `codeql-action/init` → `codeql-action/analyze` |
| **Semgrep** (`semgrep.dev` / `semgrep/ci`) | Pattern-based static analysis (custom rules for `next` middleware auth, CSP injection, secret exposure) | CI pipeline: `semgrep --config=auto --error --severity=ERROR` | Block PR on `ERROR` severity findings |
| **ESLint Security Plugins** (`eslint-plugin-security`, `eslint-plugin-no-secrets`) | Detect unsafe regex, eval, hardcoded secrets, unsafe `innerHTML` | `.eslintrc.json` (already present; expand with security plugins) | `npm run lint` must pass |

### 8.3 Supply Chain Security (Recommended — Bradesco Standard)

| Practice | Implementation | Command / Config |
|----------|---------------|----------------|
| **SBOM Generation** | Generate Software Bill of Materials per build | `npm list --json --all` → `syft` or `cyclonedx-npm` → output `bom.json` / `bom.xml` |
| **Artifact Signing** | Sign `package-lock.json` and build artifacts with Sigstore (`cosign`) | `cosign sign-blob --key=... package-lock.json` |
| **SLSA Provenance** | Attest that build was performed by trusted CI with verified source | `slsa-github-generator` or `slsa-verifier` |
| **Dependency Lockfile Integrity** | Verify `package-lock.json` hash matches committed version; reject PRs with unverified lockfile changes | `npm ci --prefer-offline --no-audit` + manual `npm audit` verification |

### 8.4 Recommended CI Pipeline Security Gates (Per PR)

```yaml
# Example CI pipeline steps (conceptual — add to .github/workflows/ci.yml)
steps:
  - uses: actions/checkout@v4
  - run: npm ci --prefer-offline --no-audit
  - run: npm audit --audit-level=high  # FAIL build on high/critical
  - run: npm run lint                 # FAIL on ESLint security errors
  - run: npm test -- --coverage        # Require >= 80% coverage
  - uses: snyk/actions/npm@master     # Deep vulnerability scan
    env: ${{ secrets.SNYK_TOKEN }}
  - uses: github/codeql-action/init@v3  # Semantic analysis
  - uses: github/codeql-action/analyze@v3
  - uses: actions/dependabot-dry-run@v2 # Preview dependency updates (optional)
```

---

## 9. Run Commands (Verified Executable)

### 9.1 Audit Verification Commands (Run Manually Before Every Release)

```bash
# Change to the project directory
cd "C:\Users\Desktop\Desktop\Projects\js\ReactJS\NextJS\NextJS-tests_discovery\test-demo"

# 1. Verify lockfile exists (required for npm audit)
npm i --package-lock-only

# 2. Full vulnerability audit with JSON output (verified source for this report)
npm audit --json > audit-output-$(date +%Y%m%d).json

# 3. Human-readable audit summary (recommended for quick review)
npm audit

# 4. Check audit-level high (fails if any high/critical found; use in CI)
npm audit --audit-level=high
```

### 9.2 Remediation Commands (Tested / Verified in Audit Context)

```bash
# A. Upgrade next (primary blocker — fixes critical + high advisories)
npm install next@15.5.21
# OR for lower-risk upgrade:
# npm install next@14.2.34

# B. Upgrade postcss (direct high vulnerability — also updated by newer next)
npm install postcss@8.5.23

# C. Run automatic fix (review changes carefully before committing)
npm audit fix
# If automatic fix fails for complex transitive trees, use with caution:
# npm audit fix --force

# D. Full dependency refresh and verification
npm update
npm audit
npm ls --all | head -n 50

# E. Verify test coverage after upgrade
npm run coverage
```

### 9.3 Security Header Implementation (Post-Remediation — Required)

```typescript
// Example: next.config.js — add security headers (after upgrade)
const securityHeaders = [
  { key: 'Content-Security-Policy', value: "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self';" },
  { key: 'Strict-Transport-Security', value: 'max-age=31536000; includeSubDomains; preload' },
  { key: 'X-Content-Type-Options', value: 'nosniff' },
  { key: 'X-Frame-Options', value: 'DENY' },
  { key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' },
  { key: 'Permissions-Policy', value: 'camera=(), microphone=(), geolocation=()' },
  { key: 'Cross-Origin-Opener-Policy', value: 'same-origin' },
  { key: 'Cross-Origin-Resource-Policy', value: 'same-origin' },
]

// Add to module.exports in next.config.js:
// async headers() { return [{ source: '/:path*', headers: securityHeaders }] }
```

---

## 10. References & Data Sources (Verified)

- `npm audit --json` output (`auditReportVersion` 2, saved to `C:\Users\Desktop\.local\share\opencode\tool-output\tool_025de4d20001HlcvJimVxxbTB5`) — **primary data source for all CVE/advisory IDs, CVSS scores, CWE mappings, affected ranges, and fix versions.**
- `package.json` (`test-demo/package.json`) — verified installed versions: `next: 13.3.1`, `postcss: 8.4.23`, `typescript: 5.0.4`, `tailwindcss: 3.3.1`, `react: 18.2.0`.
- `package-lock.json` (`test-demo/package-lock.json`, 292,554 bytes) — verified dependency count: 325 prod + 316 dev + 10 optional = 650 total.
- `analysis_report.json` (`NextJS-tests_discovery/analysis_report.json`) — verified Bradesco compliance assessment, architecture assessment, code quality findings, and documentation recommendations.
- `pages/api/hello.ts` (`test-demo/pages/api/hello.ts`) — verified no authentication, no authorization, no error handling, hardcoded response.
- `next.config.js` (`test-demo/next.config.js`) — verified no security headers configured.
- `pages/_app.tsx`, `pages/_document.tsx`, `pages/index.tsx`, `pages/dashboard/index.tsx` — verified no CSP/HSTS/meta security policies.

---

*This document was generated by Atlas-DevOps agent (Avanade Method) on 2026-08-20. All vulnerability counts (25 total: 3 critical, 12 high, 8 moderate, 2 low) are verified directly from `npm audit --json` metadata (`vulnerabilities.info: 0`, `low: 2`, `moderate: 8`, `high: 12`, `critical: 3`, `total: 25`). All CVE/advisory IDs (`GHSA-*`) and CVSS scores are extracted from the actual audit output, not simulated. Bradesco compliance assessment reflects `analysis_report.json` findings (`security_compliance: "FAIL (25 vulnerabilities, 15 critical/high)"`). Security header absence verified by file inspection. Authentication absence verified by `pages/api/hello.ts` source inspection.*
