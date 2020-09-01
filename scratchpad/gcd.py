# https://plumsempy.com/2020/08/24/gcd-and-the-magic-of-subtraction/

def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

print(gcd(100, 250))


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(abs(a - b), min(a, b))

print(gcd(100, 250))
