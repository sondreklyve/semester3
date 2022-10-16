import matplotlib.pyplot as plt
import numpy as np

data = [[np.pi/8, 1], [5*np.pi/8, 1], [-7*np.pi/8, 1], [-3*np.pi/8, 1]]
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
for z, c in zip(data, ['r', 'g', 'b', 'k']):
    theta, r = z

    ax.plot(theta, r, c+"o", label=f"exp(i({round(theta, 2)}))")
    ax.plot([0, theta], [0, r], c)
ax.legend()
plt.xlabel("Re")
plt.ylabel("Im")
ax.set_aspect(1.0)
plt.show()
