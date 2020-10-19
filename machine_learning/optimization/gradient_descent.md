# Gradient Descent

Gradient descent is an [[optimization]] algorithm for calculating the local minimum of a differentiable function. To find a local minimum of a function using gradient descent, we take steps proportional to the negative of the gradient of the function at the current point.

In a [[neural_network]] our network is a parameterized function. We use the [[backpropagation]] algorithm to calculate the gradient of each of the parameters with respect to the loss calculated by the [[loss_function]].

A step of gradient descent is then performed via:

$$w_i = w_i - \eta \frac{\partial L}{\partial w_i}$$

The traditional gradient descent algorithm calculates the gradient for every example in the training set, averages them together and then takes a single of parameter updates.

Only taking a single step after seeing every single example is incredibly slow so we most commonly use [[stochastic_gradient_descent]] (SGD). SGD involves sampling from the dataset and then calculating the average gradient is calculated from the examples sampled, a parameter update step is then taken. This sample size is also known as the [[batch_size]].

### Resources

- https://francisbach.com/gradient-descent-neural-networks-global-convergence/
- https://francisbach.com/gradient-descent-for-wide-two-layer-neural-networks-implicit-bias/