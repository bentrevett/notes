# VL-BERT: Pre-training of Generic Visual-Linguistic Representations

Uses BERT with the next sentence prediction task replaced by the visual features. Embedding vectors for words are made up of the token embedding, positional embedding, a visual embedding (output of CNN over entire image) and a segment embedding which is just 0 for text and 1 for images. The "second sentence" which would normally be from the next sentence prediction task is a sequence of RoI from the image extracted by a pre-trained RCNN. The token embedding is on `[IMG]` tokens, the positional embedding for each is shared. The visual embedding is from the RoI. Any masked out visual tokens have their RoI for the visual embedding zeroed out and the masked prediction task is to predict the class of the RoI. See fig 1.

They claim their work is superior to ViLBERT and LXMERT because those models separates out the two modalities to have their own encoder and then combines them later on, whereas VL-BERT feeds both modalities through the shared encoder.

They pre-train their model both on image-text pairs and on text only, which they state is needed due to the text component of the image-text pairs being too simplistic for downstream task usage.

See appendix A.1 for more visual BERT work. Seems to be a growing trend.
