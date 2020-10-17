# Action

An action is how an [[agent]] interacts with an [[environment]], thus allowing it to transfer between [[state]]s.

Every action made by the agent rewards a [[reward]] from the environment. The decision of which action to take is decided by the agent's [[policy]] - a function that maps states to actions:

$$\pi_\theta(\bm{s}_t) = \bm{a}_t$$