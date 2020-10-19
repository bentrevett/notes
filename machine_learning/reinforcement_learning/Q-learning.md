# Q-Learning

Q-learning is a method of performing [[reinforcement_learning]] that uses the [[Q-value]], [[temporal_difference_learning]] and [[bootstrapping]]. It learns using a $(S,A,S',R)$ tuple from a [[transition]] or [[trajectory]].

The Q-learning algorithm is:

$$Q^{new}(s_t,a_t) \leftarrow Q(s_t,a_t)+\eta \cdot \Big(r_t+\gamma \cdot \max_a Q(s_{t+1},a_t) - Q(s_t,a_t)\Big)$$

$Q(s_t,a_t)$ is the current predicted Q-value.

$\eta$ is the [[learning_rate]].

$\r_t$ is the [[reward]].

$\gamma$ is the [[discount_factor]].

$\max_a Q(s_{t+1},a_t)$ is the estimate of hte optimal future value.

$r_t+\gamma \cdot \max_a Q(s_{t+1},a_t)$ is the temporal difference target, with the whole part in the parenthesis being the [[temporal_difference_learning]].

A famous algorithm that uses Q-learing is [[DQN]].
