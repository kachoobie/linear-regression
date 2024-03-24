import utility as util
import linreg as lr


def main():

    u = util.Utility()
    data = u.read_data("./sample_data/data.csv")

    linear_regression = lr.LinReg(data)
    slope, intercept = linear_regression.perform_linear_regression(5000, 0.0001)


    u.plot_points(data, slope, intercept)


if __name__ == "__main__":
    main()