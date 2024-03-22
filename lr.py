#!/usr/bin/env python

# Three main ideas behind linear regression:
#
#   1) Fit a line to data using least squares
#   2) Calculate R^2 value
#   3) Calculate p-value for R^2
#
# References: 
# https://www.youtube.com/watch?v=PaFPbb66DxQ&ab_channel=StatQuestwithJoshStarmer
# https://www.youtube.com/watch?v=nk2CQITm_eo&ab_channel=StatQuestwithJoshStarmer
# https://www.geeksforgeeks.org/ml-linear-regression/

import matplotlib.pyplot as plt
import numpy as np

# These are helper functions that do not directly relate to performing linear
# regression. They are used mostly to scrape data from files and plot data.

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


def plot_data(data, slope, intercept, x_name="", y_name=""):
    x_points = []
    y_points = []

    min_x = data[0][0]
    max_x = data[0][0]
    for datum in data:
        x_points.append(datum[0])
        y_points.append(datum[1])

        if datum[0] < min_x:
            min_x = datum[0]
        if datum[0] > max_x:
            max_x = datum[0]
    
    x_points = np.array(x_points)
    y_points = np.array(y_points)

    x = np.linspace(min_x - len(data) * 0.2, max_x + len(data) * 0.2)
    y = slope * x + intercept

    plt.scatter(x_points, y_points)
    plt.plot(x, y, color="red")
    plt.show()


# Task 1: Fitting a line to data

# Start with line w/ 0 slope and y-intercept at the average y-value
# of the data.

def find_avg_y_value(y_values):

    sum_of_y = 0
    for i in y_values:
        sum_of_y += i[1]
    
    avg = sum_of_y / len(y_values)

    return avg

# We need a cost function to determine how well our current line fits to the data (so that we can
# compare different lines to each other). This is simply the average of the sum of the squares of 
# the difference between our predicted and observed values.
def calculate_cost(slope_guess, intercept_guess, points):

    sum_of_squares = 0
    for point in points:
        y_guess = slope_guess * point[0] + intercept_guess
        y_actual = point[1]
        sum_of_squares += (y_guess - y_actual) * (y_guess - y_actual)
    
    average_sum_of_squares = sum_of_squares / len(point)
    return average_sum_of_squares


# We use gradient descent to modify the slope and y-intercept to find the local minimum.
# Finding the line of best fit is actually a multivariate function, since the cost
# function depends both on the line's slope and y-intercept. Therefore, we perform
# gradient descent on both variables.

def nudge_intercept(slope_guess, intercept_guess, alpha, points):

    deriv = 0

    for point in points:
        observed = point[1]
        predicted = slope_guess * point[0] + intercept_guess
        difference = predicted - observed
        deriv += difference

    deriv = deriv * 2 / len(points)
    nudge = intercept_guess - alpha * deriv
    return nudge

def nudge_slope(slope_guess, intercept_guess, alpha, points):
    
    sum = 0

    for point in points:
        observed = point[1]
        predicted = slope_guess * point[0] + intercept_guess
        difference = predicted - observed
        sum += difference * point[0]
    
    deriv = sum * 2 / len(points)
    nudge = slope_guess - alpha * deriv
    return nudge

def gradient_descent(slope_initial, intercept_initial, alpha, num_iter, points):

    current_slope = slope_initial
    current_intercept = intercept_initial

    i = 0
    while i < num_iter:

        current_slope = nudge_slope(current_slope, current_intercept, alpha, points)
        current_intercept = nudge_intercept(current_slope, current_intercept, alpha, points)

        print(current_slope, current_intercept)

        i += 1
    
    return current_slope, current_intercept


if __name__ == "__main__":

    points = intake_data("./sample_data/ice_cream.csv")

    initial_intercept = find_avg_y_value(points)
    intitial_slope = 0

    vals = gradient_descent(intitial_slope, initial_intercept, 0.5, 500, points)
    plot_data(points, vals[0], vals[1])
