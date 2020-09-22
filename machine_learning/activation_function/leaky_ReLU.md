# Leaky ReLU

The leaky ReLU is an [[activation_function]]. It is a variant of the [[ReLU]] activation function.

$$
f(x) = \begin{cases}
\alpha x & \text{for } x \lt 0\\
x & \text{for } x \ge 0
\end{cases}$$

$\alpha$ is a hyperparameter, usually set to around 0.01. The leaky ReLU is also related to the [[PReLU]] function. In the PReLU function the parameter $\alpha$ is learnable.