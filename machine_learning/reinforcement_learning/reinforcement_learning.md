# Reinforcement Learning

Reinforcement learning (RL) uses [[machine_learning]] to teach an [[agent]] to interact with an [[environment]] in order to maximize a scalar [[reward]] value. The key difference from [[supervised_learning]] is that the model/agent itself acts within an environment, thus having an impact on what examples it sees in the future.

RL is usually modelled as a [[markov_decision_process]].

Most commonly when we talk about RL nowadays we mean [[deep_reinforcement_learning]] (DRL), which is just using RL algorithms with [[deep_learning]].

A common problem faced by RL, especially DRL, is [[sample_efficiency]].

There is quite a lot of terminology for RL:

- [[action]]
- [[actor-critic]]
- [[advantage_function]]
- [[agent]]
- [[bellman_equation]]
- [[bootstrapping]]
- [[credit_assignment_problem]]
- [[deadly_triad]]
- [[discount_factor]]
- [[environment]]
- [[experience_replay]]
- [[exploration]]
- [[exploitation]]
- [[greedy_policy]]
- [[epsilon-greedy_policy]]
- [[markov_decision_process]]
- [[model-based_reinforcement_learning]]
- [[model-free_reinforcement_learning]]
- [[monte_carlo]]
- [[multi-agent_reinforcement_learning]]
- [[observation]]
- [[off-policy]]
- [[offline_reinforcement_learning]]
- [[on-policy]]
- [[online_reinforcement_learning]]
- [[policy]]
- [[policy_gradient]]
- [[Q-learning]]
- [[Q-value]]
- [[return]]
- [[reward]]
- [[semi-supervised_reinforcement_learning]]
- [[state]]
- [[temporal_difference_learning]]
- [[trajectory]]
- [[transition]]
- [[value_function]]

Some notable algorithms are:

- [[REINFORCE]]
- [[A2C]]
- [[A3C]]
- [[TRPO]]
- [[PPO]]
- [[DQN]]
- [[world_models]]
- [[AlphaGo]]
- [[AlphaGo_Zero]]
- [[AlphaZero]]

Other related articles:

- [[reinforcement_learning_frameworks]]
- [[semi-supervised_reinforcement_learning]]
- [[text-based_reinforcement_learning]]

### Lectures

- https://www.youtube.com/watch?v=ISk80iLhdfU&list=PLqYmG7hTraZBKeNJ-JE_eyJHZ7XgBoAyb (DeepMind x UCL RL course, 2020)
- https://www.youtube.com/watch?v=2pWv7GOvuf0&list=PLqYmG7hTraZBiG_XpjnPrSNw-1XQaM_gB (David Silver RL course, 2015)
- https://www.davidsilver.uk/teaching/ (Notes for the above lecture series)
- https://sites.google.com/view/deep-rl-bootcamp/lectures
- http://rail.eecs.berkeley.edu/deeprlcourse/ (Berkeley RL course with videos from 2017 to 2020)
- https://www.youtube.com/watch?v=FgzM3zpZ55o&list=PLoROMvodv4rOSOPzutgyCTapiGlY2Nd8u (Stanford RL course, 2019)
- https://simoninithomas.github.io/deep-rl-course/

### Books

- http://incompleteideas.net/book/the-book.html
- https://rltheorybook.github.io/

### Resources

- https://karpathy.github.io/2016/05/31/rl/ (introductory blog post)
- https://arxiv.org/abs/1811.12560 (tutorial paper)
- https://arxiv.org/abs/cs/9605103 (survey paper)
- https://lilianweng.github.io/lil-log/2018/02/19/a-long-peek-into-reinforcement-learning.html (in-depth tutorial)
- https://spinningup.openai.com/en/latest/spinningup/rl_intro.html (in-depth tutorial)
- https://github.com/higgsfield/RL-Adventure (clean implementations)
- https://www.reddit.com/r/reinforcementlearning/comments/j6lp7v/i_asked_rlexpert_what_and_why_he_logstracks_in/ (what to log in RL experiments)
