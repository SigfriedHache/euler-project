"""
https://projecteuler.net/problem=16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

from Common.Logger import get_logger, init_logger
from Common.Utilities import performance_run


PERFORMANCE_RUNS = 1_000
BASE = 2
POWER = 1000


def fastest(*args, **kwargs) -> int:
    return brute_force(*args, **kwargs)


def brute_force(base: int, power: int) -> int:
    return sum(map(int, str(base ** power)))


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run for fastest
    performance_run(fastest, iterations=PERFORMANCE_RUNS)(BASE, POWER)
