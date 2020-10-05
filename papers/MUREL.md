# MUREL: Multimodal Relational Reasoning for Visual Question Answering

CNNs are good for extracting visual features, but not for reasoning. Soft-attention mechanisms don't do reasoning. Their MuRel cell enables reasoning, can be applied iteratively to "progressively refine the internal network representation to answer the question".

Reasoning work on CLEVR generates a program-graph-type-thing that is used to process the underlying representation of the image and answer the question. Ideally, to expand this line of work - VQA - to real-world datasets we want to move away from using this underlying representation as it isn't always available.

Important part of VQA is finding a good way to represent high-level correlations between the text and the image vector representations.

MuRel cell is shown in fig 2, network in fig 3. Uses a bag of visual features extracted by RCNN. Text encoded by a GRU. Encodings combined using "bilinear fusion" - similar to attention but output is a vector, not a scalar. Then the output of the bilinear fusion is used to find pairwise relations between each and every bilinear fusion output. Plus a residual connection. That is a single cell, of which you can use many of. At the end, there is a pooling across all pairwise relations, another bilinear fusion with the original GRU output and then an answer prediction.

The idea is that you get some final RCNN bounding box that was the most important for answering your question so you can show this to the user when answering the question. This allows for a degree of interpretability. See fig 5.
