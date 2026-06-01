# HLD: Design a URL Shortener (e.g. bit.ly)

> Take 30–45 minutes. Work through the framework in the track README. Write your
> own answer first, then compare against the discussion below.

## 1. Requirements to clarify

**Functional**
- Shorten a long URL → short code; redirect short code → long URL.
- Optional: custom aliases, expiration, click analytics.

**Non-functional**
- Read-heavy: redirects ≫ creates (often ~100:1).
- Low-latency redirects (<100 ms). High availability. Links don't change once
  created (immutable).

## 2. Back-of-envelope (state your assumptions)

- Say 100M new URLs/month ≈ 40 writes/s; 100:1 read ratio ≈ 4,000 reads/s.
- 5 years × 100M/mo ≈ 6B URLs → need a key space ≥ 6B.
- base62 (`[A-Za-z0-9]`): 62^7 ≈ 3.5 trillion → **7-char codes** are plenty.
- Storage: ~6B × ~500 bytes ≈ 3 TB. Fits with room to spare.

## 3. API

```
POST /shorten        { "url": "...", "alias?": "...", "ttl?": ... } -> { "short": "..." }
GET  /{code}         -> 301/302 redirect to the long URL
```

## 4. Data model

`mappings(code PK, long_url, created_at, expires_at, owner_id)`. Lookups are
key-value by `code` → a KV store / NoSQL (DynamoDB, Cassandra) fits the access
pattern; a relational DB is also fine at this scale.

## 5. Generating the short code — the core design choice

- **Counter + base62 encode**: a global auto-increment id, base62-encoded. Needs
  a distributed counter (e.g. a range-allocator service, or ZooKeeper). Codes
  are sequential/guessable.
- **Random + collision check**: generate random 7 chars, check uniqueness,
  retry on collision (rare at this fill level). Simpler, unguessable.
- **Hash (MD5/SHA) + truncate**: hash the URL, take first 7 chars; handle
  collisions. Same URL → same code (dedup) unless you salt.

Discuss the tradeoffs: guessability, hotspots, coordination cost.

## 6. Architecture & scaling

- Clients → CDN/LB → stateless app servers → **cache (Redis)** in front of the DB.
- Redirects are the hot path: cache `code → long_url`; ~80/20 means the cache
  absorbs most reads. Cache-aside with a long TTL (mappings are immutable).
- Shard the DB by `code` (hash). Add read replicas.
- 301 (permanent) caches in browsers/CDN → fewer hits but breaks analytics;
  302 (temporary) lets you count every click. Discuss the tradeoff.
- Analytics: emit a click event to a queue (Kafka) → async aggregation; don't
  block the redirect.

## 7. Talking points the interviewer wants to hear

- Why a KV/NoSQL store fits (simple key lookup, horizontal scale).
- Cache strategy and why immutability makes caching easy.
- Collision handling for random codes.
- 301 vs 302 tradeoff.
- Custom alias uniqueness, abuse/rate-limiting, link expiration cleanup.
