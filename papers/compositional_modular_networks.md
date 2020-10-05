# Modeling Relationships in Referential Expressions with Compositional Modular Networks

Entities within an image are often thought of in terms of their relationship with other entities. Authors introduce CMNs (compositional modular networks).

Takes an input image and "expression" (natural language). First extracts the objects ("candidate regions") from the input image and creates an exhaustive "region-pair" tuple of every single object. Then processes the expression to get a high dimensional subject, relation and object vector. Passes the subject and candiate regions to a localization module, the relation and the region pairs to a relationship module and the object with the candidate regions to another localization module. Combines the three modules to get the top region pair. See fig 1.

Useful for the task of finding multiple objects within an image, given some natural language.

Images extracted with pre-trained VGG-16.

Language representation taken from word embedding layer to a 2-layer biLSTM which then does self attention to get the weighted state to use as the subject, relation and object vectors. Localization uses a CNN on the bounding box contents that are just elementwise multiplied with the language representation. Relationship takes in two image bounding boxes for the same image, extracts the features and concatenates and then does the elementwise multiplication. See fig 2.

Natural language questions are very explicit in what they want to find in the image.
