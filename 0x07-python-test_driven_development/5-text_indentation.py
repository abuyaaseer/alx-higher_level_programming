#!/usr/bin/python3
""" this module consist of function that prints text """


def text_indentation(text):
    """ this function prints text with 2 new lines
        after each of these characters: ., ? and :

    Args:
        text: parameter

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")
