def hill_climb_string(target, n_steps):
    target = list(target.lower())
    chars = list(string.ascii_lowercase + ' ')
    best_count = -1
    best_guess = list('x' * len(target))
    for n in range(n_steps):
        should_switch = random.choices([0, 1], k = len(target))
        guess = best_guess[:]
        for i, switch in enumerate(should_switch):
            if switch:
                guess[i] = random.choice(chars)
        count = sum([1 if t == g else 0 for t, g in zip(target, guess)])
        if count > best_count:
            best_count = count
            best_guess = guess
        if n % (n_steps // 10) == 0 and n > 0:
            print(f'best guess so far: {best_guess}, {best_count}')
    return best_guess

hill_climb_string('hello world', 100_000)