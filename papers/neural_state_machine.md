# Learning by Abstraction: The Neural State Machine

Joins together neural and symbolic AI. Symbolic AI is handled by a probabilistic graph model that represents "underlying semantics". Neural part is handed by a graph neural network. See fig 1.

Humans form analogies and concepts to generalize to unseen examples. Internally we build "world models" to represent objects/concepts and their relations to other objects/concepts. Use these relations to perform reasoning.

Authors view this as humans building an internal state machine (nodes with edges forming probabilistic transitions). Objects - nodes in the graph - have concepts (or semantic properties) such as "color" and "shape" and a relation edge between that object and other objects. Each relation edge has a probability value for each semantic property, i.e. the image of a man sitting on a chair should have 1.0 probability in the "sitting on" relation edge between the "man" object node and the "chair" object node, but a 0 probability on the "eating" relation edge.

Test their methods on VQA-CP and GQA datasets - again very simple natural language questions with one or two steps of reasoning. Might not scale to real world usage.
