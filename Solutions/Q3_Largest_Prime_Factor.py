"""
https://projecteuler.net/problem=3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from numpy import sqrt

from Common.Logger import get_logger, init_logger
from Common.Primes import sieve_of_atkin
from Common.Utilities import performance_run

NUMBER = 600_851_475_143
PERFORMANCE_RUNS = 1000


def fastest(number: int = NUMBER) -> int:
    """
    This algorithm counts up from 1 to sqrt(number), factorizing the number along the way
    :param number: The number of which this function will find the greatest prime factor
    :return:
    """
    return reduction(number)


def reduction(number: int = NUMBER) -> int:
    """
    This algorithm counts up from 1 to sqrt(number), factorizing the number along the way
    --> benchmark: 56672789 ns/run (over 1000 runs)
    --> benchmark: 59520400 ns/run (over 1 run)
    :param number: The number which this function will find the greatest prime factor
    :return: The greatest prime factor
    """
    largest_prime = 1
    for i in range(2, int(sqrt(number) + 1)):
        while number % i == 0:
            largest_prime = i
            number = number/i
    return largest_prime if largest_prime != 1 else number


def cached_sieve(number: int = NUMBER) -> int:
    """
    This algorithm utilizes the Sieve of Atkin (the ~fastest~ prime sieve on the market) to generate a full list of
    primes up to sqrt(number). It then works its way backward in the list to see what the first prime factor is. The
    Primes library utilizes functools.lru_caching to avoid having to repeat calculations at runtime, so that skews the
    performance of this algorithm. Checking only once takes ~50x longer than each additional check.
    For fastest(), we'll select the method of reduction due to this behavior. Long live the cache.
    --> benchmark:   9038529 ns/run (over 1000 runs)
    --> benchmark: 463035900 ns/run (over 1 run)
    :param number: The number which this function will find the greatest prime factor
    :return: The greatest prime factor
    """
    primes = sieve_of_atkin(int(sqrt(number)))
    for i in range(1, len(primes)):
        if number % primes[-i] == 0:
            return primes[-i]
    return number


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run for the analytic solution
    logger.info(f"The {reduction.__name__}'s evaluation is {reduction()}")
    performance_run(reduction, iterations=PERFORMANCE_RUNS)()

    # Performance run for the generative solution
    logger.info(f"The {cached_sieve.__name__}'s evaluation is {cached_sieve()}")
    performance_run(cached_sieve, iterations=PERFORMANCE_RUNS)()
