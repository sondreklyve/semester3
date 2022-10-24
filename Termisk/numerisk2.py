import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class Mass:
    def __init__(self, index, filename):
        self.index = index
        self.data_set = self.load_data(filename)
        self.vx_list, self.vy_list, self.v_list = self.calculate_v()

    def load_data(self, filename):
        """Read data from file using pandas"""
        return pd.read_csv(
            filename, delim_whitespace=True, skiprows=[0, 1], names=["t", "x", "y"]
        )

    def get_data(self, type=""):
        """Return column (t, x or y) from the data set. If type is empty return entire data set"""
        if type:
            return self.data_set[type]
        else:
            return self.data_set

    def calculate_v(self):
        """Calculate velocities of the mass from its position over time"""
        v_list = np.zeros((3, len(self.data_set) - 1))
        v_list[0] = np.diff(self.get_data("x")) / np.diff(self.get_data("t"))
        v_list[1] = np.diff(self.get_data("y")) / np.diff(self.get_data("t"))
        v_list[2] = np.sqrt(v_list[0] ** 2 + v_list[1] ** 2)
        return v_list

    def scatter_pos(self):
        """Make scatter plot of the positions of the mass"""
        plt.scatter(self.get_data("x"), self.get_data("y"), marker="x", c="k")

    def scatter_v(self):
        """Make scatter plot of the velocities of the mass"""
        plt.scatter(self.vx_list, self.vy_list, marker=".", c="b")


def boltzmann_velocity_distribution(v_list):
    """Analytical estimate of velocity distribution from average velocity of masses"""
    B = 1 / np.average(v_list**2)
    return np.sqrt(B / np.pi) * np.exp(-B * v_list**2)


def boltzmann_speed_distribution(v_list):
    """Analytical estimate of speed distribution from average speed of masses"""
    B = 1 / np.average(v_list**2)
    return 2 * B * v_list * np.exp(-B * v_list**2)


def boltzmann_constant(m, T, v_list):
    """Calculate Boltzmanns constant for arbitrary particle of mass m"""
    k_b = 1.38e-23  # Boltzmanns constant [J/K]
    k_p = m * np.average(v_list**2) / (2 * T)
    T_gass = m * np.average(v_list**2) / (2 * k_b)
    return f"{k_p = :.3f}\t{T_gass = :.3e}"


def concatenate_velocities(mass_list):
    """Generate arrays of velocities from an array of mass objects"""
    v_list_x = np.concatenate([mass.vx_list for mass in mass_list])
    v_list_y = np.concatenate([mass.vy_list for mass in mass_list])
    v_list_tot = np.concatenate([mass.v_list for mass in mass_list])
    return (v_list_x, v_list_y, v_list_tot)


def plot_hist(mass_list):
    """Plot histograms for velocity of masses"""
    velocities = concatenate_velocities(mass_list)
    boltzmann_dists = (
        boltzmann_velocity_distribution(velocities[0]),
        boltzmann_velocity_distribution(velocities[1]),
        boltzmann_speed_distribution(velocities[2]),
    )
    labels = ('$v_x$', '$v_y$', '$v$')


    for v, boltzmann_dist, label in zip(velocities, boltzmann_dists, labels):
        plt.figure()
        plt.title("Histogram " + label)
        plt.hist(v, bins=20, density=True, facecolor='blue', alpha=0.5)
        plt.plot(v, boltzmann_dist, 'r.')
        plt.xlabel(label + ' (cm/s)')
        plt.ylabel('Andel fartsmålinger')


def plot_scatter(mass_list, average_v_x, average_v_y):
    """Make scatter plot of position and velocity of all masses in an array"""
    plt.figure(4)
    plt.xlabel('x (cm)')
    plt.ylabel('y (cm)')
    for mass in mass_list:
        mass.scatter_pos()

    plt.figure(5)
    plt.xlabel('$v_x$ (cm/s)')
    plt.ylabel('$v_y$ (cm/s)')
    for mass in mass_list:
        mass.scatter_v()

    # Plot average velocities to indicate drift
    plt.vlines(average_v_x, ymin=-500, ymax=500, colors="r", linestyles="dashed")
    plt.hlines(average_v_y, xmin=-500, xmax=500, colors="r", linestyles="dashed")


def average_vs_rms(v_list):
    """Compare root mean square velocity and average velocity of a mass"""
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

    for i in range(data_file_count):  # Read data from file and make mass objects
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
