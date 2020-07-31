# Dropout

Dropout is a [[regularization]] technique used in [[neural_network]] models.

For [[recurrent_neural_network]] models:
- input dropout = dropout applied directly to the input tokens
- embedding dropout = dropout applied to the output of the embedding layer
- hidden dropout = dropout applied to the hidden state between layers of the RNN
- output dropout = dropout applied to the final (top layer) hidden states of the RNN
- DropConnect aka weight-dropout = applied to the hidden to hidden weight matrixes inside the RNN 
- variational dropout = dropout applied to h_{t-1}
- locked dropout = dropout that is fixed for each time-step and only resampled for each batch, DropConnect and variational dropout are usually locked

### Resources

- https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf
- DropConnect - https://arxiv.org/abs/1708.02182