"""Linear Regression via gradient descent — fill in the TODOs.
Run: python3 starter.py
"""
import numpy as np


class LinearRegressionGD:
    def __init__(self, lr=0.01, epochs=1000):
        self.lr = lr
        self.epochs = epochs
        self.w = None
        self.b = 0.0
        self.history = []

    def fit(self, X, y):
        n, d = X.shape
        self.w = np.zeros(d)
        self.b = 0.0
        for _ in range(self.epochs):
            # TODO: y_pred = X @ self.w + self.b
            # TODO: error = y_pred - y
            # TODO: dw = (2/n) * X.T @ error
            # TODO: db = (2/n) * error.sum()
            # TODO: gradient step on self.w, self.b
            # TODO: record MSE in self.history
            pass
        return self

    def predict(self, X):
        ...  # TODO


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    X = rng.normal(size=(200, 1))
    true_w, true_b = 3.0, -2.0
    y = true_w * X[:, 0] + true_b + rng.normal(scale=0.1, size=200)

    model = LinearRegressionGD(lr=0.1, epochs=500).fit(X, y)
    print("learned w:", model.w, "b:", model.b)   # ~[3.0], ~-2.0
    print("final MSE:", model.history[-1])
