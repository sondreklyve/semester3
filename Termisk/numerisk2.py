import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class Mass:
    def __init__(self, index, filename):
        self.index = index
        self.data_set = self.load_data(filename)
        self.vx_list, self.vy_list, self.v_list = self.calculate_v()

    def load_data(self, filename):
        return pd.read_csv(
            filename, delim_whitespace=True, skiprows=[0, 1], names=["t", "x", "y"]
        )

    def get_data(self, type=""):
        if type:
            return self.data_set[type]
        else:
            return self.data_set

    def calculate_v(self):
        v_list = np.zeros((3, len(self.data_set) - 1))
        v_list[0] = np.diff(self.get_data("x")) / np.diff(self.get_data("t"))
        v_list[1] = np.diff(self.get_data("y")) / np.diff(self.get_data("t"))
        v_list[2] = np.sqrt(v_list[0] ** 2 + v_list[1] ** 2)
        return v_list

    def scatter_pos(self):
        plt.scatter(self.get_data("x"), self.get_data("y"), marker="x", c="k")

    def scatter_v(self):
        plt.scatter(self.vx_list, self.vy_list, marker=".", c="b")


def boltzmann_component_distribution(v_list):
    B = 1 / np.average(v_list**2)
    return np.sqrt(B / np.pi) * np.exp(-B * v_list**2)


def boltzmann_distribution(v_list):
    B = 1 / np.average(v_list**2)
    return 2 * B * v_list * np.exp(-B * v_list**2)


def boltzmann_constant(m, T, v_list):
    k_b = 1.38e-23  # Boltzmanns constant [J/K]
    k_p = m * np.average(v_list**2) / (2 * T)
    T_gass = m * np.average(v_list**2) / (2 * k_b)
    return f"{k_p = :.3f}\t{T_gass = :.3e}"


def concatenate_velocities(mass_list):
    v_list_x = np.concatenate([mass.vx_list for mass in mass_list])
    v_list_y = np.concatenate([mass.vy_list for mass in mass_list])
    v_list_tot = np.concatenate([mass.v_list for mass in mass_list])
    return (v_list_x, v_list_y, v_list_tot)


def plot_hist(mass_list):
    v_list_x, v_list_y, v_list_tot = concatenate_velocities(mass_list)

    plt.figure(1)
    plt.title("$v_x$")
    plt.hist(v_list_x, bins=20, density=True, facecolor="blue", alpha=0.5)
    plt.plot(v_list_x, boltzmann_component_distribution(v_list_x), "r.")

    plt.figure(2)
    plt.title("$v_y$")
    plt.hist(v_list_y, bins=20, density=True, facecolor="blue", alpha=0.5)
    plt.plot(v_list_y, boltzmann_component_distribution(v_list_y), "r.")

    plt.figure(3)
    plt.title("$v$")
    plt.hist(v_list_tot, bins=20, density=True, facecolor="blue", alpha=0.5)
    plt.plot(v_list_tot, boltzmann_distribution(v_list_tot), "r.")


def plot_scatter(mass_list, average_v_x, average_v_y):
    plt.figure(4)
    for mass in mass_list:
        mass.scatter_pos()

    plt.figure(5)
    plt.vlines(average_v_x, ymin=-500, ymax=500, colors="r", linestyles="dashed")
    plt.hlines(average_v_y, xmin=-500, xmax=500, colors="r", linestyles="dashed")
    for mass in mass_list:
        mass.scatter_v()


def average_vs_rms(v_list):
    average = np.average(v_list)
    rms = np.sqrt(np.average(v_list**2))
    ratio = average / rms
    diff = abs(ratio - np.sqrt(np.pi) / 2)
    return (
        f"{average = :.3f}\n"
        f"{rms = :.3f}\n"
        f"{ratio = :.3f}\n"
        f"√π/2 = {np.sqrt(np.pi)/2:.3f}\n"
        f"{diff = :.3f}\n"
    )


def main():
    data_file_count = 49
    mass = 0.032  # [kg]
    temperature = 300  # [K]

    masses = list()

    for i in range(data_file_count):
        masses.append(Mass(i, f"numerisk2/mass8_{i+1}.txt"))

    v_list_x, v_list_y, v_list_tot = concatenate_velocities(masses)

    # Oppgave a)
    plot_hist(masses)
    plot_scatter(masses, np.average(v_list_x), np.average(v_list_y))

    # Oppgave b)
    for v_list in concatenate_velocities(masses):
        print(boltzmann_constant(mass, temperature, v_list))

    print()  # Newline

    # Oppgave c)
    print(average_vs_rms(v_list_tot))


    plt.show()


if __name__ == "__main__":
    main()
