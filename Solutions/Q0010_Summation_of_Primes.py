"""
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from Common.Primes import sieve_of_atkin
from Common.Logger import get_logger, init_logger
from Common.Utilities import performance_run

PERFORMANCE_RUNS = 1_000
PRIME_CEILING = 2_000_000


def fastest(prime_ceiling: int = PRIME_CEILING) -> int:
    """ This is the fastest algorithm that returns the sum of all primes below PRIME_CEILING """
    return sieve_sum(prime_ceiling)


def sieve_sum(prime_ceiling: int = PRIME_CEILING) -> int:
    return sum(sieve_of_atkin(prime_ceiling))


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run for fastest
    # performance_run(fastest, iterations=PERFORMANCE_RUNS)()
    print(fastest(PRIME_CEILING))
