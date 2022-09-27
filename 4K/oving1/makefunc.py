import matplotlib.pyplot as plt
import numpy as np

def f(x):
    if (x < 2):
        return 0
    elif (x==2):
        return np.nan
    return (x-2)**5 / 120

x_vals = np.linspace(-1, 7, 1001)
y_vals = [f(x) for x in x_vals]

plt.plot(x_vals, y_vals)
#plt.show()
plt.savefig("6.3.15.pdf")
