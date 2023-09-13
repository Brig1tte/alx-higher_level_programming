#!/usr/bin/python3
"""
    function to read a text file (UTF8) and print it to stdout:

    Prototype: def read_file(filename=""):
    You must use the with statement
    You don’t need to manage file permission / file doesn't exist exceptions
"""


def read_file(filename=""):
    """ function reads a file """
    if filename:
        with open(filename, mode="r", encoding='utf-8') as file:
            for line in file:
                print(line, end="")
