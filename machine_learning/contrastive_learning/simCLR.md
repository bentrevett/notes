# SimCLR

SimCLR is a particularly elegant [[self-supervised_learning]] algorithm that managed to simplify previous approaches to their essential core and improve upon their performance. Two transformations v and v’ of the same image x are fed through the same network to produce two projections z and z’. The [[contrastive_learning]] loss aims to maximize the similarity of the two projections from the same input while minimizing the similarity to projections of other images within the same mini-batch. For example, projections of different crops of the same dog image would hopefully be more similar than crops from other random images in the same batch.

The [[multilayer_perceptron]] used for projection in SimCLR uses [[batch_normalization]] after each [[linear_layer]].

![](simclr_arch.png)

### Resources

- https://arxiv.org/abs/2002.05709
- https://arxiv.org/abs/2006.10029
- https://github.com/google-research/simclr
- https://github.com/sthalles/SimCLR