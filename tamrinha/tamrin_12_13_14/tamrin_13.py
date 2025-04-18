import numpy as np
import matplotlib.pyplot as plt

x = y = 0
pts = []

for _ in range(100000):
    r = np.random.rand()
    if r < 0.02:
        x, y = 0.5, 0.27 * y
    elif r < 0.17:
        x, y = -0.14*x + 0.26*y + 0.57, 0.25*x + 0.22*y - 0.04
    elif r < 0.30:
        x, y = 0.17*x - 0.21*y + 0.41, 0.22*x + 0.16*y + 0.09
    else:
        x, y = 0.78*x + 0.03*y + 0.11, -0.03*x + 0.74*y + 0.27
    pts.append([x, y])

pts = np.array(pts)
plt.scatter(pts[:, 0], pts[:, 1], s=0.1, c='g')
plt.axis('off')
plt.show()
