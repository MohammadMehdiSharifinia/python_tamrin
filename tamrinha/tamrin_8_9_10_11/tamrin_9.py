import random

number = 5560746193
digits = list(map(int, str(number)))

unique_digits = []
seen = set()

for digit in digits:
    if digit not in seen:
        unique_digits.append(digit)
        seen.add(digit)

random.shuffle(unique_digits)

print(unique_digits)