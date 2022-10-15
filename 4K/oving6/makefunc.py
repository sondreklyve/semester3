import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate


def integrand(v, x, t):
    return np.exp(-((x - v) ** 2) / (4 * t))


def g(x, t):
    if t == 0:
        return (abs(x) <= 1) * 100
    return (
        100
        / (2 * np.sqrt(np.pi * t))
        * integrate.quad(integrand, -1, 1, args=(x, t))[0]
    )


x, t = np.meshgrid(np.linspace(-2, 2, 200), np.linspace(0, 8, 200))
g = np.vectorize(g)
z = g(x, t)


ax = plt.axes(projection='3d')
ax.plot_surface(x, t, z, cmap='jet', edgecolor='none')

ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('$C^{\circ}$')

plt.show()
