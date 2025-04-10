
import random

number = 5560746193
digits = list(map(int, str(number)))


unique_digits = []
seen = set()
for d in digits:
    if d not in seen:
        unique_digits.append(d)
        seen.add(d)

def create_matrix():
    return [
        [random.choice(unique_digits) for _ in range(10)]
        for _ in range(10)
    ]

matrix1 = create_matrix()
matrix2 = create_matrix()

print(" matrix1")
for row in matrix1:
    print(row)

print("\n matrix2")
for row in matrix2:
    print(row)