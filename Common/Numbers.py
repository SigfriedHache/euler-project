from typing import List

from numpy import floor, math, sqrt

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
    sqrt_ceil = int(floor(sqrt(number)) + 1)
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
        raise ArithmeticError(f"The prime factorization for the number failed: "
                              f"{factors_list} with a remainder of {number}.")
    return factors_list


def n_choose_k(n: int, k: int) -> int:
    """
    This function implements the analytic solution to the n choose k function: n! / k! (n-k)!
    :param n: the sample size
    :param k: the choice size
    :return: the result of n choose k
    """
    if k > n:
        raise ValueError(f"The condition k <= n, must be upheld. In this instance, {k} <= {n} is {k <= n}.")
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))
