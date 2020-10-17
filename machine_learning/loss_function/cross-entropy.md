# Cross Entropy

For multi-class classification problems where the target is processed with [[one-hot_encoding].]

$$\text{CE}(\bm{\hat{y}}, \bm{y}) = - \sum_k y_k \log \hat{y}_k + (1-y_k)\log(1-\hat{y}_k)$$

$k$ is the number of classes. In this case, $\bm{\hat{y}}$ and $\bm{y}$ are [0, 1], usually achived by passing each through a [[sigmoid]] function.