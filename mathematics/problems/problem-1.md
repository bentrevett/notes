https://www.reddit.com/r/mathematics/comments/hx7dxw/tik_tok_trend_inspired_math_problem/

I saw this video on Tik Tok of people playing a game with Googles random number generator. You start by generating a random number between 1 and 100,000. Say you get 37,122. The next person generates one between 1 and 37,122. And so on until someone rolls a one. My question is, using this process, starting with a number between 1 and N, how many steps on average would it take to get to 1?

1 + the 99,999th harmonic number, or about 13.09.

For n > 1, the expected number of steps before getting a 1 (call it E(n)) is
E(n) = 1 + 1/n E(n) + 1/n E(n - 1) + ... + 1/n E(2) + 1/n * 0.
The first 1 is the guaranteed roll (since we have to roll at least once to make any progress). There's a 1 in n chance of getting any given number from 2 to n, at which point we start again from that number. The expected time until stopping starting from k > 1 is E(k), so that contributes 1/n E(k) to the sum. Finally, if we roll a 1, there are no further rolls, so the expected number of rolls after rolling a 1 is zero, contributing 1/n * 0 = 0 to the sum.

Writing that in summation notation, we have E(n) = 1 + 1/n sum(E(k), k, 2, n). Similarly, for n > 0, we have E(n + 1) = 1 + 1/(n + 1) sum(E(k), 2, n + 1).

Rearranging these we have
(n + 1) E(n + 1) = (n + 1) + sum(E(k), k, 2, n + 1)
(n) E(n) = (n) + sum(E(k), k, 2, n)

Subtracting the second equation from the first, we get
(n + 1) E(n + 1) - n E(n) = 1 + E(n + 1).

Finally, rearrange this to get
E(n + 1) = E(n) + 1/n, for any n > 1.

Since E(2) = 1 + 1/2 E(2) + 1/2 * 0, E(2) = 2, and so by induction,
E(n) = 1/(n - 1) + E(n - 1)
= 1/(n - 1) + 1/(n - 2) + ... + 1/2 + E(2)
= 1/(n - 1) + 1/(n - 2) + ... + 1/2 + 2
= 1/(n - 1) + 1/(n - 2) + ... + 1/2 + 1 + 1
= H(n - 1) + 1

where H(n) is the nth harmonic number.

Asymptotically, H(n) = ln(n) + γ + O(1/n), where γ is the Euler-Mascheroni constant, about 0.577216. That's actually good enough to get a rough estimate of E(100,000) as 1 + ln(99,999) + 0.577216 which is accurate to 4 or 5 decimal places (should be about 1/200,000 off). You can check the value easily enough to see how accurate that estimate is.