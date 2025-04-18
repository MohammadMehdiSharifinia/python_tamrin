import sys

with open(sys.argv[1]) as f:
    numbers = [float(line) for line in f]

print("میانگین:", sum(numbers) / 1000)
