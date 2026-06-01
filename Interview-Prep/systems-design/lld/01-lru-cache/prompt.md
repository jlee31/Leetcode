# LLD: LRU Cache

Implement a Least-Recently-Used cache with **O(1)** `get` and `put`.

## Requirements

- `LRUCache(capacity)`.
- `get(key)` → value, or -1 (or a sentinel) if absent. A `get` counts as a use
  (makes the key most-recently-used).
- `put(key, value)` → insert/update. If at capacity, **evict the
  least-recently-used** key first. A `put` also marks the key most-recently-used.
- Both operations must be **O(1)**.

## The key insight

You need two structures working together:
1. A **hash map** for O(1) lookup by key.
2. A **doubly linked list** ordered by recency (most-recent at one end,
   least-recent at the other) for O(1) move-to-front and O(1) eviction from the
   back.

The map stores `key → node`; the node lives in the linked list.

## Design questions to answer out loud

1. Why not just a list/array? (move-to-front would be O(n).)
2. Why a *doubly* linked list, not singly? (O(1) removal needs the prev pointer.)
3. In Python, `collections.OrderedDict` gives this for free
   (`move_to_end` + `popitem(last=False)`) — but interviewers usually want the
   hand-rolled hashmap + DLL version. Do both.
4. How would you make it thread-safe? (a lock around get/put; discuss contention)

## Files

- `starter.py` — hand-roll the hashmap + doubly linked list.
- `solution.py` — full hand-rolled version **and** the OrderedDict shortcut.
