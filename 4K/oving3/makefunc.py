import matplotlib.pyplot as plt
import numpy as np

def a(n):
    return (-12*(-1)**n)/(n**3)

def f(x, n):
    val = 0
    for i in range(1, n+1):
        val += a(i) * np.sin(i * x)
    return val

def r(x):
    return x*(np.pi**2 - x**2)

def rF(x):
    return 12*(np.sin(x)-np.sin(2*x)/8+np.sin(3*x)/27)

x_vals = np.linspace(-4, 4, 1001)
for n in [2, 20]:
    pass
    #plt.plot(x_vals, f(x_vals, n))
plt.plot(x_vals, r(x_vals), 'k--')
plt.plot(x_vals, rF(x_vals))
plt.show()
#plt.savefig("11.2.29.pdf")
