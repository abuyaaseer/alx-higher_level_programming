#!/usr/bin/python3
""" prints first and last name"""


def say_my_name(first_name, last_name=""):
    """ this function prints first and last name

        args:
            first_name: first parameter
            last_name: second parameter
        raises:
            TypeError: if the first name or last name is not str
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("my name is {} {}".format(first_name, last_name))
