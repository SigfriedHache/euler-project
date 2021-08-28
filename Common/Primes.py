from functools import lru_cache
from typing import List


def prime_factorization(number: int) -> List[int]:
    """
    This function calculates and returns the prime factorization of an input number. This algorithm doesn't condense
    factor multiples (e.g. f(number=24) -> [2, 2, 2, 3] and not [2, 3])
    :param number: The number whose prime factors are to be calculated
    :return: A list of integer prime factors
    """
    if number <= 1:
        return [number]

    factors_list = []
    primes_list = sieve_of_atkin(number)

    for prime in primes_list:
        while number % prime == 0:
            factors_list += [prime]
            number /= prime

    if int(number) != 1:
        raise ArithmeticError(f"The prime factorization for the {number}; the number, {number} != 1")
    else:
        return factors_list


@lru_cache(maxsize=5)
def prime_list(number_of_primes: int = 1) -> List[int]:
    """
    This algorithm returns an array of the first :param length: primes
    :param number_of_primes: The number of primes in the list
    :return: A list of prime numbers, :param length: long
    """

    # Handle lower-bound edge cases
    if number_of_primes < 1:
        raise ValueError(f"The entered value of {number_of_primes} is not a natural number (i.e. length >= 1)")
    elif number_of_primes == 1:
        return [2]

    primes = [2]
    prime_count = 1
    current_number = 3

    while prime_count < number_of_primes:
        # Check for primeness
        is_prime = True
        for p in primes:
            if current_number % p == 0:
                is_prime = False
                break

        # If prime, collect and increment prime_count
        if is_prime:
            primes += [current_number]
            prime_count += 1

        # Increment current number to the next odd number
        current_number += 2

    return primes


@lru_cache(maxsize=5)
def sieve_of_atkin(limit: int = 200) -> List[int]:
    """
    The Sieve of Atkin is an ages-old algorithm to sift out all primes under a certain maximum limit
    :param limit: This is the upper boundary for the value of the primes to be calculated
    :return:
    """
    prime_seed = [2, 3, 5, 7]
    if limit > 10:
        pass
    elif limit in (7, 8, 9, 10):
        return prime_seed[:4]
    elif limit in (5, 6):
        return prime_seed[:3]
    elif limit in (3, 4):
        return prime_seed[:2]
    elif limit == 2:
        return prime_seed[:1]
    elif limit == 1:
        return prime_seed[:0]
    else:
        raise ValueError(f"The entered value of {limit} is not a positive integer.")

    # Initialise the sieve  array with False values
    sieve = [False] * (limit + 1)
    sieve[2] ^= True
    sieve[3] ^= True

    """
    Mark siev[n] is True if one of the following is True:
    a) n = (4*x*x)+(y*y) has odd number of solutions, i.e., there exist odd number of distinct pairs (x, y) that satisfy
    the equation and n % 12 = 1 or n % 12 = 5.
    b) n = (3*x*x)+(y*y) has odd number of solutions and n % 12 = 7 c) n = (3*x*x)-(y*y) has odd number of solutions, 
    x > y and n % 12 = 11
    """
    x = 1
    while x * x < limit:
        y = 1
        while y * y < limit:
            # Main part of Sieve of Atkin
            n = (4 * x * x) + (y * y)
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] ^= True

            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True

            n = (3 * x * x) - (y * y)
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] ^= True
            y += 1
        x += 1

    # Mark all multiples of squares as non-prime
    r = 5
    while r * r < limit:
        if sieve[r]:
            for i in range(r * r, limit, r * r):
                sieve[i] = False
        r += 1

    # accrue primes using sieve[]
    primes = []
    for a in range(0, len(sieve)):
        if sieve[a]:
            primes.append(a)

    return primes
