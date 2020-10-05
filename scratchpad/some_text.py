import torch
from torchtext.experimental.datasets.text_classification import TextClassificationDataset
from torchtext.experimental.vocab import build_vocab_from_iterator
from torchtext.data.utils import get_tokenizer
from torchtext.experimental.functional import sequential_transforms, vocab_func, totensor

# load data from whatever format it's saved in to an iterable of (label, text)
my_data = [('pos', 'this film is great'), ('neg', 'this film is bad'), ('neg', 'this film is awful')]

# tokenizer can be any callable function that goes from str -> list[str]
my_tokenizer = get_tokenizer('basic_english')

# build vocabulary from data
my_vocab = build_vocab_from_iterator([my_tokenizer(text) for label, text in my_data])

# how should the label be transformed?
# str -> int -> LongTensor
label_transforms = sequential_transforms(lambda x: 1 if x == 'pos' else 0, totensor(torch.long))

# how should the text be transformed?
# str -> list[str] -> list[int] -> LongTensor
text_transforms = sequential_transforms(my_tokenizer, vocab_func(my_vocab), totensor(torch.long))

# tuple the transforms
my_transforms = (label_transforms, text_transforms)

# create TextClassificationDataset with data, vocabulary and transforms
dataset = TextClassificationDataset(my_data, my_vocab, my_transforms)
