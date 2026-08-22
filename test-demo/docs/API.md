# API Reference: `/api/hello`

> **Status:** Legacy Pages Router API Route — [Migration Path](#migration-to-app-router-route-handlers)  
> **Version:** v1.0.0  
> **Last Updated:** 2026-08-21

---

## Badges

![API Version](https://img.shields.io/badge/version-v1.0.0-blue)
![Status](https://img.shields.io/badge/status-legacy-orange)
![Next.js](https://img.shields.io/badge/Next.js-13%2B-black)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Overview

The `/api/hello` endpoint is a simple **GET-only** API route implemented using Next.js **Pages Router** (`pages/api/hello.ts`). It returns a static JSON response with a hardcoded name.

**Use Case:** Demo/health-check endpoint for verifying API routing works.

---

## OpenAPI 3.1 Specification

```yaml
openapi: 3.1.0
info:
  title: test-demo API
  version: v1.0.0
  description: Simple hello world API endpoint
servers:
  - url: http://localhost:3000
    description: Development server
  - url: https://your-domain.com
    description: Production server
paths:
  /api/hello:
    get:
      summary: Returns a greeting
      description: Returns a static JSON object with a hardcoded name
      operationId: getHello
      tags:
        - health-check
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Data'
        '405':
          description: Method not allowed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Data:
      type: object
      required:
        - name
      properties:
        name:
          type: string
          example: "John Doe"
          description: Hardcoded greeting name
    ErrorResponse:
      type: object
      required:
        - error
      properties:
        error:
          type: string
          example: "Method Not Allowed"
```

---

## Endpoint Details

| Property | Value |
|----------|-------|
| **HTTP Method** | `GET` |
| **Path** | `/api/hello` |
| **Content-Type** | `application/json` |
| **Authentication** | None |
| **Rate Limiting** | None |

### Headers

#### Request Headers

| Header | Required | Description |
|--------|----------|-------------|
| `Accept` | No | `application/json` (default) |
| `User-Agent` | No | Client identifier |

#### Response Headers

| Header | Value | Description |
|--------|-------|-------------|
| `Content-Type` | `application/json; charset=utf-8` | JSON response |
| `Cache-Control` | `no-store, max-age=0` | Prevents caching (Next.js default) |
| `X-Powered-By` | `Next.js` | Framework identifier |

---

## TypeScript Interfaces

Extracted directly from `src/pages/api/hello.ts`:

```typescript
// File: src/pages/api/hello.ts
import type { NextApiRequest, NextApiResponse } from 'next'

/**
 * Response payload shape
 */
type Data = {
  name: string
}

/**
 * API Route Handler
 * @param req - Next.js API Request object (extends IncomingMessage)
 * @param res - Next.js API Response object (extends ServerResponse)
 */
export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {
  res.status(200).json({ name: 'John Doe' })
}
```

### Type Definitions

#### `NextApiRequest` (from `next`)

```typescript
interface NextApiRequest extends IncomingMessage {
  query: { [key: string]: string | string[] | undefined }
  cookies: { [key: string]: string }
  body: any
  method?: string
  headers: IncomingHttpHeaders
  preview?: boolean
  previewData?: any
}
```

#### `NextApiResponse<Data>` (from `next`)

```typescript
interface NextApiResponse<Data> extends ServerResponse {
  status(code: number): this
  json(body: Data): this
  send(body: string | Buffer): this
  redirect(url: string): this
  redirect(status: number, url: string): this
  setHeader(name: string, value: string | number | string[]): this
  getHeader(name: string): string | number | string[] | undefined
}
```

---

## Example Requests & Responses

### cURL

```bash
# Basic request
curl -X GET http://localhost:3000/api/hello \
  -H "Accept: application/json"

# Verbose output (shows headers)
curl -v -X GET http://localhost:3000/api/hello

# With explicit method (GET is default)
curl -X GET http://localhost:3000/api/hello \
  -H "Accept: application/json" \
  -H "User-Agent: test-client/1.0"
```

### JavaScript/TypeScript (fetch)

```typescript
// Modern fetch API
async function fetchHello(): Promise<Data> {
  const response = await fetch('/api/hello', {
    method: 'GET',
    headers: {
      'Accept': 'application/json',
    },
  })

  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`)
  }

  return response.json()
}

// Usage
const data = await fetchHello()
console.log(data) // { name: "John Doe" }
```

### Response Examples

#### Success (200 OK)

```json
{
  "name": "John Doe"
}
```

#### Method Not Allowed (405)

```json
{
  "error": "Method Not Allowed"
}
```

---

## Quality Issues Analysis

> **Severity Legend:** 🔴 Critical | 🟠 High | 🟡 Medium | 🟢 Low

| # | Issue | Severity | Location | Description | Recommendation |
|---|-------|----------|----------|-------------|----------------|
| 1 | **Hardcoded Response** | 🟠 High | Line 12 | Returns static `{ name: 'John Doe' }` — no dynamic behavior | Accept query param or path param for name |
| 2 | **No Input Validation** | 🔴 Critical | Lines 8-12 | Ignores `req.query`, `req.body`, `req.method` entirely | Validate `req.method === 'GET'`, sanitize inputs |
| 3 | **No Error Handling** | 🔴 Critical | Lines 8-12 | No try/catch, no fallback for unexpected errors | Wrap in try/catch, return 500 on failure |
| 4 | **No Authentication** | 🟠 High | N/A | Endpoint is publicly accessible | Add auth middleware (NextAuth, JWT, API key) |
| 5 | **No Rate Limiting** | 🟡 Medium | N/A | Unlimited requests possible | Implement rate limiting (Upstash, Redis, Vercel Edge) |
| 6 | **No CORS Configuration** | 🟡 Medium | N/A | Relies on Next.js defaults (same-origin) | Explicit CORS headers if cross-origin needed |
| 7 | **No Request Logging** | 🟢 Low | N/A | No observability/tracing | Add structured logging (Pino, Winston) |
| 8 | **No API Versioning** | 🟢 Low | Path | Version not in path or header | Use `/api/v1/hello` or `Accept-Version` header |
| 9 | **No OpenAPI Spec** | 🟢 Low | N/A | No machine-readable contract | Generate from code or write manually |
| 10 | **No Tests** | 🟡 Medium | N/A | No unit/integration tests | Add Vitest/Jest tests for handler |

---

## Migration to App Router Route Handlers

> **Target:** Next.js 13+ App Router (`app/api/hello/route.ts`)

### Current (Pages Router)

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

### Migrated (App Router Route Handler)

```typescript
// src/app/api/hello/route.ts
import { NextRequest, NextResponse } from 'next/server'

interface Data {
  name: string
}

export async function GET(request: NextRequest): Promise<NextResponse<Data>> {
  try {
    // Optional: Extract query params
    const { searchParams } = new URL(request.url)
    const name = searchParams.get('name') ?? 'John Doe'

    // Optional: Validate input
    if (name.length > 100) {
      return NextResponse.json(
        { error: 'Name too long' } as const,
        { status: 400 }
      )
    }

    // Optional: Rate limiting check here

    return NextResponse.json({ name }, { status: 200 })
  } catch (error) {
    console.error('[GET /api/hello]', error)
    return NextResponse.json(
      { error: 'Internal Server Error' } as const,
      { status: 500 }
    )
  }
}

// Explicitly disable other methods
export async function POST(): Promise<NextResponse> {
  return NextResponse.json(
    { error: 'Method Not Allowed' } as const,
    { status: 405, headers: { Allow: 'GET' } }
  )
}
```

### Key Migration Changes

| Aspect | Pages Router | App Router |
|--------|--------------|------------|
| **File Location** | `pages/api/hello.ts` | `app/api/hello/route.ts` |
| **Request Type** | `NextApiRequest` | `NextRequest` (Web Fetch API) |
| **Response Type** | `NextApiResponse` | `NextResponse` (Web Fetch API) |
| **Handler Signature** | `export default function handler(req, res)` | `export async function GET(request)` |
| **Async Support** | Callback-based | Native `async/await` |
| **Streaming** | Not supported | Supported via `ReadableStream` |
| **Edge Runtime** | Manual config | `export const runtime = 'edge'` |

### Incremental Migration Steps

1. **Create new route handler** at `app/api/hello/route.ts`
2. **Add feature parity** (query params, validation, error handling)
3. **Write tests** for new handler
4. **Deploy to staging** behind feature flag
5. **Switch traffic** (update rewrites/middleware)
6. **Remove old** `pages/api/hello.ts`
7. **Update documentation** and OpenAPI spec

---

## Security Considerations

### Current Vulnerabilities

| Vulnerability | CWE | Risk | Mitigation |
|---------------|-----|------|------------|
| **Missing Authentication** | CWE-306 | 🔴 Critical | Implement auth (NextAuth.js, JWT, API Keys) |
| **Missing Authorization** | CWE-285 | 🔴 Critical | Add RBAC/ABAC checks per endpoint |
| **No Rate Limiting** | CWE-770 | 🟠 High | Upstash Rate Limit, Vercel Edge Config, Redis |
| **No Input Validation** | CWE-20 | 🟠 High | Zod, Valibot, or manual validation on `req.query`/`req.body` |
| **No Output Encoding** | CWE-116 | 🟡 Medium | `NextResponse.json()` auto-escapes, but verify |
| **Information Exposure** | CWE-200 | 🟡 Medium | Remove `X-Powered-By`, sanitize error messages |
| **Missing Security Headers** | CWE-693 | 🟢 Low | Add `Content-Security-Policy`, `X-Frame-Options`, etc. |

### Recommended Security Headers

```typescript
// In route.ts or middleware.ts
const securityHeaders = {
  'X-Content-Type-Options': 'nosniff',
  'X-Frame-Options': 'DENY',
  'X-XSS-Protection': '1; mode=block',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  'Permissions-Policy': 'camera=(), microphone=(), geolocation=()',
  'Content-Security-Policy': "default-src 'self'; script-src 'self' 'unsafe-inline'",
}
```

### Rate Limiting Example (App Router)

```typescript
// lib/rate-limit.ts
import { Ratelimit } from '@upstash/ratelimit'
import { Redis } from '@upstash/redis'

export const ratelimit = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.slidingWindow(10, '10 s'), // 10 requests per 10 seconds
  analytics: true,
})

