from typing import Union


def is_palindrome(value: Union[str, int, float]) -> bool:
    """
    This function determines whether the input value is a palindrome
    :param value: The input value to-be analyzed
    :return: Bool evaluation
    """
    value = str(value)
    reversed_value = ""
    for digit in value:
        reversed_value = digit + reversed_value
    return True if reversed_value == value else False


def yield_fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
