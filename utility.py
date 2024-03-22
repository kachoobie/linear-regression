"""
Utility class for reading in and plotting data.
"""

import matplotlib.pyplot as plt
import numpy as np

class Utility:

    def __init__(self) -> None:
        pass

    def read_data(self, path) -> list:

        data = []

        f = open(path)
        for line in f:
            try:
                coord = line.split(",")
                point = float(coord[0]), float(coord[1])
                data.append(point)
            except:
                continue

        f.close()
        return data
    

    def plot_points(self, points, slope, intercept):

        x_points = []
        y_points = []

        min_x = points[0][0]
        max_x = points[0][0]

        for point in points:
            x_points.append(point[0])
            y_points.append(point[1])

            if point[0] < min_x:
                min_x = point[0]
            if point[0] > max_x:
                max_x = point[0]
        
        x_points = np.array(x_points)
        y_points = np.array(y_points)

        overhang = (max_x - min_x) * 0.1
        x_regression = np.linspace(min_x - overhang, max_x + overhang)
        y_regression = slope * x_regression + intercept

        plt.scatter(x_points, y_points)
        plt.plot(x_regression, y_regression, color="red")
        plt.show()