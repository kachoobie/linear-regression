#!/usr/bin/env python

# Three main ideas behind linear regression:
#
#   1) Fit a line to data using least squares
#   2) Calculate R^2 value
#   3) Calculate p-value for R^2
#

import utility as u

util = u.Utility()
data = util.read_data("./sample_data/sample.csv")

class LinReg:

    def __init__(self, data) -> None:
        self.data = data
        self.slope = 0
        self.intercept = 0

    
    def calculate_cost(self) -> float:
        """Determines the output value of the cost function. The cost function 
        is the mean of squares of the differences between the observed and
        expected values."""

        error_squared_sum = 0

        for datum in self.data:

            observed = datum[1]
            expected = self.slope * datum[0] + self.intercept
            difference = observed - expected
            error_squared_sum += (difference * difference)
        
        num_points = len(self.data)

        return error_squared_sum / num_points
    
    def __calculate_slope_derivative(self) -> float:
        """The partial derivative with respect to the slope is the sum of 
        differences between observed and expected values multiplied by their 
        respected x values. This quantity is then multiplied by -2 over n."""

        sum_of_differences_times_x = 0

        for datum in data:

            observed = datum[1]
            expected = datum[0] * self.slope + self.intercept
            difference = observed - expected
            difference_times_x = difference * datum[0]
            sum_of_differences_times_x += difference_times_x
        
        num_points = float(len(self.data))
        deriv = sum_of_differences_times_x * -2 / num_points

        return deriv


    def __calculate_intercept_derivative(self) -> float:
        """The partial derivative with respect to the intercept is the sum of 
        the differences between observed and expected values multiplied by 
        -2 over n."""

        sum_of_differences = 0

        for datum in data:

            observed = datum[1]
            expected = datum[0] * self.slope + self.intercept
            difference = observed - expected
            sum_of_differences += difference
        
        num_points = float(len(self.data))
        deriv = sum_of_differences * -2 / num_points

        return deriv
    

    def __update_slope_and_intercept(self, alpha=0.05) -> None:

        slope_deriv = self.__calculate_slope_derivative()
        intercept_deriv = self.__calculate_intercept_derivative()

        self.slope = self.slope - alpha * slope_deriv
        self.intercept = self.intercept - alpha * intercept_deriv

        print(self.slope, self.intercept, slope_deriv, intercept_deriv)
    

    def __perform_gradient_descent(self, epochs=1000, alpha=0.05) -> None:

        for i in range(epochs):
            self.__update_slope_and_intercept(alpha)
    

    def perform_linear_regression(self, epochs=1000, alpha=0.05) -> tuple:

        self.__perform_gradient_descent(epochs, alpha)
        return self.slope, self.intercept


# --------------------
# Part 1
# --------------------

# Our initial regression line can have a random slope and 
# y-intercept. For simplicity, we set the slope to 0 and the
# intercept to the averave y-value of our observed data.

