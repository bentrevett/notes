# Compositional Attention Networks for Machine Reasoning

Main point of novelity is the MAC (Memory, Attention and Composition) cell - a type of RNN with built in self-attention mechanisms. Learns with "significantly less data" than other RNN approaches - e.g. LSTM - because of its "strong structural priors to wards compositional reasoning". See fig 3.

Extracts relevant information from a "knowledge base" (K, image) given a "task description" (q, natural language) by iteratively performing computation. See fig 1.

q is fed through an embedding layer and then a biLSTM and also a linear transform. K is fed through a frozen pre-trained ResNet101 with two CNN layers added on. The actual units in the MAC cell are basically their own LSTMs - each is not too complicated.

Need to see how many parameters are used - assume parameters are shared across time-steps like in RNNs (they are).

Their main focus is on the CLEVR dataset which are objects + questions that require reasoning but are usually grammatically simple. Real life problem will be to try and understand the implicit meaning of the text - does this require "reasoning" steps? Or just more expressive representations of the text?

See appendix for implementation details. Also has an official implementation in TF.
