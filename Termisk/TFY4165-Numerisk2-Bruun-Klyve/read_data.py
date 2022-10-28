import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""
This file is meant to separate the reading of data from the functionality in main.py.
It defines the Mass objects, which structures the data set into objects.
These objects are defined here, and used in main.py
"""

class Mass:
    def __init__(self, filename):
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
