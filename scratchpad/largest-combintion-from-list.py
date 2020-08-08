# Given a list of non-negative numbers, 
# find the largest combination of digits which is divisible by 3

def find(xs):
    # find remainders of each number divided by three
    remainders = [x % 3 for x in xs]
    # find the mod sum of the remainders
    sum_remainders = sum(remainders) % 3
    if sum_remainders == 0:
        # if it's zero then already divisible by three, just sort
        xs.sort(reverse=True)
        xs = int(''.join([str(x) for x in xs]))
        return xs
    if sum_remainders == 1:
        # if one, then either remove smallest value with remainder 1
        if 1 in remainders:
            index = remainders.index(1)
            xs = xs[:index] + xs[index+1:]
            xs.sort(reverse=True)
            xs = int(''.join([str(x) for x in xs]))
            return xs
        # or remove 2 numbers with remainder 2
        if remainders.count(2) == 2:
            pass
    else:
        # if mod sum of remainders is two
        # then either remove smallest value with remainder 2
        # or remove the two smallest values with remainder 1
        pass
    


result = find([8, 2, 5, 6, 1])
assert result == 8652, result
