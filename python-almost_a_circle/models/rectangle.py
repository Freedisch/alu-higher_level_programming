#!/usr/bin/python3
"""Module rectangle.
Create a Rectangle class, inheriting from Base.
"""
import json
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    
    @property
    def width(self):
        """Retrives the width attribute"""
        return self.__width

    @property
    def height(self):
        """Retrives the height attribute"""
        return self.__height

    @property
    def x(self):
        """Retrives the x attribute"""
        return self.__x 

    @property
    def y(self):
        """Retrives the y attribute"""
        return self.__y
    
    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @height.setter
    def height(self, value):
        """Sets the height attribute."""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("Value must be > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        """Sets the x attribute."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("Value must be > 0")
        self.__x = value
    
    @y.setter
    def y(self, value):
        """set the y attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("Value must be > 0")
        self.__x = value

    def area(self):
        """Calculate area"""
        return self.__width * self.___height

    def display(self):
        """Prints the rectangle instance with the # charcter"""

        for y in range(0, self):
            print()
        for i in range (0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns a string representation of a rectangle"""

        s = "[Rectangle] ({}) - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )
        return s

    def update(self, *args, **kwargs):
        """Update attribute of instances"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""

        my_dict = {'id': self.id, 'width': self.__width,
                   'height': self.__height, 'x': self.__x, 'y': self.__y}
        return my_dict
