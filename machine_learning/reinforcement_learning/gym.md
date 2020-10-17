# gym

gym is a framework which provides access to [[environment]]s to be used with [[reinforcement_learning]].

An example usage:

```python
import gym
env = gym.make("CartPole-v1")
observation = env.reset()
for _ in range(1000):
  env.render()
  action = env.action_space.sample() # your agent here (this takes random actions)
  observation, reward, done, info = env.step(action)

  if done:
    observation = env.reset()
env.close()
```

### Resources

- https://github.com/openai/gym
