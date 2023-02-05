"""
https://projecteuler.net/problem=24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3
and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from itertools import permutations
from typing import List

from Common.Logger import get_logger, init_logger
from Common.Utilities import performance_run

PERFORMANCE_RUNS = 1_000
DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
INDEX = 1_000_000


def fastest(*args, **kwargs):
    return iter_tool(*args, **kwargs)


def iter_tool(digits: List[int], index: int) -> str:
    digit_list = "".join(map(str, digits))
    permutation_list = list(permutations(digit_list))
    return "".join(permutation_list[index])


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run for fastest
    # performance_run(fastest, iterations=PERFORMANCE_RUNS)()
    print(iter_tool(DIGITS, INDEX))
