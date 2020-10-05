# Towards VQA Models That Can Read

Task is to read the desired text within an image - i.e. "what is the title of the red book?" - which most of the currently VQA models fail at.

Introduce a TextVQA dataset as existing datasets either don't have enough questions about text or are too small.

Also introduce a model called LoRRA (Look, Read, Reason and Answer).

Existing models fail because reasoning does not just emerge from distant supervision. It needs to be biased towards reasoning via its architecture. LoRRA does OCR and then uses the OCR'd characters with the rest of the image to reason over. LoRRA can either directly copy from the OCR'd text or produce a new output if the answer is not available within the image.

LoRRA uses GloVe embeddings and an LSTM with self-attention on the question. The bounding boxes from the image are extracted with some pre-trained OCR system and are then passed through FastText embeddings. The objects within the image are extracted with a pre-trained Faster-RCNN model and then has attention performed over them. They then combine these three components to produce an output.
