"""
https://projecteuler.net/problem=23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two
abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as
the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is
known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from Common.Logger import get_logger, init_logger
from Common.Numbers import factorization
from Common.Sum import sum_1_to_n
from Common.Utilities import performance_run

PERFORMANCE_RUNS = 10
MAX_VIABLE = 28124


def fastest(*args, **kwargs):
    return full_crawl(*args, **kwargs)


def full_crawl(ceil: int) -> int:
    """
    Step 1: Find all the abundant numbers
    Step 2: Permute and sum all pairs
    Step 3: Sum integers not in the set produced in Step 2
    """
    total_sum = sum_1_to_n(ceil)

    # Step 1: List of Abundant Numbers
    abundant_list = [n for n in range(1, ceil) if (sum(factorization(n)) - n) > n]

    # Step 2: Find all integers
    sum_list = set()
    while len(abundant_list) >= 1:
        num1 = abundant_list[0]
        for num2 in abundant_list:
            if num1 + num2 <= ceil:
                sum_list.add(num1 + num2)
            else:
                abundant_list.pop(0)
                break

    # Step 3: Return sum for all the positive integers which cannot be written as the sum of two abundant numbers
    return total_sum - sum(sum_list)


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run for fastest
    # performance_run(fastest, iterations=PERFORMANCE_RUNS)(MAX_VIABLE)
    print(full_crawl(MAX_VIABLE))
