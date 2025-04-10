import random
import numpy as np

number = 5560746193
digits = list(map(int, str(number)))
unique_digits = list(dict.fromkeys(digits))

def create_matrix():
    return [random.choices(unique_digits, k=10) for _ in range(10)]

matrix_a = create_matrix()
matrix_b = create_matrix()

np_matrix_a = np.array(matrix_a)
np_matrix_b = np.array(matrix_b)

print("\nMatrix A:")
for row in matrix_a:
    print(row)

print("\nMatrix B:")
for row in matrix_b:
    print(row)

matrix_sum = np_matrix_a + np_matrix_b
matrix_product = np.matmul(np_matrix_a, np_matrix_b)

print("\nMatrix Sum:")
for row in matrix_sum:
    print(row.tolist())

print("\nMatrix Product:")
for row in matrix_product:
    print(row.tolist())