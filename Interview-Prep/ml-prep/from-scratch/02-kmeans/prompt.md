# From Scratch: K-Means Clustering

Implement Lloyd's k-means algorithm with NumPy. Unsupervised: group `n` points
into `k` clusters by minimizing within-cluster squared distance.

## The algorithm (Lloyd's)

1. **Initialize** k centroids (random points, or k-means++).
2. **Assign**: each point → nearest centroid (Euclidean).
3. **Update**: each centroid → mean of its assigned points.
4. Repeat 2–3 until assignments stop changing (or max iters).

## Requirements

- `fit(X, k, max_iters)` → final centroids + labels.
- Detect convergence (labels unchanged) and stop early.
- Run on a synthetic dataset with well-separated blobs and confirm it recovers
  them.

## Questions to answer out loud

1. What objective does k-means minimize? (within-cluster sum of squares / inertia)
2. Why can it get stuck in a bad local optimum? How does **k-means++** init or
   multiple restarts help?
3. How do you choose `k`? (elbow method on inertia, silhouette score)
4. What are k-means' assumptions/limits? (spherical, equal-size clusters;
   sensitive to scale → standardize; bad for non-convex shapes → DBSCAN/spectral)
5. Complexity per iteration? (O(n·k·d))
