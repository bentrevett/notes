# Neural Network

A neural network (NN) is a connection of neurons (or nodes). In [[machine_learning]] we mainly mean artificial neural networks (ANNs) and not biological ones.

ANNs are made up of multiple layers. Each node in one layer is connected to each node in the subsequent layer. Connections between nodes have weights associated with them. The input to a node is the weighted sum of all of the inputs to that node plus a weighted bias term. The bias term is an extra node that always has a value of 1. This weighted sum usually has an [[activation_function]] applied.

[[deep_learning]] is a subsection of machine learning which focused on "deep" neural networks. A deep neural network is an artificial neural network with multiple layers between the input and output layers.

The weights and the biases together are called the parameters of the ANN. These weights and biases are learned via the [[backpropagation]] algorithm.

Other type of neural network architectures are the [[recurrent_neural_network]] and the [[convolutional_neural_network]].