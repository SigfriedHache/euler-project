from functools import wraps
from time import perf_counter_ns

from Common.Logger import get_logger

ITERATIONS = 100


def performance_run(func, iterations: int = ITERATIONS):
    logger = get_logger()

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        for i in range(0, iterations):
            func(*args, **kwargs)
        end = perf_counter_ns()
        run_length = int((end - start) / iterations)
        logger.info(f"{func.__name__} took a mean duration of {run_length} ns in each of {iterations} runs")

    return wrapper
