"""
https://projecteuler.net/problem=6
The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + 3^2 + 4^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
    (1 + 2 + 3 + 4 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
    3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

from Common.Utilities import get_logger, init_logger

PERFORMANCE_RUNS = 1


# def fastest(...) -> ...:
#     """
#     :return: ...
#     """
#     return ...


def generative(max_number: int = 100) -> int:
    sum_of_squares = 0
    for i in range(1, max_number+1):
        sum_of_squares += i**2

    square_of_sums = sum(i for i in range(1, max_number+1))**2

    return square_of_sums - sum_of_squares

if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()
