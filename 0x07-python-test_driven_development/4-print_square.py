#!/usr/bin/python3
""" this module consist of function that prints square"""


def print_square(size):
    """ This function prints square of inputed size

    Args:
        size: parameter

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
