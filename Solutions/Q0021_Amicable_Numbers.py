"""
https://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable
numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The
proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from Common.Logger import get_logger, init_logger
from Common.Utilities import performance_run
from Common.Numbers import factorization

PERFORMANCE_RUNS = 1_000
CEIL = 10_000


def fastest(*args, **kwargs):
    return full_crawl(*args, **kwargs)


def full_crawl(ceil: int) -> int:
    if ceil < 2:
        raise ValueError(f"This algorithm is only valid for ceil >= 2; ({ceil =})")

    a = 2
    amicable_numbers = set()
    while a < ceil:
        d_a = sum(factorization(a)) - a  # sum of aliquot divisors
        d_b = sum(factorization(d_a)) - d_a  # sum of aliquot divisors
        if a == d_a:
            pass
        elif d_b == a:
            if d_a < ceil:
                amicable_numbers.add(d_a)
            amicable_numbers.add(d_b)
        a = a + 1
    return sum(amicable_numbers)


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run for fastest
    performance_run(fastest, iterations=PERFORMANCE_RUNS)(CEIL)
    # print(full_crawl(CEIL))
