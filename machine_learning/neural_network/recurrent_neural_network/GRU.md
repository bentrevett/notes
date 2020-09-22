# GRU

The gated recurrent unit (GRU) is a [[recurrent_neural_network]] architecture. 

The GRU is the similar to the [[LSTM]] in that it consists of multiple gates, but has fewer parameters overall.

$$\begin{aligned}
z_t &= \sigma_g(W_zx_t + U_zh_{t-1}+b_z)\\
r_t &= \sigma_g(W_rx_t + U_rh_{t-1}+b_r)\\
h_t &= z_t \circ h_{t-1} + (1 - z_t) \circ \sigma_h(W_hx_t+U_h(r_t \circ h_{t-1}) + b_h)
\end{aligned}$$

$x_t$ is the input, $h_t$ is the hidden state, $z_t$ and $r_t$ are the update and reset gate vectors. $\sigma_g$ is the [[sigmoid]] [[activation_function]] and $\sigma_h$ is the [[tanh]] [[activation_function]].

GRUs are apparently better than LSTMs on smaller datasets - probably due to the lower number of parameters - but have shown to be worse than LSTMs in [[neural_machine_translation]] tasks - see wikipedia link.

### Resources

- https://en.wikipedia.org/wiki/Gated_recurrent_unit