# PReLU

The parameterized [[ReLU]] (PReLU) is an [[activation_function]].

$$
f(x) = \begin{cases}
\alpha x & \text{for } x \lt 0\\
x & \text{for } x \ge 0
\end{cases}$$

$\alpha$ is a learnable parameter which can either be the same across the whole channel or separate for each channel.

A variant of the PReLU where $\alpha$ is fixed to some constant is the [[leaky_ReLU]].

