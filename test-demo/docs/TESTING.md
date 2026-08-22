# Testing Documentation

> **Project:** test-demo  
> **Last Updated:** 2026-08-21  
> **Test Quality Score:** 6/10

---

## 1. Test Stack Overview

| Tool | Version | Purpose |
|------|---------|---------|
| **Jest** | 29.5.0 | Test runner & assertion library |
| **@testing-library/react** | 14.0.0 | React component testing utilities |
| **@testing-library/jest-dom** | 5.16.5 | Custom Jest matchers for DOM assertions |
| **jest-environment-jsdom** | 29.5.0 | Browser-like DOM environment for tests |
| **next/jest** | Built-in (Next.js 13.3.1) | Next.js-aware Jest configuration |

---

## 2. Jest Configuration

### `jest.config.mjs`

```javascript
// jest.config.mjs
import nextJest from 'next/jest.js'

const createJestConfig = nextJest({
  // Load next.config.js and .env files into test environment
  dir: './',
})

/** @type {import('jest').Config} */
const config = {
  testEnvironment: 'jest-environment-jsdom',
  // setupFilesAfterEnv: ['<rootDir>/jest.setup.js'], // Optional: global test setup
}

export default createJestConfig(config)
```

### Key Integration Points

| Feature | Description |
|---------|-------------|
| **next/jest** | Wraps Jest config to auto-load `next.config.js`, TypeScript paths, and environment variables |
| **Path Aliases** | Resolves `@/` and `@Pages/` imports via `tsconfig.json` `paths` compiler option |
| **Environment** | `jest-environment-jsdom` provides `window`, `document`, `navigator` globals |
| **Transform** | Next.js SWC compiler handles TypeScript/TSX transformation automatically |

