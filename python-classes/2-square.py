#!/usr/bin/python3
"""Defining the class"""


class Square:
    """Raising errors for the size"""
    def __init__(self, size=0):
        self.__size = size
        if size < 0:
            raise ValueError("size must be an integer")
    raise TypeError("size must be >= 0")
