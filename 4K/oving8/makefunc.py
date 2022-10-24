import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return np.exp(x) * (np.cos(y) + 1j * np.sin(y))

point = 4 + 3j

fig, ax = plt.subplots()
ax.plot(f

ax.legend()
plt.xlabel("Re")
plt.ylabel("Im")
ax.set_aspect(1.0)
plt.show()
