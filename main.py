import utility as util
import linreg as lr


def main():

    u = util.Utility()
    data = u.read_data("./sample_data/student_scores.csv")

    linear_regression = lr.LinReg(data)
    slope, intercept = linear_regression.perform_linear_regression(1000, 0.01)
    print(slope, intercept)

    u.plot_points(data, slope, intercept)


if __name__ == "__main__":
    main()