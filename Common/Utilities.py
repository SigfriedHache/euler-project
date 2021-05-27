from functools import wraps
from time import perf_counter

from Common.Utilities import get_logger
from logging import Formatter, getLogger, INFO, Logger, StreamHandler

FORMATTER_STRING = "%(message)s"
LOGGER_NAME = "Euler Project Logger"
PERFORMANCE_ITERATIONS = 100


def init_logger(logging_level: int = INFO):
    """ This function initializes the logging for this project, if and only if it doesn't already exist """
    if not len(getLogger(LOGGER_NAME).handlers):
        console_handler = StreamHandler()
        console_handler.setLevel(logging_level)
        console_handler.setFormatter(Formatter(FORMATTER_STRING))

        system_logger = getLogger(LOGGER_NAME)
        system_logger.setLevel(logging_level)
        system_logger.addHandler(console_handler)


def get_logger() -> Logger:
    """ This function returns the logger for this project """
    return getLogger(LOGGER_NAME)


def performance_run(func, iterations: int = PERFORMANCE_ITERATIONS):
    """
    :param func:
    :param iterations:
    :return:
    """
    logger = get_logger()

    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"The {func.__name__} function's evaluation is {func(*args, **kwargs)}")
        start = perf_counter()
        for i in range(0, iterations):
            func(*args, **kwargs)
        end = perf_counter()
        run_length = int(1e6 * (end - start) / iterations)
        logger.info(f"The {func.__name__} function took a mean duration of {run_length} ms "
                    f"in each of {iterations} runs")

    return wrapper
