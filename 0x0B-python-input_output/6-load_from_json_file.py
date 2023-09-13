#!/usr/bin/python3
"""
    function to create an Object from a “JSON file”:

    Prototype: def load_from_json_file(filename):
    You must use the with statement
    You don’t need to manage exceptions
    if the JSON string doesn’t represent an object
    You don’t need to manage file permissions / exceptions
"""


import json


def load_from_json_file(filename):
    """ function creates a python object from json file """
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
