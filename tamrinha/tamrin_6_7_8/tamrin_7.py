import math
import cmath  # For handling complex numbers

# Taking user input
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Calculating discriminant (delta)
delta = b**2 - 4*a*c

# Calculating the roots
root1 = (-b + cmath.sqrt(delta)) / (2*a)
root2 = (-b - cmath.sqrt(delta)) / (2*a)

# Printing the results
print(f"Roots of the equation: {root1} and {root2}")
