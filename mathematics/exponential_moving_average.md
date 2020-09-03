# Exponential Moving Average

Exponential moving average (EMA) applies weighting factors that decrease exponentially - but never reaches zero.

The EMA, $S$, of sequence $Y$ can be calculated as:

$$S_t = \begin{cases}
        Y_1, & t = 1 \\
        \alpha Y_t + (1-\alpha)\cdot S_{t-1}, & t > 1
        \end{cases}$$
