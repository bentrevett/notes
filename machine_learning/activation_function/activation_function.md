# Activation Function

In [[neural_network]] models the weighted sum of the inputs to a node has an activation function applied to it. This is a non-linear, differentiable function. It needs to be non-linear as if it is linear then even a multi-layered neural network is just a linear function. It needs to be differentiable so the gradient with respect of to its inputs can be calculated (via [[backpropagation]]) to update the parameters of the neural network (via [[gradient_descent]]).

Traditionally, the [[perceptron]] used the [[heaviside]] (aka unit step or step) function. This stopped being used as the gradient is not smooth with respect to the inputs, making updating the parameters via gradient descent difficult.

Researchers then moved on to the [[sigmoid]] (aka logistic) function. However the sigmoid is not symmetric around zero, which means it cannot keep the mean of the activations around zero. It also saturates when the input is very high or very low, i.e. the gradient is very small in those two cases, thus the parameter updates via gradient descent are very small, leading to slow learning.

The [[tanh]] (aka hyperbolic tangent) function is sometimes still used, such as in the [[LSTM]]. Though the most common activation function used now is the [[ReLU]] (rectified linear unit) function.

Other activation functions used are [[leaky_ReLU]] and [[GELU]].