### `tsconfig.json` Path Aliases (for reference)

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@Pages/*": ["src/pages/*"]
    }
  }
}
```

---

## 3. Existing Test Analysis

### Test File: `test/pages/index.test.tsx`

```tsx
import DashboardIndexPage from "@Pages/dashboard";
import "@testing-library/jest-dom";
import { render, screen } from '@testing-library/react';

describe('Dashboard Page', () => {

  it("Shoud render properly", () => {
    render(<DashboardIndexPage />);

    const header = screen.getByRole('heading');
    const expected = 'Hello World :D';

    expect(header).toHaveTextContent(expected);
  });

  it("Should have a disable button", () => {
    render(<DashboardIndexPage />);

    const button = screen.getByRole('button');

    expect(button).toBeDisabled();
  });

  it("Should have a <p> Tag with className of blue", () => {
    render(<DashboardIndexPage />);

    const P = screen.getByTestId('paragraph-blue');
    expect(P).toHaveClass('blue');
    expect(P).toHaveTextContent("Pedro <:()");
  });
});
```

### Test Coverage Summary

| Metric | Value | Details |
|--------|-------|---------|
| **Files Tested** | 1 / 5 | Only `src/pages/dashboard/index.tsx` |
| **Statements** | 100% | 1/1 lines covered |
| **Branches** | N/A | 0 branches in tested file |
| **Functions** | 100% | 1/1 functions covered |
| **Lines** | 100% | 1/1 lines covered |

### Source File Under Test: `src/pages/dashboard/index.tsx`

```tsx
export default function DashboardIndexPage() {
  return (
    <div>
      <h1>Hello World :D</h1>

      <button disabled={true}>
        Click :D
      </button>

      <p data-testid="paragraph-blue" className="blue">
        {"Pedro <:()"}
      </p>
    </div>
  );
}
```

### Test Quality Assessment (6/10)

| Criterion | Score | Notes |
|-----------|-------|-------|
| **AC Coverage** | ✅ Pass | All visible UI elements verified |
| **Edge Cases** | ❌ Missing | No error states, empty props, boundary values |
| **Accessibility** | ❌ Missing | No `jest-axe` or semantic HTML validation |
| **Interactions** | ❌ Missing | No `user-event` click/keyboard tests |
| **Snapshots** | ❌ Missing | No regression snapshot testing |
| **API Routes** | ❌ Missing | `/api/hello` untested |
| **App/Document** | ❌ Missing | `_app.tsx`, `_document.tsx` untested |
| **Main Index** | ❌ Missing | `src/pages/index.tsx` untested |

---

## 4. Missing Test Categories

### 4.1 Home Page (`src/pages/index.tsx`)

```tsx
// Currently empty - no tests exist
import Image from 'next/image';
import { Inter } from 'next/font/google';

const inter = Inter({ subsets: ['latin'] });

export default function Home() {
  return <main />;
}
```

**Required Tests:**
- Font loading verification
- Image component rendering (if used)
- Metadata/SEO validation
- Layout structure

### 4.2 API Route (`src/pages/api/hello.ts`)

```tsx
// Untested API endpoint
export default function handler(req, res) {
  res.status(200).json({ name: 'John Doe' });
}
```

**Required Tests:**
- HTTP 200 response
- JSON shape validation
- Error handling (405 for non-GET)
- Request/response type safety

### 4.3 Custom App (`src/pages/_app.tsx`)

```tsx
// Global layout wrapper - untested
export default function App({ Component, pageProps }) {
  return <Component {...pageProps} />;
}
```

**Required Tests:**
- Global CSS injection
- Page transition behavior
- Context provider wrapping
- Error boundary integration

### 4.4 Custom Document (`src/pages/_document.tsx`)

```tsx
// HTML document structure - untested
export default function Document() {
  return (
    <Html lang="en">
      <Head />
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  );
}
```

**Required Tests:**
- Lang attribute
- Critical CSS inlining
- Script loading order
- Favicon/meta tags

---

## 5. Recommended Additions

### 5.1 Accessibility Testing (`jest-axe`)

```bash
npm install --save-dev jest-axe @testing-library/user-event
```

```tsx
// test/pages/index.test.tsx (addition)
import { axe, toHaveNoViolations } from 'jest-axe';

expect.extend(toHaveNoViolations);

it('should have no accessibility violations', async () => {
  const { container } = render(<DashboardIndexPage />);
  const results = await axe(container);
  expect(results).toHaveNoViolations();
});
```

### 5.2 User Interactions (`@testing-library/user-event`)

```tsx
import userEvent from '@testing-library/user-event';

it('should handle button click when enabled', async () => {
  const user = userEvent.setup();
  render(<DashboardIndexPage buttonEnabled={true} />);
  
  const button = screen.getByRole('button');
  await user.click(button);
  
  expect(button).toHaveBeenCalledTimes(1);
});
```

### 5.3 Snapshot Testing

```tsx
it('matches snapshot', () => {
  const { container } = render(<DashboardIndexPage />);
  expect(container).toMatchSnapshot();
});

// Update snapshots: npm test -- -u
```

### 5.4 API Mock Server (MSW)

```bash
npm install --save-dev msw
```

```tsx
// test/mocks/handlers.ts
import { rest } from 'msw';

export const handlers = [
  rest.get('/api/hello', (req, res, ctx) => {
    return res(ctx.json({ name: 'Mocked User' }));
  }),
];

// test/setupTests.ts
import { setupServer } from 'msw/node';
import { handlers } from './mocks/handlers';

export const server = setupServer(...handlers);
```

---

## 6. Test Commands

| Command | Description |
|---------|-------------|
| `npm test` | Run tests in **watch mode** (default) |
| `npm run coverage` | Run tests with **coverage report** (lcov, html, json) |
| `npm test -- --ci` | Run once in CI mode (no watch) |
| `npm test -- -u` | Update snapshots |
| `npm test -- --testPathPattern=index` | Run specific test file |

### Coverage Output Locations

```
coverage/
├── lcov.info          # LCOV format (CI integration)
├── coverage-final.json # Raw coverage data
├── clover.xml         # Clover XML (SonarQube)
└── lcov-report/       # HTML report (open index.html)
```

---

## 7. Test Structure Table

| Test Path | Target | Type | Status | Coverage |
|-----------|--------|------|--------|----------|
| `test/pages/index.test.tsx` | `src/pages/dashboard/index.tsx` | Component | ✅ 3 tests | 100% |
| `test/pages/api/hello.test.ts` | `src/pages/api/hello.ts` | API Route | ❌ Missing | 0% |
| `test/pages/_app.test.tsx` | `src/pages/_app.tsx` | App Wrapper | ❌ Missing | 0% |
| `test/pages/_document.test.tsx` | `src/pages/_document.tsx` | Document | ❌ Missing | 0% |
| `test/pages/home.test.tsx` | `src/pages/index.tsx` | Page | ❌ Missing | 0% |
| `test/components/` | Shared components | Unit | 📁 Empty dir | N/A |

---

## 8. CI/CD Integration Example

### GitHub Actions (`.github/workflows/test.yml`)

```yaml
name: Test & Coverage

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '18'
          cache: 'npm'
      - run: npm ci
      - run: npm run coverage
      - uses: codecov/codecov-action@v3
        with:
          files: ./coverage/lcov.info
```

---

## 9. Troubleshooting

| Issue | Solution |
|-------|----------|
| `Module not found: @Pages/...` | Verify `tsconfig.json` paths & `jest.config.mjs` uses `next/jest` |
| `TextEncoder not defined` | Ensure `jest-environment-jsdom` is installed and configured |
| `next/jest` not loading config | Check `dir: './'` points to project root with `next.config.js` |
| Coverage 0% for new files | Add files to `collectCoverageFrom` in Jest config |

---

## 10. References

- [Jest 29 Documentation](https://jestjs.io/docs/29.x/getting-started)
- [Testing Library React](https://testing-library.com/docs/react-testing-library/intro/)
- [Next.js Testing](https://nextjs.org/docs/app/building-your-application/testing)
- [jest-axe](https://github.com/nickcolley/jest-axe)
- [MSW - Mock Service Worker](https://mswjs.io/)
- [@testing-library/user-event](https://testing-library.com/docs/user-event/intro/)