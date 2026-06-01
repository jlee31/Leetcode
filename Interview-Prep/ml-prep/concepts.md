# ML Concepts — Rapid Fire

Cover the answer, say yours out loud, then check. These are the ones that come
up again and again.

---

**Q: Bias–variance tradeoff?**
High bias = model too simple → underfits (high train & test error). High
variance = model too complex → overfits (low train, high test error). Total
error = bias² + variance + irreducible noise. Fixes for variance: more data,
regularization, simpler model. Fixes for bias: more features, more complex
model, less regularization.

**Q: L1 vs L2 regularization?**
Both penalize large weights. **L2 (ridge)** adds `λΣw²` → shrinks weights toward
0 smoothly, never exactly 0. **L1 (lasso)** adds `λΣ|w|` → drives some weights
*exactly* to 0 → feature selection / sparsity. L1's corner-shaped constraint
region is why it zeroes coefficients.

**Q: Why is accuracy a bad metric sometimes?**
Class imbalance. 99% negatives → predicting "negative" always = 99% accuracy but
useless. Use precision/recall/F1, or PR-AUC for rare positives.

**Q: Precision vs recall?**
Precision = TP/(TP+FP) — of those I flagged, how many were right. Recall =
TP/(TP+FN) — of all real positives, how many I caught. Tradeoff via the
threshold. F1 = harmonic mean. Pick based on cost of FP vs FN (spam filter:
precision; cancer screening: recall).

**Q: ROC-AUC vs PR-AUC?**
ROC plots TPR vs FPR; AUC = prob a random positive ranks above a random
negative. ROC can look optimistic under heavy imbalance — PR-AUC (precision vs
recall) is more informative when positives are rare.

**Q: How do you prevent overfitting?**
More data / augmentation, regularization (L1/L2, dropout), early stopping,
cross-validation, simpler model, ensembling. For NNs: dropout, batchnorm,
weight decay.

**Q: Bagging vs boosting?**
Bagging (random forest) trains many models in parallel on bootstrap samples,
averages → reduces **variance**. Boosting (GBDT, XGBoost) trains sequentially,
each correcting the previous one's errors → reduces **bias**, but more prone to
overfit and harder to parallelize.

**Q: Generative vs discriminative?**
Discriminative models P(y|x) directly (logistic reg, most NNs). Generative
models P(x,y) / P(x|y) (naive Bayes, GANs, diffusion). Generative can sample new
data; discriminative usually wins at pure classification.

**Q: Why ReLU over sigmoid in hidden layers?**
Sigmoid saturates → vanishing gradients for deep nets. ReLU has gradient 1 for
positive inputs → gradients flow, faster training. Downside: "dying ReLU" (stuck
at 0) → variants like LeakyReLU/GELU.

**Q: What is the vanishing/exploding gradient problem?**
In deep nets, gradients multiply through layers; <1 factors shrink to 0
(vanishing), >1 explode. Fixes: ReLU, careful init (He/Xavier), residual
connections, batchnorm, gradient clipping (for exploding), LSTMs/attention for
sequences.

**Q: SGD vs Adam?**
SGD (+momentum) is simple, often generalizes best with tuning. Adam adapts a
per-parameter learning rate (momentum + RMSProp) → fast convergence, less
tuning, popular default. Adam can generalize slightly worse; AdamW fixes weight
decay.

**Q: What is data leakage?**
Information from outside the training set (or from the target/future) sneaks into
features → over-optimistic offline metrics that collapse in production. Examples:
scaling before the train/test split, using a feature computed with future data.

**Q: Bias in train/test splitting — what to watch?**
Leakage, distribution shift, temporal data (must split by time, not randomly),
grouped data (don't split the same user across train/test).

**Q: Scaled dot-product attention (one line)?**
`Attention(Q,K,V) = softmax(QKᵀ/√d_k) · V` — each token attends to others via
query·key similarity; the `√d_k` keeps the dot products from growing large and
saturating softmax.

**Q: Handling class imbalance?**
Resampling (oversample minority/SMOTE, undersample majority), class weights in
the loss, threshold tuning, and metrics that don't hide the problem (PR-AUC, F1).

**Q: Bias vs fairness vs the bias term?**
Distinguish: statistical bias (model error), the bias *parameter* (the intercept
`b`), and fairness bias (disparate outcomes across groups). Interviewers
sometimes probe whether you conflate them.
