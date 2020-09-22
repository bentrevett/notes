import string

letters = string.ascii_lowercase

def num_to_letter(num, shift=0):
    return letters[(num + shift) % len(letters)]


for i, letter in enumerate(letters):
    print(i, num_to_letter(i))

numbers = [9, 23, 14, 14, 18, 5]

for shift in range(len(letters)):
    print(shift)
    print([num_to_letter(n, shift) for n in numbers])
