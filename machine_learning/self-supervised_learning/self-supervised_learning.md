# Self-supervised Learning

Self-supervised learning is a technique where you perform [[supervised_learning]], but the labels for your data are automatically obtained. A lot of things that used to be called [[unsupervised_learning]] are now being referred to as self-supervised learning, such as [[language_modelling]].

For example, given a set of unlabelled images randomly rotate them between 0, 90, 180 and 270 degrees, then use these 4 possible rotations as labels for a supervised learning model.

This is commonly used for [[representation_learning]] for [[pre-training]] models for [[fine-tuning]] or [[transfer_learning]].

Common algorithms:

- [[simCLR]]
- [[MoCo]]
- [[BYOL]]
- [[word2vec]]
- [[SEER]]
- [[SwAV]]
- [[Barlow_Twins]]

[[language_modelling]] is also a type of self-supervised learning.

### Resources

- https://ai.stackexchange.com/a/10624
- https://github.com/lightly-ai/lightly (self-supervised learning library in PyTorch)
- https://amitness.com/2020/02/illustrated-self-supervised-learning/
- https://ai.facebook.com/blog/self-supervised-learning-the-dark-matter-of-intelligence
- https://lilianweng.github.io/lil-log/2019/11/10/self-supervised-learning.html
