# Advantage Function

The advantage function, $A(s,a)$ determines how "good" an [[action]] is in the given [[state]].

$$A(s,a) = \mathbb{E}[r(s,a)-r(s)]$$

$r(s,a)$ is the expected [[reward]] of an action, $a$ in state $s$.

$r(s)$ is the expected reward of the entire state $s$ before the action is selected.

Can also be calculated as:

$$A(s,a) = Q(s,a) - V(s)$$

$$Q(s,a)$$ is the [[Q-value]].

$$V(s)$$ is the [[value_function]].
