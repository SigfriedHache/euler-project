"""
https://projecteuler.net/problem=4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from Common.Utilities import get_logger, init_logger
from Common.Patterns import is_palindrome
from Common.Utilities import performance_run

PERFORMANCE_RUNS = 100


def fastest() -> int:
    """ This algorithm determines the largest palindrome that can be expressed as the product of two 3-digit numbers """
    return full_search()


def full_search() -> int:
    """
    This algorithm determines the largest palindrome that can be expressed as the product of two 3-digit numbers
    --> benchmark: 19223 ms/run
    """
    x = 999
    y = 999
    floor = 836  # the largest square palindrome is 836**2 = 698896, set as a floor
    palindromes = []

    for i in range(x, floor, -1):
        for j in range(y, floor, -1):
            palindrome_candidate = i * j
            if is_palindrome(palindrome_candidate):
                palindromes += [palindrome_candidate]

    return max(palindromes)


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run
    performance_run(full_search, iterations=PERFORMANCE_RUNS)()
