# Loss Function

In [[machine_learning]] algorithms a loss function is a function that maps inputs to a single scalar value. The objective of the machine learning algorithm is to minimize the value output by this loss function via an algorithm such as [[gradient_descent]]. Tnputs are usually the ground truth label, $y$, and the model's prediction, $\hat{y}$

For [[regression]], a typical loss function is [[mean_squared_error]].

For [[classification]], wth more than one class and a single target class, we use [[negative_log-likelihood]].

For multi-class classification problems, i.e. where the target is not processed with [[one-hot_encoding]], we use the [[cross-entropy]] loss.

Both the cost function and the objective function are related to the loss function. Loss functions are usually defined for a single example and cost functions are usually defined as over multiple examples, i.e. mean squared error is the cost function version of $L_2$ loss. Objective function is a more general term for a function that you want to optimize during training.