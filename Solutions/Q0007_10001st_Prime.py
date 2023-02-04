"""
https://projecteuler.net/problem=7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

from Common.Logger import get_logger, init_logger
from Common.Primes import prime_list, yield_prime
from Common.Utilities import performance_run

PERFORMANCE_RUNS = 10
PRIME_INDEX = 10_001


def fastest(*args, **kwargs) -> int:
    """ This algorithm returns the nth prime """
    return brute_force(*args, **kwargs)


def brute_force(prime_index: int = PRIME_INDEX) -> int:
    """
    This function utilizes the prime_list function, which generates a full list of primes up to the PRIME_INDEX-th prime
    :param prime_index: The index of the prime in question
    :return: The prime in question
    """
    return prime_list(prime_index)[-1]


def generator(prime_index: int = PRIME_INDEX) -> int:
    """
    This function utilizes the prime generator function from the Primes.py package (i.e. yield_prime()) and loops over
    until it reaches the desired prime
    :param prime_index: The index of the prime in question
    :return: The prime in question
    """
    prime_generator = yield_prime()
    for _ in range(prime_index - 1):
        next(prime_generator)
    return int(next(prime_generator))


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run for brute_force
    # performance_run(brute_force, iterations=PERFORMANCE_RUNS)()
    # performance_run(generator, iterations=PERFORMANCE_RUNS)()
    print(fastest(PRIME_INDEX))
