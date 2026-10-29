"""Z-test and independent t-test for student performance."""

import numpy as np
from scipy import stats
from statsmodels.stats.weightstats import ztest


def show_decision(p_value, alpha=0.05):
    if p_value < alpha:
        print("\nResult: Reject Null Hypothesis")
    else:
        print("\nResult: Fail to Reject Null Hypothesis")


def main():
    print("----- Z-Test -----")
    marks = np.array([78, 82, 85, 88, 90, 76, 95, 89, 84, 91])
    expected_mean = 80

    z_score, probability = ztest(marks, value=expected_mean)
    print("Sample Marks:")
    print(marks)
    print("\nPopulation Mean:", expected_mean)
    print("\nZ-Statistic:", z_score)
    print("P-Value:", probability)
    show_decision(probability)

    print("\n----- Independent t-Test -----")
    group_one = np.array([78, 82, 85, 88, 90])
    group_two = np.array([72, 75, 70, 68, 74])

    t_score, probability = stats.ttest_ind(group_one, group_two)
    print("Class A Marks:")
    print(group_one)
    print("\nClass B Marks:")
    print(group_two)
    print("\nt-Statistic:", t_score)
    print("P-Value:", probability)
    show_decision(probability)


if __name__ == "__main__":
    main()
