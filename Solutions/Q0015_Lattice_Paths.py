"""
https://projecteuler.net/problem=14

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly
6 routes to the bottom right corner:

O * * * * * *        O * * * . . .        O * * * . . .        O . . . . . .        O . . . . . .        O . . . . . .
.     .     *        .     *     .        .     *     .        *     .     .        *     .     .        *     .     .
. . . . . . *        . . . * * * *        . . . * . . .        * . . . . . .        * * * * . . .        * * * * * * *
.     .     *        .     .     *        .     *     .        *     .     .        .     *     .        .     .     *
. . . . . . X        . . . . . . X        . . . * * * X        * * * * * * X        . . . * * * X        . . . . . . X

How many such routes are there through a 20×20 grid?
"""

from Common.Logger import get_logger, init_logger
from Common.Numbers import n_choose_k
from Common.Utilities import performance_run


PERFORMANCE_RUNS = 1_000
SIDE_LENGTH = 20  # This is the side-length of the square


def fastest(*args, **kwargs) -> int:
    return analytic(*args, **kwargs)


def analytic(side_length: int = SIDE_LENGTH) -> int:
    """
    This function implements an analytic solution to this problem, by simplifying the problem statement to an n choose k
    expansion problem. The number of paths is equal to 2*side_length choose side_length. E.g.: the number of paths for a
    2 x 2 grid = 4 choose 2 = (4!) / (2! * (4-2)!) = 6
    :param side_length: This is the side length of the square, as defined by the number of units across or down the
    square is. Conveniently, the total length of any solve path will be 2 * side_length long.
    :return:
    """
    return n_choose_k(2 * side_length, side_length)


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run for fastest
    performance_run(fastest, iterations=PERFORMANCE_RUNS)(SIDE_LENGTH)
    logger.info('done')
