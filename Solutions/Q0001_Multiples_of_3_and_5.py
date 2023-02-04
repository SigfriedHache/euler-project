"""
https://projecteuler.net/problem=1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from Common.Logger import get_logger, init_logger
from Common.Sum import sum_1_to_n
from Common.Utilities import performance_run

PERFORMANCE_RUNS = 10_000
NUMBER = 1_000


def fastest(*args, **kwargs) -> int:
    return analytic(*args, **kwargs)


def generative(n: int = NUMBER) -> int:
    """
    O(n) algorithm that solves the problem statement above
    :param n: The high-side boundary of the summation
    :return: The resultant sum
    """
    summation = 0
    for num in range(0, n):
        if num % 3 == 0 or num % 5 == 0:
            summation = summation + num
    return summation


def analytic(n: int = NUMBER) -> int:
    """
    :param n: The high-side boundary of the summation
    :return: The resultant sum
    """
    n = n - 1
    return (3 * sum_1_to_n(n//3)) + (5 * sum_1_to_n(n//5)) - (15 * sum_1_to_n(n//15))


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance runs for the analytic and generative solutions
    performance_run(generative, iterations=PERFORMANCE_RUNS)()
    performance_run(analytic, iterations=PERFORMANCE_RUNS)()
    # print(fastest(NUMBER))
