"""Linear Regression via gradient descent — reference solution.
Run: python3 solution.py
"""
import numpy as np


class LinearRegressionGD:
    def __init__(self, lr=0.01, epochs=1000, l2=0.0):
        self.lr = lr
        self.epochs = epochs
        self.l2 = l2            # L2 regularization strength (0 = none)
        self.w = None
        self.b = 0.0
        self.history = []

    def fit(self, X, y):
        n, d = X.shape
        self.w = np.zeros(d)
        self.b = 0.0
        for _ in range(self.epochs):
            y_pred = X @ self.w + self.b
            error = y_pred - y                       # shape (n,)

            # MSE gradients. L2 adds 2*l2*w to the weight gradient (not bias).
            dw = (2 / n) * (X.T @ error) + 2 * self.l2 * self.w
            db = (2 / n) * error.sum()

            self.w -= self.lr * dw
            self.b -= self.lr * db

            mse = np.mean(error ** 2)
            self.history.append(mse)
        return self

    def predict(self, X):
        return X @ self.w + self.b


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    X = rng.normal(size=(200, 1))
    true_w, true_b = 3.0, -2.0
    y = true_w * X[:, 0] + true_b + rng.normal(scale=0.1, size=200)

    model = LinearRegressionGD(lr=0.1, epochs=500).fit(X, y)
    print("learned w:", np.round(model.w, 3), "b:", round(model.b, 3))
    print("final MSE:", round(model.history[-1], 5))
    assert abs(model.w[0] - true_w) < 0.1 and abs(model.b - true_b) < 0.1
    print("converged near true params ✓")

# Notes:
# - lr too big -> loss diverges/oscillates; too small -> crawls, may not finish.
# - Standardize features so all dims share a scale: GD converges far faster when
#   the loss surface isn't a stretched ellipse.
# - Batch GD (here) uses all data per step (stable, slow per epoch on big data).
#   SGD uses one sample (noisy, fast, helps escape shallow minima). Mini-batch
#   is the practical middle ground.
# - The closed form w = (XᵀX)^{-1} Xᵀy exists for linear regression, but GD is
#   what generalizes to models without a closed form — which is the point here.
