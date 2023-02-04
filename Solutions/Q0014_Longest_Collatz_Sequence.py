"""
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved
yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

from Common.Logger import get_logger, init_logger
from Common.Utilities import performance_run


PERFORMANCE_RUNS = 5
LIMIT = 1_000_000


def collatz_iter(num: int) -> int:
    """
    This function iterates the input digit to the next digit using the Collatz sequence rules:
        even: num/2
        odd: 3*num + 1
    :param num: this is the input number, to-be-iterated upon
    :return: the next number in the sequence
    """
    if num % 2:
        return 3 * num + 1
    else:
        return num // 2


def fastest(*args, **kwargs) -> int:
    return crawl_with_caching_ascending(*args, **kwargs)


def full_crawl(max_num: int = LIMIT) -> int:
    """
    Generate the collatz sequence for each number, and compare its length to the previous longest Collatz length. Keep
    the newer number if there's a tie.
    :param max_num: this is the largest number that the algorithm will be run until
    """
    if max_num < 1:
        raise ValueError("The argument to this function must be a natural number (i.e. integer greater than 0).")

    seed = 1
    longest_sequence_length = 0
    longest_sequence_seed = 0

    while seed <= max_num:
        sequence = [seed]
        while sequence[-1] != 1:
            sequence = sequence + [collatz_iter(sequence[-1])]
        if len(sequence) > longest_sequence_length:
            longest_sequence_length = len(sequence)
            longest_sequence_seed = seed
        seed = seed + 1

    return longest_sequence_seed


def crawl_with_caching_ascending(max_num: int = LIMIT) -> int:
    """
    This algorithm crawls over all numbers between 1 and param:max_num to find the longest length sequence. If during
    the generation of the sequence it lands on a number whose sequence was already generated and cached, this algorithm
    will stop generating the sequence and use the cached length.
    :param max_num: this is the maximum number to which the algorithm will search
    :return: the seed number that generates the longest sequence
    """
    if max_num < 1:
        raise ValueError("The argument to this function must be a natural number (i.e. integer greater than 0).")

    seed = 1
    sequence_lengths = {str(seed): len([seed])}

    while seed <= max_num:
        seed = seed + 1
        sequence = [seed]

        while sequence[-1] != 1:
            if str(sequence[-1]) not in sequence_lengths:
                sequence = sequence + [collatz_iter(sequence[-1])]
            else:
                break

        right_of_node_length = sequence_lengths[str(sequence[-1])] - 1
        for i in range(len(sequence) - 1):
            sequence_lengths[str(sequence[i])] = len(sequence[i:]) + right_of_node_length

    return int(max(sequence_lengths, key=sequence_lengths.get))


def crawl_with_caching_descending(max_num: int = LIMIT) -> int:
    """
    This algorithm crawls over all numbers between 1 and param:max_num to find the longest length sequence. If during
    the generation of the sequence it lands on a number whose sequence was already generated and cached, this algorithm
    will stop generating the sequence and use the cached length.
    :param max_num: this is the maximum number to which the algorithm will search
    :return: the seed number that generates the longest sequence
    """
    if max_num < 1:
        raise ValueError("The argument to this function must be a natural number (i.e. integer greater than 0).")

    seed = max_num
    sequence_lengths = {'1': 1}

    while seed > 0:
        sequence = [seed]

        while sequence[-1] != 1:
            if str(sequence[-1]) not in sequence_lengths:
                sequence = sequence + [collatz_iter(sequence[-1])]
            else:
                break

        right_of_node_length = sequence_lengths[str(sequence[-1])] - 1
        for i in range(len(sequence) - 1):
            sequence_lengths[str(sequence[i])] = len(sequence[i:]) + right_of_node_length

        seed = seed - 1

    return int(max(sequence_lengths, key=sequence_lengths.get))


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run for fastest
    # performance_run(full_crawl, iterations=PERFORMANCE_RUNS)()
    # performance_run(crawl_with_caching_ascending, iterations=PERFORMANCE_RUNS)()
    # performance_run(crawl_with_caching_descending, iterations=PERFORMANCE_RUNS)()
    performance_run(fastest, iterations=PERFORMANCE_RUNS)(LIMIT)
    logger.info('done')
