# Generative Adversarial Network

Generative adversarial networks (GANs) performs [[generative_modelling]] using two [[neural_network]] models - a generator $G(z)$ which is trained to take in a latent noise vector, $z$, and generate an image $\tilde{x}$; and a discriminator $D(x)$ which is trained to output the probability that a provided image is real or from generator.

The generator and the discriminator are adversaries and the desired outcome is for them to reach equilibrium when the discriminator cannot tell the difference between real and fake images, i.e. $D(x) = D(\tilde{x}) = 0.5$.

[Training GANs is difficult](https://developers.google.com/machine-learning/gan/problems). One problem that arises is mode collapse. Mode collapse is when the generator finds one specific image that is very good at fooling the discriminator. The generator will then repeatedly generate that image. However, the discriminator will then learn to identify that image as fake, but by then the generator will be stuck in a local minimum and will be unable to escape.

### Resources

- https://github.com/kwotsin/mimicry
- Tricks for training GANs: https://www.reddit.com/r/MachineLearning/comments/i085a8/d_best_gan_tricks/
- https://medium.com/datadriveninvestor/understanding-generative-adversarial-networks-b03d34445756