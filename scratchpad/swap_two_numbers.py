# swap two variables without using a third

a = -100
b = 100

print('initial')
print(a, b)

a, b = b, a

print('tuple')
print(a, b)

a = -100
b = 100

a = a + b  # a = a + b
b = a - b  # b = a - b = (a + b) - b = a
a = a - b  # a = a - b = (a + b) - b = (a + b) - a = b

print('arithmetic')
print(a, b)

a = - 100
b = 100

a = a ^ b
b = a ^ b
a = a ^ b

print('logical')
print(a, b)
