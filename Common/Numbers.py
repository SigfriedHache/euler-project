from typing import List

import numpy as np

from Common.Primes import sieve_of_atkin


def divisors(number: int) -> List[int]:
    """
    This function calculates and returns a list of all divisors that a given number has, e.g.
    f(number=24) -> [1, 2, 3, 4, 6, 8, 12, 24]
    :param number: The number whose divisors are to be calculated
    :return: A list of integer divisors
    """
    if number < 1:
        raise ValueError(f"The input number must be greater than one ({number} !> 1).")
    if number == 1:
        return [1]

    divisor_list = set()
    sqrt_ceil = int(np.floor(np.sqrt(number)) + 1)
    for i in range(1, sqrt_ceil):
        if number % i == 0:
            divisor_list.add(i)
            divisor_list.add(int(number/i))

    return sorted(list(divisor_list))


def prime_factorization(number: int) -> List[int]:
    """
    This function calculates and returns the prime factorization of an input number. This algorithm doesn't condense
    factor multiples, e.g.
    f(number=24) -> [2, 2, 2, 3] (and not [2, 3])
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
