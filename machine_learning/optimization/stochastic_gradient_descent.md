# Stochastic Gradient Descent

Stochastic gradient descent (SGD) is an iterative version of [[gradient_descent]].

Instead of the gradient being calculated using every example in the dataset we instead calculate the gradient using only a sample of the dataset.

Technically, SGD refers to the scenario when we have a sample size (also called a [[batch_size]]) of one, i.e. we calculate the gradient for that single example and then update the parameters. Using a batch size of one is also sometimes called [[online_gradient_descent]].

A batch size of one is very slow as it does not utilize the parallelism available in GPUs. Therefore it is common to use larger batch sizes, which could be anywhere between 8 and in the hundreds, depending on the experimental set-up.

Using batch size greater than one is technically called mini-batch stochastic gradient descent, although when people talk about SGD they commonly mean mini-batch SGD.