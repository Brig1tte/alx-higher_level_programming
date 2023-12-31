#!/usr/bin/python3
"""
    class BaseGeometry (based on 6-base_geometry.py)

    Public instance method: def area(self): raises an Exception
    with the message area() is not implemented
    Public instance method:
    def integer_validator(self, name, value): that validates value:
        you can assume name is always a string if value is not an integer:
        raise a TypeError exception, with the message <name> must be an integer
        if value is less or equal to 0: raise a ValueError exception
        with the message <name> must be greater than 0
"""


class BaseGeometry:
    """ BaseGeometry class empty """

    def area(self):
        """ function to raise an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ function to validate value is an integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
