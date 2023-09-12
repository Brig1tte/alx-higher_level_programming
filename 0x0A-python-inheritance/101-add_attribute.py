#!/usr/bin/python3
""" funcion to add a new attribute when possible """

def add_attribute(obj, attr, value):
    """ function to add new attribute """
    if hasattr(obj, "__dict__"):
        obj.__dict__[attr] = value
    else:
        raise TypeError("can't add new attribute")
