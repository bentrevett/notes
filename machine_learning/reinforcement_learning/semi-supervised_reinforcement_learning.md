# Semi-supervised Reinforcement Learning

Semi-supervised reinforcement learning uses [[semi-supervised_learning]] techniques such as [[data_augmentation]] and [[contrastive_learning]] in [[reinforcement_learning]]

These techniques are used to increase [[sample_efficiency]] in [[model-free_reinforcement_learning]].

Random cropping is the most effective data augmentation technique (https://arxiv.org/pdf/2004.14990.pdf bottom of page 8) as it causes the encoder to capture the agent's state more clearly. It improves contingency awareness of the agent - recognizing aspects of the environment that are under the agent’s control.

### Resources

- https://arxiv.org/abs/2004.13649
- https://arxiv.org/abs/2004.04136
- https://arxiv.org/abs/2004.14990