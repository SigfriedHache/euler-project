"""
https://projecteuler.net/problem=5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from numpy import prod

from Common.Logger import get_logger, init_logger
from Common.Numbers import prime_factorization
from Common.Utilities import performance_run

PERFORMANCE_RUNS = 100_000
UPPER_BOUND = 20


def fastest(ceiling: int = UPPER_BOUND) -> int:
    """
    This algorithm finds the prime factorization of every number between 1 and ceiling, maintains the greatest counts of
    each prime factor found, and then multiplies them out at the end
    :param ceiling: The upper bound (inclusive) of the factor for which to find the evenly-divided quotient
    :return: The quotient evenly-divisible by every number from 1 to ceiling
    """
    return prime_tally(ceiling)


def prime_tally(ceiling: int = UPPER_BOUND) -> int:
    """
    This algorithm finds the prime factorization of every number between 1 and ceiling, maintains the greatest counts of
    each prime factor found, and then multiplies them out at the end
    --> benchmark: 104 ms/run
    :param ceiling: The upper bound (inclusive) of the factor for which to find the evenly-divided quotient
    :return: The quotient evenly-divisible by every number from 1 to ceiling
    """
    factorization_merge = []

    for number in range(1, ceiling+1):
        number_factorization = prime_factorization(number)
        for factor in set(number_factorization):
            factor_count_difference = number_factorization.count(factor) - factorization_merge.count(factor)
            if factor_count_difference > 0:
                factorization_merge += [factor] * factor_count_difference

    return prod(factorization_merge)


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run
    performance_run(prime_tally, iterations=PERFORMANCE_RUNS)()
