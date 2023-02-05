"""
https://projecteuler.net/problem=25

The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

from Common.Logger import get_logger, init_logger
from Common.Patterns import yield_fib
from Common.Utilities import performance_run

PERFORMANCE_RUNS = 1_000
DIGIT_COUNT = 1_000


# def fastest(*args, **kwargs):
#     return fx(*args, **kwargs)


def fib_yield_fx(digit_count: int) -> int:
    index = 1
    fib_generator = yield_fib()
    while len(str(next(fib_generator))) < digit_count:
        index = index + 1
    return index


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run for fastest
    # performance_run(fastest, iterations=PERFORMANCE_RUNS)()
    print(fib_yield_fx(DIGIT_COUNT))
