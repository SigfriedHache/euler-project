"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
from time import perf_counter_ns

from Common.Logger import get_logger, init_logger
from Common.Sum import sum_1_to_n

PERFORMANCE_RUNS = 1_000_000


def generative(n: int = 1000) -> int:
    """
    O(n) algorithm that solves the problem statement above
    --> benchmark: 113.204ms/run
    :param n: The high-side boundary of the summation
    :return: The resultant sum
    """
    summation = 0
    for i in range(0, n):
        if i % 15 == 0:
            summation += i
        elif i % 5 == 0:
            summation += i
        elif i % 3 == 0:
            summation += i
        else:
            pass
    return summation


def analytic(n: int = 1000) -> int:
    """
    O(1) algorithm that solves the problem statement above
    --> benchmark: 1.174ms/run
    :param n: The high-side boundary of the summation
    :return: The resultant sum
    """
    n -= 1
    return (3 * sum_1_to_n(int(n/3))) + (5 * sum_1_to_n(int(n/5))) - (15 * sum_1_to_n(int(n/15)))


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run for the analytic solution
    start = perf_counter_ns()
    for run in range(PERFORMANCE_RUNS):
        analytic()
    analytic_delta = perf_counter_ns() - start

    # Performance run for the generative solution
    start = perf_counter_ns()
    for run in range(PERFORMANCE_RUNS):
        generative()
    generative_delta = perf_counter_ns() - start

    # Print the results
    logger.info(f"Analytic answer:   {analytic()}  in  {int(analytic_delta/PERFORMANCE_RUNS)} ns")
    logger.info(f"Generative answer: {generative()}  in  {int(generative_delta/PERFORMANCE_RUNS)} ns")
