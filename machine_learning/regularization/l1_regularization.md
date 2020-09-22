# L1 Regularization

L1 regularization, also known as Lasso Regression when used in [[linear_regression]], is a [[regularization]] technique. 

The L1 regularization term is calculated as:

$$\lambda \sum_{j=1}^M |\beta_j|$$

$\lambda$ is the regularization co-efficient and the $\beta$ terms are the value of the weights.

This term is added to your [[loss_function]], such as [[MSE]], like so:

$$L(\bm{\beta, \bm{x}, \bm{y}}) = \sum_{i=1}^N (y_i - \sum_{j=1}^Mx_{ij}\beta_j)^2 + \lambda \sum_{j=1}^M |\beta_j|$$

L1 regularization is simplying adding the sum of the absolute value of each of our weights, multiplied by a regularization co-efficient, to the loss.

L1 regularization encourages *sparsity* in the weights by trying to make them zero. This is good because it reduces the number of features we use to make our predictions, and thus helps with [[overfitting]].