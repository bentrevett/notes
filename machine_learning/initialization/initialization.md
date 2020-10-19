# Initialization

This is how you initialize the weights and biases of your [[neural_network]]. Usually initialized using an initialization scheme such as:

- [[xavier_initialization]]
- [[kaiming_initialization]]
- [[LSUV_initialization]]

Things to mention: glorot or he - apparently glorot is for tanh/sigmoid and he is for relu.

what about dead [[ReLU]]? need biases initialized to a small pos. constant to prevent dead relus. leaky relus help.

what about mish?

### Resources

- https://towardsdatascience.com/weight-initialization-in-neural-networks-a-journey-from-the-basics-to-kaiming-954fb9b47c79
- https://arxiv.org/abs/1912.08957
