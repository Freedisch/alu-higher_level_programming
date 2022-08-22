#!/usr/bin/python3
"""
Prototype: def add_integer(a, b=98):
a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b
"""



def add_integer(a, b=98):
    """Find somme of 2 integer"""
    if type(a) is not int and type (a) is not float:
        raise TypeError("a must be an integer")
    elif a is float: int(a)

    if type(b) is not int and type (b) is not float:
        raise TypeError("b is not an integer")
    elif b is float: int(b)

    return a + b;

