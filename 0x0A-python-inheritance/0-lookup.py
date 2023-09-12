#!/usr/bin/python3
""" function to return a list of available attributes and methods """


def lookup(obj):
    """ function to look for all attributes and methods of obj """
    return [method for method in dir(obj)]
