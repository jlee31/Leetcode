# Systems Design Track

Two flavors of design interview:

- **HLD (high-level design)** — "Design a URL shortener." Whiteboard-level:
  requirements, APIs, data model, scaling, tradeoffs. See [hld/](hld/).
- **LLD (low-level design)** — "Implement an LRU cache / parking lot." Actual
  class design and working code. See [lld/](lld/).

## A framework for HLD (use this structure every time)

1. **Clarify & scope** (≈5 min) — functional vs non-functional requirements.
   Ask: read/write ratio? scale (DAU, QPS)? latency target? consistency needs?
2. **Estimate** — back-of-envelope: QPS, storage/year, bandwidth. State your
   assumptions out loud.
3. **API design** — the handful of endpoints, their inputs/outputs.
4. **Data model** — entities, schema, SQL vs NoSQL and *why*.
5. **High-level architecture** — boxes and arrows: clients → LB → services →
   cache → DB. Identify the write path and read path.
6. **Deep dive** — pick the 1–2 hardest components and go deep.
7. **Scale & bottlenecks** — caching, sharding/partitioning, replication, CDN,
   async/queues. Name the bottleneck before you "solve" it.
8. **Tradeoffs & failure modes** — CAP, consistency vs availability, what breaks
   and how you detect/recover.

## Concepts to have crisp

- **CAP / PACELC**, strong vs eventual consistency
- **Sharding** strategies (range, hash, consistent hashing) and hotspots
- **Caching** (cache-aside, write-through, write-back), eviction, invalidation
- **Load balancing** (L4 vs L7), **rate limiting** (token bucket, leaky bucket)
- **Queues / pub-sub** for decoupling and backpressure (Kafka-style)
- **Replication** (leader-follower, multi-leader), failover, quorum
- **Idempotency**, exactly-once vs at-least-once delivery

## HLD prompts (try one per session)

1. [URL Shortener](hld/01-url-shortener.md) — start here; great fundamentals.
2. [API Rate Limiter](hld/02-rate-limiter.md) — algorithms + distributed state.
3. [News Feed](hld/03-news-feed.md) — fan-out-on-write vs read; the celebrity
   problem.

## LLD exercises

1. [LRU Cache](lld/01-lru-cache/) — code it. O(1) get/put.
2. [Parking Lot](lld/02-parking-lot.md) — class design, no code required.
