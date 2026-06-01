# ML Interview Prep Track

Three things ML interviews test, mapped to three sub-folders:

- **Concepts** — rapid-fire fundamentals. [concepts.md](concepts.md).
- **Implement-from-scratch** — code a model/algorithm with just NumPy, no
  sklearn. [from-scratch/](from-scratch/).
- **ML system design** — "Design YouTube recommendations." Like systems design
  but ML-specific (data, features, training, serving, metrics).
  [ml-system-design/](ml-system-design/).

## Setup

```bash
python3 -m pip install numpy        # the from-scratch exercises use only numpy
```

## What to be able to do cold

- Explain **bias–variance tradeoff**, over/underfitting, and 3 fixes for each.
- Derive/code **gradient descent** for linear & logistic regression.
- Explain **regularization** (L1 vs L2: sparsity vs shrinkage) and why.
- **Evaluation**: precision/recall/F1, ROC-AUC vs PR-AUC, when accuracy lies
  (class imbalance), train/val/test + cross-validation, data leakage.
- **Trees & ensembles**: bagging vs boosting, random forest vs gradient boosting.
- Basics of **neural nets**: backprop intuition, activation functions, why ReLU,
  vanishing gradients, batchnorm/dropout, Adam vs SGD.
- **Transformers/attention** at a high level (scaled dot-product attention).

## From-scratch exercises

1. [Linear Regression via Gradient Descent](from-scratch/01-linear-regression-gd/)
2. [K-Means Clustering](from-scratch/02-kmeans/)

## ML system design

1. [Recommendation System](ml-system-design/01-recommendation.md)

## A framework for ML system design

1. **Clarify the problem & framing** — is it classification/ranking/regression?
   What's the business metric vs the ML metric?
2. **Data** — sources, labels (how do you get ground truth?), volume, freshness.
3. **Features** — user/item/context features; embeddings; feature store.
4. **Model** — baseline first (logistic reg / GBDT), then deep models. Justify.
5. **Training** — offline pipeline, retraining cadence, handling skew.
6. **Serving** — online inference latency, candidate generation → ranking,
   batch vs real-time, caching.
7. **Evaluation** — offline metrics + **online A/B test**; guardrail metrics.
8. **Iteration & monitoring** — drift, feedback loops, cold start.
