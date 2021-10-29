"""
https://projecteuler.net/problem=9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from Common.Geometry import is_pythagorean_triple
from Common.Logger import get_logger, init_logger
from Common.Utilities import performance_run

PERFORMANCE_RUNS = 1_000
TRIPLET_SUM = 1000


def fastest(triplet_sum: int = TRIPLET_SUM) -> int:
    """ This algorithm returns the product of the pythagorean triple that sums to 1000 """
    return full_search(triplet_sum)


def full_search(triplet_sum: int = TRIPLET_SUM) -> int:
    """
    This algorithm performs a full search for the triplet that satisfies all three of the following equations:
        a < b < c
        a + b + c = triplet_sum
        a^2 + b^2 = c^2
    Then, this algorithm returns a product of the triplet.
    :param triplet_sum: This is the maximum value that the triplet must sum to
    :return: The product of a*b*c
    """
    # a, b march up, while c marches down
    a = 1
    a_limit = int(triplet_sum/3) - 1
    b = 2
    c = triplet_sum - (a + b)

    while a < a_limit:
        while b < c:
            if is_pythagorean_triple(a, b, c):
                return a*b*c
            b += 1
            c -= 1
        a += 1
        b = a + 1
        c = triplet_sum - (a + b)


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run for fastest
    performance_run(full_search, iterations=PERFORMANCE_RUNS)()
