# Contrastive Learning

Contrastive learning is a [[representation_learning]] technique commonly used in [[self-supervised_learning]].

It is the process of training a classifier to distinguish between “similar” and “dissimilar” input data. For [[MoCo]] and [[simCLR]] specifically, the classifier’s positive examples are modified versions of the same image, while negative examples are other images in the same data set. For example, suppose there is a picture of a dog. In that case, the positive examples could be different crops of that image, while the negative examples could be crops from entirely different images.

Contrastive learning is used by [[siamese_neural_network]] models as well as algorithms such as [[MoCo]], [[simCLR]] and [[CURL]].

### Resources

- https://arxiv.org/abs/2004.11362
- https://arxiv.org/abs/2006.09882