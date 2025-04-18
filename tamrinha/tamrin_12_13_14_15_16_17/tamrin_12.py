
import numpy as np
import matplotlib.pyplot as plt

v = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
p = np.array([0.0, 0.0])
n = 50000
d = np.empty((n, 2))

for i in range(n):
    p = (p + v[np.random.randint(3)]) / 2
    d[i] = p

plt.scatter(d[:, 0], d[:, 1], s=0.1, c='g')
plt.axis('off')
plt.show()
