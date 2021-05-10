from functools import lru_cache


@lru_cache(maxsize=5)
def sieve_of_atkin(limit: int = 200):
    # Initialise the sieve  array with False values
    sieve = [False] * limit
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
