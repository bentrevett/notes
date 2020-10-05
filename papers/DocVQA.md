# DocVQA: A Dataset for VQA on Document Images

A dataset that has scanned documents and questions about each document. See fig 1.

"Scene text VQA" = understanding the text is a scene is required to answer the question posed, i.e. the image is a picture of a letter and the question is to get the address on the letter.

Existing VQA models - they use LoRRA and M4C - are not good at this task. Understandable as the datasets they have been designed for only require a general understanding of a scene and not any explicit OCR components.

They find that a pre-trained BERT model applied to OCR'd text significantly outperforms LoRRA and M4C - implying that you do need some OCR and decently powered text processing for this task.
