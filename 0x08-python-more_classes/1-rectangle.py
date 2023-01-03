#!/usr/bin/python3
"""class rectangle that defines a rectangle"""


class Rectangle:
    """class rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """initialize rectangle"""
        self.width = width
        self.height = height

    @property
    """width"""
    def width(self):
        return self.__width

    @property
    """height"""
    def height(self):
        return self.__height

    @width.setter
    """width setter"""
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @height.setter
    """height setter"""
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
