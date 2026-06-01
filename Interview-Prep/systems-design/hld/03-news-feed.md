# HLD: Design a News Feed (e.g. Twitter/Instagram home timeline)

> Users follow others; the feed shows recent posts from followees, newest first.

## 1. Requirements

**Functional** — post; view a feed of followees' posts in (roughly) reverse-
chron order; follow/unfollow.

**Non-functional** — very read-heavy; feed load latency low (<200 ms);
eventual consistency is acceptable (a post can take seconds to appear);
massive fan-out for popular accounts.

## 2. Estimate

- Say 500M DAU, each opens the feed ~10×/day → ~50K–100K feed-reads/s.
- Posts/s far lower than reads/s → optimize the read path.

## 3. The core decision: fan-out

- **Fan-out on write (push)**: when A posts, push the post id into the
  precomputed feed of every follower (e.g. Redis list per user).
  - ✅ Feed read is a cheap lookup. ❌ A celebrity with 50M followers causes a
    write storm; wasteful for inactive followers.
- **Fan-out on read (pull)**: store posts per author; at read time, fetch
  followees' recent posts and merge.
  - ✅ Cheap writes; no wasted work. ❌ Expensive reads (merge many timelines).
- **Hybrid (the real answer)**: push for normal users; for celebrities, don't
  fan out — pull their posts at read time and merge into the precomputed feed.
  This is "the celebrity problem" and the interviewer wants this hybrid.

## 4. Data model & storage

- `posts(post_id, author_id, content, created_at)` — sharded by `post_id`.
- `follows(follower_id, followee_id)` — and a reverse index for fan-out.
- Precomputed feeds in Redis: `feed:{user_id}` → list of recent post ids
  (cap the length, e.g. last 800).

## 5. Architecture

- Write path: post → write to posts store → enqueue a fan-out job (Kafka) →
  workers push to followers' Redis feeds (skip celebrities).
- Read path: read `feed:{user}` from Redis → hydrate post ids → merge in any
  celebrity-followee posts pulled live → rank → return.
- Ranking: chronological is the baseline; mention ML ranking as an extension.

## 6. Tradeoffs / talking points

- Push vs pull vs hybrid, and *when* each wins (the celebrity threshold).
- Eventual consistency: it's fine if a post appears a few seconds late.
- Feed length cap and pagination (cursor on `created_at`/`post_id`).
- Hot-key and thundering-herd issues for viral posts; CDN for media.
