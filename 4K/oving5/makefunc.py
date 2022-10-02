import matplotlib.pyplot as plt
import numpy as np

def a(n):
    return 1/(n**2)

def f(x, n):
    val = 0
    for i in range(1, n+1):
        val += a(i) * np.sin(i * x)
    return val

def g(x, n):
    val = np.pi/2 
    for i in range(1, n+1, 2):
        val += a(i) * np.cos(i * x)
    return val

x_vals = np.linspace(-4, 4, 1001)
for n in [20]:
    plt.plot(x_vals, f(x_vals, n), 'b')
    plt.plot(x_vals, g(x_vals, n), 'r')
plt.show()
#plt.savefig("11.2.29.pdf")
#def E(N):
#	return 2*np.pi**3/3 - 4*np.pi*sum([1/n**2 for n in range(1, N+1)])
#[print(i, E(i)) for i in [1, 2,3,4,5,10, 100, 1000]]
