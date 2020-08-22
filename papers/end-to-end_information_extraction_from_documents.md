# Attend, Copy and Parse: End-to-end Information Extraction from Documents

- https://github.com/Tradeshift/attend-copy-parse
- https://github.com/naiveHobo/InvoiceNet

Document information extract = taking PDF and extracting string outputs

Humans doing information extraction are implicitly creating a dataset of PDF-to-fields.

Current systems need word level labels which are expensive to create. This system does not need word level labels.

End-to-end data tells us *what* the total (or creation date, etc.) is, data labeled on the word level tells us *where* the total is.

End-to-end data is hard to learn from but abundant, word labels are easy to learn from but scarce.

Their model generalizes across document templates and can be applied to unseen templates, e.g. invoices from different companies.

**ASSUMPTION:** the same information must be extracted from every document. Fine with invoices as it's usually always the same information.

Invoices have spatial structure with text and images. Their model takes spatial structure into account w/ convolutions on the concatenated text and image modalities. Text modality is embedding extracted text in a spatial grid. Assume text is extracted with OCR.

Explicit pattern matching (regex) takes time and does not generalize. Modern NER uses deep learning over word embeddings, downside is that every word needs to be labelled. Distant supervision = generate labels heuristically from data, downside is that the quality of labels depends on the quality of the heuristic and if you have a good heuristic then just do pattern matching. CV for document images usually focuses on labelled dataset with information on *where* the targets are, e.g. bounding boxes.Previous work fused modalities late, this work fuses them early. They also use external memory.

x = document as image.
w = all (word, position) tuples in the document, position is [0, 1] in four dimensions
t_K = target strings for K values to be extracted

extract K output strings, y = [y_1, ... y_K] for a given (x, w).

- must be able to generalize across templates
- must be able to handle normalized target strings, i.e. target string might not appear exactly the same in the document
- target string spans multiple words in the input, e.g. target string is "2019-07-23" and input might be ["23rd", "july", "2018"]
- outputs might be optional

human approach: locate string, parse into desired format

a_k = Attend_k(x, w)
c_k = Copy_k(a_k, w)
h_k = Context_k(x, w)
y_k = Parse_k(c_k, h_k)

external memory bank the same size of the document image containing the words encoded as a sequence of characters at the memory positions corresponding to the positions of the words in the image
attend module attends to the memory bank
copy module copies out the attended string
parse module parses the attended string into the desired output

they train a separate model for each of the K fields

EXTERNAL MEMORY

external memory, M = [0, 1]^{H x W x G x L x D} with n-grams up to length G = 4. n-grams created by dividing the document into a number of "non intersection lines and sorts the words by their horizontal position inside each line"
L is the maximum sequence length per line
D is the size of the character set, i.e. vocabulary size
L = 128, D = 103
first two dimensions are spatial dimensions and the third is the lenth of the n-gram
very large tensor so must represent as sparse tensor
where to store n-grams (as they go over multiple pixels)? store in top-left pixel slot of first word.

ATTEND

unnormalized attention logits, u ^ {HxWxG} for each slot in the memory. -1000 to every empty slot in the memory so we don't attend over it. use softmax to get attention distribution.

how to get u?
r = concat of (input image, 32 dimensional word, pattern and character embedding, binary indicator for amount/date, normalized horizontal and vertical positions, binary indicator for memory bank here empty or not) 

pattern embedding is embedding of the word after all characters have been replaced with x, digits with 0, and others with a dot. - used to get embeddings of currencies and dates, etc.

word and pattern embeddings replicated across the spatial extent of the word. character embeddings across each character in the word. (isn't that the same thing?) in case of an overlap, rightmost character wins. 

r is passed through 4 x dilated convolutional blocks. concatenated channel-wise. each dilated block contains 4 x dilated convolutions, etc etc etc. 32 3x3 filters, relu, 128 channels when concatenated. then a final convolution with 3x3 filters and no non-linearity.

COPY

not actually a hard copy, a soft differentiable copy. so each output, c, is a weighted sum over all n-grams in the document. each copied character is a distribution over all the characters in the vocabulary.

CONTEXT

context of an n-gram is important for parsing it, dates can be in US or EU formats. context is attention with output of last dilated convolutional block in the attend module. 

PARSE

given attended word, c, and context vector, h, (from context module) we parse it into the output y. this is a character based sequence to sequence task.

they use four different parsers.
- no-op, y=c
- optional parse, linear over context with sigmoid to get scalar, use to weight copy or eos.
- date parser, 