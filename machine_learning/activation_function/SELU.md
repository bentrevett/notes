# SELU

The scaled exponential linear unit (SELU) is an [[activation_function]].

$$
f(x) = \lambda \begin{cases}
\alpha (e^x - 1) & \text{for } x \lt 0\\
x & \text{for } x \ge 0
\end{cases}$$

$\lambda = 1.0507$ and $\alpha = 1.67326$. 

SELU is closely related to the [[ELU]] function.

### Resources

- https://arxiv.org/abs/1706.02515