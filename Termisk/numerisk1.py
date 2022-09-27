import matplotlib.pyplot as plt
import numpy as np

NT = 3000  # Totalt antall tidssteg
NT_list = np.arange(1, NT)  # En liste med alle tidssteg
N = 1000  # Antall lopper
NA = np.zeros(NT)  # Lopper på hund A
NB = np.zeros(NT)  # Lopper på hund B
loppested = np.full(N, 1)  # Alle loppene plasseres på hund A

NA[0] = N

# Genererer en liste med hvilke loppe som hopper ved gitt tidssteg
hopper = np.random.randint(0, high=N, size=NT)

# Looper over alle tidssteg
for i in NT_list:
    if loppested[hopper[i]] == 1:
        loppested[hopper[i]] = 0  # Flytt loppe til hund B
        NB[i] = NB[i - 1] + 1  # Inkrementer NB
        NA[i] = NA[i - 1] - 1  # Dekrementer NA
    else:
        loppested[hopper[i]] = 1  # Flytt loppe til hund A
        NA[i] = NA[i - 1] + 1  # Inkrementer NA
        NB[i] = NB[i - 1] - 1  # Dekrementer NB


def analytical(t):
    """Analytisk løsning av problemet"""
    return N / 2 * (1 + np.exp(-2 * t / N))


plt.plot(NT_list, analytical(NT_list))  # Plotter analytisk løsning
plt.plot(NT_list, NA[:NT-1])  # Plotter lopper på hund A over tid
plt.xlabel("X")
plt.ylabel("Y")
plt.show()  # Viser plot
