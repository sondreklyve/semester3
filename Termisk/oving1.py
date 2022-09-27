import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

p0 = 600  # Pa
R = 8.314
g = 3.71
m = 0.04334

def T(z):
    return 234 - 2.25*z + 14*np.exp(-2*z)


def integrand(z):
    return (m * g) / (R * T(z))

def p(z):
    return p0 * np.exp(integrate.quad(integrand, 0, z)[0])

def p2(z):
    return p0 * np.exp(- (z * m * g)/(R * 234))

z_vals = np.arange(0, 180)
p_vals = [p(z) for z in z_vals]
p2_vals = [p2(z) for z in z_vals]
plt.plot(p_vals, z_vals)
plt.plot(p2_vals, z_vals, 'y--')
plt.grid(True)
plt.show()
