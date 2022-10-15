import matplotlib.pyplot as plt
import numpy as np
I = [0.924, 1.206, 1.446, 1.668, 1.854, 2.038, 2.268, 2.365, 2.516, 2.660, 2.796, 2.930]
V = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
mV = np.array([0.2, 0.8, 1.8, 3.1, 4.7, 6.5, 9.5, 10.8, 13.2, 15.7, 18.4, 21.1])
alpha = 4.5e-3
sigma = 5.67e-8
T0 = 25.2
R0 = 0.270226

T = np.array([(T0+(V[i]/I[i]-R0)/(alpha*R0)) for i in range(len(I))])
koeff = mV[0] / (sigma*T[0]**4)
plt.plot(V, mV, 'b')
plt.plot(V, 0.25*koeff*sigma*T**4, 'g')

print(koeff)

plt.show()
