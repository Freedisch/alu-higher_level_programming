#!/usr/bin/python3
"""
Prototype: def add_integer(a, b=98):
a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
"""


def add_integer(a, b):
    """Find somme of 2 integer"""
    if type(a) is not int and type (a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type (b) is not float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
