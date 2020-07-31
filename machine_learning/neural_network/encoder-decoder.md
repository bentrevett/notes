# Encoder-Decoder

A [[neural_network|neural network]] architecture used for sequence-to-sequence learning, such as [[neural_machine_translation]] (NMT), and commonly uses a [[recurrent_neural_network]] (RNN) architecture such as an [[LSTM]] or a [[GRU]].

Usually consists of two neural networks. The first is an *encoder*, which takes in the input/source sequence and converts it into a context vector. The second is a *decoder*, which takes in the context vector and must produce the output/target sequence. We can think of the context vector as a summary of the input/source sequence.

The decoder is usually conditioned on the context vector, the previously decoded token, and - when using an RNN - the previous hidden state.

For NMT, it is common to use [[attention]], which requires multiple context vectors, one per token in the input sequence.

### Resources

- https://d2l.ai/chapter_recurrent-modern/encoder-decoder.html