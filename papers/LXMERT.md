# LXMERT: Learning Cross-Modality Encoder Representations from Transformers

Learning Cross-Modality Encoder Representations from Transformers (LXMERT) has three encoders: one for object relationship, one for language and one for "cross-modality". See fig 1.

Pre-train all encoders on five pre-training tasks, all multi-modal. This allows the model to infer features from either the elements in the same modality or aligned components in the other modality, i.e. helps with intra-modality and cross-modality.

Language encoder is standard BERT encoder. Object relationship encoder takes in the RoI (region of interest) from bounding boxes and some position aware embedding - no pre-trained CNN extraction of features - passed into a standard BERT encoder. The outputs of both of these encoders are then passed to the cross-modality encoder, a dual headed encoder which performs attention between the two representations from the image/text encoders.
