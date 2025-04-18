import numpy as np
import matplotlib.pyplot as plt

x = 0.5
y = 0
d = []

for _ in range(100000):
    r = np.random.rand()
    if r < 0.4:
        x, y = 0.31*x - 0.53*y + 0.89, -0.46*x - 0.29*y + 1.04
    elif r < 0.55:
        x, y = 0.31*x - 0.08*y + 0.22, 0.15*x - 0.45*y + 0.34
    else:
        x, y = 0.55*y + 0.01, 0.69*x - 0.20*y + 0.38
    d.append([x, y])

d = np.array(d)
plt.scatter(d[:, 0], d[:, 1], s=0.1, c='g')
plt.axis('off')
plt.show()
