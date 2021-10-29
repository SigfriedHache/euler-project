from functools import wraps
from time import perf_counter

from Common.Logger import get_logger

ITERATIONS = 100


def performance_run(func, iterations: int = ITERATIONS):
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
                    f"for each of {iterations} runs")

    return wrapper
