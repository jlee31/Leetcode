"""K-Means (Lloyd's algorithm) — reference solution.  Run: python3 solution.py"""
import numpy as np


class KMeans:
    def __init__(self, k, max_iters=100, n_init=10, seed=0):
        self.k = k
        self.max_iters = max_iters
        self.n_init = n_init                   # restarts; keep the best result
        self.rng = np.random.default_rng(seed)
        self.centroids = None
        self.labels = None

    @staticmethod
    def _assign(X, centroids):
        # dists[i, j] = squared Euclidean distance from point i to centroid j.
        # Broadcasting: X[:, None, :] is (n,1,d), centroids[None] is (1,k,d).
        dists = ((X[:, None, :] - centroids[None, :, :]) ** 2).sum(axis=2)
        return dists.argmin(axis=1)            # nearest centroid per point

    def _single_run(self, X):
        n = X.shape[0]
        # Initialize: k distinct random points as centroids.
        centroids = X[self.rng.choice(n, size=self.k, replace=False)].copy()
        labels = None
        for _ in range(self.max_iters):
            new_labels = self._assign(X, centroids)
            if labels is not None and np.array_equal(new_labels, labels):
                break                          # converged: no point switched
            labels = new_labels
            for j in range(self.k):
                members = X[labels == j]
                if len(members):               # guard against empty clusters
                    centroids[j] = members.mean(axis=0)
        return centroids, labels

    def fit(self, X):
        # Lloyd's only finds a LOCAL optimum, and a bad random init can split
        # one true cluster while merging two others. Run n_init times from
        # different seeds and keep the run with the lowest inertia.
        best_inertia = np.inf
        for _ in range(self.n_init):
            centroids, labels = self._single_run(X)
            inertia = ((X - centroids[labels]) ** 2).sum()
            if inertia < best_inertia:
                best_inertia = inertia
                self.centroids, self.labels = centroids, labels
        return self

    def predict(self, X):
        return self._assign(X, self.centroids)

    def inertia(self, X):
        """Within-cluster sum of squared distances — the k-means objective."""
        d = ((X - self.centroids[self.labels]) ** 2).sum()
        return d


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    blob = lambda cx, cy: rng.normal([cx, cy], 0.4, size=(100, 2))
    X = np.vstack([blob(0, 0), blob(5, 5), blob(0, 5)])

    km = KMeans(k=3).fit(X)
    print("centroids:\n", np.round(km.centroids, 2))
    print("inertia:", round(km.inertia(X), 2))

    # Each true center should be matched by some learned centroid.
    truth = np.array([[0, 0], [5, 5], [0, 5]])
    for t in truth:
        nearest = np.min(((km.centroids - t) ** 2).sum(axis=1))
        assert nearest < 0.5, f"no centroid near {t}"
    print("recovered all three blobs ✓")

# Notes:
# - Objective = inertia (within-cluster SSE). Lloyd's only finds a LOCAL min;
#   the random init can land badly -> this solution runs n_init restarts and
#   keeps the lowest-inertia result (what sklearn does by default). k-means++
#   (spread initial centroids by distance) is the other standard remedy.
# - Choose k via the elbow (inertia vs k) or silhouette score.
# - Standardize features first: k-means uses raw Euclidean distance, so an
#   unscaled large-range feature dominates the clustering.
