"""
https://projecteuler.net/problem=20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

from Common.Logger import get_logger, init_logger
from Common.Utilities import performance_run
from math import factorial

PERFORMANCE_RUNS = 1_000
BASE = 100


def fastest(*args, **kwargs):
    return brute_force(*args, **kwargs)


def brute_force(n: int) -> int:
    if n > 150:
        raise MemoryError(f"The value {n}! produces too large of a value, please select a smaller number.")
    return sum(map(int, str(factorial(n))))


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run for fastest
    # performance_run(fastest, iterations=PERFORMANCE_RUNS)(BASE)
    print(brute_force(BASE))
