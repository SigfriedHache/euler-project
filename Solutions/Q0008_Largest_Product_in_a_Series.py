"""
https://projecteuler.net/problem=8

The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?
"""

from functools import reduce
from operator import mul

from Common.Logger import get_logger, init_logger
from Common.Utilities import performance_run

PERFORMANCE_RUNS = 10_000
RUN_LENGTH = 13
NUMBER = int('73167176531330624919225119674426574742355349194934'
             '96983520312774506326239578318016984801869478851843'
             '85861560789112949495459501737958331952853208805511'
             '12540698747158523863050715693290963295227443043557'
             '66896648950445244523161731856403098711121722383113'
             '62229893423380308135336276614282806444486645238749'
             '30358907296290491560440772390713810515859307960866'
             '70172427121883998797908792274921901699720888093776'
             '65727333001053367881220235421809751254540594752243'
             '52584907711670556013604839586446706324415722155397'
             '53697817977846174064955149290862569321978468622482'
             '83972241375657056057490261407972968652414535100474'
             '82166370484403199890008895243450658541227588666881'
             '16427171479924442928230863465674813919123162824586'
             '17866458359124566529476545682848912883142607690042'
             '24219022671055626321111109370544217506941658960408'
             '07198403850962455444362981230987879927244284909188'
             '84580156166097919133875499200524063689912560717606'
             '05886116467109405077541002256983155200055935729725'
             '71636269561882670428252483600823257530420752963450')


def fastest(number: int = NUMBER, run_length: int = RUN_LENGTH) -> int:
    """ This returns the largest product of any given run_length-long run in the input number """
    return full_parse(number, run_length)


def full_parse(number: int = NUMBER, run_length: int = RUN_LENGTH) -> int:
    """
    This algorithm moves a run_length-long window over the input number, and checks
    :param number: This is the number being looked through for this searching algorithm
    :param run_length: This is the length of the run in question, e.g. 'largest product of 13 consecutive numbers'
    :return: This is the greatest product in the provided number!
    """
    number = str(number)
    largest_product = 0
    for i in range(0, len(number)-run_length+1):
        run = number[i:i+run_length]
        if '0' not in run:
            product = reduce(mul, [int(n) for n in run])
            largest_product = product if product > largest_product else largest_product

    return largest_product


def chop_and_check(number: int = NUMBER, run_length: int = RUN_LENGTH) -> int:
    """
    This is the "chop and check" solution. This algorithm recognizes that any 0 in a run of numbers will automatically
    disqualify that run from being the largest product. After splitting up the number into different runs, it performs
    a brute force search.
    :param number: This is the number being looked through for this searching algorithm
    :param run_length: This is the length of the run in question, e.g. 'largest product of 13 consecutive numbers'
    :return: This is the greatest product in the provided number!
    """
    # Chop up the number set, removing all 0's and clean up the vestigial {''} element
    number_set = set(str(number).split('0'))
    number_set.remove('')

    # Create groomed list of runs that are of length exactly run_length
    number_runs = set()
    for n in number_set:
        if len(n) > run_length:
            for i in range(0, len(n)-run_length+1):
                number_runs.add(n[i:i+run_length])
        elif len(n) == run_length:
            number_runs.add(n)

    # Largest product searching algorithm
    largest_product = 0
    for run in number_runs:
        product = reduce(mul, [int(n) for n in run])
        largest_product = product if product > largest_product else largest_product

    return largest_product


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run for fastest
    # performance_run(full_parse, iterations=PERFORMANCE_RUNS)()
    # performance_run(chop_and_check, iterations=PERFORMANCE_RUNS)()
    print(fastest(NUMBER, RUN_LENGTH))