// In route.ts
import { ratelimit } from '@/lib/rate-limit'
import { NextRequest, NextResponse } from 'next/server'

export async function GET(request: NextRequest) {
  const ip = request.ip ?? 'anonymous'
  const { success, limit, reset, remaining } = await ratelimit.limit(ip)

  if (!success) {
    return NextResponse.json(
      { error: 'Too Many Requests' },
      { status: 429, headers: { 'Retry-After': String(reset) } }
    )
  }

  return NextResponse.json({ name: 'John Doe' }, {
    headers: {
      'X-RateLimit-Limit': String(limit),
      'X-RateLimit-Remaining': String(remaining),
      'X-RateLimit-Reset': String(reset),
    }
  })
}
```

---

## Testing Checklist

- [ ] Unit test: Returns 200 with correct JSON shape
- [ ] Unit test: Returns 405 for non-GET methods
- [ ] Integration test: Full request/response cycle
- [ ] Load test: Verify rate limiting (if implemented)
- [ ] Security test: Auth bypass attempts
- [ ] Contract test: OpenAPI spec matches implementation

---

## Related Documentation

| Document | Description |
|----------|-------------|
| [ARCHITECTURE.md](./ARCHITECTURE.md) | System architecture overview |
| [TESTING.md](./TESTING.md) | Testing strategies and examples |
| [Next.js API Routes Docs](https://nextjs.org/docs/pages/building-your-application/routing/api-routes) | Official Pages Router API routes guide |
| [Next.js Route Handlers](https://nextjs.org/docs/app/building-your-application/routing/route-handlers) | Official App Router route handlers guide |

---

## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v1.0.0 | 2026-08-21 | Paige | Initial documentation from source code |

---

> **Document Owner:** Paige (Technical Writer)  
> **Review Cycle:** Quarterly or on API changes  
> **Source of Truth:** `src/pages/api/hello.ts` → `src/app/api/hello/route.ts` (post-migration)