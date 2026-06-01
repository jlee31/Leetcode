# From Scratch: Linear Regression via Gradient Descent

Implement linear regression trained with batch gradient descent — NumPy only,
no sklearn. This tests whether you understand the loss, the gradient, and the
update rule, not just the API.

## The math

- Model: `ŷ = Xw + b` (or fold `b` into `w` with a bias column).
- Loss (MSE): `L = (1/n) Σ (ŷ_i − y_i)²`.
- Gradients:
  - `∂L/∂w = (2/n) Xᵀ (ŷ − y)`
  - `∂L/∂b = (2/n) Σ (ŷ − y)`
- Update: `w ← w − α · ∂L/∂w`, `b ← b − α · ∂L/∂b`.

## Requirements

- `fit(X, y, lr, epochs)` — run gradient descent; track loss per epoch.
- `predict(X)`.
- Verify it converges on a synthetic linear dataset and the recovered `w`, `b`
  are close to the true values.

## Questions to answer out loud

1. Why MSE and not MAE here? (differentiable everywhere; what MAE gives you.)
2. What happens if the learning rate is too big? Too small?
3. Why standardize features before GD? (conditioning / convergence speed.)
4. Batch vs stochastic vs mini-batch GD — tradeoffs.
5. How would you add L2 regularization to the gradient?
