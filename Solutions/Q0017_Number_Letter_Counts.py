"""
https://projecteuler.net/problem=17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one
hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

from num2words import num2words

from Common.Logger import get_logger, init_logger
from Common.Utilities import performance_run

PERFORMANCE_RUNS = 1_000
MAX_NUMBER = 1_000


def fastest(*args, **kwargs) -> int:
    return full_crawl(*args, **kwargs)


def full_crawl(n: int) -> int:
    length = 0
    for number in range(1, n+1):
        length = length + len(num2words(number).replace(' ', '').replace('-', ''))
    return length


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run for fastest
    performance_run(fastest, iterations=PERFORMANCE_RUNS)(MAX_NUMBER)
