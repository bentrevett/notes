# MoCo

Momentum Contrast (MoCo) is a [[contrastive_learning]] algorithm for [[self-supervised_learning]].

![](moco_v2_arch.png)

Relative to [[simCLR]], MoCo v2 manages to both decrease the [[batch_size]] (from 4096 to 256) and improve the performance. Unlike simCLR, where the top and bottom row in the diagram represent the same network (parameterized by $\theta$), MoCo splits the single network into an online network (top row) parameterized by $\theta$ and a [[momentum]] network (bottom row) parameterized by $\xi$. The online network is updated by stochastic gradient descent, while the momentum network is updated based on an [[exponential_moving_average]] of the online network weights. The momentum network allows MoCo to efficiently use a memory bank of past projections as negative examples for the contrastive loss. This memory bank is what enables the much smaller batch sizes. As an example, the positive examples would be crops of the same image of a dog. The negative examples are completely different images that were used in past mini-batches, projections of which are stored in the memory bank.

The [[multilayer_perceptron]] used for projection in MoCo v2 does not use [[batch_normalization]]

### Resources

- https://arxiv.org/abs/1911.05722