# Self-supervised Learning

Self-supervised learning is a technique where you perform [[supervised_learning]], but the labels for your data are automatically obtained.

For example, given a set of unlabelled images randomly rotate them between 0, 90, 180 and 270 degrees, then use these 4 possible rotations as labels for a supervised learning model.

This is commonly used for [[representation_learning]] for [[pre-training]] models for [[fine-tuning]] or [[transfer_learning]].

Common algorithms:

- [[simCLR]]
- [[MoCo]]
- [[BYOL]]
- [[word2vec]]
- [[SEER]]
- [[SwAV]]

[[language_modelling]] is also a type of self-supervised learning.

### Resources

- https://ai.stackexchange.com/a/10624
- https://github.com/lightly-ai/lightly (self-supervised learning library in PyTorch)
