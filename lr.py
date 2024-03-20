#!/usr/bin/env python

# Three main ideas behind linear regression:
#
#   1) Fit a line to data using least squares
#   2) Calculate R^2 value
#   3) Calculate p-value for R^2
#
# References: https://www.youtube.com/watch?v=PaFPbb66DxQ&ab_channel=StatQuestwithJoshStarmer
# https://www.youtube.com/watch?v=nk2CQITm_eo&ab_channel=StatQuestwithJoshStarmer

import matplotlib.pyplot as plt
import numpy as np

# Read in data from csv file, convert to tuples, and return as
# list of tuples.
def intake_data(file_path="./sample_data/sample.csv"):

    data = []

    f = open(file_path)
    for line in f:
        try:
            coord = line.split(",")
            point = float(coord[0]), float(coord[1])
            data.append(point)
        except:
            continue
    
    f.close()

    return data


def plot_data(data, x_name="", y_name=""):
    x_points = []
    y_points = []

    for datum in data:
        x_points.append(datum[0])
        y_points.append(datum[1])
    
    x_points = np.array(x_points)
    y_points = np.array(y_points)

    plt.scatter(x_points, y_points)
    plt.show()

plot_data(intake_data())

# Task 1: Fitting a line to data

# Start with line w/ 0 slope and y-intercept at the average y-value
# of the data.

def find_avg_y_value(y_values):

    sum_of_y = 0
    for i in y_values:
        sum_of_y += i[1]
    
    avg = sum_of_y / len(y_values)

    return avg

# Next, determine how well the line fits to the data using residuals.
# Note, you will need to take the sum of squares of the residuals. This is 
# necessary since some points may be above your line, making the residual 
# negative. This in turn would suggest a better fit than in reality.

def find_y_value(slope, intercept, x):
    return slope * x + intercept

def calc_sum_of_squares(real_points, slope_guess, intercept_guess):
    pass