"""
https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is:
    1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is:
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is:
    3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

from Common.Logger import get_logger, init_logger
from Common.Sum import sum_1_to_n
from Common.Utilities import performance_run

PERFORMANCE_RUNS = 10_000
UPPER_BOUND = 100


def fastest(upper_bound: int = UPPER_BOUND) -> int:
    """ This algorithm returns the difference between the sum of the squares and the square of the sum """
    return analytic(upper_bound)


def analytic(upper_bound: int = UPPER_BOUND) -> int:
    """
    This function calculates the answer to Q6 using an analytic solution to the (sum of n)^2, and a generator for the
    solution of sum(n^2) as no analytic shortcuts exist.
    :param upper_bound: This is the upper bound to which this calculation is completed
    :return: The int answer to Q6
    """
    sum_of_squares = 0
    for n in range(1, upper_bound+1):
        sum_of_squares += n**2

    square_of_sum = sum_1_to_n(upper_bound)**2

    return square_of_sum - sum_of_squares


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    performance_run(analytic, iterations=PERFORMANCE_RUNS)()
