import matplotlib.pyplot as plt
import numpy as np


def a(n):
    return -4 / (np.pi * n**2)


def c(n):
    return 100/np.pi * (1/(n * np.sinh(n * np.pi)))


def f(x, n):
    val = np.pi / 2
    for i in range(1, n + 1):
        val += a(i) * np.sin(i * x)
    return val


def g(x, t):
    val = np.pi / 2
    n = 50
    for i in range(1, n + 1, 2):
        val += a(i) * np.cos(i * x) * np.exp(-i * t)
    return val

def u(x, y):
    n = 100
    val = 0
    for i in range(1, n + 1, 2):
        val += c(i) * np.sin(i * np.pi * x / 24) * np.sinh(i * np.pi * y / 24)
    return val


x, y = np.meshgrid(np.linspace(0, 24, 400), np.linspace(0, 24, 400))
z = u(x, y) 
 
fig, ax = plt.subplots()
ax.set_aspect(1)
plt.pcolormesh(x, y, z, cmap='jet')
plt.colorbar()
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
#plt.savefig("11.6.12.pdf")
# def E(N):
# 	return 2*np.pi**3/3 - 4*np.pi*sum([1/n**2 for n in range(1, N+1)])
# [print(i, E(i)) for i in [1, 2,3,4,5,10, 100, 1000]]
