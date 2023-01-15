#!/usr/bin/python3
""" adds two integers and return the sum """


def add_integer(a, b=98):
    """ Function that adds two integer

        args:
            a: first number
            b: second number

        raises:
            TypeError: if a or b aren't integers or float

        returns:
            the sum of a and b
     """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
