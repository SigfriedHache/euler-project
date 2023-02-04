"""
https://projecteuler.net/problem=22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

from os import path, PathLike
from typing import Union

from Common.Logger import get_logger, init_logger
from Common.Utilities import performance_run

PERFORMANCE_RUNS = 1_000
NAME_FILE = path.relpath('./data/Q0022_names.txt')


def fastest(*args, **kwargs):
    return solution(*args, **kwargs)


def solution(filepath: Union[PathLike, str]) -> int:
    with open(filepath) as name_file:
        names_raw = name_file.read()
    names = names_raw.replace('"', '').split(',')
    names.sort()

    ord_gauge = 1 - ord('A')
    running_sum = 0
    for i, name in enumerate(names):
        for letter in name:
            running_sum = running_sum + (ord(letter.upper()) + ord_gauge) * (i+1)

    return running_sum


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run for fastest
    # performance_run(fastest, iterations=PERFORMANCE_RUNS)(NAME_FILE)
    print(solution(NAME_FILE))
