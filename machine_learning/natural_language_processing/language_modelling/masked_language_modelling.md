# Masked Language Modelling

A masked language modelling is a variant of the [[language_modelling]]]] task.

Instead of predicting the next word from a sequence of words, you are instead given a sequence of words in which some of the words are "masked" - replaced by a common mask token.

This is theorized to be superior to standard language modelling in the context of [[pre-training]] as the model learns to predict words using context on both sides of the masked tokens, forward and backward. A standard language model is only trained to predict the next word from the previous words, therefore only gets context from the previous words.

This technique was introduced with the [[BERT]] model.

### Resources

- https://arxiv.org/abs/1905.02450