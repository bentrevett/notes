# ULMFiT

Universal Language Model Fine-tuning (ULMFiT) is a [[transfer_learning]] method for [[natural_language_processing]].

The method involves using a [[neural_network]] model, specifically an [[LSTM]] in three distinct stages:

1. The model is first trained as language model on a general-domain corpus, WikiText-103. 
1. Next, the model is trained as a language model on the downstream task data 
1. Finally, the model is trained on the downstream task data for the downstream task.


There are a few novel techniques introduced in the ULMFiT paper:

1. Discriminative fine-tuning - as early layers capture more general types of information then should not change as much as the later layers, which capture more specific information, when transfer learning. The way they solve this is by having earlier layers have a lower learning rate than later layers. This is used in steps 2 and 3.

1. Slanted triangular learning rates - early on you want the model to quickly converge to a suitable region of the parameter space and then slowly refine its parameters. This is achived by rapidly increasing the learning rate for the first few iterations and then linearly decaying it as training increases. This is used in steps 2 and 3.

1. Gradual unfreezing - performing transfer learning on all layers at once risks Catastrophic Forgetting. To solve this they gradually unfreeze the model starting from the final layer. They unfreeze the final layer, train for a single epoch and then unfreeze the next layer - repeating the process until all layers have had their parameters frozen for at least one epoch.

### Resources

- https://arxiv.org/abs/1801.06146