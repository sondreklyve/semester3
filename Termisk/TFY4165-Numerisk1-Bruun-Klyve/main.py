import matplotlib.pyplot as plt
import numpy as np

def simulate_fleas(N, NT):
    """Simulerer tidsutvikling av loppene på hund A, og plotter utviklingen"""
    NT_list = np.arange(1, NT)  # En liste med alle tidssteg
    NA = np.zeros(NT)  # Lopper på hund A
    NB = np.zeros(NT)  # Lopper på hund B
    loppested = np.full(N, 1)  # Alle loppene plasseres på hund A

    NA[0] = N

    # Genererer en liste med hvilke loppe som hopper ved gitt tidssteg
    hopper = np.random.randint(0, high=N, size=NT)

    # Itererer over alle tidssteg
    for i in NT_list:
        if loppested[hopper[i]] == 1:
            loppested[hopper[i]] = 0  # Flytt loppe til hund B
            NB[i] = NB[i - 1] + 1  # Inkrementer NB
            NA[i] = NA[i - 1] - 1  # Dekrementer NA
        else:
            loppested[hopper[i]] = 1  # Flytt loppe til hund A
            NA[i] = NA[i - 1] + 1  # Inkrementer NA
            NB[i] = NB[i - 1] - 1  # Dekrementer NB

    # Plot utviklingen
    plt.figure()
    plt.title(f'Tidsutvikling med {N} lopper')
    plt.plot(NT_list, analytical(NT_list, N), label='Analytisk')  # Plotter analytisk løsning
    plt.plot(NT_list, NA[:NT-1], label='Numerisk')  # Plotter lopper på hund A over tid
    plt.xlabel("t/s")
    plt.ylabel("Antall lopper på hund A")
    plt.legend()
    plt.savefig(f"{N}_lopper.pdf")

    
def analytical(t, N):
    """Analytisk løsning av problemet"""
    return N / 2 * (1 + np.exp(-2 * t / N))


def main():
    NT = [100, 3000, 30000]  # Totalt antall tidssteg
    N = [6, 1000, 20000]  # Antall lopper
    [simulate_fleas(n, nt) for n, nt in zip(N, NT)]
    # plt.show()


if __name__ == '__main__':
    main()

