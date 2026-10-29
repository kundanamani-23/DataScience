"""Bernoulli and Binomial distributions: student pass/fail analysis."""

from scipy.stats import bernoulli, binom


def main():
    pass_probability = 0.7

    print("----- Bernoulli Distribution -----")
    outcomes = bernoulli.rvs(pass_probability, size=10)
    print("Probability of Passing:", pass_probability)
    print("Student Outcomes (1=Pass, 0=Fail):")
    print(outcomes)

    print("\nProbability of Pass:")
    print(bernoulli.pmf(1, pass_probability))
    print("Probability of Fail:")
    print(bernoulli.pmf(0, pass_probability))

    print("\n----- Binomial Distribution -----")
    students = 10
    passing = 8
    chance_exactly_passing = binom.pmf(passing, students, pass_probability)

    print("Number of Students:", students)
    print("Probability of Passing:", pass_probability)
    print(f"Probability that exactly {passing} students pass:")
    print(chance_exactly_passing)

    trials = binom.rvs(students, pass_probability, size=5)
    print("\nRandom Binomial Outcomes:")
    print(trials)


if __name__ == "__main__":
    main()
