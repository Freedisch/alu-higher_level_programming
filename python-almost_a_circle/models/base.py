#!/usr/bin/python3
""" Create Class Base"""


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if type(id) != int and id is not None:
            raise TypeError("id must be an integer")
        if id is not None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON representation of list_dictionaries"""
