# Language Modelling

Language modelling is a [[natural_language_processing]] task which involves training a language model.

Definitively a language model (LM) is a probability distribution over sequences of words.

$$P(x_0,\dots,x_t)$$

The probability of a sequence of words can be obtained from the probability of each word given the context of words preceding it:

$$P(x_0,\dots,x_t) = P(x_0)P(x_1|x_0)P(x_2|x_0,x_1) \cdots P(x_t|x_0,\dots,x_{t-1},x_t)$$

Typically, when we talk about LMs we mean a [[neural_network]] that is trained to output this probability distribution over a sequence of words, commonly a [[recurrent_neural_network]] such as an [[LSTM]], or a [[transformer]].

A LM is trained via [[backpropagation]] to predict word $x_{t+1}$ from all words $x_0$ to $x_t$ - i.e. from all previous words - in order to maximize the log-likelihood:

$$L(\theta) = \sum_t \log P(x_t|x_0,\dots,x_{t-1})$$

It is usually computationally unfeasible to condition on all previous words, so we usually use the last 30-100, depending on the capacity of the model.

Language models can also be used for [[natural_language_generation]] by sampling from the probability distribution after each step and then feeding that back into the LM.

We can think of a language model as a compressor, i.e. if a LM is given the first 1GB of a 10GB text document and can predict the next 9GB then as long as the LM Itself is less than 9GB we have compressed that 10G of text. [Compression can be seen as a form of intelligence](http://prize.hutter1.net/hfaq.htm#compai).

There is also a variation of the language modelling task called [[masked_language_modelling]].

Common LM algorithms are:
- [[ELMo]]
- [[BERT]]
- [[GPT-2]]
- [[GPT-3]]
- [[ULMFiT]]