import numpy as np
import matplotlib.pyplot as plt

def شکار(x, y, a, b, d, g):
    return a*x - b*x*y, d*x*y - g*y

x, y = 40, 9
آهو, گرگ = [x], [y]

for _ in range(500):
    dx, dy = شکار(x, y, 0.1, 0.02, 0.01, 0.1)
    x += dx * 0.1
    y += dy * 0.1
    آهو.append(x)
    گرگ.append(y)

plt.plot(آهو, label='آهو')
plt.plot(گرگ, label='گرگ')
plt.legend()
plt.show()
