from functools import lru_cache
from typing import List, Iterator


LRU_CACHE_MAXSIZE = 2


def yield_prime() -> Iterator[int]:
    primes = {2}
    yield 2

    current_number = 3
    while True:
        is_prime = True
        for p in primes:
            if current_number % p == 0:
                is_prime = False
                break

        if is_prime:
            primes.add(current_number)
            yield current_number

        current_number = current_number + 2


@lru_cache(maxsize=LRU_CACHE_MAXSIZE)
def prime_list(count: int) -> List[int]:
    if not isinstance(count, int) or count < 1:
        raise ArithmeticError(f"{count} is not a valid number of primes to calculate. An int >= 1 is required.")

    return [prime for _, prime in zip(range(count), yield_prime())]


def nth_prime(n: int) -> int:
    if not isinstance(n, int) or n < 1:
        raise ArithmeticError(f"{n} is not a valid number of primes to calculate. An int >= 1 is required.")

    return prime_list(n)[-1]


@lru_cache(maxsize=LRU_CACHE_MAXSIZE)
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
    Mark sieve[n] is True if one of the following is True:
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
