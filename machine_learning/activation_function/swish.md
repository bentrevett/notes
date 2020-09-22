# Swish 

Swish is an [[activation_function]].

$$f(x) = x \cdot \sigma(\beta x) = \frac{x}{1+e^{-\beta x}}$$

$\sigma(x)$ is the [[sigmoid]] function. $\beta$ is a hyperparameter, usually set to 1, although can also be a learnable parameter.

Interestingly, at $\beta=1$ the function is non-monotonic when $x<0$

When $\beta=1$, Swish is equal to the [[SiLU]]. 

### Resources

- https://arxiv.org/abs/1710.05941