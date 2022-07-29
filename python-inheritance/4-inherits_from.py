#!/usr/bin/python3
""" pffff with """


def inherits_from(obj, a_class):
    """ Review """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
