# Linear Congruential Generator

# linear as it applies a linear equation
# congruential just means it uses a modulus
# LGC next_seed = (a * seed + b) mod m

init_seed = 1
print(f'initial seed: {init_seed}')

# for java random LCG, they use:

a = 25_214_903_917
b = 11
m = 2 ** 48

# problems - alternates between even and odd
# bottom bits repeat with small period
# at most 2^48 different seeds because of the mod
# java only gives you the top 32 bits to avoid this problem


def LCG(seed, a, b, m):
    return (a * seed + b) % m


seed = init_seed
seeds = []
for i in range(10):
    seed = LCG(seed, a, b, m)
    seeds.append(seed)

# how can we reverse this process?
# well, we can find a number that we multiply with a
# that gives us a number which is a multiple of 2^48
# this can be found with the extended euclidean algorithm
# here is such a number:

x = 246_154_705_703_781

assert (x * a) % m == 1

# we can now re-arrange the LCG equation to get:
# x * (seed - 11) = prev_seed (both sides are mod m)
# this is also an LCG (with different a and b values)
# turns out every LCG has a backwards LCG

final_seed = seeds[-1]
print(f'final seed: {final_seed}')

a = x
b = x * -11
m = 2 ** 48

seed = final_seed

seeds = []
for i in range(10):
    seed = LCG(seed, a, b, m)
    seeds.append(seed)

calculated_init_seed = seed
actual_init_seed = init_seed

print('Calculated initial seed correctly? ', end='')
print(calculated_init_seed == actual_init_seed)
