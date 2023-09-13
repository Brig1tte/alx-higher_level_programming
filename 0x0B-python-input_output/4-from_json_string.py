#!/usr/bin/python3
"""
    function to return an object (Python data structure)
    represented by a JSON string:

    Prototype: def from_json_string(my_str):
    You don’t need to manage exceptions
    if the JSON string doesn’t represent an object
"""


import json


def from_json_string(my_str):
    """ function takes json str and gives a python object """
    return json.loads(my_str)
