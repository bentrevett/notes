# LSTM

Long short-term memory (LSTM) is a [[recurrent_neural_network]] architecture, similar to the [[GRU]]. It is used over traditional RNN architectures, such as the Elman network, as it handles the [[vanishing_gradient_problem]]. It does not solve the [[exploding_gradient_problem]], but this can be solved with [[gradient_clipping]].

As well as the standard hidden state, the LSTM contains a cell state and multiple gates which control the flow of information in to and out of the LSTM's internal memory.

$$\begin{aligned}
f_t &= \sigma_g(W_fx_t + U_fh_{t-1}+b_f)\\
i_t &= \sigma_g(W_ix_t + U_ih_{t-1}+b_i)\\
o_t &= \sigma_g(W_ox_t + U_oh_{t-1}+b_o)\\
\tilde{c}_t &= \sigma_h(W_cx_t + U_ch_{t-1}+b_c)\\
c_t &= f_t \circ c_{t-1} + i_t \circ \tilde{c}_t\\
h_t &= o_t \circ \sigma_h(c_t)
\end{aligned}$$

- $x_t$ is the input
- $f_t, i_t, o_t$ are the forget, input and output gates' activation vectors
- $h_t$ is the hidden state
- $c_t$ is the cell state and $\tilde{c}_t$ is the cell activation vector
- $\sigma_g$ is the [[sigmoid]] [[activation_function]]
- $\sigma_h$ is the [[tanh]] [[activation_function]]

The LSTM is commonly used in [[natural_language_processing]] tasks such as [[sentiment_analysis]], [[neural_machine_translation]] and [[language_modelling]].

### Resources

- https://en.wikipedia.org/wiki/Long_short-term_memory
- https://colah.github.io/posts/2015-08-Understanding-LSTMs/