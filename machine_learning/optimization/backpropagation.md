# Backpropagation

Backpropagation is an algorithm common used to train [[neural_network]] models. It calculates the gradient of the [[loss_function]] with respect to each parameter in the neural network.

The calculated gradient is then used to update the parameters of the neural network with [[gradient_descent]], [[stochastic_gradient_descent]] or another gradient based algorithm, such as [[rmsprop]], [[adam]], etc.

In machine learning libraries such as [[pytorch]] and [[tensorflow]], backpropagation is performed by [[automatic_differentiation]].

### Resources

- http://neuralnetworksanddeeplearning.com/