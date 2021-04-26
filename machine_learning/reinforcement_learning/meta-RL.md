# Meta-RL

Meta-RL involves using [[reinforcement_learning]] to train an [[agent]] which learns to solve not one task, but a distribution of tasks. The trained agents are then evaluated on how well they can perform on unseen tasks drawn from a similar distribution.

The simplest case is a distribution of [[multi-armed_bandit]]s. The agent must learn the policy for performing the experiment in each environment and also learn a policy for explointing that learned knowledge. 

### Resources

- https://awjuliani.medium.com/japanese-role-playing-games-as-a-meta-reinforcement-learning-benchmark-2907f527f0f3
