#!/usr/bin/python3
"""Defining the class"""


class Square:
    """Test"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Get/set size of the square"""
        return(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif value > 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The area of the square"""
        return(self.__size * self.__size)