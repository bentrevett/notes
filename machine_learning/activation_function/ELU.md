# ELU

The exponential linear unit (ELU) is an [[activation_function]].

$$
f(x) = \begin{cases}
\alpha (e^x-1) & \text{for } x \le 0\\
x & \text{for } x > 0
\end{cases}$$

$\alpha$ is a hyperparamter, usually set to 1.0.

ELU is closely related to the [[SELU]] function.