#!/usr/bin/python3
"""
    function returns True if the object is exactly an instance
    of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """ function to return true if obj is instance of a class """
    return type(obj) is a_class
