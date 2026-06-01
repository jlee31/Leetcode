"""K-Means — fill in the TODOs.  Run: python3 starter.py"""
import numpy as np


class KMeans:
    def __init__(self, k, max_iters=100, seed=0):
        self.k = k
        self.max_iters = max_iters
        self.rng = np.random.default_rng(seed)
        self.centroids = None
        self.labels = None

    def fit(self, X):
        n = X.shape[0]
        # TODO: initialize centroids = k random rows of X
        for _ in range(self.max_iters):
            # TODO: assign step
            #   dists[i, j] = ||X[i] - centroids[j]||  -> labels = argmin over j
            # TODO: update step
            #   new_centroids[j] = mean of points with label j
            # TODO: if labels unchanged from last iter, break
            pass
        return self

    def predict(self, X):
        ...  # TODO: nearest-centroid assignment


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    blob = lambda cx, cy: rng.normal([cx, cy], 0.4, size=(100, 2))
    X = np.vstack([blob(0, 0), blob(5, 5), blob(0, 5)])

    km = KMeans(k=3).fit(X)
    print("centroids:\n", np.round(km.centroids, 2))
    # Should sit near (0,0), (5,5), (0,5) in some order.
