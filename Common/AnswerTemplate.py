"""
https://projecteuler.net/problem=
...
"""

from Common.Logger import get_logger, init_logger
from Common.Utilities import performance_run

PERFORMANCE_RUNS = 1_000


# def fastest(*args, **kwargs):
#     return fx(*args, **kwargs)


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run for fastest
    # performance_run(fastest, iterations=PERFORMANCE_RUNS)()
