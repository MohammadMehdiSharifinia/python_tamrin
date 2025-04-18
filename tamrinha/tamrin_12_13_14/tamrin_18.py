import sys

numbers = [float(line) for line in sys.stdin]

print("میانگین:", sum(numbers) / 1000)

#cat data.txt | python tamrin_18.py