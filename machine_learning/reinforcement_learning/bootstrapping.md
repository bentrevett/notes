# Bootstrapping

Bootstrapping is a concept in [[reinforcement_learning]] when using [[temporal_difference_learning]] (TD) algorithms.

TD algorithms update their parameters using targets that depend on their own parameters, i.e.:

$$Q(s,a)\leftarrow Q(s,a) = \alpha (R_{t+1} + \gamma Q(s',a')-q(s,a))$$

The $R_{t+1}+\gamma Q(s'a')$ term is an estimate for the true value of $Q(s,a)$ that is calculated using the [[agent]]'s [[policy]].

### Resources

- https://datascience.stackexchange.com/a/26945