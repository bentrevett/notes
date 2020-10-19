import torch
from torchtext.experimental.datasets import WikiText2
import numpy as np
import time


def generate_batch_idxs(data, batch_size, seq_len):
    t0 = time.monotonic()
    step_size = len(data) // batch_size
    n_steps = len(data) // step_size
    n_batches = step_size // (seq_len + 1)
    batch_idxs = np.tile(np.arange(seq_len+1), n_steps * n_batches)
    offsets = np.tile(np.repeat(np.arange(n_steps) * step_size, seq_len + 1), n_batches)
    _offsets = np.repeat(np.repeat(np.arange(n_batches) * seq_len, seq_len + 1), n_steps)
    batch_idxs += offsets + _offsets
    print(time.monotonic() - t0)
    return batch_idxs


train_set, val_set, test_set = WikiText2()

batch_size = 5
seq_len = 10

class Collator:
    def __init__(self):
        pass

    def collate(self, batch):
        batch = torch.tensor(batch)
        batch = batch.view(batch_size, -1)
        batch = batch.t()
        return batch

collator = Collator()

train_iter = torch.utils.data.DataLoader(train_set,
                                         batch_size = batch_size * (seq_len + 1),
                                         sampler = generate_batch_idxs(train_set, batch_size, seq_len),
                                         collate_fn = collator.collate)

vocab = train_set.get_vocab()

for tokens in train_iter:
    print(tokens)
    print(tokens.shape)
    input()