# Markov Decision Process

A Markov decision process (MDP) is used to model state, actions and rewards within a decision making control process - such as in [[reinforcement_learning/reinforcement_learning]] (RL).

Looking at it from a RL lense - at each time-step the agent is in some state $s_t$, uses its policy to choose an action $a_t$ which is available in state $s_t$. It then moves into a new state, $s_{t+1}$ and receives reward $R_{a_t}(s_t,s_{t+1})$. 

The probability that it will move from $s_t$ to $s_{t+1}$ is given by the state transition function, $P_{a_t}(s, s_{t+1})$.

MDPs follow the Markov property: that the reward and transition function only depend on the **current** state and action and are independent of all previous states and actions.