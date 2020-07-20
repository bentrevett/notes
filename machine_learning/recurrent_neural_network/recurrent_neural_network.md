# Recurrent Neural Network

A recurrent neural network (RNN) is a type of [[neural_network]] with recurrent connections, i.e. they are a directed graph whereas standard neural networks are a directed acyclic graph.

At each time-step the RNN takes in both the current input, $x_t$, as well as the previous hidden state, $h_{t-1}$, and returns the current hidden state, $h_t$. 

We can think of the hidden state as an internal memory structure, containing all relevant information from the sequence so far. What the RNN deems relevant information depends on the features it has learned to extract for the task at hand via [[backpropagation]].

The recurrent connections makes RNNs suitable for temporal tasks, i.e. the order of the elements within a sequence matters.

The most basic RNN algorithm is the Elman network

$$h_t = \sigma (W_hx_t+U_hh_{t-1}+b_h)$$

Elman RNNs suffer from both the [[exploding_gradient_problem]] and the [[vanishing_gradient_problem]] so typically RNN variants such as the [[LSTM]] and the [[GRU]] are used.