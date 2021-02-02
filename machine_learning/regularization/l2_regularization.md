# L2 Regularization

L2 regularization, also known as Ridge Regression when used in [[linear_regression]], is a [[regularization]] technique.

The L2 regularization term is calculated as:

$$\lambda \sum_{j=1}^M \beta_j^2$$

$\lambda$ is the regularization co-efficient and the $\beta$ terms are the value of the weights.

This term is added to your [[loss_function]], such as [[mean_squared_error]], like so:

$$L(\boldsymbol{\beta, \boldsymbol{x}, \boldsymbol{y}}) = \sum_{i=1}^N (y_i - \sum_{j=1}^Mx_{ij}\beta_j)^2 + \lambda \sum_{j=1}^M \beta_j^2$$

L2 regularization is simplying adding the sum of the squared value of each of our weights, multiplied by a regularization co-efficient, to the loss.

Unlike [[l1_regularization]] which tries to make weights zero, L2 regularization instead shrinks outlier weights by making them close to zero. This reduction in the outlier weights helps prevent against [[overfitting]].
