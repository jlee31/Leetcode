# ML System Design: Recommendation System (e.g. YouTube/Netflix)

> Recommend items (videos) a user is likely to engage with. Use the ML system
> design framework in the track README.

## 1. Problem framing

- Clarify the objective: watch time? clicks? long-term retention? These conflict
  — optimizing clicks alone breeds clickbait. Usually a **ranking** problem with
  a blended objective.
- ML metric (AUC, NDCG) vs business metric (watch time, DAU). Name both.

## 2. Two-stage architecture (the standard answer)

Serving millions of items per request at low latency is impossible to rank
exhaustively, so split it:

1. **Candidate generation (retrieval)** — narrow millions → ~hundreds. Cheap,
   high-recall. Techniques: collaborative filtering / matrix factorization,
   two-tower embedding model (user tower + item tower, approximate nearest
   neighbor lookup), co-visitation.
2. **Ranking** — score those hundreds precisely with a heavier model (GBDT or
   deep net) using rich features. Optimize the blended objective.
3. (Optional) **Re-ranking** — diversity, freshness, business rules, dedup.

## 3. Data & labels

- Implicit feedback (clicks, watch %, skips) ≫ explicit ratings. Watch-time
  thresholds define positive labels; design negatives carefully (impressed but
  not clicked, plus random negatives).
- Beware **feedback loops**: the model influences what's shown, which becomes
  training data. Add exploration.

## 4. Features

- **User**: history, demographics, context (time, device).
- **Item**: metadata, age, popularity, embeddings.
- **User×Item interaction**: past affinity, same-author watched, etc.
- Embeddings for high-cardinality IDs. A **feature store** for train/serve
  consistency (avoid training-serving skew).

## 5. Models

- Baseline: popularity + collaborative filtering (matrix factorization).
- Retrieval: two-tower neural net → ANN index (FAISS/ScaNN).
- Ranking: GBDT (strong baseline) → deep models (wide & deep, DLRM).
- Cold start: content-based features for new items; onboarding signals for new
  users.

## 6. Evaluation

- Offline: AUC / NDCG / recall@k on held-out data; **split by time**.
- Online: **A/B test** on real metrics (watch time, retention) with guardrails
  (don't tank diversity or short-term satisfaction). Offline wins don't always
  hold online — emphasize this.

## 7. Serving & ops

- Retrieval embeddings precomputed; ANN at request time; ranking model behind a
  low-latency service; cache candidates per user for a short TTL.
- Retraining cadence (daily/hourly) for freshness; monitor for drift,
  popularity bias, and degenerate feedback loops.

## Talking points the interviewer wants

- The **two-stage retrieval → ranking** split and *why* (latency/scale).
- Implicit feedback + negative sampling + feedback loops.
- Offline vs online evaluation and the **A/B test** as ground truth.
- Cold start and training-serving skew.
