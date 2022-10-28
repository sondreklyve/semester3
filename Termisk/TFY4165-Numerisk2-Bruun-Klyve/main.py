import numpy as np
import matplotlib.pyplot as plt

from read_data import Mass

"""
Imports Mass class from read_data.py, and make various plots and calculations on these objects.
Most functionality is defined in the functions below,
while the code is executed from the main-function at the very bottom of this file.

The code run in main are structured into the subproblems as suggested in the assignement text,
which is made clear by the comments.
"""


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
    k_p = m * np.average(v_list**2) / (2 * T)
    return f"{k_p = :.3f} J/K"


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
    plt.title('Spredningsplott posisjon')
    plt.xlabel('x (cm)')
    plt.ylabel('y (cm)')
    for mass in mass_list:
        mass.scatter_pos()

    plt.figure(5)
    plt.title('Spredningsplott hastighet')
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
        f"{average = :.3f} cm/s \n"
        f"{rms = :.3f} cm/s \n"
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
        masses.append(Mass(f"data/mass8_{i+1}.txt"))

    v_list_x, v_list_y, v_list_tot = concatenate_velocities(masses)

    # Oppgave a)
    plot_hist(masses)
    plot_scatter(masses, np.average(v_list_x), np.average(v_list_y))

    # Oppgave b)
    print(boltzmann_constant(mass, temperature, v_list_tot))

    print()  # Newline

    # Oppgave c)
    print(average_vs_rms(v_list_tot))

    print()  # Newline

    # Oppgave d)
    print(f"Average velocity x: {np.average(v_list_x):.3f} cm/s")
    print(f"Average velocity y: {np.average(v_list_y):.3f} cm/s")

    
    plt.show()



if __name__ == "__main__":
    main()
