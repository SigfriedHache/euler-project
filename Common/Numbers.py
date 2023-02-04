from typing import List, Iterator

from numpy import floor, math, sqrt

from Common.Primes import sieve_of_atkin, prime_list


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


def nth_triangular_number(n: int) -> int:
    if n < 1:
        raise ValueError(f"The argument provided, {n}, must be a natural number (i.e. an integer greater than or equal "
                         f"to 1)")
    return int(n*(n+1)/2)


def smallest_number_with_n_factors(n: int) -> int:
    number = 1
    while factor_count(number) != n:
        number += 1
    return number


def yield_factor(n: int) -> Iterator[int]:
    if not isinstance(n, int) or n < 1:
        raise ArithmeticError(f"The argument {n} must be a natural number.")
    else:
        factor_set = set()
        for num in range(1, int(sqrt(n)+1)):
            if n % num == 0:
                yield num
                if (n/num) != num:
                    factor_set.add(int(n/num))
        for num in sorted(factor_set):
            yield num


def factorization(n: int) -> List[int]:
    return [num for num in yield_factor(n)]


def factor_count(n: int) -> int:
    return sum(1 for _ in yield_factor(n))


def yield_prime_factor(n: int) -> Iterator[int]:
    if not isinstance(n, int) or n < 2:
        raise ArithmeticError(f"The argument {n} must be a natural number greater than or equal to 2.")
    else:
        primes_list = sieve_of_atkin(n)
        for prime in primes_list:
            while n % prime == 0:
                n /= prime
                yield prime


def prime_factorization(n: int) -> List[int]:
    return [num for num in yield_prime_factor(n)]


def prime_factor_count(n: int) -> int:
    return sum(1 for _ in yield_prime_factor(n))
