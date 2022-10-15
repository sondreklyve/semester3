import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
# Kort om fysiske enheter i numeriske beregninger
# Enheter
h_bar = 1
m_e = 1
e = 1

N = 10
delta_x = 0.01
x_0, x_n = 0, N
x_vec = np.arange(x_0, x_n, delta_x)
E_vec = np.zeros(N)


def normalizing_factor(psi):
    return integrate.quad(abs(psi)**2, -np.inf, np.inf)


def solve_schrodinger(V, m):
    N = len(V)
    H = np.zeros((N, N))

    for i in range(N):
        H[i, i] = h_bar ** 2 / (m * delta_x ** 2) + V[i]
        if i+1 < N:
            H[i, i+1] = - h_bar ** 2 / (2 * m * delta_x ** 2) + V[i]
        if i > 0:
            H[i, i-1] = - h_bar ** 2 / (2 * m * delta_x ** 2) + V[i]

    print(H)

    val, vec = np.linalg.eig(H)

    print(val)
    print(vec)


