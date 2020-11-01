# Offline Reinforcement Learning

Offline [[reinforcement_learning]] - also known as batch reinforcement learning or data-driven reinforcement learning - is a way to bridge the gap between reinforcement learning and [[supervised_learning]]. It is the opposite of [[online_reinforcement_learning]].

In offline RL, the [[agent]] does not learn through interactions with the [[environment]] but instead learns from a [[transition]] or a [[trajectory]] collected by a trained agent or from a human demonstrator.

Offline RL is similar to, but not the same as, [[off-policy]] reinforcement learning as your offline algorithm could only sample a next state transition where the offline RL algorithm has the highest action probability.

Offline RL improves [[sample_efficiency]] by decoupling [[optimization]] from [[exploration]] and [[exploitation]] and is useful when safety is concerned.

Offline RL can be considered a form of [[pre-training]] and thus can be used with [[transfer_learning]] to adapt the agent trained on the transition/trajectory dataset into an [[online_reinforcement_learning]] setting where the agent actually interacts with the environment.

Is it beneficial to learn an [[ensemble]] of offline RL algorithms according to: https://arxiv.org/abs/1907.04543.

An example of an offline RL algorithm is the [[world_models]] algorithm.

### Resources

- https://github.com/deepmind/deepmind-research/tree/master/rl_unplugged
- https://offline-rl-neurips.github.io/
- https://offline-rl.github.io/
- https://arxiv.org/abs/2005.01643
- https://arxiv.org/abs/1907.04543
- https://arxiv.org/abs/2004.07219
- https://danieltakeshi.github.io/2020/06/28/offline-rl/
- https://jacobbuckman.com/2020-10-31-updating-the-accepted-wisdom-in-offline-rl/
- https://twitter.com/kargarisaac/status/1313406101950472192