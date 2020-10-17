# Pre-Training

For [[neural_network]] models we can initialize the parameters randomly from a desired [[initialization]] scheme.

However, it is beneficial  to first train a model, or part of a model on another task. This is pre-training your model. We then use these learned weights for the desired downstream task.

If we keep the pre-trained weights fixed, then this is called [[fine-tuning]], and if we allow the weights to change from their pre-trained values then this is called [[transfer_learning]].

Pre-training causes the model to converge faster an achieve an improved overall test performance compared to initializing weights randomly.

Common tasks for pre-training in [[natural_language_processing]] are [[language_modelling]] and for [[computer_vision]] we use [[image_classification]] or [[self-supervised_learning]].

### Resources

- https://arxiv.org/abs/2006.06882 (for CV, self-training is better than transfer from an image classification model)
