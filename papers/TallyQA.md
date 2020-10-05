# TallyQA: Answering Complex Counting Questions

Paper is specifically studying VQA algorithms' ability to count. TallyQA dataset is a VQA dataset focused on counting problems. See also: HowMany-QA benchmark dataset, CountQA.

Simple counting questions only require object detection "count the dogs", whereas complex counting questions require reasoning "count the brown dogs". Most existing datasets only have simple counting questions.

Traditional VQA systems are not good at counting - why? "due to the way their architectures are designed these systems operate on image embeddings computed using a CNN that uses pooling operations which destroys information used to determine how many objects of a particular type are present".

Two approaches, counting as classification or do object detection and count the relevant objects deterministically.

Model is built from two relation networks (RNs). See fig 3. Question is encoded by a GRU. Image has both objects and background extracted from it. Objects with a pre-trained Faster R-CNN and the background with ResNet-152 over the entire image. These are both fed to the RN with the encoded question.
