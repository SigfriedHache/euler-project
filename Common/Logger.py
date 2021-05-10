from logging import Formatter, getLogger, INFO, Logger, StreamHandler

FORMATTER_STRING = "%(filename)s %(message)s"
LOGGER_NAME = "Euler Project Logger"


def init_logger(logging_level: int = INFO):
    """ This function initializes the logging for this project, if it doesn't already exist """
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
