"""
https://projecteuler.net/problem=12
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""
import numpy as np

from Common.Logger import get_logger, init_logger
from Common.Utilities import performance_run
from Common.Numbers import factorization, nth_triangular_number

PERFORMANCE_RUNS = 10
DIVISOR_COUNT = 500


def fastest(*args, **kwargs) -> int:
    """ This is the fastest function that finds the largest product in a grid series """
    return generative(*args, **kwargs)


def generative(divisor_count: int = DIVISOR_COUNT) -> int:
    """
    This method starts from the beginning and performs a full search of triangular numbers to find the first one that
    satisfies the minimum number of required divisors
    :param divisor_count: This is the minimum number of divisors criteria that the solution has to find
    :return: This is the number that satisfies the minimum number of divisors criteria
    """
    divisor_list = []
    i = 0
    number = 0
    while len(divisor_list) < divisor_count:
        i = i + 1
        number = number + i
        divisor_list = factorization(number)
    return number


def predictive(divisor_count: int = DIVISOR_COUNT) -> int:
    """
    This method jumps ahead to a triangular number that could viably contain the number of divisors that are being
    sought in the answer.
    :param divisor_count: This is the minimum number of divisors criteria that the solution has to find
    :return: This is the number that satisfies the minimum number of divisors criteria
    """
    divisor_list = []
    i = ((1 + int(np.sqrt(8*divisor_count + 1))) // 2) - 1  # This primes the algorithm to start at further-along value
    number = nth_triangular_number(i)

    while len(divisor_list) < divisor_count:
        i = i + 1
        number = number + i
        divisor_list = factorization(number)

    return number


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run for fastest
    performance_run(generative, iterations=PERFORMANCE_RUNS)()
    performance_run(predictive, iterations=PERFORMANCE_RUNS)()
    # print(fastest())
