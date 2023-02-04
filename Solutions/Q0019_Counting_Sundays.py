"""
https://projecteuler.net/problem=19

You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

from Common.Logger import get_logger, init_logger
from Common.Utilities import performance_run
from datetime import datetime, timedelta

PERFORMANCE_RUNS = 1_000
START_DATE = datetime(year=1901, month=1, day=1)
END_DATE = datetime(year=2000, month=12, day=31)
WEEKDAY = 'sunday'
DAYS_OF_THE_WEEK = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def fastest(*args, **kwargs):
    return library_support(*args, **kwargs)


def library_support(start_date: datetime, end_date: datetime, weekday: str) -> int:
    # Groom inputs
    if start_date.day != 1:
        start_date = start_date + timedelta(days=(32 - start_date.day))
        start_date = start_date + timedelta(days=(1 - start_date.day))

    if end_date < start_date:
        return 0

    # Solution
    count = 0
    weekday = DAYS_OF_THE_WEEK.index(weekday.lower())
    date = start_date

    while date < end_date:
        if date.weekday() == weekday:
            count = count + 1
        date = date + timedelta(days=32)
        date = date + timedelta(days=(1 - date.day))

    return count


if __name__ == "__main__":
    # Log stuff
    init_logger()
    logger = get_logger()

    # Performance run for fastest
    # performance_run(library_support, iterations=PERFORMANCE_RUNS)(START_DATE, END_DATE, WEEKDAY)
    print(library_support(START_DATE, END_DATE, WEEKDAY))
