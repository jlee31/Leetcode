# HLD: Design an API Rate Limiter

> Limit each client to N requests per time window across a fleet of servers.

## 1. Requirements

**Functional** — allow/deny a request given a client identifier; configurable
limits (e.g. 100 req/min per API key); return `429 Too Many Requests` with a
`Retry-After` header when exceeded.

**Non-functional** — low latency (it's on every request's hot path), accurate
*enough*, works across many app servers (distributed state), fault-tolerant
(fail open or closed — discuss).

## 2. Where does it run?

- Client-side (untrusted, easily bypassed) ❌
- **API gateway / middleware** (typical) ✅
- A dedicated rate-limit service called by the gateway.

## 3. Algorithms (know the tradeoffs)

| Algorithm | Idea | Pros | Cons |
|---|---|---|---|
| **Fixed window** | count per `(client, window)` | trivial | bursty at window edges (2× at boundary) |
| **Sliding window log** | store timestamps, count those in window | accurate | memory per request |
| **Sliding window counter** | weighted blend of current+previous window | smooths edges, cheap | approximate |
| **Token bucket** | tokens refill at rate r, cap b; each req takes 1 | allows bursts up to b | two params to tune |
| **Leaky bucket** | requests queue, drain at fixed rate | smooth output | no bursting, needs a queue |

Token bucket is the most common default answer — explain refill rate `r` and
burst capacity `b`.

## 4. Distributed state

- Counters/tokens live in **Redis** (fast, shared across app servers).
- Atomicity matters: a naive GET-then-SET races. Use `INCR` + `EXPIRE`, or a
  **Lua script** to make check-and-decrement atomic, or Redis `INCR` with TTL.
- Per-client key: `rl:{client_id}:{window}`.

## 5. Tradeoffs & failure modes

- **Fail open vs fail closed**: if Redis is down, do you allow all traffic
  (availability) or block it (protection)? Usually fail open for non-critical,
  fail closed for abuse-sensitive endpoints.
- **Latency**: a local in-memory tier + async sync to Redis reduces round-trips
  at the cost of slight inaccuracy.
- **Hot keys**: a single very busy client can hotspot one Redis shard.
- Return `429` + `Retry-After` and `X-RateLimit-Remaining` headers.

## Talking points

- Pick token bucket, justify it, and write the refill math.
- Explain the atomicity problem and the Lua-script/`INCR` fix.
- Address the multi-server consistency question explicitly — that's the crux.
