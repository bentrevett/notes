def newton_sqrt(n, n_steps = 100):
    m = n / 2
    for _ in range(n_steps):
        m = m - (m**2 - n)/(2 * m)
    return m