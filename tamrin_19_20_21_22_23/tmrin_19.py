import math

def cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))

print(cdf(1.0))
