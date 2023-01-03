#!/usr/bin/python3
"""class rectangle that defines a rectangle"""


class Rectangle:
    """class rectangle"""
    def __init__(self, width, height):
        """ Instantiation with optional """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width """
        return self.__width

    @property
    def height(self):
        """ height """
        return self.__height

    @width.setter
    def width(self, value):
        """ width setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """returns area"""
        return self.__height * self.__width

    def perimeter(self):
        """returns perimeter"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2
